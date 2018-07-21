from ar_markers import HammingMarker
import cv2
import numpy as np

marker = HammingMarker(1)
img = marker.generate_image()

cv2.imwrite('tag_1.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
