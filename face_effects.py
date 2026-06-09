import cv2


class FaceEffects:
    def draw_clown_mask(self, frame, face_landmarks):
        h, w, _ = frame.shape

        # В новом MediaPipe Tasks face_landmarks — это обычный список точек
        lm = face_landmarks

        def point(index):
            return int(lm[index].x * w), int(lm[index].y * h)

        # Нос
        nose = point(1)
        cv2.circle(frame, nose, 18, (0, 0, 255), -1)

        # Глаза
        left_eye = point(33)
        right_eye = point(263)

        cv2.circle(frame, left_eye, 28, (255, 255, 255), -1)
        cv2.circle(frame, right_eye, 28, (255, 255, 255), -1)

        cv2.circle(frame, left_eye, 9, (0, 0, 0), -1)
        cv2.circle(frame, right_eye, 9, (0, 0, 0), -1)

        # Улыбка
        mouth_center = point(13)
        cv2.ellipse(
            frame,
            mouth_center,
            (90, 45),
            0,
            10,
            170,
            (0, 0, 255),
            8
        )

        # Щёки
        left_mouth = point(61)
        right_mouth = point(291)

        cv2.circle(frame, left_mouth, 16, (0, 120, 255), -1)
        cv2.circle(frame, right_mouth, 16, (0, 120, 255), -1)

        return frame