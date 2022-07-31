import cv2 as cv

def plot_image(image, boxes):
    img = cv.imread(image)
    for box in boxes:
        assert len(box) == 4
        x1 = int(box[0] - (box[2] / 2))
        y1 = int(box[1] - (box[3] / 2))
        x2 = int(box[0] + (box[2] / 2))
        y2 = int(box[1] + (box[3] / 2))
        print(f'{x1}    {x2}    {y1}    {y2}')

        rect = cv.rectangle(img, (x1,y1),(x2,y2), (0, 255, 0), thickness=2)
    cv.imshow('image', img)
    cv.waitKey(0)

# Testing
image_org = cv.imread('../../Obj_Detection/img2.jpeg')
# height = image_org.shape[0]
# width = image_org.shape[1]
# # print(height)
# # print(width)
# x = width/2
# y = height/2
# rec_width = 200
# rec_height = 300
boxes = [[300,400,100,100]]
# let boxes corrdinate:
# boxes = []
image = 'img2.jpeg'
plot_image(image,boxes)

# cv.rectangle(image_org,boxes)