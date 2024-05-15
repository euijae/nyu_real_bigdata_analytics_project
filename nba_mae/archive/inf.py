import pytorchvideo.data

from pytorchvideo.transforms import (
    ApplyTransformToKey,
    Normalize,
    RandomShortSideScale,
    RemoveKey,
    ShortSideScale,
    UniformTemporalSubsample,
)

from torchvision.transforms import (
    Compose,
    Lambda,
    RandomCrop,
    RandomHorizontalFlip,
    Resize,
)




mean = image_processor.image_mean
std = image_processor.image_std
if "shortest_edge" in image_processor.size:
    height = width = image_processor.size["shortest_edge"]
else:
    height = image_processor.size["height"]
    width = image_processor.size["width"]
resize_to = (height, width)

num_frames_to_sample = model.config.num_frames
sample_rate = 4
fps = 30
clip_duration = num_frames_to_sample * sample_rate / fps
print(num_frames_to_sample)




# test_transform = Compose(
#     [
#         ApplyTransformToKey(
#             key="video",
#             transform=Compose(
#                 [
#                     UniformTemporalSubsample(num_frames_to_sample),
#                     Lambda(lambda x: x / 255.0),
#                     Normalize(mean, std),
#                     RandomShortSideScale(min_size=256, max_size=320),
#                     RandomCrop(resize_to),
#                     RandomHorizontalFlip(p=0.5),
#                 ]
#             ),
#         ),
#     ]
# )
dataset_root_path = './dataset'
test_dataset = pytorchvideo.data.Ucf101(
    data_path=os.path.join(dataset_root_path, "test"),
    clip_sampler=pytorchvideo.data.make_clip_sampler("uniform", clip_duration),
    decode_audio=False,
    transform=test_transform,
)

sample_video = next(iter(train_dataset))
video_cls = pipeline(model=model_path)
logits = video_cls(sample_video["video"])