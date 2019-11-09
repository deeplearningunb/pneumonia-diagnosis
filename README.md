<h1 align="center">Pneumonia Diagnosis from Chest Ray</h1>

<p align="center">
    <i>A Tensorflow 2.0 implementation</i>
</p>

<p align="center">
    <img src="https://i.imgur.com/jZqpV51.png" height=300>
</p>

---

## What is the problem?
The problem is that x-ray diagnoses are reliable on humans and prone to errors. Doctors oppinions might vary and they aren`t precise.

## What is the solution?
The algorithm attemps to solve the problem above using state-of-the art machine learning techniques. The implementation will provide better data for doctors to provide their diagnoses. 

There is also a possibility for the algorithm do predict and classify the suscetibility of users having pneumonia based on their chest xray images.

## Who the solution will benefit?
It will benefit the general population that does exams and want a more reliable source of diagnose.

## Kaggle dataset

Content
The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.

For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.

## Dependencies

- Docker
- Docker compose

## Usage

Run the following in the command line:

```docker-compose up```

## Datasets

[1] https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia
