import math


class GestureDetector:
    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def is_pinch(self, hand_landmarks, threshold=0.045):
        thumb_tip = hand_landmarks[4]
        index_tip = hand_landmarks[8]
        return self.distance(thumb_tip, index_tip) < threshold

    def is_fist(self, hand_landmarks):
        fingers = [
            (8, 6),
            (12, 10),
            (16, 14),
            (20, 18),
        ]

        folded = 0

        for tip, pip in fingers:
            if hand_landmarks[tip].y > hand_landmarks[pip].y:
                folded += 1

        return folded >= 4

    def palms_together(self, left_hand, right_hand, threshold=0.12):
        if left_hand is None or right_hand is None:
            return False

        left_wrist = left_hand[0]
        right_wrist = right_hand[0]

        return self.distance(left_wrist, right_wrist) < threshold

    def palms_apart(self, left_hand, right_hand, threshold=0.30):
        if left_hand is None or right_hand is None:
            return False

        left_wrist = left_hand[0]
        right_wrist = right_hand[0]

        return self.distance(left_wrist, right_wrist) > threshold