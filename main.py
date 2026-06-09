import time
import cv2
import numpy as np
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from gesture_detector import GestureDetector
from volume_controller import VolumeController
from face_effects import FaceEffects
from background_effects import BackgroundEffects


def put_text(frame, text, y):
    cv2.putText(frame, text, (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)


def create_hand_landmarker():
    base_options = python.BaseOptions(model_asset_path="models/hand_landmarker.task")
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.6,
        min_hand_presence_confidence=0.6,
        min_tracking_confidence=0.6,
    )
    return vision.HandLandmarker.create_from_options(options)


def create_face_landmarker():
    base_options = python.BaseOptions(model_asset_path="models/face_landmarker.task")
    options = vision.FaceLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_faces=1,
        min_face_detection_confidence=0.6,
        min_face_presence_confidence=0.6,
        min_tracking_confidence=0.6,
    )
    return vision.FaceLandmarker.create_from_options(options)


def create_segmenter():
    base_options = python.BaseOptions(model_asset_path="models/selfie_segmenter.tflite")
    options = vision.ImageSegmenterOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        output_category_mask=True,
    )
    return vision.ImageSegmenter.create_from_options(options)


def main():
    cap = cv2.VideoCapture(0)

    detector = GestureDetector()
    volume = VolumeController()
    face_effects = FaceEffects()
    background_effects = BackgroundEffects()

    mask_enabled = False
    blur_enabled = False

    last_action_time = 0
    cooldown = 1.5

    with create_hand_landmarker() as hand_landmarker, \
         create_face_landmarker() as face_landmarker, \
         create_segmenter() as segmenter:

        while True:
            success, frame = cap.read()

            if not success:
                print("Ошибка: камера не найдена")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            timestamp_ms = int(time.time() * 1000)

            hand_result = hand_landmarker.detect_for_video(mp_image, timestamp_ms)
            face_result = face_landmarker.detect_for_video(mp_image, timestamp_ms)
            segmentation_result = segmenter.segment_for_video(mp_image, timestamp_ms)

            left_hand = None
            right_hand = None

            if hand_result.hand_landmarks:
                for i, landmarks in enumerate(hand_result.hand_landmarks):
                    handedness = hand_result.handedness[i][0].category_name

                    # Из-за зеркального отображения камеры стороны инвертируем
                    if handedness == "Left":
                        right_hand = landmarks
                    elif handedness == "Right":
                        left_hand = landmarks

                    h, w, _ = frame.shape
                    for lm in landmarks:
                        x = int(lm.x * w)
                        y = int(lm.y * h)
                        cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            current_time = time.time()

            if current_time - last_action_time > cooldown:
                if left_hand and detector.is_pinch(left_hand):
                    volume.volume_up()
                    last_action_time = current_time
                    print("Левая рука pinch: громкость +")

                elif right_hand and detector.is_pinch(right_hand):
                    volume.volume_down()
                    last_action_time = current_time
                    print("Правая рука pinch: громкость -")

                elif left_hand and detector.is_fist(left_hand):
                    mask_enabled = True
                    last_action_time = current_time
                    print("Левая рука кулак: маска включена")

                elif right_hand and detector.is_fist(right_hand):
                    mask_enabled = False
                    last_action_time = current_time
                    print("Правая рука кулак: маска выключена")

                elif detector.palms_together(left_hand, right_hand):
                    blur_enabled = True
                    last_action_time = current_time
                    print("Ладони вместе: blur включен")

                elif detector.palms_apart(left_hand, right_hand):
                    blur_enabled = False
                    last_action_time = current_time
                    print("Ладони разведены: blur выключен")

            if blur_enabled:
                category_mask = segmentation_result.category_mask.numpy_view()
                frame = background_effects.blur_background(frame, category_mask)

            if mask_enabled and face_result.face_landmarks:
                face_landmarks = face_result.face_landmarks[0]
                frame = face_effects.draw_clown_mask(frame, face_landmarks)

            put_text(frame, f"Mask: {'ON' if mask_enabled else 'OFF'}", 30)
            put_text(frame, f"Background Blur: {'ON' if blur_enabled else 'OFF'}", 60)

            cv2.imshow("AI Gesture Controller", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()