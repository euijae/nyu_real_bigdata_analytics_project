# Title 

 Build a video classification model running on large scale dataflow pipeline. Please traverse to the subfolders, and find the .md files to proceed.

# Team 
- Devansh Purohit (dnp9357@nyu.edu)
- Euijae Kim (ek3955@nyu.edu)

# Problem 

Analyze NBA video data to develop a classifier model that stores data for a video clip for these fields: [`SHOT_TYPE`, `BLK`, `FOUL`] (Description below). `SHOT_TYPE` can have the following values:
- SHOT_TYPE
  - 2PM_Layup
  - 2PM_JumpShot
  - 3PM
  - Missed_shot (also has shot clock violations)
  - FT_Made
  - FT_Missed
- BLK: A binary field storing whether a turnover happened due to a Block.
- FOUL can have the following values:
  - 0: No Foul
  - 1: Foul by defensive team
  - 2: Foul by offensive team.

A few paper already exists on similar problems (1: https://github.com/jackwu502/nsva ; https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136970019.pdf) (2: https://aircconline.com/csit/papers/vol11/csit110712.pdf). The goal of this project is to further the accuracy and dataset size for this problem, and try more Neural network architectures to improve results. Live video captioning can also be explored as an alternate problem statement. 

# Dataset(s) 

Currently, we can use the available NVSA dataset that has ~45k clips from 132 games in the 2018-2019 season. A data can be obtained through multiple ways. It's available as an API or downloadable compressed file on the internet.

## Questions to be asked on the Datasets: 

- Is there a way to pre-label these datasets?
- Can a partially labeled dataset, or a model trained on a partially labeled dataset help us train a model on a larger dataset, increasing our accuracy?
- Can we process the large amount of video data efficiently using Big data technologies?

## Baseline metrics for evaluation: 

1. Trimming a given input video frames as not every frame is relevant. For example, the length of available videos is up to 30 seconds. The trimming process can cut the length by 40%.
2. Employing a range of techniques to effectively enhance these images, including:
   - GAN-based method
   - UNet based method
3. To evaluate the outcomes, we will compare the prediction with the label

## (Optional) What are you going to compare against: 

Accuracy of classification model is one of the most important things in this study. We are going to try at least two video classification models and compare against each other to see which one is better way to go.

# Alternate for Systems oriented projects: 

We can't state what category our project can be classified as we're going to focus video classification and building a large scale dataflow. 

## Question: 

### Measure/Metrics (Performance, Abstraction or Property): 

- Accuracy and Recall of categorizing unlabeled data.
- Speed of categorization: Realtime? Acceptable delay?

### Baselines: 

- Integrate Spark for data flow and ML model

### What do you need for your project: 

At least two video training models are required. Since video file size is larger than 

# First Step of Execution

- Formalize dataset by either configuring existing NVSA Dataset or by scraping publicly available clips
- Create naive classification model on labeled data

## Tools: 

- Pytorch
- Pytorch-lightning
- Spark
- Python
- NumPy
- Colab and HPC

## How are you using HPC? 

- Parallel processing on Spark for real-time video analysis through our ML model
- Creation of ML model using GPU enabled compute instances.

## What is Big Data in your project? (few MB is not big data) 

- Vast swathes of unlabeled video data
