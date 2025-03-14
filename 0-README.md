# SleepImpact-TERMProject

## Project Overview

In this project, I will investigate the effects of daily caffeine consumption, social media usage, cigarette smoking, and step count on the time taken to fall asleep and overall sleep quality. The sleep data will be sourced from the Sleep Cycle app, social media usage from the iPhone's Focus Time feature, and daily step count from Apple Health. Additionally, sleep quality will be measured using both my subjective assessments and objective data from Sleep Cycle. The goal is to analyze how lifestyle habits impact sleep, using a scientific and data-driven approach to develop strategies for improving sleep quality.

## Objectives

- **Sleep Performance Relationship:**  
  Determine the impact of daily caffeine consumption, social media usage, cigarette smoking, and step count on sleep onset time and overall sleep quality.
  
- **Identification of Key Variables:**  
  Identify the factors that most significantly affect sleep quality and propose lifestyle adjustments focusing on these key variables.
  
- **Data-Driven Optimization:**  
  Based on the collected data, develop recommendations to optimize sleep patterns and enhance overall quality of life.
  
- **Application of Data Science Skills:**  
  Apply the theoretical knowledge and techniques I have learned by testing them on real-world data to improve my data analysis and visualization skills.
  

## Motivation

- **Personal Growth:**  
  Sleep is crucial for daily performance and overall health. By understanding which habits affect my sleep quality, I aim to improve my lifestyle.
  
- **Scientific Approach:**  
  I want my decision-making process to be more objective and data-driven. This project will support subjective perceptions with unbiased measurements to yield clear outcomes.
  
- **Practical Application:**  
  Collecting and analyzing data using the technologies I use daily (Sleep Cycle, iPhone Focus Time, Apple Health) and providing actionable insights makes this project both engaging and practical.

## Dataset

- **Date:** The specific record date  
- **Caffeine (mg):** Daily caffeine consumption  
- **Social Media Usage (minutes):** Daily social media usage duration measured via the iPhone’s Focus Time  
- **Cigarettes:** Daily number of cigarettes smoked  
- **Step Count:** Daily step count from Apple Health  
- **Sleep Onset Time (minutes):** The time taken to fall asleep  
- **Sleep Quality:** Both subjective evaluation (on a scale of 1-10) and objective sleep quality data from Sleep Cycle
    

*Note: Any anomalies (e.g., illness, unusual routine changes) will be noted and flagged for review before analysis.*

## Tools and Technologies

- **Python:** Primary language for data analysis and automation  
- **Pandas:** For data cleaning, manipulation, and preprocessing  
- **Matplotlib and Seaborn:** For creating visualizations such as scatter plots, heatmaps, and time series  
- **SciPy:** For hypothesis testing and regression analysis  
- **Jupyter Notebooks :** For an interactive environment to write, run, and document code  

## Analysis Plan

1. **Data Collection and Preparation:**
   
   - Gather daily data from the relevant sources (Sleep Cycle, iPhone, Apple Health) and import it into a Pandas DataFrame.  
   - Identify and standardize missing or inconsistent data.
     
2. **Visualization:**
   
   - Create interactive charts to illustrate the relationships between caffeine consumption, social media usage, cigarette smoking, step count, and both sleep onset time and sleep quality.
   - For example, a scatter plot visualizing the relationship between caffeine consumption and time taken to fall asleep.
     
3. **Hypothesis Testing:**
   
   - **H₀:** Daily habits have no effect on sleep onset time and sleep quality.  
   - **Hₐ:** Specific daily habits (e.g., high caffeine or intense social media usage) significantly affect sleep onset time and sleep quality.  
   - Test these hypotheses using regression analysis and other statistical tests with Statsmodels and scikit-learn.
     
4. **Trend Analysis:**
   
   - Investigate changes in sleep onset time and sleep quality over time.  
   - For example, analyze the impact of increases or decreases in social media usage on sleep quality.
     

## Example Analysis

To illustrate, I will create a scatter plot to visualize the relationship between daily caffeine consumption and sleep onset time. On the x-axis, I will plot the daily caffeine intake (in mg), and on the y-axis, the time taken to fall asleep (in minutes). If there is a clear upward trend, it may indicate a strong correlation between higher caffeine intake and a longer time to fall asleep.

Another example involves examining days with high cigarette consumption versus days with no or low cigarette consumption to see whether there is a noticeable difference in subjective or objective sleep quality. This could reveal how nicotine intake affects overall restfulness.

Similarly, I will look at variations in social media usage. By comparing days with heavy social media activity (e.g., multiple hours) against days with minimal usage, I can observe whether higher screen time correlates with later bedtimes or decreased sleep quality. 

Lastly, step count trends will be analyzed to see if increases or decreases in daily physical activity align with improvements in sleep onset time or subjective sleep ratings. For instance, if days with higher step counts consistently show better sleep quality, it might suggest that physical activity is a key factor in improving rest.


## Conclusion

By the end of this project, I aim to answer the following questions:

- Which daily habits have the greatest impact on sleep onset time and overall sleep quality?
- Can small, data-driven modifications lead to noticeable improvements in sleep quality?
- Are there significant differences in the impact of social media usage versus caffeine consumption on sleep?
- How can these findings be translated into practical strategies for improving sleep patterns and overall quality of life?

*This project not only aims to enhance sleep quality but also to demonstrate the benefits of data-driven decision making in everyday life.*
