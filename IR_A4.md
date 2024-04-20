**Review Summarization using GPT-2**

This repository contains code for implementing review summarization using GPT-2 and evaluating the generated summaries using ROUGEscores.

**Overview**

The goal of this assignment is to train a GPT-2 model on the Amazon Fine Food Reviews dataset and fine-tune it to generate summaries of product reviews. The generated summaries are then evaluated using ROUGEscores to assess their quality compared to the actual summaries provided in the dataset.

**Dataset**

The Amazon Fine Food Reviews dataset is used for this assignment. It consists of reviews of various food products along with corresponding summaries. The dataset is preprocessed to clean the text and prepare it for training.

**Model Training**

1. **Initialization**:
   1. The GPT-2 tokenizer and model are initialized from the Hugging Face library.
1. **Data Preparation**:
   1. The dataset is divided into training and testing sets.
   1. Custom dataset classes are implemented to tokenize and prepare the data for training.
1. **Fine-Tuning**:
- The GPT-2 model is fine-tuned on the review dataset to generate summaries.
- Different hyperparameters such as learning rate, batch size, and number of epochs are experimented with to optimize the model's performance.

**Evaluation**

After training, ROUGEscores are computed on the test set to assess the model's overall performance. ROUGEmetrics (ROUGE-1,ROUGE-2,and ROUGE-L)are calculated for every predicted summary compared to the actual summary provided in the dataset.

**Results**

- **ROUGE-1**: Precision: 0.7826, Recall: 1.0, F1-Score: 0.8780
- **ROUGE-2**: Precision: 0.6552, Recall: 1.0, F1-Score: 0.7917
- **ROUGE-L**: Precision: 0.7826, Recall: 1.0, F1-Score: 0.8780
- **Example**:
  - **Given Review Text**: "product arrived labeled jumbo salted peanuts the peanut actually small sized unsalted sure error vendor intended represent product jumbo"
  - **Given Summary**: "advertised"
  - **Generated Summary**: "product arrived labeled jumbo salted peanuts the peanut actually small sized unsalted sure error vendor intended represent product jumbo advertised as small size peanuts."
