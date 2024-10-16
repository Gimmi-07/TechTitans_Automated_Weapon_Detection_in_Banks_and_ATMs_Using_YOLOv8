from ultralytics import YOLO

model = YOLO('best.pt')
results = model.predict(r'C:\Users\arshi\OneDrive\Documents\IIIT HYDERABAD\5b4c9e09-img2.jpg')
results.show()