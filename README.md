# Requirements Elicitation Follow-Up Question Generation

## Summary of Artifact

This artifact is designed to generate and evaluate follow-up questions for requirements elicitation interviews using GPT-4o. It helps interviewers improve their questioning strategy by:

1. Generating context-aware follow-up questions based on interview history
2. Evaluating existing questions against 14 quality criteria
3. Generating improved questions that meet specific criteria
4. Conducting self-evaluation of generated questions

The system takes interview transcripts as input (in CSV format) and produces:
- Generated follow-up questions
- Classification of questions against quality criteria
- Improved versions of questions that meet all criteria

This tool was developed to help developers improve their questioning techniques during requirements elicitation interviews, ensuring more effective information gathering and better quality requirements.

## Description of Artifact

### Dataset

The datasets of this work are in /datasets folder.

`study1.csv` - the turn context dataset used in Study 1. Note that some of the data in this file may appear to look like duplicates, but in fact they are just partially the same, which happens because the interviewer's follow-up question depends on a longer previous context that has already been analyzed prior in this dataset. Below is a mock example:

  Data Row 1:
  Interviewee: OK, I want an apartment that has a large kitchen.
  Follow-up Question: What features do you want in the kitchen?
  No. of relevant speaker turns: 1.

  Data Row 2:
  Interviewee: OK, I want an apartment that has a large kitchen.
  Interviewer: What amenities do you want in the kitchen?
  Interviewee: I want the kitchen to have a fireplace and a modern stove.
  Follow-up Question: Alright, you mentioned you want a large kitchen, how big should it be?
  No. of relevant speaker turns: 3.


`study2.csv` - the raw data of 30 interviewee-interviewer pairs used in Study 2, 3 and Side Study.

`survey_results.csv` - the 128 instances survey results from Study 3. Since the question orders are shuffled, we added a column 'origin' to trace back the source of Q1 and Q2 during analysis, where 'origin'=0 means Q1 is from LLM, 'origin'=1 means Q1 is from the human analyst. The columns 'A1' indicates results for comparing which question avoids a mistake better, where 'A1'=1 means Q1 is better, 'A1'=2 means Q2 is better. The rest of the columns correspond to the 5-point scale scores for each question with respect to relevancy (A2), clarity (A3), and informativeness (A4). Note that this file contains the same raw data as study2.csv but also includes results from study 3.

`side_study.csv` - Side Study dataset (same raw data as study2.csv but with results from GPT-4o generation of follow-up questions, and the re-evaluation results) where the interviewer_response column is replaced with LLM-generated questions that attempt to avoid all mistake types. The re-evaluation results are under each mistake type.

### Code
We release the code containing Study 1, 2, 3 and side study prompting procedures in `code.ipynb`.

### 14 Published Papers for Formulating the Mistake Framework
We release references to the 14 published papers in the `references.pdf` file.


## System Requirements

### Required Software
- Python 3.x
- Jupyter Notebook or JupyterLab

### Required Python Packages
- pandas
- openai
- python-dotenv

### API Requirements
- OpenAI API key with access to GPT-4o

## Installation Instructions

1. Clone the repository:
```bash
git clone [repository-url]
cd Requirements-Elicitation-Follow-Up-Question-Generation
```

2. Install required Python packages:
```bash
pip install pandas openai python-dotenv jupyter
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key to the file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Open the Jupyter notebook:
```bash
jupyter notebook code.ipynb
```

## Usage Instructions

1. In the notebook:
   - Update the `OPEN_AI_KEY` variable with your API key
   - Ensure your input CSV files are in the correct format with the following columns:
     - `Interview Domain`
     - `Interview Turns`
     - `Interviewee_Speech`
     - `Interviewer_Response`
     - `Domain`

2. Run the cells in sequence to:
   - Generate follow-up questions
   - Evaluate questions against criteria
   - Generate improved questions
   - Save results to output CSV files

### Input Data Format
The system expects CSV files with the following structure:
- For Study 1:  CSV file with columns for interview domain and turns
- For Study 2 & 3: CSV files with columns for interviewee speech, interviewer response, and domain

### Output
The system generates:
- `study1_out.csv`: Contains generated follow-up questions
- `study2_out.csv`: Contains classifications and improved questions
- `side_study.csv`: Contains questions meeting all criteria and their evaluations

## Steps to Reproduce

1. Reproducing the model predictions for each study requires executing the notebook `code.ipynb`. Detailed instructions about the code are provided in docstrings. 
2. A potential threat to reproducibility is that GPT-4o is a closed-source model by OpenAI. The scores reported in the paper may be subject to minor changes due to repeated updates to the GPT-4o model. Nevertheless, the key findings reported in the paper are likely to remain valid.
3. In this paper, we also conducted surveys with crowdworkers to compare GPT-generarted questions with human follow-up questions. We ran statistical tests to validate our hypotheses. While it is not possible to reproduce the results of these studies directly, we have described our survey design process in detail in the paper. The `dataset` folder contains the examples used in the survey. 


## Author Information 

1. Yuchen Shen - Carnegie Mellon University (yuchens2@andrew.cmu.edu)
2. Anmol Singhal - Carnegie Mellon University (anmolsinghal@cmu.edu)
3. Travis Breaux - Carnegie Mellon University (tdbreaux@andrew.cmu.edu)

## Artifact Location

The artifact can be found at:

## How to cite

If you use this work in your research, please cite:

### APA

Y. Shen, A. Singhal, T.D. Breaux (2025). "Requirements Elicitation Follow-up Question Generation." 33rd IEEE International Requirements Engineering Conference. 

## License

See the [LICENSE](LICENSE) file for details.
