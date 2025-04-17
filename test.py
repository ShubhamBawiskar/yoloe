from ultralytics import YOLOE

# Initialize a YOLOE model
model = YOLOE("yoloe-11l-seg.pt")  # or select yoloe-11s/m-seg.pt for different sizes

# Set text prompt
names = ["head with helmet"]
model.set_classes(names, model.get_text_pe(names))

# Execute prediction for specified categories on an image
results = model.predict("artifacts/helmet.jpeg")

# Show results
results[0].save("del.jpg")

###################################################################3

# from ultralytics import YOLOE

# # Initialize a YOLOE model
# model = YOLOE("yoloe-11l-seg-pf.pt")

# # Execute prediction for specified categories on an image
# results = model.predict("artifacts/helmet.jpeg")

# # Show results
# results[0].show()

#################################################################3

# import numpy as np

# from ultralytics import YOLOE
# from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# # Initialize a YOLOE model
# model = YOLOE("yoloe-11l-seg.pt")

# # Set visual prompt
# visuals = dict(
#     bboxes=np.array(
#         [
#             [221.52, 405.8, 344.98, 857.54],  # For person
#             [120, 425, 160, 445],  # For glasses
#         ],
#     ),
#     cls=np.array(
#         [
#             0,  # For person
#             1,  # For glasses
#         ]
#     ),
# )

# # Execute prediction for specified categories on an image
# results = model.predict(
#     "artifacts/helmet.jpeg",
#     visual_prompts=visuals,
#     predictor=YOLOEVPSegPredictor,
# )

# # Show results
# results[0].save("del.jpg")