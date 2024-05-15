from autogluon.multimodal import MultiModalPredictor
import os

from autogluon.core.utils.loaders import load_zip

#zip_file = "https://automl-mm-bench.s3.amazonaws.com/object_detection/dataset/pothole.zip"
download_dir = "./"

#load_zip.unzip(zip_file, unzip_dir=download_dir)
data_dir = os.path.join(download_dir, "data")

train_path = os.path.join(data_dir, "train/a", "_annotations.coco.json")
val_path = os.path.join(data_dir, "valid/a", "_annotations.coco.json")
test_path = os.path.join(data_dir, "test/a", "_annotations.coco.json")

checkpoint_name = "yolox_s"
num_gpus = 1  # only use one GPU
print("!")
predictor = MultiModalPredictor(
    hyperparameters={
        "model.mmdet_image.checkpoint_name": checkpoint_name,
        "env.num_gpus": num_gpus,
    },
    problem_type="object_detection",
    sample_data_path=train_path,
)
print("!")
import time
start = time.time()
predictor.fit(
    train_path,
    hyperparameters={
        "optimization.learning_rate": 5e-6, # we use two stage and detection head has 100x lr
        "optimization.max_epochs": 100,
        "optimization.check_val_every_n_epoch": 1, # make sure there is at least one validation
        "env.per_gpu_batch_size": 2,  # decrease it when model is large
    },
)
end = time.time()

print("This finetuning takes %.2f seconds." % (end - start))

predictor.evaluate(test_path)