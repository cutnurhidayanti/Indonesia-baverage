from ultralytics import YOLO

def valid_model():
    # Load a model
    model = YOLO("runs/detect/train28/weights/best.pt")

    # Validate with a custom dataset
    metrics = model.val(data="data.yaml")
    print(metrics.box.map)  # map50-95
    print(metrics.box.map50)  # mAP50
    print(metrics.box.map75)  # mAP75
    print(metrics.box.maps)  # list of mAP50-95 for each category
        # model.to('cuda')

if __name__ == '__main__':
    valid_model()  # Call the function inside the main block
