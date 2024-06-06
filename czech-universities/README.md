# Graduation from Czech Universities

## Introduction

In this project, I'll be taking the data from this Kaggle Dataset, "Graduation from Czech universities" (https://www.kaggle.com/datasets/jetakow/graduation-from-czech-universities/data) through the entire Data Science process.

To work with this dataset and effectively communicate the process in clear, concise steps, I'll use the CRISP-DM Methodology.

## 01. Business Understanding

The first step in the CRISP-DM Methodology is Business Understanding. In this step, our goal is to understand the business problem; what we hope to gather from the data in order to get a solution.

### Questions to answer at the end of the methodology
- What was the biggest cause of not graduating?
- Which colleges have the highest and lowest graduation rates?
- Which programs have the highest and lowest graduation rates?
- Do the programs, when grouped by college, show a similar trend to the programs individually in relation to graduation rates?

## 02. Data Understanding

In this stage, our goal is to understand the data and its contents. I'll handle tasks such as data collection, data description, data exploration (Exploratory Data Analysis, or EDA); among others.

In terms of data collection, as mentioned previously, the dataset that I will be working with comes from Kaggle. It's called, "Graduation from Czech universities". This dataset, according to the Kaggle Contributor who uploaded it (Daniel Herman), is a "scraped collection of data from a Czech Statistical Institute website tracking course of studies at public and private universities."

### Year of Enrollment Histogram
![year_of_enrollment_histogram](https://github.com/davidgb9716/data-science/assets/83733181/7183ff55-c003-4bd1-bd7b-22ffd9cc8dcb)

We can observe that the peak of student enrollment was around 2004. With this information, I want to figure out what were the most active colleges and those college's most active faculties.

There's a noticeable down trend, which prompts further investigation as to why that's happening.

(DataFrame or Screen Shot)
As shown in the DataFrame (or image) above, that the most active study programs are bachelor's degrees. Therefore, we're only going to focus on the most active colleges and faculties in the year with the highest enrollment (2004), and in their most popular study program (Bachelor's degree).

### Correlation Heatmap
![correlation_heatmap](https://github.com/davidgb9716/data-science/assets/83733181/74f0e232-bdbb-41ad-843d-426f7f9c4c76)

### Correlation Heatmap with Annotations
![correlation_heatmap_with_annotations](https://github.com/davidgb9716/data-science/assets/83733181/5ddc00e3-6f24-4f66-bf0a-1fe0adc58fb3)

## 03. Data Preparation

In this stage, our goal is to manipulate and transform the data in order to use it more effectively in later stages. I'll identify and handle any potential missing data, remove duplicates, identify and handle outliers, normalize and standardize the data, handle inconsistent data, perform string encoding, and save this new dataset which will then be used in the following stages.

## 04. Modeling

## 05. Evaluation

## 06. Deployment

## Conclusion
