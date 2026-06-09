import cv2
import numpy as np


class BackgroundEffects:
    def blur_background(self, frame, segmentation_mask):
        blurred = cv2.GaussianBlur(frame, (55, 55), 0)

        # Маска может прийти в формате (H, W, 1), приводим к (H, W)
        if len(segmentation_mask.shape) == 3:
            segmentation_mask = segmentation_mask[:, :, 0]

        condition = segmentation_mask > 0.55

        # Делаем формат (H, W, 3), чтобы совпал с frame
        condition = np.repeat(condition[:, :, np.newaxis], 3, axis=2)

        output = np.where(condition, frame, blurred)

        return output.astype(np.uint8)