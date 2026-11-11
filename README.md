# Awesome AI for Astronomy

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/Xin-YuXiao/Awesome-AI-for-Astronomy)

A curated list of papers, models, datasets, benchmarks and software for artificial intelligence in astronomy, astrophysics, cosmology, heliophysics and planetary science.

General astronomy resources are covered by [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy), and classical astronomical data science by [awesome-astro-datascience](https://github.com/mpi-astronomy/awesome-astro-datascience). This list tracks machine learning work with public papers, linking public code where it exists, with emphasis on foundation models, language models, agents and benchmarks released since 2021, together with established deep learning methods in each subfield.

**Notes**

1. Entries are sorted chronologically within each subsection by first arXiv version.
2. The venue tag shows the peer-reviewed venue when it is confirmed by the journal DOI, the official repository or the publisher page. Otherwise it shows `arXiv` and the year.
3. Every arXiv identifier, DOI and repository link in this list was checked against the paper page or the official repository README before inclusion. Entries in [Tools and Libraries](#tools-and-libraries) link to the software only.
4. Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry template.

## Contents

- [Surveys and Reviews](#surveys-and-reviews)
- [Foundation Models and Representation Learning](#foundation-models-and-representation-learning)
  - [Images](#images)
  - [Spectra](#spectra)
  - [Time Series](#time-series)
  - [Multimodal](#multimodal)
- [Language and Vision-Language Models](#language-and-vision-language-models)
- [Agents and Retrieval Systems](#agents-and-retrieval-systems)
- [Benchmarks](#benchmarks)
- [Galaxies](#galaxies)
  - [Morphology and Catalogues](#morphology-and-catalogues)
  - [Anomaly Detection](#anomaly-detection)
  - [Physical Properties and Photometric Redshifts](#physical-properties-and-photometric-redshifts)
- [Gravitational Lensing](#gravitational-lensing)
- [Source Detection, Deblending and Image Simulation](#source-detection-deblending-and-image-simulation)
- [Stars and Stellar Spectroscopy](#stars-and-stellar-spectroscopy)
- [Time-Domain Astronomy and Transients](#time-domain-astronomy-and-transients)
- [Exoplanets](#exoplanets)
- [Cosmology and Large-Scale Structure](#cosmology-and-large-scale-structure)
- [Simulation-Based Inference](#simulation-based-inference)
- [High-Energy Astrophysics and Astroparticle Physics](#high-energy-astrophysics-and-astroparticle-physics)
- [Gravitational Waves](#gravitational-waves)
- [Solar Physics and Heliophysics](#solar-physics-and-heliophysics)
- [Radio Astronomy](#radio-astronomy)
- [Planetary Science and Small Bodies](#planetary-science-and-small-bodies)
- [Datasets](#datasets)
  - [Observational Datasets](#observational-datasets)
  - [Simulation Datasets](#simulation-datasets)
- [Tools and Libraries](#tools-and-libraries)
- [Communities and Groups](#communities-and-groups)
- [Related Awesome Lists](#related-awesome-lists)

## Surveys and Reviews

- *Machine Learning in Astronomy: A Practical Overview* `arXiv 2019`  
  [[Paper](https://arxiv.org/abs/1904.07248)]  
  Lecture notes from the IAC Winter School 2018 covering supervised and unsupervised learning for astronomical datasets.

- *The Frontier of Simulation-Based Inference* `PNAS 2020`  
  [[Paper](https://arxiv.org/abs/1911.01429)] [[Journal](https://doi.org/10.1073/pnas.1912789117)]  
  Review of simulation-based inference methods and the role of machine learning in inference with intractable likelihoods.

- *Enhancing Gravitational-Wave Science with Machine Learning* `MLST 2021`  
  [[Paper](https://arxiv.org/abs/2005.03745)] [[Journal](https://doi.org/10.1088/2632-2153/abb93a)]  
  Review of machine learning for LIGO and Virgo data quality, signal modeling, searches and parameter estimation.

- *The Dawes Review 10: The Impact of Deep Learning for the Analysis of Galaxy Surveys* `PASA 2023`  
  [[Paper](https://arxiv.org/abs/2210.01813)] [[Journal](https://doi.org/10.1017/pasa.2022.55)]  
  Review of deep learning applications to galaxy surveys covering classification, property estimation, discovery and cosmological inference.

- *Astronomia ex machina: A History, Primer and Outlook on Neural Networks in Astronomy* `R. Soc. Open Sci. 2023`  
  [[Paper](https://arxiv.org/abs/2211.03796)] [[Journal](https://doi.org/10.1098/rsos.221454)]  
  Historical review of neural networks in astronomy with a primer on deep learning and an outlook on astronomical foundation models.

- *Machine Learning for Observational Cosmology* `Rep. Prog. Phys. 2023`  
  [[Paper](https://arxiv.org/abs/2303.15794)] [[Journal](https://doi.org/10.1088/1361-6633/acd2ea)]  
  Review of machine learning applications in time-domain astronomy, galaxy surveys and emulation for cosmology.

- *Constructing Impactful Machine Learning Research for Astronomy: Best Practices for Researchers and Reviewers* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2310.12528)]  
  Recommendations on baselines, validation, reproducibility and reporting for machine learning papers in astronomy.

- *Deep Learning Based Systems for Crater Detection: A Review* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2310.07727)]  
  Review of CNN, U-Net, R-CNN and transformer crater detection algorithms for the Moon, Mars and Mercury.

- *What is the Role of Large Language Models in the Evolution of Astronomy Research?* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2409.20252)]  
  Use cases, survey results and recommendations on LLM adoption in astronomy research.

- *Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.24047)]  
  Survey of LLM-based scientific agents with a section on astronomy and cosmology applications.

- *From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.14111)] [[Code](https://github.com/AgenticScience/Awesome-Agent-Scientists)]  
  Domain-oriented survey of autonomous scientific discovery including agentic astronomy and cosmology research.

- *A Survey of Scientific Large Language Models: From Data Foundations to Agent Frontiers* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.21148)]  
  Survey of scientific LLMs and their training data, including astronomy datasets and models.

- *The Revolution in Strong Lensing Discoveries from Euclid* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.14624)]  
  Review of how machine learning, citizen science and expert inspection found about 500 high-quality lens candidates in Euclid Q1.

- *Deep Learning in Astrophysics* `ARA&A 2025`  
  [[Paper](https://arxiv.org/abs/2510.10713)]  
  Annual Review covering inductive biases, simulation-based inference, anomaly detection, foundation models, reinforcement learning and LLM agents in astronomy.

- *Advances and Challenges in Solar Flare Prediction: A Review* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.20465)]  
  Review of statistical, physics-based and deep learning flare forecasting including CNN, LSTM and transformer models.

- *Opportunities in AI/ML for the Rubin LSST Dark Energy Science Collaboration* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2601.14235)]  
  LSST DESC roadmap covering photometric redshifts, transient classification, weak lensing inference, foundation models and infrastructure.

- *The Role of Artificial Intelligence in the SKA Era* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.28493)]  
  Chapter on deep learning for source finding, RFI mitigation, imaging, anomaly detection and scheduling for the SKA.

- *Source Finding and Characterisation for SKAO Science* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2607.03736)]  
  Review of classical and machine learning source finding and morphology classification for SKAO surveys.

## Foundation Models and Representation Learning

### Images

- **(SSL-SDSS)** *Self-Supervised Representation Learning for Astronomical Images* `ApJL 2021`  
  [[Paper](https://arxiv.org/abs/2012.13083)] [[Code and Models](https://portal.nersc.gov/project/dasrepo/self-supervised-learning-sdss)] [[Journal](https://doi.org/10.3847/2041-8213/abf2c7)]  
  Contrastive pretraining on about 1.2M SDSS galaxy images, evaluated on morphology classification and photometric redshift estimation.

- **(Galaxy Search)** *Self-Supervised Similarity Search for Large Scientific Datasets* `NeurIPS 2021 Workshop (ML4PS)`  
  [[Paper](https://arxiv.org/abs/2110.13151)] [[Code](https://github.com/georgestein/galaxy_search)]  
  Self-supervised representations of 42M DESI Legacy Imaging Survey galaxies with a public similarity search tool.

- **(Zoobot Representations)** *Practical Galaxy Morphology Tools from Deep Supervised Representation Learning* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2110.12735)] [[Code](https://github.com/mwalmsley/zoobot)]  
  Representations learned from Galaxy Zoo labels reused for similarity search, anomaly finding and new classification tasks.

- **(Zoobot FM)** *Towards Foundation Models for Galaxy Morphology* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2206.11927)] [[Code](https://github.com/mwalmsley/zoobot)]  
  Pretraining galaxy morphology encoders on Galaxy Zoo volunteer responses for transfer to downstream tasks.

- **(Zoobot)** *Zoobot: Adaptable Deep Learning Models for Galaxy Morphology* `JOSS 2023`  
  [[Code](https://github.com/mwalmsley/zoobot)] [[PyPI](https://pypi.org/project/zoobot/)]  
  Pretrained galaxy morphology encoders and finetuning utilities, deployed in the Euclid morphology pipeline.

- **(Rare Galaxy Classes)** *Rare Galaxy Classes Identified In Foundation Model Representations* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2312.02910)] [[Code](https://github.com/mwalmsley/zoobot)]  
  Searches Zoobot representation space for rare morphological classes.

- **(Galaxy Scaling Laws)** *Scaling Laws for Galaxy Images* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2404.02973)] [[Code](https://github.com/mwalmsley/zoobot)]  
  Supervised scaling study on 840k galaxy images with over 100M Galaxy Zoo annotations.

- **(AstroPT)** *AstroPT: Scaling Large Observation Models for Astronomy* `ICML 2024 Workshop (AI4Science)`  
  [[Paper](https://arxiv.org/abs/2405.14930)] [[Euclid Paper](https://arxiv.org/abs/2503.15312)] [[Code](https://github.com/Smith42/astroPT)] [[Model](https://huggingface.co/Smith42/astroPT_v2.0)]  
  Autoregressive transformers from 1M to 2.1B parameters pretrained on 8.6M DESI Legacy Survey galaxy images.

### Spectra

- **(SDSS-VAE)** *Dimensionality Reduction of SDSS Spectra with Variational Autoencoders* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2002.10464)] [[Code](https://github.com/stephenportillo/SDSS-VAE)]  
  Variational autoencoder compression of SDSS galaxy spectra into a low-dimensional latent space.

- **(Cycle-StarNet)** *Cycle-StarNet: Bridging the Gap between Theory and Data by Leveraging Large Data Sets* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2007.03109)] [[Code](https://github.com/teaghan/Cycle_SN)] [[Journal](https://doi.org/10.3847/1538-4357/abca96)]  
  Domain adaptation between synthetic and observed stellar spectra with cycle-consistent networks.

- **(spender)** *Autoencoding Galaxy Spectra I: Architecture* `AJ 2023`  
  [[Paper](https://arxiv.org/abs/2211.07890)] [[Code](https://github.com/pmelchior/spender)] [[Journal](https://doi.org/10.3847/1538-3881/ace0ff)]  
  Attentive convolutional autoencoder that models galaxy spectra in the rest frame with explicit redshifting and resampling, trained on SDSS-II.

- **(Stellar FM)** *Towards an Astronomical Foundation Model for Stars with a Transformer-Based Model* `MNRAS 2024`  
  [[Paper](https://arxiv.org/abs/2308.10944)] [[Code](https://github.com/henrysky/astroNN_stars_foundation)]  
  Transformer trained on cross-survey APOGEE, Gaia and 2MASS data that performs discriminative and generative stellar tasks without task-specific finetuning.

- **(SpectraFM)** *SpectraFM: Tuning into Stellar Foundation Models* `NeurIPS 2024 Workshop (FM4Science)`  
  [[Paper](https://arxiv.org/abs/2411.04750)]  
  Transformer pretrained on synthetic stellar spectra and transferred to real spectra across wavelength ranges.

- *Applying Vision Transformers on Spectral Analysis of Astronomical Objects* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.00294)]  
  Converts one-dimensional spectra into images for pretrained ViT backbones in classification and regression.

- **(SpecCLIP)** *SpecCLIP: Aligning and Translating Spectroscopic Measurements for Stars* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2507.01939)] [[LoRA Fine-tuning](https://arxiv.org/abs/2507.20972)]  
  Contrastive alignment of LAMOST low-resolution and Gaia XP spectra foundation models for parameter estimation and cross-spectrum prediction.

- **(OmniSpectra)** *OmniSpectra: A Unified Foundation Model for Native Resolution Astronomical Spectra* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2601.15351)]  
  Masked-modeling transformer pretrained on 5.5 million spectra from eight surveys at native resolution.

### Time Series

- **(ASTROMER)** *ASTROMER: A Transformer-Based Embedding for the Representation of Light Curves* `A&A 2023`  
  [[Paper](https://arxiv.org/abs/2205.01677)] [[Code](https://github.com/astromer-science)] [[Journal](https://doi.org/10.1051/0004-6361/202243928)] [[Astromer 2](https://arxiv.org/abs/2502.02717)]  
  Self-supervised light-curve encoder pretrained with masked magnitude prediction on MACHO R-band data.

- **(Astroconformer)** *Astroconformer: The Prospects of Analyzing Stellar Light Curves with Transformer-Based Deep Learning Models* `MNRAS 2024`  
  [[Paper](https://arxiv.org/abs/2309.16316)] [[Journal](https://doi.org/10.1093/mnras/stae068)] [[Workshop Version](https://arxiv.org/abs/2207.02787)]  
  Conformer model for Kepler light curves that infers surface gravity and frequency of maximum oscillation power.

- **(Maven)** *Maven: A Multimodal Foundation Model for Supernova Science* `MLST 2024`  
  [[Paper](https://arxiv.org/abs/2408.16829)] [[Code](https://github.com/ThomasHelfer/multimodal-supernovae)]  
  Contrastive alignment of supernova photometry and spectroscopy, pretrained on 0.5M synthetic events and finetuned on ZTF.

- **(FALCO)** *FALCO: A Foundation Model of Astronomical Light Curves for Time Domain Astronomy* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2504.20290)]  
  Self-supervised transformer on Kepler light curves for variability classification, surface gravity estimation and flare identification.

- *What Does Self-supervision Add to Engineered Features for Stellar Light Curves?* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2610.14283)]  
  Measures the information that self-supervised light-curve encoders add beyond engineered periodogram and variability features.

### Multimodal

- **(AstroCLIP)** *AstroCLIP: A Cross-Modal Foundation Model for Galaxies* `MNRAS 2024`  
  [[Paper](https://arxiv.org/abs/2310.03024)] [[Code](https://github.com/PolymathicAI/AstroCLIP)] [[Journal](https://doi.org/10.1093/mnras/stae1450)]  
  Contrastive alignment of DESI galaxy images and spectra in a shared embedding space.

- **(MPP)** *Multiple Physics Pretraining for Physical Surrogate Models* `NeurIPS 2024`  
  [[Paper](https://arxiv.org/abs/2310.02994)] [[Code](https://github.com/PolymathicAI/multiple_physics_pretraining)]  
  Autoregressive pretraining of a single surrogate model across heterogeneous physical simulation systems.

- **(PAPERCLIP)** *PAPERCLIP: Associating Astronomical Observations and Natural Language with Multi-Modal Models* `COLM 2024`  
  [[Paper](https://arxiv.org/abs/2403.08851)] [[Code](https://github.com/smsharma/PAPERCLIP-Hubble)]  
  CLIP finetuned on Hubble Space Telescope observations paired with observing proposal abstracts.

- **(AstroM3)** *AstroM3: A Self-Supervised Multimodal Model for Astronomy* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2411.08842)] [[Code](https://github.com/MeriDK/AstroM3)]  
  Trimodal CLIP-style pretraining on variable-star light curves, spectra and metadata.

- **(AION-1)** *AION-1: Omnimodal Foundation Model for Astronomical Sciences* `NeurIPS 2025`  
  [[Paper](https://arxiv.org/abs/2510.17960)] [[Code](https://github.com/PolymathicAI/AION)] [[Model](https://huggingface.co/polymathic-ai/aion-base)]  
  Token-based masked modeling over 39 modalities from Legacy Survey, HSC, SDSS, DESI and Gaia, released at 300M to 3.1B parameters.

## Language and Vision-Language Models

- **(astroBERT)** *Building astroBERT, a Language Model for Astronomy & Astrophysics* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2112.00590)] [[Model](https://huggingface.co/adsabs/astroBERT)]  
  BERT model with 110M parameters trained on NASA ADS papers for named entity recognition and classification.

- **(AstroLLaMA)** *AstroLLaMA: Towards Specialized Foundation Models in Astronomy* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2309.06126)] [[Model](https://huggingface.co/universeTBD)]  
  LLaMA-2-7B finetuned on over 300k astro-ph abstracts.

- **(AstroLLaMA-Chat)** *AstroLLaMA-Chat: Scaling AstroLLaMA with Conversational and Diverse Datasets* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2401.01916)] [[Model](https://huggingface.co/universeTBD)]  
  Continual pretraining on abstracts, introductions and conclusions followed by domain conversational finetuning.

- **(cosmosage)** *cosmosage: A Natural-Language Assistant for Cosmology* `Astron. Comput. 2025`  
  [[Paper](https://arxiv.org/abs/2407.04420)] [[Code](https://github.com/tijmen/cosmosage)] [[Model](https://huggingface.co/Tijmen2/cosmosage-v3.1)] [[Journal](https://doi.org/10.1016/j.ascom.2025.100934)]  
  Cosmology assistant built by continued pretraining on cosmology papers and textbooks followed by question-answer finetuning.

- **(AstroLLaMA-2-70B)** *AstroMLab 2: AstroLLaMA-2-70B Model and Benchmarking Specialised LLMs for Astronomy* `SC 2024 Workshop (AI4S)`  
  [[Paper](https://arxiv.org/abs/2409.19750)] [[Model](https://huggingface.co/AstroMLab)]  
  Releases AstroLLaMA-3-8B and AstroLLaMA-2-70B and reports that the 7B AstroLLaMA series underperforms its base model.

- **(AstroSage-8B)** *AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model* `Sci. Rep. 2025`  
  [[Paper](https://arxiv.org/abs/2411.09012)] [[Model](https://huggingface.co/AstroMLab/AstroSage-8B)] [[Journal](https://doi.org/10.1038/s41598-025-97131-y)]  
  Llama-3.1-8B with continued pretraining on about 250k astro-ph and gr-qc preprints, SFT and model merging. Scores 80.9% on AstroMLab 1.

- **(Astro-HEP-BERT)** *Astro-HEP-BERT: A Bidirectional Language Model for Studying the Meanings of Concepts in Astrophysics and High Energy Physics* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2411.14877)] [[Model](https://huggingface.co/arnosimons/astro-hep-bert)]  
  BERT model adapted to astrophysics and high energy physics literature for concept analysis.

- **(AstroLLaVA)** *AstroLLaVA: Towards the Unification of Astronomical Data and Natural Language* `ICLR 2025 Workshop (SCI-FM)`  
  [[Paper](https://arxiv.org/abs/2504.08583)] [[Code](https://github.com/UniverseTBD/AstroLLaVA)]  
  LLaVA finetuned on about 30k captioned images from APOD, ESO and Hubble for astronomical visual question answering.

- **(AstroSage-70B)** *AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.17592)] [[Model](https://huggingface.co/AstroMLab/AstroSage-70B-20251009)]  
  Llama-3.1-70B with continued pretraining and reasoning-chain SFT. Scores 89.0% on a validated 3,846-question subset of AstroMLab 1.

- *Rethinking Domain Specialization for Open-Ended Scientific Reasoning in Astronomy Language Models* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2609.17644)]  
  Evaluates whether continued pretraining and instruction tuning on astronomy corpora help open-ended scientific reasoning.

## Agents and Retrieval Systems

- **(pathfinder)** *pathfinder: A Semantic Framework for Literature Review and Knowledge Discovery in Astronomy* `ApJS 2024`  
  [[Paper](https://arxiv.org/abs/2408.01556)] [[Demo](https://pfdr.app)]  
  Retrieval-augmented literature search and synthesis over about 350k ADS papers with time and citation weighting.

- **(cmbagent)** *Multi-Agent System for Cosmological Parameter Analysis* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2412.00431)] [[Follow-up](https://arxiv.org/abs/2507.07257)] [[Code](https://github.com/CMBAgents/cmbagent)]  
  Planning and control system of about 30 LLM agents for autonomous cosmological data analysis.

- **(StarWhisper Telescope)** *StarWhisper Telescope: An AI Framework for Automating End-to-End Astronomical Observations* `Commun. Eng. 2025`  
  [[Paper](https://arxiv.org/abs/2412.06412)] [[Code](https://github.com/Yu-Yang-Li/StarWhisper)] [[Journal](https://doi.org/10.1038/s44172-025-00520-4)]  
  LLM agent that plans observations, controls a 10-telescope network and runs transient detection for the Nearby Galaxy Supernovae Survey.

- **(AstroAgents)** *AstroAgents: A Multi-Agent AI for Hypothesis Generation from Mass Spectrometry Data* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.23170)] [[Code](https://github.com/amirgroup-codes/AstroAgents)]  
  Multi-agent system that proposes astrobiology hypotheses from mass spectrometry data.

- *AI Agents for Ground-Based Gamma Astronomy* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.00821)]  
  LLM agent prototypes for CTAO control software and Gammapy analysis code generation with retrieval augmentation.

- **(AI Cosmologist)** *The AI Cosmologist I: An Agentic System for Automated Data Analysis* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2504.03424)] [[Code](https://github.com/adammoss/aicosmologist)]  
  Agents for planning, coding, execution, analysis and synthesis that run machine learning experiments on cosmological datasets.

- **(Mephisto)** *Mephisto: Self-Improving Large Language Model-Based Agents for Automated Interpretation of Multi-band Galaxy Observations* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.08354)] [[Short Paper](https://arxiv.org/abs/2409.14807)] [[Code](https://zenodo.org/records/15589045)]  
  Multi-agent tree search over CIGALE SED models with a self-updating knowledge base, applied to JWST Little Red Dots.

- **(Denario)** *The Denario Project: Deep Knowledge AI Agents for Scientific Discovery* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.26887)] [[Code](https://github.com/AstroPilot-AI/Denario)] [[Demo](https://huggingface.co/spaces/astropilot-ai/Denario)]  
  Modular multi-agent research assistant for idea generation, analysis and paper drafting, using cmbagent as its analysis backend.

- **(CTAgent / Gammapygpt)** *Domain-Specific Agents for Cherenkov Telescope Array Control Software and Gamma-Ray Data Analysis* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.01299)]  
  Agents that generate and validate CTAO control software and Gammapy analysis scripts with automated self-correction.

- **(auto_research)** *A Semi-autonomous Multi-agent Pipeline for High-energy Astrophysics Research with Enforced Provenance and Verifiable Self-extension* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2611.05251)]  
  Multi-agent pipeline that retrieves HEASARC data and writes its own tools, tested by reproducing IXPE polarimetry results.

## Benchmarks

- **(MLGWSC-1)** *MLGWSC-1: The First Machine Learning Gravitational-Wave Search Mock Data Challenge* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2209.11146)] [[Code](https://github.com/gwastro/ml-mock-data-challenge-1)]  
  Common datasets and metrics for comparing machine learning gravitational-wave search algorithms.

- **(AstroMLab 1)** *AstroMLab 1: Who Wins Astronomy Jeopardy!?* `Astron. Comput. 2025`  
  [[Paper](https://arxiv.org/abs/2407.11194)]  
  4,425 multiple-choice questions curated from the Annual Review of Astronomy and Astrophysics for evaluating LLM knowledge recall.

- **(AstroVisBench)** *AstroVisBench: A Code Benchmark for Scientific Computing and Visualization in Astronomy* `NeurIPS 2025 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2505.20538)] [[Code](https://github.com/SebaJoe/AstroVisBench)] [[Project](https://astrovisbench.github.io)]  
  864 processing and visualization tasks from 110 NOIRLab and STScI notebooks, scored by execution and a VLM judge.

- **(AstroMMBench)** *AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Models Capabilities in Astronomy* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.00063)]  
  621 expert-reviewed multiple-choice questions on astronomical images across six subfields, used to evaluate 25 MLLMs.

- **(IOAA)** *Large Language Models Achieve Gold Medal Performance at the International Olympiad on Astronomy & Astrophysics (IOAA)* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.05016)]  
  Evaluates five LLMs on 49 theory and 8 data analysis problems from the 2022 to 2025 IOAA exams.

- *A Systematic Evaluation of Vision-Language Models for Observational Astronomical Reasoning Tasks* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2604.24589)]  
  Benchmark of vision-language models on reasoning over real multi-modal observational data.

## Galaxies

### Morphology and Catalogues

- **(GaMorNet)** *Galaxy Morphology Network: A Convolutional Neural Network Used to Study Morphology and Quenching in ~100,000 SDSS and ~20,000 CANDELS Galaxies* `ApJ 2020`  
  [[Paper](https://arxiv.org/abs/2006.14639)] [[Code](https://github.com/aritraghsh09/GaMorNet)]  
  CNN pretrained on simulated galaxies and transferred to SDSS and CANDELS bulge-to-total classification.

- **(GZ DECaLS)** *Galaxy Zoo DECaLS: Detailed Visual Morphology Measurements from Volunteers and Deep Learning for 314,000 Galaxies* `MNRAS 2022`  
  [[Paper](https://arxiv.org/abs/2102.08414)] [[Code](https://github.com/mwalmsley/zoobot)] [[Data](https://doi.org/10.5281/zenodo.4196266)] [[Journal](https://doi.org/10.1093/mnras/stab2093)]  
  7.5M volunteer classifications and Bayesian CNN posteriors for 314k DECaLS galaxies.

- *A Comparison of Deep Learning Architectures for Optical Galaxy Morphology Classification* `ICECET 2021`  
  [[Paper](https://arxiv.org/abs/2111.04353)] [[Journal](https://doi.org/10.1109/ICECET52533.2021.9698414)]  
  Compares deep learning architectures for optical galaxy morphology classification using the Zoobot library.

- **(DeepAstroUDA)** *DeepAstroUDA: Semi-Supervised Universal Domain Adaptation for Cross-Survey Galaxy Morphology Classification and Anomaly Detection* `MLST 2023`  
  [[Paper](https://arxiv.org/abs/2302.02005)] [[Code](https://github.com/deepskies/DeepAstroUDA)]  
  Universal domain adaptation between SDSS, DECaLS and LSST mock images that also clusters unknown classes.

- *Harnessing the Hubble Space Telescope Archives: A Catalogue of 21,926 Interacting Galaxies* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2303.00366)]  
  Zoobot-based search of the HST archive for interacting galaxies.

- **(Astroformer)** *Astroformer: More Data Might Not be All You Need for Classification* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2304.05350)] [[Code](https://github.com/Rishit-dagli/Astroformer)]  
  Hybrid transformer and convolutional classifier trained in the low-data regime on Galaxy10 DECals.

- *Transfer Learning for Galaxy Feature Detection: Finding Giant Star-forming Clumps in Low Redshift Galaxies Using Faster R-CNN* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2312.03503)]  
  Object detection of star-forming clumps in galaxy images with transfer learning.

- *Euclid Preparation. Measuring Detailed Galaxy Morphologies for Euclid with Machine Learning* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2402.10187)]  
  Zoobot trained to predict detailed morphology for Euclid imaging.

- *Uncovering Tidal Treasures: Automated Classification of Faint Tidal Features in DECaLS Data* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2404.06487)]  
  Classification of faint tidal features in DECaLS images using pretrained morphology models.

- *Galaxy Zoo: Stronger Bars Facilitate Quenching in Star-forming Galaxies* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2405.05960)]  
  Uses deep learning bar classifications to study the link between bar strength and quenching.

- *Galaxy Zoo DESI: Large-scale Bars as a Secular Mechanism for Triggering AGN* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2406.20096)]  
  Uses Galaxy Zoo DESI deep learning morphologies to study bars and AGN.

- *Euclid Q1: Exploring Galaxy Morphology across Cosmic Time through Sersic Fits* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15309)]  
  Euclid Q1 morphology study listed among Zoobot applications.

- *Euclid Q1: First Visual Morphology Catalogue* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15310)]  
  First Euclid visual morphology catalogue produced with Galaxy Zoo volunteers and Zoobot.

- *Euclid Q1: A First Look at the Fraction of Bars in Massive Galaxies at z < 1* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15311)]  
  Bar fraction measurement in Euclid Q1 using machine learning morphology.

- *Euclid Q1: A Census of Dwarf Galaxies across a Range of Distances and Environments* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15335)]  
  Dwarf galaxy census in Euclid Q1 listed among Zoobot applications.

### Anomaly Detection

- **(Weirdest Galaxies)** *The Weirdest SDSS Galaxies: Results from an Outlier Detection Algorithm* `MNRAS 2017`  
  [[Paper](https://arxiv.org/abs/1611.07526)] [[Code](https://github.com/dalya/WeirdestGalaxies)] [[Journal](https://doi.org/10.1093/mnras/stw3021)]  
  Unsupervised random forest outlier scores for about two million SDSS galaxy spectra.

- **(Sequencer)** *Extracting the Main Trend in a Dataset: the Sequencer Algorithm* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2006.13948)] [[Code](https://github.com/dalya/Sequencer)]  
  Unsupervised ordering algorithm that recovers one-dimensional trends in spectra and other datasets.

- **(Astronomaly)** *Astronomaly: Personalised Active Anomaly Detection in Astronomical Data* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2010.11202)] [[Protege](https://arxiv.org/abs/2411.04188)] [[Code](https://github.com/MichelleLochner/astronomaly)]  
  Active learning framework that combines anomaly scores with user feedback to rank interesting objects.

- **(HSC Anomalies)** *Anomaly Detection in Hyper Suprime-Cam Galaxy Images with Generative Adversarial Networks* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2105.02434)] [[Code](https://github.com/kstoreyf/anomalies-GAN-HSC)] [[Workshop Version](https://arxiv.org/abs/2012.08082)]  
  Wasserstein GAN anomaly scores for HSC galaxy images.

- **(DeepAdversaries)** *DeepAdversaries: Examining the Robustness of Deep Learning Models for Galaxy Morphology Classification* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2111.00961)] [[Code](https://github.com/AleksCipri/DeepAdversaries)]  
  Studies the robustness of galaxy morphology classifiers to image perturbations.

- *Astronomaly at Scale: Searching for Anomalies Amongst 4 Million Galaxies* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2309.08660)]  
  Applies Astronomaly to about 4M galaxies using pretrained Zoobot representations.

- *Enabling Unsupervised Discovery in Astronomical Images through Self-Supervised Representations* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2311.14157)]  
  Self-supervised features with clustering, artefact removal, anomaly detection and similarity search on survey images.

- **(AnomalyMatch)** *AnomalyMatch: Discovering Rare Objects of Interest with Semi-supervised and Active Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.03509)]  
  FixMatch with EfficientNet and a user-in-the-loop active learning interface, integrated into ESA Datalabs.

- **(AnomalyMatch HLA)** *Identifying Astrophysical Anomalies in 99.6 Million Source Cutouts from the Hubble Legacy Archive Using AnomalyMatch* `A&A 2025`  
  [[Paper](https://arxiv.org/abs/2505.03508)]  
  Applies AnomalyMatch to the full Hubble Legacy Archive and reports 1,176 new anomalies across 19 classes.

- **(Coniferest)** *Coniferest: A Complete Active Anomaly Detection Framework* `Astron. Comput. 2025`  
  [[Code](https://github.com/snad-space/coniferest)] [[Journal](https://doi.org/10.1016/j.ascom.2025.100960)]  
  Isolation-forest based active anomaly detection with expert feedback, used by the SNAD team on ZTF data.

- *Re-envisioning Euclid Galaxy Morphology: Identifying and Interpreting Features with Sparse Autoencoders* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.23749)]  
  Sparse autoencoders on Zoobot and masked-autoencoder embeddings of Euclid Q1 galaxies to surface interpretable features.

- **(astromorph)** *astromorph: Self-supervised Machine Learning Pipeline for Astronomical Morphology Analysis* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2602.09223)]  
  BYOL-based embedding pipeline applied to ALMA protoplanetary disks and infrared dark clouds.

- *Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2608.23688)]  
  DINOv2 light-curve embeddings, isolation forests and multimodal LLM agents that vet anomaly candidates.

### Physical Properties and Photometric Redshifts

- **(ANNz2)** *ANNz2: Photometric Redshift and Probability Distribution Function Estimation Using Machine Learning* `PASP 2016`  
  [[Paper](https://arxiv.org/abs/1507.00490)] [[Code](https://github.com/IftachSadeh/ANNZ)]  
  Ensembles of neural networks and boosted decision trees for photometric redshift PDFs.

- **(Delight)** *Data-driven, Interpretable Photometric Redshifts Trained on Heterogeneous and Unrepresentative Data* `ApJ 2017`  
  [[Paper](https://arxiv.org/abs/1612.00847)] [[Code](https://github.com/ixkael/Delight)]  
  Gaussian process photometric redshifts that combine templates with data-driven flux modeling.

- **(Pasquet Photo-z)** *Photometric Redshifts from SDSS Images Using a Convolutional Neural Network* `A&A 2019`  
  [[Paper](https://arxiv.org/abs/1806.06607)] [[Code](https://github.com/jpasquet/photoz)]  
  CNN that predicts redshift probability densities directly from multiband SDSS images.

- **(dense_basis)** *Nonparametric Star Formation History Reconstruction with Gaussian Processes. I. Counting Major Episodes of Star Formation* `ApJ 2019`  
  [[Journal](https://doi.org/10.3847/1538-4357/ab2052)] [[Code](https://github.com/kartheikiyer/dense_basis)]  
  Gaussian process representation of galaxy star formation histories for SED fitting.

- **(speculator)** *SPECULATOR: Emulating Stellar Population Synthesis for Fast and Accurate Galaxy Spectra and Photometry* `ApJS 2020`  
  [[Paper](https://arxiv.org/abs/1911.11778)] [[Code](https://github.com/justinalsing/speculator)] [[Journal](https://doi.org/10.3847/1538-4365/ab917f)]  
  Neural network emulator of stellar population synthesis for fast SED fitting.

- **(PROVABGS)** *The DESI PRObabilistic Value-Added Bright Galaxy Survey (PROVABGS) Mock Challenge* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2202.01809)] [[Code](https://github.com/changhoonhahn/provabgs)]  
  Bayesian SED modeling pipeline for DESI BGS that uses neural emulators for speed.

- **(SEDflow)** *Accelerated Bayesian SED Modeling Using Amortized Neural Posterior Estimation* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2203.07391)] [[Code](https://github.com/changhoonhahn/SEDflow)] [[Journal](https://doi.org/10.3847/1538-4357/ac7b84)]  
  Amortized neural posterior estimation of 12 SED parameters in about one second per galaxy.

- **(GaMPEN)** *GaMPEN: A Machine-learning Framework for Estimating Bayesian Posteriors of Galaxy Morphological Parameters* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2207.05107)] [[Code](https://github.com/aritraghsh09/GaMPEN)]  
  Bayesian CNN that predicts posteriors of bulge-to-total ratio, effective radius and flux.

- **(Mangrove)** *Mangrove: Learning Galaxy Properties from Merger Trees* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2210.13473)] [[Code](https://github.com/astrockragh/Mangrove)]  
  Graph neural networks on dark matter merger trees that emulate semi-analytic galaxy properties.

- **(SBI++)** *SBI++: Flexible, Ultra-fast Likelihood-free Inference Customized for Astronomical Applications* `ApJL 2023`  
  [[Paper](https://arxiv.org/abs/2304.05281)] [[Code](https://github.com/wangbingjie/sbi_pp)]  
  Neural posterior estimation for galaxy SED fitting that handles missing data and out-of-distribution noise.

- **(pzflow)** *Probabilistic Forward Modeling of Galaxy Catalogs with Normalizing Flows* `AJ 2024`  
  [[Paper](https://arxiv.org/abs/2405.04740)] [[Code](https://github.com/jfcrenshaw/pzflow)]  
  Normalizing flows for modeling galaxy catalogs and photometric redshift posteriors.

- *Galaxy Spectroscopy without Spectra: Galaxy Properties from Photometric Images with Conditional Diffusion Models* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2406.18175)]  
  Diffusion model with contrastive networks that predicts optical spectra and photometric redshifts from SDSS images.

- **(CLAP)** *CLAP. I. Resolving Miscalibration for Deep Learning-based Galaxy Photometric Redshift Estimation* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2410.19390)]  
  Supervised contrastive learning with adaptive KNN to calibrate photometric redshift probability densities.

- **(Hybrid-z)** *Hybrid-z: Enhancing the Kilo-Degree Survey Bright Galaxy Sample Photometric Redshifts with Deep Learning* `A&A 2025`  
  [[Paper](https://arxiv.org/abs/2501.01942)]  
  Inception CNN on four-band images combined with an MLP on nine-band magnitudes for 1.2 million KiDS-Bright galaxies.

- **(RAIL)** *Redshift Assessment Infrastructure Layers (RAIL): Rubin-era Photometric Redshift Stress-testing and At-scale Production* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.02928)] [[Code](https://github.com/LSSTDESC/rail)]  
  LSST DESC framework for training, evaluating and running photometric redshift estimators.

- *Template-Fitting Meets Deep Learning: Redshift Estimation Using Physics-Guided Neural Networks* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2507.00866)]  
  Multimodal network with cross-attention and Bayesian layers that integrates SED templates on HSC PDR3 data.

- *Deep Learning Improves Photometric Redshifts in All Regions of Color Space* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2507.06299)]  
  Self-organizing map analysis showing lower scatter and attenuation bias for image-based photo-z on SDSS.

- **(PITA)** *Optimizing Deep Learning Photometric Redshifts for the Roman Space Telescope with HST/CANDELS* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2602.10207)]  
  Semi-supervised network that combines contrastive, color and redshift losses on CANDELS images.

## Gravitational Lensing

- **(CMU DeepLens)** *CMU DeepLens: Deep Learning for Automatic Image-based Galaxy-Galaxy Strong Lens Finding* `MNRAS 2018`  
  [[Paper](https://arxiv.org/abs/1703.02642)] [[Code](https://github.com/McWilliamsCenter/CMUDeepLens)]  
  Residual network strong lens finder.

- **(DeepMass)** *Deep Learning Dark Matter Map Reconstructions from DES SV Weak Lensing Data* `MNRAS 2020`  
  [[Paper](https://arxiv.org/abs/1908.00543)] [[Code](https://github.com/NiallJeffrey/DeepMass)]  
  U-Net mass mapping of Dark Energy Survey Science Verification weak lensing data.

- **(Substructure Mining)** *Mining for Dark Matter Substructure: Inferring Subhalo Population Properties from Strong Lenses with Machine Learning* `arXiv 2019`  
  [[Paper](https://arxiv.org/abs/1909.02005)] [[Code](https://github.com/smsharma/mining-for-substructure-lens)]  
  Likelihood-ratio estimation with neural networks for subhalo population inference from lensed images.

- **(DeepLense)** *Deep Learning the Morphology of Dark Matter Substructure* `ApJ 2020`  
  [[Journal](https://doi.org/10.3847/1538-4357/ab7925)] [[Code](https://github.com/ML4SCI/DeepLense)]  
  Classifies strong lensing images by dark matter substructure type with deep learning.

- **(ovejero)** *Hierarchical Inference with Bayesian Neural Networks: An Application to Strong Gravitational Lensing* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2010.13787)] [[Code](https://github.com/swagnercarena/ovejero)]  
  Bayesian neural networks for population-level lens parameter inference.

- **(h0rton)** *Large-scale Gravitational Lens Modeling with Bayesian Neural Networks for Accurate and Precise Inference of the Hubble Constant* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2012.00042)] [[Code](https://github.com/jiwoncpark/h0rton)]  
  Bayesian neural network lens modeling for time-delay cosmography.

- **(deeplenstronomy)** *deeplenstronomy: A Dataset Simulation Package for Strong Gravitational Lensing* `JOSS 2021`  
  [[Paper](https://arxiv.org/abs/2102.02830)] [[Code](https://github.com/deepskies/deeplenstronomy)] [[Journal](https://doi.org/10.21105/joss.02854)]  
  Configuration-driven simulation of strong lensing training sets for deep learning.

- **(Lens Mining)** *Mining for Strong Gravitational Lenses with Self-supervised Learning* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2110.00023)] [[Code](https://github.com/georgestein/ssl-legacysurvey)]  
  Self-supervised representations of DESI Legacy Survey images used to find new strong lens candidates.

- **(GIGA-Lens)** *GIGA-Lens: Fast Bayesian Inference for Strong Gravitational Lens Modeling* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2202.07663)] [[Code](https://github.com/giga-lens/gigalens)]  
  GPU-accelerated lens modeling with gradient-based optimization, variational inference and HMC.

- **(paltas)** *From Images to Dark Matter: End-to-end Inference of Substructure from Hundreds of Strong Gravitational Lenses* `ApJ 2023`  
  [[Paper](https://arxiv.org/abs/2203.00690)] [[Code](https://github.com/swagnercarena/paltas)]  
  Simulation-based inference of subhalo mass function parameters from many lenses.

- **(Score Lensing)** *Posterior Samples of Source Galaxies in Strong Gravitational Lenses with Score-Based Priors* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2211.03812)] [[Code](https://github.com/AlexandreAdam/score_models)]  
  Score-based generative priors for lensed source reconstruction.

- **(caustics)** *Caustics: A Python Package for Accelerated Strong Gravitational Lensing Simulations* `JOSS 2024`  
  [[Paper](https://arxiv.org/abs/2406.15542)] [[Code](https://github.com/Ciela-Institute/caustics)]  
  Differentiable, GPU-accelerated lensing simulator for machine learning workflows.

- *Euclid: Finding Strong Gravitational Lenses in the Early Release Observations Using Convolutional Neural Networks* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2502.09802)]  
  Five CNN lens finders applied to 13 Euclid ERO fields, followed by visual inspection and spectroscopic confirmation.

- *Euclid Q1: The Strong Lensing Discovery Engine A, System Overview and Lens Catalogue* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15324)]  
  Overview of the Euclid Q1 strong lens search combining volunteers and machine learning.

- *Euclid Q1: The Strong Lensing Discovery Engine C, Finding Lenses with Machine Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15326)]  
  Machine learning lens finders applied to Euclid Q1.

- *Euclid Q1: The Strong Lensing Discovery Engine D, Double-Source-Plane Lens Candidates* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15327)]  
  Double-source-plane lens candidates from the Euclid Q1 search.

- *Euclid Q1: The Strong Lensing Discovery Engine E, Ensemble Classification of Strong Gravitational Lenses* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15328)]  
  Ensemble classification of lens candidates and lessons for Euclid DR1.

- **(LEMON)** *Euclid Quick Data Release (Q1). LEMON -- Lens Modelling with Neural Networks. Automated and Fast Modelling of Euclid Gravitational Lenses with a Singular Isothermal Ellipsoid Mass Profile* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.15329)]  
  Bayesian neural network that predicts lens mass and light parameters and initialises classical lens modelling.

- **(GLUE I)** *Gravitational Lenses in UNIONS and Euclid (GLUE) I: A Search for Strong Gravitational Lenses in UNIONS with Subaru, CFHT, and Pan-STARRS Data* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.05032)]  
  ResNet lens finder based on CMU-DeepLens applied to 8 million UNIONS galaxies.

- *Euclid Quick Data Release (Q1). Searching for Giant Gravitational Arcs in Galaxy Clusters with Mask Region-based Convolutional Neural Networks* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.03064)]  
  Mask R-CNN instance segmentation of cluster-scale lensed arcs trained on Euclidised HST simulations.

## Source Detection, Deblending and Image Simulation

- **(scarlet)** *scarlet: Source Separation in Multi-band Images by Constrained Matrix Factorization* `Astron. Comput. 2018`  
  [[Paper](https://arxiv.org/abs/1802.10157)] [[Code](https://github.com/pmelchior/scarlet)] [[Journal](https://doi.org/10.1016/j.ascom.2018.07.001)]  
  Constrained matrix factorization deblender for multiband survey images.

- **(Astro R-CNN)** *Deblending and Classifying Astronomical Sources with Mask R-CNN Deep Learning* `MNRAS 2019`  
  [[Journal](https://doi.org/10.1093/mnras/stz2845)] [[Code](https://github.com/burke86/astro_rcnn)]  
  Instance segmentation for joint detection, deblending and star-galaxy classification.

- **(DeblenderVAE)** *Deblending Galaxies with Variational Autoencoders: A Joint Multi-band, Multi-instrument Approach* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2005.12039)] [[Code](https://github.com/LSSTDESC/DeblenderVAE)] [[Updated Code](https://github.com/astrodeepnet/debvader)]  
  VAE-based deblender trained jointly on ground and space-based simulated images.

- **(galsim-hub)** *Deep Generative Models for Galaxy Image Simulations* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2008.03833)] [[Code](https://github.com/McWilliamsCenter/galsim_hub)]  
  Conditional generative models of galaxy light profiles integrated with GalSim.

- **(MuyGPs Star-Galaxy)** *Star-Galaxy Separation via Gaussian Processes with Model Reduction* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2010.06094)] [[Code](https://github.com/LLNL/MuyGPyS)]  
  Gaussian process classification of stars and galaxies with dimensionality reduction.

- **(PS1 Point Source Catalog II)** *A Morphological Classification Model to Identify Unresolved PanSTARRS1 Sources II: Update to the PS1 Point Source Catalog* `PASP 2021`  
  [[Paper](https://arxiv.org/abs/2012.01544)] [[Code](https://github.com/adamamiller/PS1_star_galaxy)]  
  Random forest star and galaxy separation for Pan-STARRS1 sources.

- **(MuyGPs Star-Galaxy Images)** *Star-Galaxy Image Separation with Computationally Efficient Gaussian Process Classification* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2105.01106)] [[Code](https://github.com/LLNL/MuyGPyS)]  
  Scalable local Gaussian process classification of star and galaxy image cutouts.

- **(MuyGPs Blends)** *Gaussian Process Classification of Galaxy Blend Identification in LSST* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2107.09246)] [[Code](https://github.com/LLNL/MuyGPyS)]  
  Gaussian process classifiers that flag blended galaxies in simulated LSST images.

- **(astroddpm)** *Realistic Galaxy Image Simulation via Score-Based Generative Models* `MNRAS 2022`  
  [[Paper](https://arxiv.org/abs/2111.01713)] [[Code](https://github.com/Smith42/astroddpm)]  
  Denoising diffusion models that generate realistic galaxy images.

- **(WaveDiff)** *Rethinking Data-driven Point Spread Function Modeling with a Differentiable Optical Model* `Inverse Problems 2023`  
  [[Paper](https://arxiv.org/abs/2203.04908)] [[Code](https://github.com/CosmoStat/wf-psf)]  
  Differentiable wavefront-based PSF model that captures chromatic variations for Euclid-like telescopes.

- **(MuyGPs Stellar Blends)** *Stellar Blend Image Classification Using Computationally Efficient Gaussian Processes* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2407.19297)] [[Code](https://github.com/LLNL/MuyGPyS)]  
  Scalable Gaussian process classification of blended stellar images.

- *Denoising Diffusion Probabilistic Model for Realistic and Fast Generated Euclid-like Data for Weak Lensing Analysis* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2504.07183)]  
  DDPM trained on CANDELS images that generates Euclid-like galaxies for shear calibration.

- **(BTK)** *The Blending ToolKit: A Simulation Framework for Evaluation of Galaxy Detection and Deblending* `OJAp 2025`  
  [[Journal](https://doi.org/10.33232/001c.129699)] [[Code](https://github.com/LSSTDESC/BlendingToolKit)]  
  Simulation and metrics framework for benchmarking detection and deblending algorithms.

- **(GalaxySD)** *Can AI Dream of Unseen Galaxies? Conditional Diffusion Model for Galaxy Morphology Augmentation* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.16233)]  
  Stable Diffusion fine-tuned on Galaxy Zoo 2 morphology prompts to augment classifiers and find rare dusty early-type galaxies.

- **(GalCatDiff)** *Category-based Galaxy Image Generation via Diffusion Models* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.16255)]  
  Class-conditioned diffusion model with residual attention blocks trained on Galaxy10 DECaLS categories.

- *Diffusion-based Galaxy Simulations for the Roman High Latitude Survey* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2604.22917)]  
  DDPM trained on JWST JADES imaging to generate Roman-like multi-band galaxy stamps for weak lensing.

- **(scarlet2)** *scarlet2: Astronomical Scene Modeling in JAX* `JOSS 2026`  
  [[Code](https://github.com/pmelchior/scarlet2)] [[Journal](https://doi.org/10.21105/joss.09646)]  
  JAX scene modeling for multi-band, multi-epoch and multi-instrument data with neural network priors.

## Stars and Stellar Spectroscopy

- **(astroNN)** *Deep Learning of Multi-element Abundances from High-resolution Spectroscopic Data* `MNRAS 2019`  
  [[Paper](https://arxiv.org/abs/1808.04428)] [[Code](https://github.com/henrysky/astroNN)] [[Journal](https://doi.org/10.1093/mnras/sty3217)]  
  Bayesian neural networks for stellar parameters and abundances from APOGEE spectra.

- **(Blancato CNN)** *Data-driven Derivation of Stellar Properties from Photometric Time Series Data Using Convolutional Neural Networks* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2005.09682)] [[Code](https://github.com/kblancato/theia-net)]  
  CNNs that infer stellar rotation and surface gravity from Kepler light curves.

- **(stella)** *stella: Convolutional Neural Networks for Flare Identification in TESS* `JOSS 2020`  
  [[Journal](https://doi.org/10.21105/joss.02347)] [[Code](https://github.com/afeinstein20/stella)]  
  CNN flare detection in TESS two-minute light curves.

- **(LightPred)** *Accurate and Robust Stellar Rotation Periods Catalog for 82771 Kepler Stars Using Deep Learning* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2407.06858)]  
  LSTM and transformer model pretrained contrastively on Kepler light curves and trained on spot-model simulations.

- *Predicting Metallicities and Carbon Abundances from Gaia XP Spectra for (Carbon-enhanced) Metal-poor Stars* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2410.11077)]  
  Heteroscedastic neural network ensemble that predicts [Fe/H] and [C/Fe] for more than 10 million XP stars.

- *Mapping the Milky Way with Gaia Bp/Rp Spectra I: Systematic Flux Corrections and Atmospheric Parameters for 68 Million Stars* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2411.19105)]  
  APOGEE-trained network that corrects XP flux systematics before model-atmosphere fitting.

- **(UA-CSNet)** *Metallicities of 20 Million Giant Stars Based on Gaia XP Spectra* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.05281)]  
  Uncertainty-aware cost-sensitive network that estimates metallicities down to [Fe/H] about -4 for giants.

- *Millions of Main-Sequence Binary Stars from Gaia BP/RP Spectra* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2507.09622)]  
  Neural spectral emulator of single stars used to identify more than 14 million binary candidates from XP spectra.

- *The Use of Conditional Variational Autoencoders in Generating Stellar Spectra* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.17059)]  
  CVAE that generates stellar spectra over a grid of atmospheric parameters, rotation and instrumental resolution.

- **(EBOP MAVEN)** *EBOP MAVEN: A Machine Learning Model to Estimate the Input Parameters for Analytic Fitting of Detached Eclipsing Binary Light Curves* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.21465)]  
  CNN that predicts detached eclipsing binary parameters from phase-folded TESS light curves to initialise JKTEBOP fits.

- *A Generalist Model Including Evolved Star Mass and Age* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2603.03732)]  
  Extends a transformer stellar foundation model to infer mass and age of giants from Gaia XP spectra.

- **(ASTRAFier)** *ASTRAFier: A Novel and Scalable Transformer-based Stellar Variability Classifier* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2604.07437)]  
  BiLSTM, attention and CNN classifier applied to about 2.8 million TESS light curves.

## Time-Domain Astronomy and Transients

- **(snmachine)** *Photometric Supernova Classification with Machine Learning* `ApJS 2016`  
  [[Paper](https://arxiv.org/abs/1603.00882)] [[Rubin Study](https://arxiv.org/abs/2107.07531)] [[Code](https://github.com/LSSTDESC/snmachine)]  
  Feature extraction and classifier pipeline for photometric supernova typing.

- **(SuperNNova)** *SuperNNova: An Open-Source Framework for Bayesian, Neural Network Based Supernova Classification* `MNRAS 2020`  
  [[Paper](https://arxiv.org/abs/1901.06384)] [[Code](https://github.com/supernnova/SuperNNova)] [[Journal](https://doi.org/10.1093/mnras/stz3312)]  
  Recurrent and Bayesian neural networks for light-curve classification.

- **(DeepStreaks)** *DeepStreaks: Identifying Fast-moving Objects in the Zwicky Transient Facility Data with Deep Learning* `MNRAS 2019`  
  [[Paper](https://arxiv.org/abs/1904.05920)] [[Code](https://github.com/dmitryduev/DeepStreaks)]  
  CNN ensemble that identifies streaks from fast-moving near-Earth objects in ZTF images.

- **(braai)** *Real-bogus Classification for the Zwicky Transient Facility Using Deep Learning* `MNRAS 2019`  
  [[Paper](https://arxiv.org/abs/1907.11259)] [[Code](https://github.com/dmitryduev/braai)]  
  CNN real-bogus classifier deployed in the ZTF alert pipeline.

- **(Cyclic-Permutation Networks)** *Classification of Periodic Variable Stars with Novel Cyclic-permutation Invariant Neural Networks* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2011.01243)] [[Code](https://github.com/kmzzhang/periodicnetwork)]  
  Phase-folded light-curve classifiers that are invariant to cyclic permutations.

- **(SCoPe)** *The ZTF Source Classification Project: I. Methods and Infrastructure* `AJ 2021`  
  [[Paper](https://arxiv.org/abs/2102.11304)] [[Code](https://github.com/ZwickyTransientFacility/scope)] [[Journal](https://doi.org/10.3847/1538-3881/abe853)]  
  Modular machine learning framework for classifying variable sources in ZTF light curves.

- **(Time-Series Transformer)** *Paying Attention to Astronomical Transients: Introducing the Time-series Transformer for Photometric Classification* `RASTI 2024`  
  [[Paper](https://arxiv.org/abs/2105.06178)] [[Code](https://github.com/tallamjr/astronet)]  
  Transformer classifier for multiband transient light curves evaluated on PLAsTiCC.

- **(SCONE)** *SCONE: Supernova Classification with a Convolutional Neural Network* `AJ 2021`  
  [[Paper](https://arxiv.org/abs/2106.04370)] [[Code](https://github.com/helenqu/scone)] [[Early-time Paper](https://arxiv.org/abs/2111.05539)]  
  CNN on wavelength-time heatmaps of supernova light curves.

- **(Roman Microlensing NPE)** *Real-time Likelihood-free Inference of Roman Binary Microlensing Events with Amortized Neural Posterior Estimation* `AJ 2021`  
  [[Code](https://github.com/kmzzhang/nbi)] [[Journal](https://doi.org/10.3847/1538-3881/abf42e)]  
  ResNet-GRU featurizer and normalizing flow that infer binary microlensing parameters in real time.

- **(ACAI)** *Phenomenological Classification of the Zwicky Transient Facility Astronomical Event Alerts* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2111.12142)] [[Code](https://github.com/dmitryduev/acai)]  
  Multi-label deep learning classifiers for ZTF alert phenomenology.

- **(MuyGPs Light Curves)** *Light Curve Completion and Forecasting Using Fast and Scalable Gaussian Processes (MuyGPs)* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2208.14592)] [[Code](https://github.com/LLNL/MuyGPyS)]  
  Scalable Gaussian processes for filling gaps in and forecasting light curves.

- *Identifying Light-curve Signals with a Deep-learning-based Object Detection Algorithm. II. A General Light-curve Classification Framework* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2311.08080)]  
  Object-detection based classifier on light curves and power spectra from Kepler, TESS and ZTF.

- **(BTSbot)** *The Zwicky Transient Facility Bright Transient Survey. III. BTSbot: Automated Identification and Follow-up of Bright Transients with Deep Learning* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2401.15167)] [[Follow-up](https://arxiv.org/abs/2512.11957)] [[Code](https://github.com/nabeelre/BTSbot)]  
  Multimodal CNN that selects bright transients for automated spectroscopic follow-up.

- **(CATS)** *Transient Classifiers for Fink* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2404.08798)]  
  Tree-based and deep learning classifiers in the Fink broker evaluated on ELAsTiCC, including the CATS architecture.

- **(ORACLE)** *ORACLE: A Real-Time, Hierarchical, Deep-Learning Photometric Classifier for the LSST* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2501.01496)] [[Code](https://github.com/uiucsn/ORACLE)]  
  Hierarchical recurrent classifier for real-time LSST alert streams.

- **(AMPEL)** *AMPEL Workflows for LSST: Modular and Reproducible Real-time Photometric Classification* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2501.16511)]  
  SNGuess, FollowMe and FinalBet classification channels for ELAsTiCC alerts.

- *Real-Time Active Learning for Optimised Spectroscopic Follow-up: Enhancing Early SN Ia Classification with the Fink Broker* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2502.19555)]  
  Active learning loop on the Fink stream that selects spectroscopic targets to improve early SN Ia classifiers.

- **(PIE-ADA)** *PIE-ADA: Physics-Informed Ensemble with Adaptive Data Augmentation for Photometric Transient Classification* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.29367)]  
  Physics-motivated light-curve augmentation for rare classes combined with gradient boosted ensembles.

- **(NAPTIME)** *NAPTIME: A Neural-Process Framework for Rubin Alert Classification* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2607.19236)]  
  Neural process that jointly reconstructs and classifies sparse multiband light curves on ELAsTiCC2 and MALLORN.

## Exoplanets

- **(Pearson Exoplanet AI)** *Searching for Exoplanets Using Artificial Intelligence* `MNRAS 2018`  
  [[Paper](https://arxiv.org/abs/1706.04319)] [[Code](https://github.com/pearsonkyle/Exoplanet-Artificial-Intelligence)]  
  Neural networks that detect transit signals in simulated and Kepler light curves.

- **(AstroNet)** *Identifying Exoplanets with Deep Learning: A Five-planet Resonant Chain around Kepler-80 and an Eighth Planet around Kepler-90* `AJ 2018`  
  [[Journal](https://doi.org/10.3847/1538-3881/aa9e09)] [[Code](https://github.com/google-research/exoplanet-ml)]  
  CNN transit classifier for Kepler threshold crossing events.

- **(HELA)** *Supervised Machine Learning for Analysing Spectra of Exoplanetary Atmospheres* `Nature Astronomy 2018`  
  [[Paper](https://arxiv.org/abs/1806.03944)] [[Code](https://github.com/exoclime/HELA)]  
  Random forest atmospheric retrieval for exoplanet transmission spectra.

- **(ExoGAN)** *ExoGAN: Retrieving Exoplanetary Atmospheres Using Deep Convolutional Generative Adversarial Networks* `AJ 2018`  
  [[Paper](https://arxiv.org/abs/1806.02906)] [[Code](https://github.com/ucl-exoplanets/ExoGAN_public)]  
  Generative adversarial network for atmospheric retrieval.

- **(AstroNet-K2)** *Identifying Exoplanets with Deep Learning II: Two New Super-Earths Uncovered by a Neural Network in K2 Data* `AJ 2019`  
  [[Paper](https://arxiv.org/abs/1903.10507)] [[Code](https://github.com/aedattilo/models_K2)]  
  AstroNet adapted to K2 light curves.

- **(Astronet-Triage)** *Identifying Exoplanets with Deep Learning III: Automated Triage and Vetting of TESS Candidates* `AJ 2019`  
  [[Paper](https://arxiv.org/abs/1904.02726)] [[Code](https://github.com/yuliang419/Astronet-Triage)] [[Journal](https://doi.org/10.3847/1538-3881/ab21d6)]  
  Neural networks for triage and vetting of TESS transit signals.

- **(SPOCK)** *Predicting the Long-term Stability of Compact Multiplanet Systems* `PNAS 2020`  
  [[Paper](https://arxiv.org/abs/2007.06521)] [[Follow-up](https://arxiv.org/abs/2408.08873)] [[Code](https://github.com/dtamayo/spock)]  
  Gradient boosted classifier on short N-body integrations that predicts multiplanet stability.

- **(BNN Chaos)** *A Bayesian Neural Network Predicts the Dissolution of Compact Planetary Systems* `PNAS 2021`  
  [[Paper](https://arxiv.org/abs/2101.04117)] [[Code](https://github.com/MilesCranmer/bnn_chaos_model)]  
  Bayesian neural network that predicts instability times of compact planetary systems.

- **(MARGE)** *Accurate Machine-learning Atmospheric Retrieval via a Neural-network Surrogate Model for Radiative Transfer* `PSJ 2021`  
  [[Code](https://github.com/exosports/MARGE)] [[Journal](https://doi.org/10.3847/PSJ/abe3fd)]  
  Neural surrogate for radiative transfer that accelerates exoplanet atmospheric retrieval.

- **(ExoMiner)** *ExoMiner: A Highly Accurate and Explainable Deep Learning Classifier that Validates 301 New Exoplanets* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2111.10009)] [[Code](https://github.com/nasa/ExoMiner)] [[Journal](https://doi.org/10.3847/1538-4357/ac4399)]  
  Multi-branch network that mimics expert vetting diagnostics and validates 301 Kepler planets.

- **(HSR4HCI)** *Half-sibling Regression Meets Exoplanet Imaging: PSF Modeling and Subtraction Using a Flexible, Domain Knowledge-driven, Causal Framework* `A&A 2022`  
  [[Paper](https://arxiv.org/abs/2204.03439)] [[Code](https://github.com/timothygebhard/hsr4hci)]  
  Data-driven PSF subtraction for high-contrast imaging based on half-sibling regression.

- **(SBI-EAR)** *Neural Posterior Estimation for Exoplanetary Atmospheric Retrieval* `A&A 2023`  
  [[Paper](https://arxiv.org/abs/2301.06575)] [[Code](https://github.com/MalAstronomy/sbi-ear)]  
  Normalizing-flow posterior estimation for exoplanet atmospheric retrieval.

- **(AESTRA)** *AESTRA: Deep Learning for Precise Radial Velocity Estimation in the Presence of Stellar Activity* `AJ 2024`  
  [[Paper](https://arxiv.org/abs/2311.18326)] [[Code](https://github.com/yanliang-astro/aestra)] [[Journal](https://doi.org/10.3847/1538-3881/ad0e01)] [[Paper II](https://arxiv.org/abs/2606.13574)]  
  Self-supervised spectrum autoencoder and RV estimator that separate Doppler shifts from activity-induced line-profile changes.

- **(FlopPITy)** *FlopPITy: Enabling Self-consistent Exoplanet Atmospheric Retrievals with Machine Learning* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2401.04168)]  
  Sequential neural posterior estimation with neural spline flows for self-consistent atmospheric retrievals.

- **(FMPE Retrieval)** *Flow Matching for Atmospheric Retrieval of Exoplanets: Where Reliability Meets Adaptive Noise Levels* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2410.21477)]  
  Flow matching posterior estimation with importance sampling to verify retrievals and estimate the evidence.

- **(FASTER)** *Near-instantaneous Atmospheric Retrievals and Model Comparison with FASTER* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2502.18045)]  
  Neural ratio estimation for marginal posteriors and amortized Bayesian model comparison, applied to WASP-39b.

- *Exoplanet Transit Candidate Identification in TESS Full-Frame Images via a Transformer-Based Algorithm* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2502.07542)]  
  Convolutional embeddings and transformer encoder applied to flux, centroid and background series of 4.1 million light curves.

- **(DART-Vetter)** *DART-Vetter: A Deep LeARning Tool for Automatic Triage of Exoplanet Candidates* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.05556)]  
  Compact CNN on phase-folded light curves that triages TESS and Kepler threshold crossing events.

- *Towards the Habitable Worlds Observatory: Retrieval of Reflection Spectra from Evolving Earth Analogues Using 1D CNNs* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.00076)]  
  1D CNN retrieval of composition and planetary properties from HWO-like reflected-light spectra.

- *Supervised Machine Learning Methods with Uncertainty Quantification for Exoplanet Atmospheric Retrievals from Transmission Spectroscopy* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.04982)]  
  Benchmark of PLS, SVM, KNN, tree ensembles and XGBoost on Ariel-like transmission spectra.

- *Exoplanetary Atmospheres Retrieval via a Quantum Extreme Learning Machine* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.03617)]  
  Quantum extreme learning machine retrieval executed on IBM quantum hardware.

- *Identifying Exoplanets with Deep Learning: A CNN and RNN Classifier for Kepler DR25 and Candidate Vetting* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.04793)]  
  CNN, bidirectional LSTM and attention classifier for Kepler DR25 transit signals.

- **(WATSON-Net)** *WATSON-Net: Vetting, Validation, and Analysis of Transits from Space Observations with Neural Networks* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.08768)]  
  Multi-branch network for transit vetting integrated into the SHERLOCK pipeline.

- **(RAVEN)** *Automatic Search for Transiting Planets in TESS-SPOC FFIs with RAVEN: Over 100 Newly Validated Planets and Over 2000 Vetted Candidates* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2603.22597)]  
  Machine learning classifiers trained on injected simulations combined with statistical validation for TESS FFI candidates.

- **(ExoNet)** *ExoNet: Calibrated Multimodal Deep Learning for TESS Exoplanet Candidate Vetting Using Phase-Folded Light Curves, Stellar Parameters, and Multi-Head Attention* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2604.15560)]  
  Late fusion of light-curve CNN features with attention and stellar parameters, calibrated by temperature scaling.

## Cosmology and Large-Scale Structure

- **(CosmoGAN)** *Creating Virtual Universes Using Generative Adversarial Networks* `arXiv 2017`  
  [[Paper](https://arxiv.org/abs/1706.02390)] [[Code](https://github.com/MustafaMustafa/cosmoGAN)]  
  GAN that generates weak lensing convergence maps.

- **(IMNN)** *Automatic Physical Inference with Information Maximizing Neural Networks* `PRD 2018`  
  [[Journal](https://doi.org/10.1103/PhysRevD.97.083004)] [[Code](https://github.com/tomcharnock/IMNN)]  
  Neural compression that maximises Fisher information for downstream inference.

- **(NNhealpix)** *Convolutional Neural Networks on the HEALPix Sphere: A Pixel-based Algorithm and Its Application to CMB Data Analysis* `A&A 2019`  
  [[Journal](https://doi.org/10.1051/0004-6361/201935211)] [[Code](https://github.com/ai4cmb/NNhealpix)]  
  Pixel-based convolutions on HEALPix maps applied to CMB analysis.

- **(3DcosmoGAN)** *Cosmological N-body Simulations: A Challenge for Scalable Generative Models* `arXiv 2019`  
  [[Paper](https://arxiv.org/abs/1908.05519)] [[Code](https://github.com/nperraud/3DcosmoGAN)]  
  Scalable 3D GAN for N-body density fields.

- **(Symbolic DL)** *Discovering Symbolic Models from Deep Learning with Inductive Biases* `NeurIPS 2020`  
  [[Paper](https://arxiv.org/abs/2006.11287)] [[Code](https://github.com/MilesCranmer/symbolic_deep_learning)]  
  Graph networks distilled into symbolic expressions, including a dark matter halo example.

- **(FlowPM)** *FlowPM: Distributed TensorFlow Implementation of the FastPM Cosmological N-body Solver* `Astron. Comput. 2021`  
  [[Paper](https://arxiv.org/abs/2010.11847)] [[Code](https://github.com/DifferentiableUniverseInitiative/flowpm)]  
  Differentiable particle-mesh N-body simulation for gradient-based inference and hybrid ML models.

- **(LDL)** *Learning Effective Physical Laws for Generating Cosmological Hydrodynamics with Lagrangian Deep Learning* `PNAS 2021`  
  [[Paper](https://arxiv.org/abs/2010.02926)] [[Code](https://github.com/biweidai/LDL)]  
  Learned displacement layers that map dark matter simulations to baryonic fields.

- **(deep21)** *deep21: A Deep Learning Method for 21cm Foreground Removal* `JCAP 2021`  
  [[Paper](https://arxiv.org/abs/2010.15843)] [[Code](https://github.com/tlmakinen/deep21)] [[Journal](https://doi.org/10.1088/1475-7516/2021/04/081)]  
  3D UNet ensemble that separates cosmological HI signal from radio foregrounds.

- **(Stellar Streams SBI)** *Towards Constraining Warm Dark Matter with Stellar Streams through Neural Simulation-based Inference* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2011.14923)] [[Code](https://github.com/JoeriHermans/constraining-dark-matter-with-stellar-streams-and-ml)]  
  Neural ratio estimation for dark matter constraints from stream density variations.

- **(Moment Networks)** *Solving High-dimensional Parameter Inference: Marginal Posterior Densities & Moment Networks* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2011.05991)] [[Code](https://github.com/NiallJeffrey/MomentNetworks)]  
  Networks that estimate marginal posterior moments for high-dimensional inference.

- **(ForSE)** *ForSE: A GAN-based Algorithm for Extending CMB Foreground Models to Subdegree Angular Scales* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2011.02221)] [[Code](https://github.com/ai4cmb/ForSE)] [[Journal](https://doi.org/10.3847/1538-4357/abe71c)]  
  GAN that adds small-scale non-Gaussian structure to Galactic dust foreground maps.

- **(DeepSphere)** *DeepSphere: A Graph-based Spherical CNN* `ICLR 2020`  
  [[Paper](https://arxiv.org/abs/2012.15000)] [[Code](https://github.com/deepsphere/deepsphere-pytorch)]  
  Graph convolutions on spherical sky maps such as HEALPix.

- **(globalemu)** *GLOBALEMU: A Novel and Robust Approach for Emulating the Sky-averaged 21-cm Signal from the Cosmic Dawn and Epoch of Reionization* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2104.04336)] [[Code](https://github.com/htjb/globalemu)]  
  Neural network emulator of the global 21-cm signal.

- **(CosmoPower)** *CosmoPower: Emulating Cosmological Power Spectra for Accelerated Bayesian Inference from Next-generation Surveys* `MNRAS 2022`  
  [[Paper](https://arxiv.org/abs/2106.03846)] [[Code](https://github.com/alessiospuriomancini/cosmopower)] [[Journal](https://doi.org/10.1093/mnras/stac064)]  
  Neural emulators of CMB and matter power spectra.

- **(FieldIMNNs)** *Lossless, Scalable Implicit Likelihood Inference for Cosmological Fields* `JCAP 2021`  
  [[Paper](https://arxiv.org/abs/2107.07405)] [[Code](https://github.com/tlmakinen/FieldIMNNs)] [[Journal](https://doi.org/10.1088/1475-7516/2021/11/049)]  
  Information maximising neural network compression of Gaussian and lognormal fields followed by simulation-based inference.

- **(HaloGraphNet)** *Inferring Halo Masses with Graph Neural Networks* `ApJ 2022`  
  [[Paper](https://arxiv.org/abs/2111.08683)] [[Code](https://github.com/PabloVD/HaloGraphNet)]  
  Graph neural networks trained on CAMELS to infer halo masses from galaxy properties.

- **(harmonic)** *Machine Learning Assisted Bayesian Model Comparison: Learnt Harmonic Mean Estimator* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2111.12720)] [[Code](https://github.com/astro-informatics/harmonic)] [[Flow Version](https://arxiv.org/abs/2307.00048)]  
  Learned harmonic mean estimator of the Bayesian evidence from posterior samples.

- **(DeepMass CMB)** *Single Frequency CMB B-mode Inference with Realistic Foregrounds from a Single Training Image* `MNRAS Letters 2021`  
  [[Paper](https://arxiv.org/abs/2111.01138)] [[Code](https://github.com/NiallJeffrey/DeepMass)]  
  Moment networks trained on a single foreground image for CMB B-mode inference.

- **(DeepLSS)** *DeepLSS: Breaking Parameter Degeneracies in Large-scale Structure with Deep Learning Analysis of Combined Probes* `PRX 2022`  
  [[Paper](https://arxiv.org/abs/2203.09616)] [[Code](https://github.com/tomaszkacprzak/deeplss)]  
  Deep learning analysis of combined weak lensing and galaxy clustering maps.

- **(LINNA)** *LINNA: Likelihood Inference Neural Network Accelerator* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2203.05583)] [[Code](https://github.com/chto/linna)]  
  Neural network emulation of the likelihood for accelerated cosmological parameter inference.

- **(CosmoGraphNet)** *Learning Cosmology and Clustering with Cosmic Graphs* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2204.13713)] [[Code](https://github.com/PabloVD/CosmoGraphNet)]  
  Graph neural networks on galaxy catalogues for cosmological parameter inference.

- **(CONNECT)** *CONNECT: A Neural Network Based Framework for Emulating Cosmological Observables and Cosmological Parameter Inference* `JCAP 2023`  
  [[Paper](https://arxiv.org/abs/2205.15726)] [[Code](https://github.com/AarhusCosmology/connect_public)]  
  Iteratively trained emulators of CLASS observables for MCMC.

- **(21cmVAE)** *21cmVAE: A Very Accurate Emulator of the 21 cm Global Signal* `ApJ 2022`  
  [[Journal](https://doi.org/10.3847/1538-4357/ac6424)] [[Code](https://github.com/christianhbye/21cmVAE)]  
  Variational autoencoder emulator of the global 21-cm signal.

- **(CosmoPower-JAX)** *CosmoPower-JAX: High-dimensional Bayesian Inference with Differentiable Cosmological Emulators* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2305.06347)] [[Code](https://github.com/dpiras/cosmopower-jax)]  
  JAX version of CosmoPower for gradient-based samplers.

- *In Search of Global 21-cm Signal Using Artificial Neural Network in Light of ARCADE 2* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2306.02039)]  
  Neural network that extracts global 21-cm parameters from antenna temperatures with foregrounds and ionospheric distortion.

- **(Capse.jl)** *Capse.jl: Efficient and Auto-differentiable CMB Power Spectra Emulation* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2307.14339)] [[Code](https://github.com/CosmologicalEmulators/Capse.jl)]  
  Julia neural emulator of CMB power spectra for gradient-based samplers.

- **(21cmEMU)** *21cmEMU: An Emulator of 21cmFAST Summary Observables* `MNRAS 2024`  
  [[Paper](https://arxiv.org/abs/2309.05697)] [[Code](https://github.com/21cmfast/21cmEMU)]  
  Neural emulator of 21cmFAST power spectra and global signals.

- *Optimal Neural Summarisation for Full-Field Weak Lensing Cosmological Implicit Inference* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2407.10877)] [[Code](https://github.com/DifferentiableUniverseInitiative/sbi_lens)]  
  Compares neural compression losses against an HMC full-field reference with a differentiable lognormal simulator.

- *Simulation-based Inference Benchmark for Weak Lensing Cosmology* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2409.17975)]  
  Compares simulation budgets of explicit and implicit full-field inference for LSST Y10-like convergence maps.

- *Nonlinear Reconstruction of 21cm Global Signal from 21cm Power Spectrum with Artificial Neural Networks* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2412.20862)]  
  Neural network that predicts the global 21-cm signal from power spectrum measurements under SKA-like noise.

- **(Effort.jl)** *Effort.jl: A Fast and Differentiable Emulator for the Effective Field Theory of the Large Scale Structure of the Universe* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2501.04639)] [[Code](https://github.com/CosmologicalEmulators/Effort.jl)]  
  Differentiable neural emulator of EFTofLSS galaxy power spectra.

- *Dark Energy Survey Year 3 Results: wCDM Cosmology from Simulation-based Inference with Persistent Homology on the Sphere* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.13439)]  
  Spherical persistent homology summaries with neural compression and likelihood estimation on DES Y3 lensing maps.

- **(21cmLSTM / 21cmKAN)** *Emulating Global 21 cm Cosmology Observations from the Lunar Far Side to Achieve Quick and Reliable Physical Constraints* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.00976)] [[Code](https://github.com/jdorigojones/21cmKAN)]  
  LSTM and Kolmogorov-Arnold network emulators of the global 21-cm signal for Bayesian inference.

- *Exploring the Early Universe with Deep Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.22018)]  
  Benchmark of deep learning models that recover the neutral hydrogen fraction from 2D 21-cm power spectra.

- *Dark Energy Survey Year 3 Results: Simulation-based wCDM Inference from Weak Lensing and Galaxy Clustering Maps with Deep Learning. I. Analysis Design* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.04681)]  
  Graph CNN compression of spherical lensing and clustering maps with normalizing-flow likelihoods.

- *Fast End-to-End Framework for Cosmological Parameter Inference from CMB Data Using Machine Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.01291)]  
  Combines analytical blind separation of foregrounds with neural network parameter inference.

- *Deep-learning Mitigation of Foregrounds and Beam Effects in 21-cm Intensity Mapping Using Hybrid Frequency Differencing and PCA* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.15072)]  
  Two-channel UNet with frequency-differenced and PCA-cleaned inputs for HI reconstruction under realistic beams.

- *Dark Energy Survey Year 3 Results: Optimized wCDM Simulation-based Inference with Weak Lensing Map-level Hybrid Statistics* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.11309)]  
  Hybrid power spectrum and neural summaries that compress DES Y3 lensing maps to seven statistics.

- *Field-level Weak Lensing Cosmology with 60 Simulations Using Multifidelity Simulation-based Inference* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.23346)]  
  Pretraining on lognormal mocks and fine-tuning on 60 N-body simulations for KiDS-Legacy field-level inference.

- *Simulation-Based Inference for Cluster Cosmology with Set-Based Neural Network Architectures* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.27439)]  
  Set-based networks and autoregressive flows on eRASS1-like cluster catalogues.

- *From Dark Matter to Galaxies: Halo-Free Mock Generation via Conditional Point-Cloud Diffusion* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2607.19808)]  
  Point-cloud diffusion that generates galaxy positions and star formation rates from IllustrisTNG dark matter fields.

## Simulation-Based Inference

- **(pydelfi)** *Fast Likelihood-free Cosmology with Neural Density Estimators and Active Learning* `MNRAS 2019`  
  [[Paper](https://arxiv.org/abs/1903.00007)] [[Code](https://github.com/justinalsing/pydelfi)]  
  Density-estimation likelihood-free inference with active simulation acquisition.

- **(swyft)** *Truncated Marginal Neural Ratio Estimation* `NeurIPS 2021`  
  [[Paper](https://arxiv.org/abs/2107.01214)] [[Code](https://github.com/undark-lab/swyft)]  
  Simulation-efficient marginal posterior estimation with prior truncation.

- **(swyft TMNRE)** *Fast and Credible Likelihood-Free Cosmology with Truncated Marginal Neural Ratio Estimation* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2111.08030)] [[Code](https://github.com/undark-lab/swyft)]  
  Truncated marginal neural ratio estimation applied to CMB cosmological inference.

- **(margarine)** *Marginal Post Processing of Bayesian Inference Products with Normalizing Flows and Kernel Density Estimators* `MNRAS 2023`  
  [[Paper](https://arxiv.org/abs/2205.12841)] [[Code](https://github.com/htjb/margarine)]  
  Normalizing flows and KDEs that learn nuisance-free marginal posteriors for marginal KL divergences and emulation.

- **(pocoMC)** *Accelerating Astronomical and Cosmological Inference with Preconditioned Monte Carlo* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2207.05660)] [[Code](https://github.com/minaskar/pocomc)]  
  Sequential Monte Carlo sampler preconditioned with normalizing flows.

- **(GPry)** *Fast and Robust Bayesian Inference Using Gaussian Processes with GPry* `JCAP 2023`  
  [[Paper](https://arxiv.org/abs/2211.02045)] [[Code](https://github.com/jonaselgammal/GPry)] [[Journal](https://doi.org/10.1088/1475-7516/2023/10/021)]  
  Active-learning Gaussian process surrogate of the posterior for expensive cosmological likelihoods.

- **(TARP)** *Sampling-Based Accuracy Testing of Posterior Estimators for General Inference* `ICML 2023`  
  [[Paper](https://arxiv.org/abs/2302.03026)] [[Code](https://github.com/Ciela-Institute/tarp)]  
  Coverage test that checks generative posterior estimators using samples alone.

- **(nautilus)** *nautilus: Boosting Bayesian Importance Nested Sampling with Deep Learning* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2306.16923)] [[Code](https://github.com/johannesulf/nautilus)]  
  Importance nested sampling with neural network emulation of the likelihood contours.

- **(nbi)** *nbi: The Astronomer's Package for Neural Posterior Estimation* `NeurIPS 2023 Workshop (DLIP)`  
  [[Paper](https://arxiv.org/abs/2312.03824)] [[Code](https://github.com/kmzzhang/nbi)]  
  Neural posterior estimation package with featurizers for light curves and spectra.

- **(LtU-ILI)** *LtU-ILI: An All-in-One Framework for Implicit Inference in Astrophysics and Cosmology* `OJAp 2024`  
  [[Paper](https://arxiv.org/abs/2402.05137)] [[Code](https://github.com/maho3/ltu-ili)] [[Journal](https://doi.org/10.33232/001c.120559)]  
  Unified interface over sbi, pydelfi and lampe with validation and calibration tools.

## High-Energy Astrophysics and Astroparticle Physics

- **(GCE BGCNN)** *Galactic Center Excess in a New Light: Disentangling the γ-Ray Sky with Bayesian Graph Convolutional Neural Networks* `PRL 2020`  
  [[Paper](https://arxiv.org/abs/2006.12504)] [[Code](https://github.com/FloList/GCE_NN)] [[Journal](https://doi.org/10.1103/PhysRevLett.125.241102)]  
  Bayesian graph CNNs on HEALPix maps that separate point-source and smooth contributions to the Fermi Galactic Center Excess.

- **(GCE SCD)** *Extracting the Galactic Center Excess' Source-count Distribution with Neural Nets* `PRD 2021`  
  [[Paper](https://arxiv.org/abs/2107.09070)] [[Code](https://github.com/FloList/GCE_NN)] [[Journal](https://doi.org/10.1103/PhysRevD.104.123022)]  
  Neural networks that estimate source-count distributions and flux fractions of gamma-ray templates.

- **(Fermi GCE SBI)** *A Neural Simulation-based Inference Approach for Characterizing the Galactic Center γ-ray Excess* `arXiv 2021`  
  [[Paper](https://arxiv.org/abs/2110.06931)] [[Code](https://github.com/smsharma/fermi-gce-flows)]  
  Normalizing-flow posterior estimation on spherical Fermi-LAT maps with graph neural network summaries.

- **(GraphNeT IceCube)** *Graph Neural Networks for Low-Energy Event Classification & Reconstruction in IceCube* `JINST 2022`  
  [[Paper](https://arxiv.org/abs/2209.03042)] [[Code](https://github.com/graphnet-team/graphnet)] [[Journal](https://doi.org/10.1088/1748-0221/17/11/P11003)]  
  Point-cloud GNN that classifies and reconstructs GeV-scale neutrino events in IceCube.

- **(DeepGRB)** *Deep Learning for Gamma-Ray Bursts: A Data Driven Event Framework for X/Gamma-Ray Analysis in Space Telescopes* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2401.15632)]  
  Neural background estimation with FOCuS-Poisson trigger search on Fermi-GBM count rates.

- *A Robust Neural Determination of the Source-count Distribution of the Fermi-LAT Sky at High Latitudes* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2505.02906)]  
  Neural ratio estimation with spherical convolutions on 14 years of high-latitude Fermi-LAT photon maps.

- *Unsupervised Machine Learning Classification of Gamma-ray Bursts Based on the Rest-frame Prompt Emission Parameters* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.08224)]  
  Unsupervised clustering of GRBs into types using rest-frame prompt emission properties.

- **(ASID)** *Towards a Foundation Model for Astrophysical Source Detection: An End-to-End Gamma-Ray Data Analysis Pipeline Using Deep Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.25128)]  
  U-Net detection with CNN classification and deep-ensemble flux estimation on Fermi-LAT and CTAO simulations.

- *Multivariate Time Series Classification of Fermi-Detected Gamma-Ray Transients Using Convolutional-Recurrent Neural Networks* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.22412)]  
  CNN-LSTM classifiers that separate GRBs, TGFs, solar flares and SGRs in Fermi-GBM light curves and flag outliers.

## Gravitational Waves

- **(Magic Bullet)** *Convolutional Neural Networks: A Magic Bullet for Gravitational-wave Detection?* `PRD 2019`  
  [[Paper](https://arxiv.org/abs/1904.08693)] [[Code](https://github.com/timothygebhard/magic-bullet)]  
  Critical evaluation of CNN-based gravitational-wave detection.

- **(VItamin)** *Bayesian Parameter Estimation Using Conditional Variational Autoencoders for Gravitational-wave Astronomy* `Nature Physics 2022`  
  [[Paper](https://arxiv.org/abs/1909.06296)] [[Code](https://github.com/hagabbar/vitamin_c)]  
  Conditional VAE for rapid compact binary parameter estimation.

- **(DeepClean)** *Noise Reduction in Gravitational-wave Data via Deep Learning* `arXiv 2020`  
  [[Paper](https://arxiv.org/abs/2005.06534)] [[Code](https://github.com/ML4GW/DeepClean)]  
  Neural network for low-frequency noise subtraction in gravitational-wave detectors.

- **(nessai)** *Nested Sampling with Normalizing Flows for Gravitational-wave Inference* `PRD 2021`  
  [[Paper](https://arxiv.org/abs/2102.11056)] [[Importance Nested Sampling](https://arxiv.org/abs/2302.08526)] [[Code](https://github.com/mj-will/nessai)]  
  Nested sampler that uses normalizing flows to propose new live points.

- **(DINGO)** *Real-time Gravitational-wave Science with Neural Posterior Estimation* `PRL 2021`  
  [[Paper](https://arxiv.org/abs/2106.12594)] [[Code](https://github.com/dingo-gw/dingo)] [[Journal](https://doi.org/10.1103/PhysRevLett.127.241103)]  
  Normalizing-flow posteriors for binary black hole events with inference times of about a minute.

- **(flowMC)** *flowMC: Normalizing Flow Enhanced Sampling Package for Probabilistic Inference in JAX* `arXiv 2022`  
  [[Paper](https://arxiv.org/abs/2211.06397)] [[Code](https://github.com/kazewong/flowMC)]  
  MCMC with normalizing-flow global proposals, used for gravitational-wave parameter estimation.

- **(Peregrine)** *Peregrine: Sequential Simulation-based Inference for Gravitational Wave Signals* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2304.02035)] [[Code](https://github.com/PEREGRINE-GW/peregrine)]  
  Truncated marginal neural ratio estimation for compact binary parameter estimation.

- **(Aframe)** *A Machine-learning Pipeline for Real-time Detection of Gravitational Waves from Compact Binary Coalescences* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2403.18661)] [[Code](https://github.com/ML4GW/aframe)]  
  Low-latency neural network search pipeline used in O4.

- **(GWAK)** *GWAK: Gravitational-Wave Anomalous Knowledge with Recurrent Autoencoders* `MLST 2024`  
  [[Journal](https://doi.org/10.1088/2632-2153/ad3a31)] [[Code](https://github.com/ML4GW/gwak)]  
  Semi-supervised anomaly detection for unmodeled gravitational-wave transients.

- **(DINGO-BNS)** *Real-time Inference for Binary Neutron Star Mergers Using Machine Learning* `Nature 2025`  
  [[Paper](https://arxiv.org/abs/2407.09602)] [[Code](https://github.com/dingo-gw/dingo)]  
  Prior-conditioned neural posterior estimation that infers all BNS parameters in about one second, including before merger.

- *A Machine-learning Classifier for the Postmerger Remnant of Binary Neutron Stars* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2408.10678)]  
  Gradient boosted trees trained on numerical-relativity simulations predict BNS merger outcomes from inspiral parameters.

- *A Binary Neutron Star Merger Search Pipeline Powered by Deep Learning* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2409.06266)]  
  CNN on matched-filter SNR time series that detects BNS mergers and is robust to glitches.

- *AI-enabled Gravitational-waves Searches for Binary Neutron Stars at Optimal Sensitivity* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2607.01372)]  
  Neural network BNS search with heterodyned inputs that runs in real time on a single GPU.

- *Scalable and Sequential Inference of the Neutron Star Equation of State with the Einstein Telescope* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2610.07975)]  
  Normalizing-flow stacking of single-event posteriors with GPU sequential Monte Carlo for EOS inference.

- *Deep-Learning-Assisted Bayesian Inference for Extreme-Mass-Ratio Inspirals* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2611.11922)]  
  Deep learning acceleration of Bayesian parameter inference for EMRI signals.

## Solar Physics and Heliophysics

- **(DeepVel)** *DeepVel: Deep Learning for the Estimation of Horizontal Velocities at the Solar Surface* `A&A 2017`  
  [[Paper](https://arxiv.org/abs/1703.05128)] [[Code](https://github.com/aasensio/deepvel)]  
  End-to-end network that estimates horizontal velocity fields from pairs of granulation images.

- **(Enhance)** *Enhancing SDO/HMI Images Using Deep Learning* `A&A 2018`  
  [[Paper](https://arxiv.org/abs/1706.02933)] [[Code](https://github.com/cdiazbas/enhance)]  
  Deconvolution and super-resolution of HMI continuum images and magnetograms.

- **(SDOML)** *A Machine-learning Data Set Prepared from the NASA Solar Dynamics Observatory Mission* `ApJS 2019`  
  [[Paper](https://arxiv.org/abs/1903.04538)] [[Code](https://github.com/fluxtransport/SDOML)] [[Journal](https://doi.org/10.3847/1538-4365/ab1005)]  
  Curated 6.5 TB AIA, HMI and EVE dataset with baselines for EUV irradiance forecasting and instrument translation.

- **(SICON)** *Stokes Inversion Based on Convolutional Neural Networks* `A&A 2019`  
  [[Paper](https://arxiv.org/abs/1904.03714)] [[Code](https://github.com/aasensio/sicon)]  
  Fully convolutional networks that invert Hinode Stokes maps into 3D thermodynamic and magnetic cubes.

- **(Slic)** *Fast Solar Image Classification Using Deep Learning and Its Importance for Automation in Solar Physics* `Solar Physics 2019`  
  [[Paper](https://arxiv.org/abs/1905.13575)] [[Code](https://github.com/rhero12/Slic)]  
  CNN classification of solar features in H-alpha images.

- **(Unsupervised MFBD)** *Learning to Do Multiframe Blind Deconvolution Unsupervisedly* `A&A 2021`  
  [[Paper](https://arxiv.org/abs/2006.01438)] [[Code](https://github.com/aasensio/unsupervisedMFBD)]  
  Unsupervised neural multiframe blind deconvolution of solar observations.

- **(NF2)** *Probing the Solar Coronal Magnetic Field with Physics-informed Neural Networks* `Nature Astronomy 2023`  
  [[Code](https://github.com/RobertJaro/NF2)] [[Journal](https://doi.org/10.1038/s41550-023-02030-9)] [[Multi-height](https://doi.org/10.3847/2041-8213/ad2450)]  
  Physics-informed neural network extrapolation of force-free coronal magnetic fields from photospheric magnetograms.

- **(Surya)** *Surya: Foundation Model for Heliophysics* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.14112)] [[Code](https://github.com/NASA-IMPACT/Surya)]  
  366M-parameter spatiotemporal model trained on eight AIA channels and five HMI products at native resolution.

- *Solar Flare Forecasting with Foundational Transformer Models across Image, Video, and Time-series Modalities* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.23400)]  
  Compares SigLIP2, VideoMAE and Moirai2 on SDO/HMI magnetograms and GOES X-ray fluxes.

- **(JW-Flare)** *JW-Flare: Accurate Solar Flare Forecasting Method Based on Multimodal Large Language Models* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2511.08970)]  
  Multimodal LLM fine-tuned with LoRA on magnetograms and textual magnetic parameters for 24-hour flare forecasts.

- *Prediction of Major Solar Flares Using Interpretable Class-dependent Reward Framework with Active Region Magnetograms and Domain Knowledge* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2602.16264)]  
  CNN, CNN-BiLSTM and transformer models with class-dependent rewards for imbalanced M-class flare prediction.

- *Predicting Associations between Solar Flares and Coronal Mass Ejections Using SDO/HMI Magnetograms and a Hybrid Neural Network* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2604.10016)]  
  ViT and LSTM hybrid that predicts whether upcoming flares will be eruptive or confined.

## Radio Astronomy

- **(FETCH)** *FETCH: A Deep-learning Based Classifier for Fast Transient Classification* `MNRAS 2020`  
  [[Paper](https://arxiv.org/abs/1902.06343)] [[Code](https://github.com/devanshkv/fetch)]  
  CNN classifier for fast radio burst and single-pulse candidates.

- **(ClaRAN)** *Radio Galaxy Zoo: ClaRAN, a Deep Learning Classifier for Radio Morphologies* `MNRAS 2019`  
  [[Journal](https://doi.org/10.1093/mnras/sty2646)] [[Code](https://github.com/chenwuperth/rgz_rcnn)]  
  Faster R-CNN detection and classification of radio source morphologies.

- **(Pulsar SGAN)** *Pulsar Candidate Identification Using Semi-supervised Generative Adversarial Networks* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2010.07457)] [[Code](https://github.com/vishnubk/sgan)] [[Journal](https://doi.org/10.1093/mnras/stab1308)]  
  Semi-supervised GAN classifier for pulsar candidates with few labelled examples.

- **(Attention Gating)** *Attention-gating for Improved Radio Galaxy Classification* `MNRAS 2021`  
  [[Paper](https://arxiv.org/abs/2012.01248)] [[Code](https://github.com/mb010/AstroAttention)]  
  Attention-gated CNNs for FRI and FRII radio galaxy classification.

- **(POLISH)** *Deep Radio-interferometric Imaging with POLISH: DSA-2000 and Weak Lensing* `MNRAS 2022`  
  [[Paper](https://arxiv.org/abs/2111.03249)] [[Code](https://github.com/liamconnor/polish-pub)]  
  Super-resolution network for radio interferometric image reconstruction.

- **(radionets)** *Deep Learning-based Imaging in Radio Interferometry* `A&A 2022`  
  [[Journal](https://doi.org/10.1051/0004-6361/202142113)] [[Code](https://github.com/radionets-project/radionets)]  
  Neural networks that reconstruct radio images from incomplete visibility data.

- **(Radio Galaxy Zoo FM)** *Radio Galaxy Zoo: Building a Multipurpose Foundation Model for Radio Astronomy with Self-supervised Learning* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2305.16127)] [[Code](https://github.com/inigoval/byol)]  
  BYOL pretraining on unlabelled radio galaxy images for downstream classification.

- **(AIRI)** *Plug-and-play Imaging with Model Uncertainty Quantification in Radio Astronomy* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2312.07137)] [[Code](https://github.com/basp-group/AIRI)]  
  Learned denoisers in proximal algorithms for radio-interferometric imaging with uncertainty quantification.

- **(R2D2)** *The R2D2 Deep Neural Network Series Paradigm for Fast Precision Imaging in Radio Astronomy* `ApJS 2024`  
  [[Paper](https://arxiv.org/abs/2403.05452)] [[Code](https://github.com/basp-group/R2D2-RI)] [[Journal](https://doi.org/10.3847/1538-4365/ad46f5)]  
  Series of residual networks for radio interferometric imaging.

- *Simulating Images of Radio Galaxies with Diffusion Models* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2410.07794)]  
  Continuous-time diffusion model that generates radio galaxy images with control over flux and morphology.

- *Classification of Radio Sources Through Self-Supervised Learning* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2503.19111)]  
  Self-supervised pretraining and deep clustering that classify LoTSS-DR2 radio galaxies into 12 morphology classes.

- *Simulating Realistic Radio Continuum Survey Maps with Diffusion Models* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2506.11715)]  
  Diffusion-generated radio galaxies assembled into sky models and imaged to mimic LoTSS pointings.

- **(YOLO-CIANNA)** *YOLO-CIANNA: Galaxy Detection with Deep Learning in Radio Data* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2509.12082)]  
  3D CNN detector for HI sources in SKA SDC2 hyperspectral cubes, extending the method that won SDC2.

- **(YOLO-Chars)** *Radio Galaxies Detection and Characterization Using Deep Learning Techniques* `MNRAS 2026`  
  [[Paper](https://arxiv.org/abs/2608.21474)]  
  Two-stage YOLO detection and characterisation network for flux, size and position angle on SKA SDC1 images.

## Planetary Science and Small Bodies

- **(DeepMoon)** *Lunar Crater Identification via Deep Learning* `Icarus 2019`  
  [[Paper](https://arxiv.org/abs/1803.02192)] [[Code](https://github.com/silburt/DeepMoon)] [[Data](https://doi.org/10.5281/zenodo.1133969)]  
  CNN crater detection on lunar digital elevation maps, transferred to Mercury.

- **(AstroVision)** *AstroVision: Towards Autonomous Feature Detection and Description for Missions to Small Bodies Using Deep Learning* `Acta Astronaut. 2023`  
  [[Paper](https://arxiv.org/abs/2208.02053)] [[Data](https://huggingface.co/datasets/travisdriver/astrovision-data)] [[Journal](https://doi.org/10.1016/j.actaastro.2023.01.009)]  
  115,970 annotated real images of 16 small bodies for keypoint detection and description benchmarks.

- *Deep Learning Universal Crater Detection Using Segment Anything Model (SAM)* `arXiv 2023`  
  [[Paper](https://arxiv.org/abs/2304.07764)]  
  Zero-shot crater segmentation with SAM on lunar and Martian images and DEMs.

- **(Lunar Twins)** *Lunar Twins: We Choose to Go to the Moon with Large Language Models* `ACL Findings 2025`  
  [[Paper](https://aclanthology.org/2025.findings-acl.69/)]  
  Earth-Moon collaborative Chang'e large model with Yutu-Text and Yutu-VL small models, the Lunar_GenData multi-agent instruction workflow built on Chang'e mission data, and the Lunar_Eval suite.

- *Deep Learning Framework for Crater Detection and Identification on the Moon and Mars* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2508.03920)] [[Code](https://github.com/sydney-machine-learning/crater-identification)]  
  Two-stage YOLO detection and CNN or ResNet-50 size classification of craters with an annotated dataset.

- *Vision-Language Model for Accurate Crater Detection* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2601.07795)]  
  OWLv2 vision transformer fine-tuned on LRO images for lunar crater detection.

- **(LLaVA-LE)** *LLaVA-LE: Large Language-and-Vision Assistant for Lunar Exploration* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2603.24696)]  
  LLaVA adapted to lunar remote sensing with LUCID, 96k panchromatic images paired with scientific captions and question-answer pairs.

- *Deep Learning-Based Lunar Crater Terrain Relative Navigation* `arXiv 2026`  
  [[Paper](https://arxiv.org/abs/2606.14776)]  
  U-Net++ crater detector coupled with an extended Kalman filter for lunar landing navigation.

- **(Lunar-Bench)** *Lunar-Bench: Towards Evaluating Task-Oriented Reasoning of LLMs in Lunar Exploration Scenarios* `ACL Findings 2026`  
  [[Paper](https://aclanthology.org/2026.findings-acl.83/)]  
  3,000 tasks derived from lunar mission procedures with Environmental Scenario Indicators for safety, efficiency, integrity and alignment; the best of 36 models reaches 47.8% against 65.1% for human experts.

- **(Lunar-R1)** *Lunar-R1: Efficient Reasoning of Large Language Models for Lunar Exploration via Reinforcement Learning* `EMNLP 2026 Industry`  
  [[Paper](https://aclanthology.org/2026.emnlp-industry.5/)]  
  8B reasoning model trained by continued pretraining, SFT and RL, with Latent Difficulty Perception that cuts chain-of-thought tokens by 38.9%, the Lunar-QA benchmark and RK3588 NPU deployment.

## Datasets

### Observational Datasets

- **(PLAsTiCC)** *The Photometric LSST Astronomical Time-series Classification Challenge (PLAsTiCC): Data Set* `arXiv 2018`  
  [[Paper](https://arxiv.org/abs/1810.00001)] [[Kaggle](https://www.kaggle.com/c/PLAsTiCC-2018)]  
  Simulated LSST multi-band light curves for transient and variable classification.

- **(Galaxy10 DECaLS)** *Galaxy10 DECaLS* `Dataset 2021`  
  [[Code](https://github.com/henrysky/Galaxy10)] [[Data](https://doi.org/10.5281/zenodo.10845026)]  
  17,736 DECaLS g, r, z galaxy images in 10 morphology classes with Galaxy Zoo labels.

- **(Multimodal Universe)** *The Multimodal Universe: Enabling Large-Scale Machine Learning with 100 TB of Astronomical Scientific Data* `NeurIPS 2024 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2412.02527)] [[Code](https://github.com/MultimodalUniverse/MultimodalUniverse)]  
  Images, spectra, time series and catalogs for hundreds of millions of objects, distributed as Hugging Face datasets with benchmark tasks.

### Simulation Datasets

- **(Quijote)** *The Quijote Simulations* `ApJS 2020`  
  [[Paper](https://arxiv.org/abs/1909.05273)] [[Journal](https://doi.org/10.3847/1538-4365/ab9d82)]  
  44,100 N-body simulations spanning more than 7,000 cosmological models, designed for information quantification and ML training.

- **(CAMELS)** *The CAMELS Project: Cosmology and Astrophysics with MachinE Learning Simulations* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2010.00619)] [[Code](https://github.com/franciscovillaescusa/CAMELS)] [[Project](https://www.camel-simulations.org)]  
  4,233 cosmological simulations varying cosmological and feedback parameters, designed for training ML models.

- **(The Well)** *The Well: A Large-Scale Collection of Diverse Physics Simulations for Machine Learning* `NeurIPS 2024 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2412.00568)] [[Code](https://github.com/PolymathicAI/the_well)]  
  15 TB across 16 physics simulation datasets, including MHD and supernova explosion simulations.

## Tools and Libraries

- [AspGap](https://github.com/jiadonglee/aspgap) infers red giant stellar parameters and abundances from Gaia XP spectra.
- [astroML](https://github.com/astroML/astroML) provides machine learning and statistics routines for astronomy.
- [astrorapid](https://github.com/daniel-muthukrishna/astrorapid) classifies transients in real time with recurrent neural networks.
- [avocado](https://github.com/kboone/avocado) classifies photometric transients with Gaussian process augmentation and boosted trees.
- [BLISS](https://github.com/prob-ml/bliss) performs Bayesian light source separation with amortized variational inference.
- [ctlearn](https://github.com/ctlearn-project/ctlearn) trains deep learning models for imaging atmospheric Cherenkov telescope event reconstruction.
- [D3M](https://github.com/siyucosmo/ML-Recon) emulates N-body displacement fields with deep learning.
- [DASH](https://github.com/daniel-muthukrishna/astrodash) classifies supernova spectra with deep learning.
- [Deep-HiTS](https://github.com/guille-c/Deep-HiTS) classifies HiTS transient candidates with convolutional neural networks.
- [deep-potential](https://github.com/gregreen/deep-potential) recovers gravitational potentials from phase-space snapshots with normalizing flows.
- [DeepBench](https://github.com/deepskies/DeepBench) generates simple physics and astronomy benchmark datasets for machine learning.
- [DeepDISC](https://github.com/grantmerz/deepdisc) applies Detectron2 instance segmentation to astronomical source detection.
- [DeepMerge](https://github.com/deepskies/deepmerge-public) classifies high-redshift merging galaxies with CNNs.
- [DeepSource](https://github.com/vafaei-ar/deepsource) detects point sources in radio images with deep learning.
- [E2CNNRadGal](https://github.com/as595/E2CNNRadGal) classifies radio galaxies with group-equivariant CNNs.
- [fink-science](https://github.com/astrolabsoftware/fink-science) hosts the science modules and classifiers run on the Fink alert stream.
- [Fink](https://github.com/astrolabsoftware/fink-broker) is an LSST alert broker with machine learning classification modules.
- [FLEET](https://github.com/gmzsebastian/FLEET) selects superluminous supernova and tidal disruption event candidates for follow-up.
- [FlexCode](https://github.com/tpospisi/FlexCode) estimates conditional densities for photometric redshifts.
- [Galaxy Zoo Bayesian CNN](https://github.com/mwalmsley/galaxy-zoo-bayesian-cnn) trains Bayesian CNNs with active learning on Galaxy Zoo labels.
- [galaxy-datasets](https://github.com/mwalmsley/galaxy-datasets) loads Galaxy Zoo datasets for PyTorch training.
- [GalaxyGAN](https://github.com/SpaceML/GalaxyGAN_python) recovers features from degraded galaxy images with GANs.
- [GPz](https://github.com/OxfordML/GPz) estimates photometric redshifts with sparse Gaussian processes.
- [Gravity Spy](https://github.com/Gravity-Spy/GravitySpy) classifies LIGO detector glitches with citizen science and machine learning.
- [herculens](https://github.com/Herculens/herculens) performs differentiable strong lens modeling in JAX.
- [InstrumentToInstrument](https://github.com/RobertJaro/InstrumentToInstrument) translates solar observations between instruments.
- [IrregularTimeSeriesAutoencoder](https://github.com/bnaul/IrregularTimeSeriesAutoencoderPaper) learns recurrent autoencoder features from irregularly sampled light curves.
- [jax-cosmo](https://github.com/DifferentiableUniverseInitiative/jax_cosmo) provides differentiable cosmology computations in JAX.
- [jax-lensing](https://github.com/CosmoStat/jax-lensing) implements probabilistic mass mapping with neural score estimation ([paper](https://arxiv.org/abs/2011.08271)).
- [JaxPM](https://github.com/DifferentiableUniverseInitiative/JaxPM) implements a differentiable particle-mesh N-body solver in JAX.
- [jim](https://github.com/kazewong/jim) performs gravitational-wave parameter estimation in JAX with flow-enhanced sampling.
- [lampe](https://github.com/probabilists/lampe) implements neural ratio and posterior estimation for likelihood-free inference in PyTorch.
- [lc_classifier](https://github.com/alercebroker/lc_classifier) classifies light curves in the ALeRCE broker.
- [LIA](https://github.com/dgodinez77/LIA) classifies microlensing events with random forests.
- [light-curve](https://github.com/light-curve/light-curve-python) extracts light-curve features for transient and variable classification.
- [magnify](https://github.com/jiwoncpark/magnify) models AGN light curves with Gaussian process and neural network tools.
- [map2map](https://github.com/eelregit/map2map) trains field-to-field neural networks on cosmological simulations.
- [MCCD](https://github.com/CosmoStat/mccd) models the PSF across multiple CCDs with data-driven methods.
- [MiraBest](https://github.com/fmporter/MiraBest-full) provides a labelled FRI and FRII radio galaxy dataset.
- [ml4gw](https://github.com/ML4GW/ml4gw) provides PyTorch utilities for gravitational-wave machine learning.
- [ML_GBT_SETI](https://github.com/PetchMa/ML_GBT_SETI) searches Green Bank Telescope data for technosignatures with machine learning.
- [MLZ](https://github.com/mgckind/MLZ) estimates photometric redshifts with TPZ random forests.
- [Morpheus](https://github.com/morpheus-project/morpheus) performs pixel-level morphological classification of astronomical images.
- [MuyGPyS](https://github.com/LLNL/MuyGPyS) provides scalable Gaussian process estimation used for star-galaxy separation.
- [ParSNIP](https://github.com/kboone/parsnip) builds generative models of transient light curves with physics-enabled deep learning.
- [PICS](https://github.com/zhuww/ubc_AI) classifies pulsar candidates with image pattern recognition.
- [pmwd](https://github.com/eelregit/pmwd) implements differentiable particle-mesh N-body simulation in JAX.
- [PySR](https://github.com/MilesCranmer/PySR) performs symbolic regression for interpretable scientific models ([paper](https://arxiv.org/abs/2305.01582)).
- [QuasarNET](https://github.com/ngbusca/QuasarNET) classifies quasar spectra and estimates redshifts with a convolutional network.
- [ramjet](https://github.com/golmschenk/ramjet) detects transits and microlensing events in light curves with neural networks.
- [RESSPECT](https://github.com/COINtoolbox/RESSPECT) applies active learning to supernova spectroscopic follow-up.
- [sbi](https://github.com/sbi-dev/sbi) implements neural posterior, likelihood and ratio estimation ([JOSS](https://doi.org/10.21105/joss.02505)).
- [ShapeDeconv](https://github.com/CosmoStat/ShapeDeconv) deconvolves galaxy images with deep learning for shape measurement.
- [SimBIG](https://github.com/changhoonhahn/simbig) performs simulation-based inference of galaxy clustering.
- [single_pulse_ml](https://github.com/liamconnor/single_pulse_ml) classifies single-pulse and fast radio burst candidates with deep learning.
- [star-galaxy CNN](https://github.com/EdwardJKim/dl4astro) separates stars and galaxies with CNNs.
- [StarNet](https://github.com/astroai/starnet) infers stellar parameters from spectra with CNNs.
- [sunbird](https://github.com/florpi/sunbird) emulates galaxy clustering summary statistics with neural networks.
- [Superphot+](https://github.com/VTDA-Group/superphot-plus) fits and classifies supernova light curves.
- [Superphot](https://github.com/griffin-h/superphot) classifies supernovae from photometric light curves.
- [SuperRAENN](https://github.com/villrv/SuperRAENN) classifies supernova light curves with recurrent autoencoder features.
- [The Cannon](https://github.com/andycasey/AnniesLasso) provides a data-driven model for stellar labels from spectra.
- [The Payne](https://github.com/tingyuansen/The_Payne) fits stellar spectra with neural network spectral emulators.
- [transomaly](https://github.com/daniel-muthukrishna/transomaly) detects anomalous transients in real time.
- [xVal](https://github.com/PolymathicAI/xVal) encodes real numbers as continuous embeddings for language models on scientific data.

## Communities and Groups

- [Polymathic AI](https://polymathic-ai.org) develops AstroCLIP, AION-1, MPP, the Multimodal Universe and The Well.
- [UniverseTBD](https://universetbd.org) develops AstroLLaMA, AstroPT and AstroLLaVA.
- [AstroMLab](https://huggingface.co/AstroMLab) develops the AstroMLab benchmark and the AstroSage models.
- [ML4GW](https://github.com/ML4GW) develops machine learning pipelines for gravitational-wave astronomy.

## Related Awesome Lists

- [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy) covers general resources for professional astronomers.
- [awesome-astro-datascience](https://github.com/mpi-astronomy/awesome-astro-datascience) covers astronomical data science resources.
- [awesome-astrodata](https://github.com/gully/awesome-astrodata) covers data and tools for machine learning in astronomy.
- [taotie](https://github.com/dr-guangtou/taotie) covers resources for astrophysical research.
- [awesome-space](https://github.com/orbitalindex/awesome-space) covers space-related packages and resources.
- [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) covers scientific language models across domains.

## Contributing

Pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
