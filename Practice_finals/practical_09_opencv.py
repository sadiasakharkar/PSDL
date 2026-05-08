import cv2

def read_img(path):
    img = cv2.imread(path)
    
    if img is None:
        print("Image not found")
    else:
        return img

def display_img(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(img):
    img_new = cv2.imwrite('New image.jpeg', img)
    print("image is saved as img_new.jpeg")
    
def resize_img(img):
    resized = cv2.resize(img, (300 , 300))
    return resized
    
def flip_img(img):
    print("Enter how you want to resize you image:\n1. horizontal. \n2. vertical. \n3. both")
    ch = int(input())
    
    if ch == 1:
        flipped = cv2.flip(img , 1)
    elif ch == 2:
        flipped = cv2.flip(img , 0)
    elif ch == 3:
        flipped = cv2.flip(img, -1)
    else:
        print("Enter a valid choice")
        return img
    return flipped

def crop_img(img):
    h, w = img.shape[:2]
    if h < 50 or w < 50 :
        print("Invalid image.. image cannnot be cropped as its small in size")
        return img
    else:
        cropped = img[150 : h-150 , 150 : w-150]
        print("Original Size:", img.shape)
        print("Cropped Size:", cropped.shape)
    return cropped  

def gray_img(img):
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    return gray
def increase_brightness(img):
    bright = cv2.convertScaleAbs(img , alpha = 1.5 , beta = 2.0)
    return bright
    
def main():
    path = input("Enter image path:")
    img = read_img(path)
    
    while True:
        print("\n===== Image Processing Using OpenCV =====")
        print("1. Display Image")
        print("2. Save Image")
        print("3. Resize Image")
        print("4. Flip Image")
        print("5. Crop Image")
        print("6. Convert to Gray")
        print("7. Increase Brightness")
        print("8. Exit")

        print("Enter your choice:")
        ch = int(input())
        
        if ch == 1:
            display_img(img)
        elif ch == 2:
            save_image(img)
        elif ch == 3:
            resized = resize_img(img)
            display_img(resized)
        elif ch == 4:
            flipped = flip_img(img)
            display_img(flipped)
        elif ch == 5:
            cropped = crop_img(img)
            display_img(cropped)
        elif ch == 6:
            gray = gray_img(img)
            display_img(gray)
        elif ch == 7:
            new_img = increase_brightness(img)
            display_img(new_img)
        elif ch == 8:
            break


if __name__ == "__main__":
    main()