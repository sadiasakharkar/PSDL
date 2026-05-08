import cv2

def read_img(path):
    img = cv2.imread(path)
    
    if img is None:
        print("Image not found")
    else:
        return img

def display_img(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(img):
    img_name =cv2.imwrite("new_image.jpg", img)
    print("Image is saved as new_image.jpg")
    return img_name

def resize_img(img):
    resized = cv2.resize(img, (300,300))
    return resized

def flip_img(img):
    print("1.horizontal 2.vertical 3.both")
    print("Enter the directiion you want to flip")
    ch = int(input())
        
    if ch == 1:
        flipped = cv2.flip(img, 1)
    elif ch == 2:
        flipped = cv2.flip(img , 0)
    elif ch == 3:
        flipped = cv2.flip (img, -1)
    else:
        print("Enter a vlaid choice")
    return flipped

def crop_img(img):
    h ,  w = img.shape[:2]
    if h < 100 or w < 100:
        print("Image is too short to be cropped")
    else:
        cropped = img[50:h-50 , 50:w-50]
    return cropped

def gray_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def increase_brightness(img):
    new_img = cv2.convertScaleAbs(img , alpha = 1.5, beta = 50);
    return new_img

def main():
    path = input("Enter the path of image:")
    img = read_img(path)
    
    while True:
        print("1. display 2. save 3.resize 4.flip 5.crop 6.gray 7.increase brightness 8. exit")
        print("Enter your choice:")
    
        ch = int(input())
    
        if ch == 1:
            display_img(img)
        elif ch == 2: 
            save_image(img)
            display_img
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
            print("Program ended")
            break
        else:
            print("Enter a valid choice")
        
if __name__ == "__main__":   
    main()