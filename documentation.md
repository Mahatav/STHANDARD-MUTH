# Project Documentation

## 1. Project Overview

### 1.1 Project Statement
- **Problem Statement**: This project is designed to provide relief and comfort to individuals seeking to identify and reconnect with their roots, especially those displaced, moved, or adopted. Accessing reliable and relevant ancestry information can be difficult, particularly for those separated from their family roots. This project aims to use AI to help such individuals trace their lineage by analyzing web search results and providing meaningful insights.
  
- **Objectives**:
  1. Create a user-friendly platform that assists individuals in tracing their ancestry.
  2. Use AI-powered tools to refine web search results and provide the most relevant ancestry information.
  3. Integrate a chatbot to guide users through the process and help interpret the results.

- **Target Audience**: Individuals who have been displaced, adopted, or separated from their family roots.

### 1.2 Proposed Solution
- **Solution Overview**: Our project utilizes the DuckDuckGo API to retrieve search results, which are then processed by Meta’s LLaMA model to refine and present the most relevant ancestry data. The tool also integrates Amazon Q chatbot to provide an interactive interface that guides users through their search and explains the results.

- **Key Features**:
  1. **DuckDuckGo API**: Retrieves top 5 search results based on user input.
  2. **Meta LLaMA**: Processes search results and refines them for relevant ancestry insights.
  3. **Amazon Q Chatbot**: An interactive assistant to guide users through the process and help interpret results.
  4. **Frontend Design**: Clean and intuitive user interface developed using HTML, CSS, and JavaScript, designed in Figma.

- **Expected Impact**: The project aims to assist displaced and adopted individuals in reconnecting with their lineage, providing a reliable and accessible AI-driven tool for ancestry searches. This solution will offer a user-friendly interface and accurate, insightful results, giving users a sense of relief and connection.

### 1.3 Technical Aspects
- **Programming Languages**:
  - **Python**: Backend development, including Flask and LLaMA integration.
  - **JavaScript**: Frontend functionality and chatbot integration.
  - **HTML/CSS**: Frontend design and structure.

- **Frameworks and Libraries**:
  - **Flask**: Handles backend operations and API interactions.
  - **Meta LLaMA**: Used for natural language processing and data refinement.
  - **Amazon Q**: Powers the chatbot functionality for user interaction.
  - **Figma**: UI/UX design tool used to create wireframes and visual designs.
  
---

## 2. Documentation of AI Tools Used

### 2.1 Overview of AI Tools
- **Meta LLaMA**: Processes and refines the top 5 search results retrieved from DuckDuckGo. Its NLP capabilities allow for better ancestry-related data interpretation.
  
- **Amazon Q Chatbot**: Provides users with an interactive interface for asking follow-up questions and refining search results.
  
- **ChatGPT**: Used for generating unit tests and validating key components of the backend and web scraping processes.

### 2.2 Application of AI Tools
- **Meta LLaMA**:
  - **When Applied**: During the data refinement stage after DuckDuckGo search results are fetched.
  - **How Applied**: LLaMA processes the results and extracts the most relevant data for ancestry insights.
  - **Rationale**: Chosen for its NLP capabilities, LLaMA helps generate meaningful outputs from unstructured web data.

- **Amazon Q Chatbot**:
  - **When Applied**: During user interaction, guiding them through the search and result interpretation.
  - **How Applied**: Chatbot allows users to ask questions and get assistance with refining their search queries.
  - **Rationale**: Provides real-time conversational assistance, enhancing user experience.

- **ChatGPT**:
  - **When Applied**: During the testing and validation phases.
  - **How Applied**: ChatGPT generated unit tests for API endpoints and web scraper validation.
  - **Rationale**: Used for efficient and accurate test generation.

### 2.3 Total use of AI Tools
- **Raunak Khanna**:
  - **% Usage**: 30% on brainstorming, 25% on development, 15% on documentation, 30% on testing.
  - **Tools Used**: ChatGPT for unit testing and validation.

- **Mahatav Arora**:
  - **% Usage**: 40% on brainstorming, 35% on development, 10% on documentation, 15% on testing.
  - **Tools Used**: Meta LLaMA and ChatGPT for AI implementation and testing.

- **Aaditya Golash**:
  - **% Usage**: 35% on brainstorming, 25% on development, 20% on documentation, 20% on testing.
  - **Tools Used**: Meta LLaMA for data refinement, Amazon Q for chatbot integration, ChatGPT for testing.

---

## 3. Challenges Faced

### 3.1 API Rate Limits
We encountered rate limitations while using DuckDuckGo's API, restricting the number of queries we could handle. To optimize this, we implemented efficient data handling and query management.

### 3.2 Chatbot Integration
Integrating Amazon Q presented challenges when handling complex user queries. We had to train the AI to understand and respond to ancestry-related queries accurately.

### 3.3 Scalability
Scaling the system to handle large volumes of ancestry search requests required backend and AI processing optimization, which was a key focus during development.

---

## 4. Future Enhancements

### 4.1 Authentication (OAuth)
We plan to implement Google OAuth to enable users to log in, save searches, and return to their ancestry results in future sessions.

### 4.2 Expansion of Data Sources
Future versions will include additional data sources, such as government records and historical databases, to improve the accuracy of results.

### 4.3 Multi-language Support
Support for multiple languages will be added to make the tool accessible to a global audience.

### 4.4 Accessibility Features
We plan to integrate features such as text-to-speech to ensure accessibility for users with disabilities.

---

## 5. Testing and Validation

Unit tests generated by **ChatGPT** were used to ensure the reliability and functionality of the following:
- **API Endpoints**: Tested the DuckDuckGo API integration and ensured that valid results were returned for further processing.
- **Data Processing**: Verified that LLaMA refined the search results and provided accurate outputs.
- **Web Scraper**: Ensured the correct data retrieval and processing from the web without losing relevant information.

---

## 6. Conclusion

The Ancestry Searcher project uses AI-driven tools to provide a powerful platform for individuals to trace their lineage. By integrating DuckDuckGo with Meta LLaMA’s data processing capabilities and Amazon Q's chatbot, the tool offers a unique way for users to discover their ancestry. Future enhancements, including multi-language support, expanded data sources, and accessibility features, will further improve the tool's usability and impact.
