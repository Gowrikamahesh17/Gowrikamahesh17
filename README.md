<div align="center">

<img src="./assets/gowrika-hero.svg" alt="Gowrika Mahesh — Data Analytics & AI | Agentic AI | GenAI Systems | ML" width="100%"/>

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-gowrikamahesh17.github.io-701A3D?style=for-the-badge&labelColor=10070C)](https://gowrikamahesh17.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gowrika_Mahesh-701A3D?style=for-the-badge&logo=linkedin&logoColor=F8F0F3&labelColor=10070C)](https://www.linkedin.com/in/gowrika-mahesh-092873215/)
[![GitHub](https://img.shields.io/badge/GitHub-gowrikamahesh17-701A3D?style=for-the-badge&logo=github&logoColor=F8F0F3&labelColor=10070C)](https://github.com/gowrikamahesh17)

</div>

---

## 👋 About Me

I'm a **Master's student in Applied Data Science and AI** at SRH University Heidelberg (thesis phase, graduating 03/2027). I build applied AI systems (agentic workflows, RAG and LLM pipelines), and I check carefully whether they actually work, with benchmarks against ground truth and honest baselines.

Before this, I spent two years as a **System Engineer at Merck Group (Sigma-Aldrich)**, supporting infrastructure for 60,000 users and the global Passkey MFA rollout.

- 🔬 Currently working on: my Master's thesis on graph learning for Metal-Organic Framework property prediction (see below), plus ML for drug discovery (blood-brain barrier and P-gp prediction with RDKit, ChemBERTa and PyTorch)
- 🌱 Currently learning: Model Context Protocol (MCP), Polars
- 🗣️ Languages: English (C1), German (A2, improving), Kannada, Hindi
- 📍 Based in Heidelberg, Germany, open to relocation

---

## 🎓 Master's Thesis (in progress)

**Language-Model-Enriched Graph Learning with Black Hole Sparsification for Metal-Organic Framework Property Prediction**
<br/><sub>M.Sc. Applied Data Science and Analytics, SRH University Heidelberg · Thesis exposé submitted September 2026</sub>

My earlier MOFQuantumNet case study found that simple Random Forest and k-NN baselines beat every GNN, because the similarity graph was built from information already in each node's features. The thesis tests whether a graph built from genuinely **different** information can change that.

- **Core idea:** build the graph from frozen ChemBERTa embeddings of each MOF's linker SMILES (MolT5 as a secondary comparison), instead of fingerprints alone.
- **Target and data:** Pore Limiting Diameter (PLD) on a 14,296-MOF dataset, using GCN and GraphSAGE.
- **Sparsification:** tests whether Black Hole graph pruning at 30% and 50% keeps performance on the new graphs, compared with random and k-center sampling.
- **Method:** keeps the leakage-free evaluation protocol from the case study, and treats a second negative result as a valid scientific answer.

**Tech:** PyTorch Geometric, ChemBERTa, RDKit, scikit-learn, FastAPI

---

## 🏆 Achievements and Certifications

**📄 Published research**
- **CitePrism: Human-in-the-Loop AI for Citation Auditing and Editorial Integrity**, arXiv preprint, May 2026, [arXiv:2605.16000](https://arxiv.org/abs/2605.16000)

**🎓 Certifications**
- NVIDIA: *Building LLM Applications with Prompt Engineering* (2025)
- NVIDIA: *Fundamentals of Deep Learning* (2025)
- *Creating Agentic AI Solutions with Microsoft Foundry*
- *Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)*
- *Adding Knowledge to LLMs*

**🎓 Education**
- M.Sc. Applied Data Science and AI, SRH University Heidelberg (04/2025 – 03/2027, expected)
- B.E. Computer Science and Engineering, ATME College of Engineering, Mysuru (2018 – 2022)

---

## 🚀 Selected Projects

| Project | What it does | Tech |
|---|---|---|
| **[CitePrism](https://arxiv.org/abs/2605.16000)**<br/>*LLM citation auditing, co-authored paper* | Automates slow, manual reference verification. A four-tier retrieval fallback with source-grounded prompting stops the model from fabricating citations. Benchmarked against expert labels on 20 papers (Cohen's Kappa 0.429, moderate agreement). | Gemini, Llama-3.1, embeddings, Python |
| **[MOFQuantumNet](https://gowrikamahesh17.github.io)**<br/>*Molecular property prediction* | Audited and reimplemented a GNN pipeline for metal-organic framework properties. Fixed data leakage and test-set reuse, and showed that simple Random Forest and k-NN baselines beat every GNN. Includes a FastAPI console for non-technical users and a 23-page case study. | RDKit, SMILES, PyTorch Geometric, FastAPI |
| **[AI CEO](https://gowrikamahesh17.github.io)**<br/>*Strategic intelligence agent (university project)* | Weekly research-monitoring agent that extracts and summarizes 200+ articles from live sources into structured output. Streamlit UI shows the agent's reasoning steps, with automatic failover between LLM providers. | Gemini, Llama-3.1, Hugging Face, Streamlit |

**Also built:** a responsible-AI healthcare agent (SHAP, LIME, Fairlearn; HIPAA, GDPR and EU AI Act grounding), a multi-agent RAG system for policy documents, and a serverless GCP data pipeline (PySpark, dbt, BigQuery).

👉 More details on my [portfolio](https://gowrikamahesh17.github.io).

---

## 🛠️ My Stack

**Generative and Agentic AI**<br/>
<img src="https://img.shields.io/badge/Python-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=python" alt="Python"/>
<img src="https://img.shields.io/badge/LangGraph-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="LangGraph"/>
<img src="https://img.shields.io/badge/RAG-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="RAG"/>
<img src="https://img.shields.io/badge/ChromaDB-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="ChromaDB"/>
<img src="https://img.shields.io/badge/FAISS-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="FAISS"/>
<img src="https://img.shields.io/badge/Gemini-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=googlegemini" alt="Gemini"/>
<img src="https://img.shields.io/badge/Llama%203.1-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=meta" alt="Llama 3.1"/>
<img src="https://img.shields.io/badge/GPT--4o--mini-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=openai" alt="GPT-4o-mini"/>
<img src="https://img.shields.io/badge/Ollama-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=ollama" alt="Ollama"/>
<img src="https://img.shields.io/badge/Hugging%20Face-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=huggingface" alt="Hugging Face"/>
<img src="https://img.shields.io/badge/Prompt%20Engineering-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="Prompt Engineering"/>
<img src="https://img.shields.io/badge/MCP-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="MCP"/>

**Machine Learning**<br/>
<img src="https://img.shields.io/badge/scikit--learn-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=scikitlearn" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/XGBoost-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="XGBoost"/>
<img src="https://img.shields.io/badge/TensorFlow-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=tensorflow" alt="TensorFlow"/>
<img src="https://img.shields.io/badge/PyTorch-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=pytorch" alt="PyTorch"/>
<img src="https://img.shields.io/badge/PyTorch%20Geometric-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=pyg" alt="PyTorch Geometric"/>
<img src="https://img.shields.io/badge/Fairlearn-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="Fairlearn"/>
<img src="https://img.shields.io/badge/SHAP-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="SHAP"/>
<img src="https://img.shields.io/badge/LIME-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="LIME"/>

**Scientific and Chemical Data**<br/>
<img src="https://img.shields.io/badge/RDKit-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="RDKit"/>
<img src="https://img.shields.io/badge/SMILES-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="SMILES"/>
<img src="https://img.shields.io/badge/ChemBERTa-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="ChemBERTa"/>
<img src="https://img.shields.io/badge/Molecular%20Similarity-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3" alt="Molecular Similarity"/>

**Data and Platforms**<br/>
<img src="https://img.shields.io/badge/SQL-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=mysql" alt="SQL"/>
<img src="https://img.shields.io/badge/Snowflake-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=snowflake" alt="Snowflake"/>
<img src="https://img.shields.io/badge/Palantir%20Foundry-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=palantir" alt="Palantir Foundry"/>
<img src="https://img.shields.io/badge/PySpark-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=apachespark" alt="PySpark"/>
<img src="https://img.shields.io/badge/dbt-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=dbt" alt="dbt"/>
<img src="https://img.shields.io/badge/BigQuery-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=googlebigquery" alt="BigQuery"/>

**Tools and Workflow**<br/>
<img src="https://img.shields.io/badge/Git-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=git" alt="Git"/>
<img src="https://img.shields.io/badge/Docker-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=docker" alt="Docker"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=githubactions" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/FastAPI-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=fastapi" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Streamlit-701A3D?style=for-the-badge&labelColor=10070C&logoColor=F8F0F3&logo=streamlit" alt="Streamlit"/>

---

## 📊 GitHub Stats

<div align="center">

<img src="https://streak-stats.demolab.com/?user=gowrikamahesh17&hide_border=true&background=190B12&ring=C77B9B&fire=C77B9B&currStreakLabel=E5B5C7&sideLabels=E5B5C7&currStreakNum=F8F0F3&sideNums=F8F0F3&dates=B89AA7" alt="Contributions and streak" width="100%"/>

<br/>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=gowrikamahesh17&theme=dark" alt="Total commits, PRs, stars" height="170"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=gowrikamahesh17&theme=dark" alt="Languages" height="170"/>

<br/><br/>

<img src="https://ghchart.rshah.org/701A3D/gowrikamahesh17" alt="GitHub contribution graph" width="100%"/>

<br/><br/>

![Followers](https://img.shields.io/github/followers/gowrikamahesh17?style=for-the-badge&color=701A3D&labelColor=10070C&logo=github&logoColor=F8F0F3)
![Public repos](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/users/gowrikamahesh17&query=$.public_repos&label=Public%20repos&style=for-the-badge&color=701A3D&labelColor=10070C)

</div>

<sub>Live data pulled from my GitHub account by third-party services (public contributions only).</sub>

---

<div align="center">

<img src="./assets/gowrika-footer.svg" alt="Thanks for visiting" width="100%"/>

</div>
