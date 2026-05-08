from PIL import Image, ImageOps, ImageEnhance

def read_img(path):
    try:
        img = Image.open(path)
        return img
    except:
        print("Image not found")


def display_img(img):
    img.show()

def save_image(img):    
    img.save("new_image.jpg")
    print("Image is saved as new_image.jpg")

def resize_img(img):
    resized = img.resize((300, 300))
    return resized

def flip_img(img):
    print("1. Horizontal")
    print("2. Vertical")
    print("3. Both")
    print("Enter the direction you want to flip:")
    
    ch = int(input())
    if ch == 1:
        flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif ch == 2:
        flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif ch == 3:
        temp = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped = temp.transpose(Image.FLIP_TOP_BOTTOM)

    else:
        print("Enter a valid choice")
        return img
    return flipped

def crop_img(img):
    w, h = img.size
    if h < 100 or w < 100:
        print("Image is too small to crop")
        return img
    else:
        cropped = img.crop((50, 50, w - 50, h - 50))
        return cropped

def gray_img(img):
    gray = ImageOps.grayscale(img)
    return gray

def increase_brightness(img):
    enhancer = ImageEnhance.Brightness(img)
    new_img = enhancer.enhance(1.5)
    return new_img

def main():
    path = input("Enter the path of image: ")
    img = read_img(path)
    if img is None:
        return
    while True:
        print("\n===== Image Processing Using PIL =====")
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
            print("Program Ended")
            break
        else:
            print("Enter a valid choice")


if __name__ == "__main__":
    main()