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

We can observe that the peak of student enrollment was around 2004. With this information, I want to figure out what were the most active colleges and what those college's most active faculties were.

It's also important to observe that there's a noticeable down trend in the enrollment of Czech universities, which prompts further investigation as to why that's happening. According to the Czech Education Ministry's annual report released to the ČTK (Czech News Agency), one significant reason that explains the decline in enrollment to these universities is the demographic decline that has led to fewer young people entering higher education. Additionally, economic factors, such as low public funding for universities, have made higher education less accessible and appealing. What's more, the Czech Republic has one of the lowest rates of university graduates in the European Union. Only about 26.67% of Czechs aged 25 - 64 have a university degree, which is significantly below the European Union's average of 37.67%​.

![Screen Shot 2024-06-07 at 20 14 41](https://github.com/davidgb9716/data-science/assets/83733181/a3b6a937-938a-4eb7-a010-4f85a5d0a7db)

As shown in the DataFrame (or image) above, that the most active study programs are bachelor's degrees. Therefore, we're only going to focus on the most active colleges and faculties in the year with the highest enrollment (2004), and in their most popular study program (Bachelor's degree).

According to Eurydice (https://eurydice.eacea.ec.europa.eu/national-education-systems/czechia/bachelor), "The standard length of studies [in the Czech Republic] including practical training is no less than three and no more than four years."

Since it takes at least three years to get a Bachelor's degree from a Czech university, we'll use the year with the highest enrollment numbers as reference. We'll take into account the three years we previously talked about, and within that year, We can observe the following results:

![Screen Shot 2024-06-09 at 1 24 35](https://github.com/davidgb9716/data-science/assets/83733181/5f96e248-6d7a-41c2-bc2a-3b3a605d0b4e)

The Univerisites with the most students who completed their Bachelor's degree program are:
1. Jan Amos Comenius University Prague, s.r.o. (1187)
2. AMBIS - college, a. s. (894)
3. Tomas Bata University in Zlín (769)
4. University of Mining - Technical University of Ostrava (739)
5. Czech University of Agriculture in Prague (709)

The problem with this approach is that even though we're considering the universities with the most program completions, we're also separating them by their respective faculties.

The better approach would be to group the universities together and count again, not taking the faculties into consdiration. The results are the following:

![Screen Shot 2024-06-10 at 13 34 29](https://github.com/davidgb9716/data-science/assets/83733181/b2948313-ec7c-41ed-b946-850bbe0bc3af)


### Correlation Heatmap
![correlation_heatmap](https://github.com/davidgb9716/data-science/assets/83733181/cdcad8d2-24e4-4592-ae61-4ea3fa04a3c5)

### Correlation Heatmap with Annotations
![correlation_heatmap_with_annotations](https://github.com/davidgb9716/data-science/assets/83733181/a5fecb91-1e79-46f1-9fc7-8ea35864fcd4)

## 03. Data Preparation

In this stage, our goal is to manipulate and transform the data in order to use it more effectively in later stages. I'll identify and handle any potential missing data, remove duplicates, identify and handle outliers, normalize and standardize the data, handle inconsistent data, perform string encoding, and save this new dataset which will then be used in the following stages.

## 04. Modeling

## 05. Evaluation

## 06. Deployment

## Conclusion

## Sources

