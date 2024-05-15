from autogluon.multimodal.utils import visualize_detection
from autogluon.multimodal import MultiModalPredictor
from autogluon.core.utils.loaders import load_zip

download_dir = "./"

#load_zip.unzip(zip_file, unzip_dir=download_dir)
data_dir = os.path.join(download_dir, "data")

train_path = os.path.join(data_dir, "train/a", "_annotations.coco.json")
val_path = os.path.join(data_dir, "valid/a", "_annotations.coco.json")
test_path = os.path.join(data_dir, "test/a", "_annotations.coco.json")

better_predictor = MultiModalPredictor.load("/scratch/dnp9357/obDet/AutogluonModels/ag-20240506_084614/epoch=11-step=108.ckpt")
better_predictor.set_num_gpus(1)

# Evaluate new predictor
better_predictor.evaluate(test_path)

pred = better_predictor.predict(test_path)

conf_threshold = 0.25  # Specify a confidence threshold to filter out unwanted boxes
visualization_result_dir = "./"  # Use the pwd as result dir to save the visualized image
visualized = visualize_detection(
    pred=pred[12:13],
    detection_classes=better_predictor.get_predictor_classes(),
    conf_threshold=conf_threshold,
    visualization_result_dir=visualization_result_dir,
)
from PIL import Image
from IPython.display import display
img = Image.fromarray(visualized[0][:, :, ::-1], 'RGB')
display(img)