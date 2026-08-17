import cv2
import numpy as np

image = cv2.imread('/home/kakon/Downloads/parkinson dieses/Pasted image.png',cv2.IMREAD_GRAYSCALE)

dark_mask = image < 50
dark_pixel = image[dark_mask]

print(f"pixel number:{len(dark_pixel)}")
print(f"pixel value:{dark_pixel}")

processed_image = np.where(image < 50, 255, 0).astype(np.uint8)

cv2.imshow('original image:',image)
cv2.imshow('processed:',processed_image)

print("press any key to stop")
cv2.waitKey(0)
cv2.destroyAllWindows()