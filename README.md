<!-- This file is generated from data/entries.yml by scripts/build.py. Edit the YAML file and run the script instead of editing this file. -->

# Awesome AI for Astronomy

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/Xin-YuXiao/Awesome-AI-for-Astronomy)

A curated list of papers, models, datasets, benchmarks and software for artificial intelligence in astronomy, astrophysics, cosmology, heliophysics and planetary science. The list currently holds 344 papers and 64 software packages.

A searchable version with section, year, code and venue filters and a one-sentence summary of every paper is available at [xin-yuxiao.github.io/Awesome-AI-for-Astronomy](https://xin-yuxiao.github.io/Awesome-AI-for-Astronomy/).

General astronomy resources are covered by [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy), and classical astronomical data science by [awesome-astro-datascience](https://github.com/mpi-astronomy/awesome-astro-datascience). This list tracks machine learning work with public papers, linking public code where it exists, with emphasis on foundation models, language models, agents and benchmarks released since 2021, together with established deep learning methods in each subfield.

**Notes**

1. Papers are listed newest first within each subsection. The date column gives the month of the first arXiv version, or the publication year when there is no arXiv version.
2. The venue column shows the peer-reviewed venue when it is confirmed by the journal DOI, the official repository or the publisher page. Otherwise it shows `arXiv` and the year.
3. Every arXiv identifier, DOI and repository link was checked against the paper page or the official repository README before inclusion. Hovering over a paper title shows its one-sentence summary.
4. Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.

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
  - [Data and Modality Benchmarks](#data-and-modality-benchmarks)
  - [Multimodal Model Evaluation](#multimodal-model-evaluation)
  - [Text and Reasoning Evaluation](#text-and-reasoning-evaluation)
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

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.07 |  | [Source Finding and Characterisation for SKAO Science](https://arxiv.org/abs/2607.03736 "Review of classical and machine learning source finding and morphology classification for SKAO surveys.") | arXiv 2026 | - | - |
| 2026.06 |  | [The Role of Artificial Intelligence in the SKA Era](https://arxiv.org/abs/2606.28493 "Chapter on deep learning for source finding, RFI mitigation, imaging, anomaly detection and scheduling for the SKA.") | arXiv 2026 | - | - |
| 2026.03 |  | [Deep Learning-Based Astronomical Multimodal Data Fusion: A Comprehensive Review](https://arxiv.org/abs/2603.00699 "Review of deep learning methods that fuse images, spectra, time series and catalogues in astronomy.") | arXiv 2026 | - | - |
| 2026.01 |  | [Opportunities in AI/ML for the Rubin LSST Dark Energy Science Collaboration](https://arxiv.org/abs/2601.14235 "LSST DESC roadmap covering photometric redshifts, transient classification, weak lensing inference, foundation models and infrastructure.") | arXiv 2026 | - | - |
| 2025.11 |  | [Advances and Challenges in Solar Flare Prediction: A Review](https://arxiv.org/abs/2511.20465 "Review of statistical, physics-based and deep learning flare forecasting including CNN, LSTM and transformer models.") | arXiv 2025 | - | - |
| 2025.10 |  | [Deep Learning in Astrophysics](https://arxiv.org/abs/2510.10713 "Annual Review covering inductive biases, simulation-based inference, anomaly detection, foundation models, reinforcement learning and LLM agents in astronomy.") | ARA&A 2025 | - | - |
| 2025.08 |  | [From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](https://arxiv.org/abs/2508.14111 "Domain-oriented survey of autonomous scientific discovery including agentic astronomy and cosmology research.") | arXiv 2025 | [Code](https://github.com/AgenticScience/Awesome-Agent-Scientists) | - |
| 2025.08 |  | [A Survey of Scientific Large Language Models: From Data Foundations to Agent Frontiers](https://arxiv.org/abs/2508.21148 "Survey of scientific LLMs and their training data, including astronomy datasets and models.") | arXiv 2025 | - | - |
| 2025.08 |  | [The Revolution in Strong Lensing Discoveries from Euclid](https://arxiv.org/abs/2508.14624 "Review of how machine learning, citizen science and expert inspection found about 500 high-quality lens candidates in Euclid Q1.") | arXiv 2025 | - | - |
| 2025.03 |  | [Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047 "Survey of LLM-based scientific agents with a section on astronomy and cosmology applications.") | arXiv 2025 | - | - |
| 2024.09 |  | [What is the Role of Large Language Models in the Evolution of Astronomy Research?](https://arxiv.org/abs/2409.20252 "Use cases, survey results and recommendations on LLM adoption in astronomy research.") | arXiv 2024 | - | - |
| 2023.10 |  | [Constructing Impactful Machine Learning Research for Astronomy: Best Practices for Researchers and Reviewers](https://arxiv.org/abs/2310.12528 "Recommendations on baselines, validation, reproducibility and reporting for machine learning papers in astronomy.") | arXiv 2023 | - | - |
| 2023.10 |  | [Deep Learning Based Systems for Crater Detection: A Review](https://arxiv.org/abs/2310.07727 "Review of CNN, U-Net, R-CNN and transformer crater detection algorithms for the Moon, Mars and Mercury.") | arXiv 2023 | - | - |
| 2023.03 |  | [Machine Learning for Observational Cosmology](https://arxiv.org/abs/2303.15794 "Review of machine learning applications in time-domain astronomy, galaxy surveys and emulation for cosmology.") | Rep. Prog. Phys. 2023 | - | [Journal](https://doi.org/10.1088/1361-6633/acd2ea) |
| 2022.11 |  | [Astronomia ex machina: A History, Primer and Outlook on Neural Networks in Astronomy](https://arxiv.org/abs/2211.03796 "Historical review of neural networks in astronomy with a primer on deep learning and an outlook on astronomical foundation models.") | R. Soc. Open Sci. 2023 | - | [Journal](https://doi.org/10.1098/rsos.221454) |
| 2022.10 |  | [The Dawes Review 10: The Impact of Deep Learning for the Analysis of Galaxy Surveys](https://arxiv.org/abs/2210.01813 "Review of deep learning applications to galaxy surveys covering classification, property estimation, discovery and cosmological inference.") | PASA 2023 | - | [Journal](https://doi.org/10.1017/pasa.2022.55) |
| 2020.05 |  | [Enhancing Gravitational-Wave Science with Machine Learning](https://arxiv.org/abs/2005.03745 "Review of machine learning for LIGO and Virgo data quality, signal modeling, searches and parameter estimation.") | MLST 2021 | - | [Journal](https://doi.org/10.1088/2632-2153/abb93a) |
| 2019.11 |  | [The Frontier of Simulation-Based Inference](https://arxiv.org/abs/1911.01429 "Review of simulation-based inference methods and the role of machine learning in inference with intractable likelihoods.") | PNAS 2020 | - | [Journal](https://doi.org/10.1073/pnas.1912789117) |
| 2019.04 |  | [Machine Learning in Astronomy: A Practical Overview](https://arxiv.org/abs/1904.07248 "Lecture notes from the IAC Winter School 2018 covering supervised and unsupervised learning for astronomical datasets.") | arXiv 2019 | - | - |

## Foundation Models and Representation Learning

### Images

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2024.05 | **AstroPT** | [AstroPT: Scaling Large Observation Models for Astronomy](https://arxiv.org/abs/2405.14930 "Autoregressive transformers from 1M to 2.1B parameters pretrained on 8.6M DESI Legacy Survey galaxy images.") | ICML 2024 Workshop (AI4Science) | [Code](https://github.com/Smith42/astroPT) | [Euclid Paper](https://arxiv.org/abs/2503.15312) [Model](https://huggingface.co/Smith42/astroPT_v2.0) |
| 2024.04 | **Galaxy Scaling Laws** | [Scaling Laws for Galaxy Images](https://arxiv.org/abs/2404.02973 "Supervised scaling study on 840k galaxy images with over 100M Galaxy Zoo annotations.") | arXiv 2024 | [Code](https://github.com/mwalmsley/zoobot) | - |
| 2023.12 | **Rare Galaxy Classes** | [Rare Galaxy Classes Identified In Foundation Model Representations](https://arxiv.org/abs/2312.02910 "Searches Zoobot representation space for rare morphological classes.") | arXiv 2023 | [Code](https://github.com/mwalmsley/zoobot) | - |
| 2023 | **Zoobot** | [Zoobot: Adaptable Deep Learning Models for Galaxy Morphology](https://github.com/mwalmsley/zoobot "Pretrained galaxy morphology encoders and finetuning utilities, deployed in the Euclid morphology pipeline.") | JOSS 2023 | [Code](https://github.com/mwalmsley/zoobot) | [PyPI](https://pypi.org/project/zoobot/) |
| 2022.06 | **Zoobot FM** | [Towards Foundation Models for Galaxy Morphology](https://arxiv.org/abs/2206.11927 "Pretraining galaxy morphology encoders on Galaxy Zoo volunteer responses for transfer to downstream tasks.") | arXiv 2022 | [Code](https://github.com/mwalmsley/zoobot) | - |
| 2021.10 | **Galaxy Search** | [Self-Supervised Similarity Search for Large Scientific Datasets](https://arxiv.org/abs/2110.13151 "Self-supervised representations of 42M DESI Legacy Imaging Survey galaxies with a public similarity search tool.") | NeurIPS 2021 Workshop (ML4PS) | [Code](https://github.com/georgestein/galaxy_search) | - |
| 2021.10 | **Zoobot Representations** | [Practical Galaxy Morphology Tools from Deep Supervised Representation Learning](https://arxiv.org/abs/2110.12735 "Representations learned from Galaxy Zoo labels reused for similarity search, anomaly finding and new classification tasks.") | arXiv 2021 | [Code](https://github.com/mwalmsley/zoobot) | - |
| 2020.12 | **SSL-SDSS** | [Self-Supervised Representation Learning for Astronomical Images](https://arxiv.org/abs/2012.13083 "Contrastive pretraining on about 1.2M SDSS galaxy images, evaluated on morphology classification and photometric redshift estimation.") | ApJL 2021 | [Code and Models](https://portal.nersc.gov/project/dasrepo/self-supervised-learning-sdss) | [Journal](https://doi.org/10.3847/2041-8213/abf2c7) |

### Spectra

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.01 | **OmniSpectra** | [OmniSpectra: A Unified Foundation Model for Native Resolution Astronomical Spectra](https://arxiv.org/abs/2601.15351 "Masked-modeling transformer pretrained on 5.5 million spectra from eight surveys at native resolution.") | arXiv 2026 | - | - |
| 2025.07 | **SpecCLIP** | [SpecCLIP: Aligning and Translating Spectroscopic Measurements for Stars](https://arxiv.org/abs/2507.01939 "Contrastive alignment of LAMOST low-resolution and Gaia XP spectra foundation models for parameter estimation and cross-spectrum prediction.") | arXiv 2025 | - | [LoRA Fine-tuning](https://arxiv.org/abs/2507.20972) |
| 2025.06 |  | [Applying Vision Transformers on Spectral Analysis of Astronomical Objects](https://arxiv.org/abs/2506.00294 "Converts one-dimensional spectra into images for pretrained ViT backbones in classification and regression.") | arXiv 2025 | - | - |
| 2024.11 | **SpectraFM** | [SpectraFM: Tuning into Stellar Foundation Models](https://arxiv.org/abs/2411.04750 "Transformer pretrained on synthetic stellar spectra and transferred to real spectra across wavelength ranges.") | NeurIPS 2024 Workshop (FM4Science) | - | - |
| 2023.08 | **Stellar FM** | [Towards an Astronomical Foundation Model for Stars with a Transformer-Based Model](https://arxiv.org/abs/2308.10944 "Transformer trained on cross-survey APOGEE, Gaia and 2MASS data that performs discriminative and generative stellar tasks without task-specific finetuning.") | MNRAS 2024 | [Code](https://github.com/henrysky/astroNN_stars_foundation) | - |
| 2022.11 | **spender** | [Autoencoding Galaxy Spectra I: Architecture](https://arxiv.org/abs/2211.07890 "Attentive convolutional autoencoder that models galaxy spectra in the rest frame with explicit redshifting and resampling, trained on SDSS-II.") | AJ 2023 | [Code](https://github.com/pmelchior/spender) | [Journal](https://doi.org/10.3847/1538-3881/ace0ff) |
| 2020.07 | **Cycle-StarNet** | [Cycle-StarNet: Bridging the Gap between Theory and Data by Leveraging Large Data Sets](https://arxiv.org/abs/2007.03109 "Domain adaptation between synthetic and observed stellar spectra with cycle-consistent networks.") | ApJ 2021 | [Code](https://github.com/teaghan/Cycle_SN) | [Journal](https://doi.org/10.3847/1538-4357/abca96) |
| 2020.02 | **SDSS-VAE** | [Dimensionality Reduction of SDSS Spectra with Variational Autoencoders](https://arxiv.org/abs/2002.10464 "Variational autoencoder compression of SDSS galaxy spectra into a low-dimensional latent space.") | arXiv 2020 | [Code](https://github.com/stephenportillo/SDSS-VAE) | - |

### Time Series

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.10 |  | [What Does Self-supervision Add to Engineered Features for Stellar Light Curves?](https://arxiv.org/abs/2610.14283 "Measures the information that self-supervised light-curve encoders add beyond engineered periodogram and variability features.") | arXiv 2026 | - | - |
| 2025.04 | **FALCO** | [FALCO: A Foundation Model of Astronomical Light Curves for Time Domain Astronomy](https://arxiv.org/abs/2504.20290 "Self-supervised transformer on Kepler light curves for variability classification, surface gravity estimation and flare identification.") | arXiv 2025 | - | - |
| 2024.08 | **Maven** | [Maven: A Multimodal Foundation Model for Supernova Science](https://arxiv.org/abs/2408.16829 "Contrastive alignment of supernova photometry and spectroscopy, pretrained on 0.5M synthetic events and finetuned on ZTF.") | MLST 2024 | [Code](https://github.com/ThomasHelfer/multimodal-supernovae) | - |
| 2023.09 | **Astroconformer** | [Astroconformer: The Prospects of Analyzing Stellar Light Curves with Transformer-Based Deep Learning Models](https://arxiv.org/abs/2309.16316 "Conformer model for Kepler light curves that infers surface gravity and frequency of maximum oscillation power.") | MNRAS 2024 | - | [Journal](https://doi.org/10.1093/mnras/stae068) [Workshop Version](https://arxiv.org/abs/2207.02787) |
| 2022.05 | **ASTROMER** | [ASTROMER: A Transformer-Based Embedding for the Representation of Light Curves](https://arxiv.org/abs/2205.01677 "Self-supervised light-curve encoder pretrained with masked magnitude prediction on MACHO R-band data.") | A&A 2023 | [Code](https://github.com/astromer-science) | [Journal](https://doi.org/10.1051/0004-6361/202243928) [Astromer 2](https://arxiv.org/abs/2502.02717) |

### Multimodal

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2025.10 | **AION-1** | [AION-1: Omnimodal Foundation Model for Astronomical Sciences](https://arxiv.org/abs/2510.17960 "Token-based masked modeling over 39 modalities from Legacy Survey, HSC, SDSS, DESI and Gaia, released at 300M to 3.1B parameters.") | NeurIPS 2025 | [Code](https://github.com/PolymathicAI/AION) | [Model](https://huggingface.co/polymathic-ai/aion-base) |
| 2024.11 | **AstroM3** | [AstroM3: A Self-Supervised Multimodal Model for Astronomy](https://arxiv.org/abs/2411.08842 "Trimodal CLIP-style pretraining on variable-star light curves, spectra and metadata.") | arXiv 2024 | [Code](https://github.com/MeriDK/AstroM3) | - |
| 2024.03 | **PAPERCLIP** | [PAPERCLIP: Associating Astronomical Observations and Natural Language with Multi-Modal Models](https://arxiv.org/abs/2403.08851 "CLIP finetuned on Hubble Space Telescope observations paired with observing proposal abstracts.") | COLM 2024 | [Code](https://github.com/smsharma/PAPERCLIP-Hubble) | - |
| 2023.10 | **AstroCLIP** | [AstroCLIP: A Cross-Modal Foundation Model for Galaxies](https://arxiv.org/abs/2310.03024 "Contrastive alignment of DESI galaxy images and spectra in a shared embedding space.") | MNRAS 2024 | [Code](https://github.com/PolymathicAI/AstroCLIP) | [Journal](https://doi.org/10.1093/mnras/stae1450) |
| 2023.10 | **MPP** | [Multiple Physics Pretraining for Physical Surrogate Models](https://arxiv.org/abs/2310.02994 "Autoregressive pretraining of a single surrogate model across heterogeneous physical simulation systems.") | NeurIPS 2024 | [Code](https://github.com/PolymathicAI/multiple_physics_pretraining) | - |

## Language and Vision-Language Models

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.09 |  | [Rethinking Domain Specialization for Open-Ended Scientific Reasoning in Astronomy Language Models](https://arxiv.org/abs/2609.17644 "Evaluates whether continued pretraining and instruction tuning on astronomy corpora help open-ended scientific reasoning.") | arXiv 2026 | - | - |
| 2025.05 | **AstroSage-70B** | [AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a 70B-Parameter Domain-Specialized Reasoning Model](https://arxiv.org/abs/2505.17592 "Llama-3.1-70B with continued pretraining and reasoning-chain SFT. Scores 89.0% on a validated 3,846-question subset of AstroMLab 1.") | arXiv 2025 | - | [Model](https://huggingface.co/AstroMLab/AstroSage-70B-20251009) |
| 2025.04 | **AstroLLaVA** | [AstroLLaVA: Towards the Unification of Astronomical Data and Natural Language](https://arxiv.org/abs/2504.08583 "LLaVA finetuned on about 30k captioned images from APOD, ESO and Hubble for astronomical visual question answering.") | ICLR 2025 Workshop (SCI-FM) | [Code](https://github.com/UniverseTBD/AstroLLaVA) | - |
| 2024.11 | **AstroSage-8B** | [AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model](https://arxiv.org/abs/2411.09012 "Llama-3.1-8B with continued pretraining on about 250k astro-ph and gr-qc preprints, SFT and model merging. Scores 80.9% on AstroMLab 1.") | Sci. Rep. 2025 | - | [Model](https://huggingface.co/AstroMLab/AstroSage-8B) [Journal](https://doi.org/10.1038/s41598-025-97131-y) |
| 2024.11 | **Astro-HEP-BERT** | [Astro-HEP-BERT: A Bidirectional Language Model for Studying the Meanings of Concepts in Astrophysics and High Energy Physics](https://arxiv.org/abs/2411.14877 "BERT model adapted to astrophysics and high energy physics literature for concept analysis.") | arXiv 2024 | - | [Model](https://huggingface.co/arnosimons/astro-hep-bert) |
| 2024.09 | **AstroLLaMA-2-70B** | [AstroMLab 2: AstroLLaMA-2-70B Model and Benchmarking Specialised LLMs for Astronomy](https://arxiv.org/abs/2409.19750 "Releases AstroLLaMA-3-8B and AstroLLaMA-2-70B and reports that the 7B AstroLLaMA series underperforms its base model.") | SC 2024 Workshop (AI4S) | - | [Model](https://huggingface.co/AstroMLab) |
| 2024.07 | **cosmosage** | [cosmosage: A Natural-Language Assistant for Cosmology](https://arxiv.org/abs/2407.04420 "Cosmology assistant built by continued pretraining on cosmology papers and textbooks followed by question-answer finetuning.") | Astron. Comput. 2025 | [Code](https://github.com/tijmen/cosmosage) | [Model](https://huggingface.co/Tijmen2/cosmosage-v3.1) [Journal](https://doi.org/10.1016/j.ascom.2025.100934) |
| 2024.01 | **AstroLLaMA-Chat** | [AstroLLaMA-Chat: Scaling AstroLLaMA with Conversational and Diverse Datasets](https://arxiv.org/abs/2401.01916 "Continual pretraining on abstracts, introductions and conclusions followed by domain conversational finetuning.") | arXiv 2024 | - | [Model](https://huggingface.co/universeTBD) |
| 2023.09 | **AstroLLaMA** | [AstroLLaMA: Towards Specialized Foundation Models in Astronomy](https://arxiv.org/abs/2309.06126 "LLaMA-2-7B finetuned on over 300k astro-ph abstracts.") | arXiv 2023 | - | [Model](https://huggingface.co/universeTBD) |
| 2021.12 | **astroBERT** | [Building astroBERT, a Language Model for Astronomy & Astrophysics](https://arxiv.org/abs/2112.00590 "BERT model with 110M parameters trained on NASA ADS papers for named entity recognition and classification.") | arXiv 2021 | - | [Model](https://huggingface.co/adsabs/astroBERT) |

## Agents and Retrieval Systems

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.11 | **auto\_research** | [A Semi-autonomous Multi-agent Pipeline for High-energy Astrophysics Research with Enforced Provenance and Verifiable Self-extension](https://arxiv.org/abs/2611.05251 "Multi-agent pipeline that retrieves HEASARC data and writes its own tools, tested by reproducing IXPE polarimetry results.") | arXiv 2026 | - | - |
| 2025.10 | **Mephisto** | [Mephisto: Self-Improving Large Language Model-Based Agents for Automated Interpretation of Multi-band Galaxy Observations](https://arxiv.org/abs/2510.08354 "Multi-agent tree search over CIGALE SED models with a self-updating knowledge base, applied to JWST Little Red Dots.") | arXiv 2025 | [Code](https://zenodo.org/records/15589045) | [Short Paper](https://arxiv.org/abs/2409.14807) |
| 2025.10 | **Denario** | [The Denario Project: Deep Knowledge AI Agents for Scientific Discovery](https://arxiv.org/abs/2510.26887 "Modular multi-agent research assistant for idea generation, analysis and paper drafting, using cmbagent as its analysis backend.") | arXiv 2025 | [Code](https://github.com/AstroPilot-AI/Denario) | [Demo](https://huggingface.co/spaces/astropilot-ai/Denario) |
| 2025.10 | **CTAgent / Gammapygpt** | [Domain-Specific Agents for Cherenkov Telescope Array Control Software and Gamma-Ray Data Analysis](https://arxiv.org/abs/2510.01299 "Agents that generate and validate CTAO control software and Gammapy analysis scripts with automated self-correction.") | arXiv 2025 | - | - |
| 2025.04 | **AI Cosmologist** | [The AI Cosmologist I: An Agentic System for Automated Data Analysis](https://arxiv.org/abs/2504.03424 "Agents for planning, coding, execution, analysis and synthesis that run machine learning experiments on cosmological datasets.") | arXiv 2025 | [Code](https://github.com/adammoss/aicosmologist) | - |
| 2025.03 | **AstroAgents** | [AstroAgents: A Multi-Agent AI for Hypothesis Generation from Mass Spectrometry Data](https://arxiv.org/abs/2503.23170 "Multi-agent system that proposes astrobiology hypotheses from mass spectrometry data.") | arXiv 2025 | [Code](https://github.com/amirgroup-codes/AstroAgents) | - |
| 2025.03 |  | [AI Agents for Ground-Based Gamma Astronomy](https://arxiv.org/abs/2503.00821 "LLM agent prototypes for CTAO control software and Gammapy analysis code generation with retrieval augmentation.") | arXiv 2025 | - | - |
| 2024.12 | **cmbagent** | [Multi-Agent System for Cosmological Parameter Analysis](https://arxiv.org/abs/2412.00431 "Planning and control system of about 30 LLM agents for autonomous cosmological data analysis.") | arXiv 2024 | [Code](https://github.com/CMBAgents/cmbagent) | [Follow-up](https://arxiv.org/abs/2507.07257) |
| 2024.12 | **StarWhisper Telescope** | [StarWhisper Telescope: An AI Framework for Automating End-to-End Astronomical Observations](https://arxiv.org/abs/2412.06412 "LLM agent that plans observations, controls a 10-telescope network and runs transient detection for the Nearby Galaxy Supernovae Survey.") | Commun. Eng. 2025 | [Code](https://github.com/Yu-Yang-Li/StarWhisper) | [Journal](https://doi.org/10.1038/s44172-025-00520-4) |
| 2024.08 | **pathfinder** | [pathfinder: A Semantic Framework for Literature Review and Knowledge Discovery in Astronomy](https://arxiv.org/abs/2408.01556 "Retrieval-augmented literature search and synthesis over about 350k ADS papers with time and citation weighting.") | ApJS 2024 | - | [Demo](https://pfdr.app) |

## Benchmarks

Benchmarks are grouped by input type. Data and modality benchmarks provide observational or simulated data with fixed splits and metrics for task-specific models. The two evaluation subsections test general or domain-adapted language and vision-language models.

### Data and Modality Benchmarks

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.07 | **Moonstone** | [Moonstone: A Multimodal Foundation Model and Benchmark for Lunar Remote Sensing](https://arxiv.org/abs/2607.03644 "Lunar remote sensing foundation model released with a benchmark of six downstream tasks.") | arXiv 2026 | - | - |
| 2025.10 | **Mars-Bench** | [Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks](https://arxiv.org/abs/2510.24010 "20 orbital and rover image datasets for classification, segmentation and object detection used to compare natural-image, Earth observation and vision-language backbones.") | NeurIPS 2025 (Datasets and Benchmarks) | - | - |
| 2025.10 | **MMAE** | [Multi-Modal Masked Autoencoders for Learning Image-Spectrum Associations for Galaxy Evolution and Cosmology](https://arxiv.org/abs/2510.22527 "Paired dataset of 134,533 HSC galaxy images and DESI spectra with a masked autoencoder baseline for cross-modal reconstruction and redshift estimation.") | arXiv 2025 | - | - |
| 2025.08 | **SuryaBench** | [SuryaBench: Benchmark Dataset for Advancing Machine Learning in Heliophysics and Space Weather Prediction](https://arxiv.org/abs/2508.14107 "Curated SDO core dataset with application benchmarks on active region emergence, flares, magnetic field extrapolation, EUV irradiance and solar wind prediction.") | arXiv 2025 | - | - |
| 2025.07 | **CosmoBench** | [CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning](https://arxiv.org/abs/2507.03707 "About 34,000 point clouds from Quijote, CAMELS-SAM and CAMELS together with 25,000 merger trees for cosmological parameter inference and tree tasks.") | NeurIPS 2025 (Datasets and Benchmarks) | - | - |
| 2023.12 | **RadioGalaxyNET** | [RadioGalaxyNET: Dataset and Novel Computer Vision Algorithms for the Detection of Extended Radio Galaxies and Infrared Hosts](https://arxiv.org/abs/2312.00306 "2,800 radio and infrared images with 4,155 expert-annotated galaxies in COCO format for multi-component radio galaxy and host detection.") | arXiv 2023 | - | - |
| 2023.05 | **MiraBest** | [MiraBest: A Dataset of Morphologically Classified Radio Galaxies for Machine Learning](https://arxiv.org/abs/2305.11108 "1,256 NVSS and FIRST radio-loud AGN labelled by Fanaroff-Riley class with confidence flags, distributed as a batched dataset for deep learning libraries.") | RASTI 2023 | [Code](https://github.com/fmporter/MiraBest-full) | [Journal](https://doi.org/10.1093/rasti/rzad017) |
| 2023.03 | **SKA SDC2** | [SKA Science Data Challenge 2: Analysis and Results](https://arxiv.org/abs/2303.07943 "Detection and characterisation of 233,245 simulated HI sources in a 2,000 h SKA-MID spectral line cube, with reproducibility awards for open pipelines.") | arXiv 2023 | - | - |
| 2022.09 | **MLGWSC-1** | [MLGWSC-1: The First Machine Learning Gravitational-Wave Search Mock Data Challenge](https://arxiv.org/abs/2209.11146 "Common datasets and metrics for comparing machine learning gravitational-wave search algorithms.") | arXiv 2022 | [Code](https://github.com/gwastro/ml-mock-data-challenge-1) | - |
| 2018.02 |  | [The Strong Gravitational Lens Finding Challenge](https://arxiv.org/abs/1802.03609 "Open challenge in which participants classified 100,000 simulated space-based and ground-based cutouts as lenses or non-lenses, comparing CNNs, SVMs, arc finders and visual inspection.") | A&A 2019 | - | - |

### Multimodal Model Evaluation

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.05 | **AstroAlertBench** | [AstroAlertBench: Evaluating the Accuracy, Reasoning, and Honesty of Multimodal LLMs in Astronomical Classification](https://arxiv.org/abs/2605.05573 "Evaluates 13 multimodal LLMs on transient alert review through metadata grounding, scientific reasoning and hierarchical classification over five classes.") | arXiv 2026 | [Code](https://github.com/LLM-for-Astronomy/AstroAlertBench) | - |
| 2026.04 | **AstroVLBench** | [A Systematic Evaluation of Vision-Language Models for Observational Astronomical Reasoning Tasks](https://arxiv.org/abs/2604.24589 "More than 4,100 expert-verified instances over five tasks covering HSC imaging, FIRST and NVSS radio maps, AKARI photometry, PLAsTiCC light curves and optical spectra.") | arXiv 2026 | - | [Data](https://huggingface.co/datasets/XiaomanZhang/AstroVLBench) |
| 2026.02 | **MarsRetrieval** | [MarsRetrieval: Benchmarking Vision-Language Models for Planetary-Scale Geospatial Retrieval on Mars](https://arxiv.org/abs/2602.13961 "Benchmark of vision-language models on retrieval over Mars orbital imagery at planetary scale.") | arXiv 2026 | - | - |
| 2025.10 | **AstroMMBench** | [AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Models Capabilities in Astronomy](https://arxiv.org/abs/2510.00063 "621 expert-reviewed multiple-choice questions on astronomical images across six subfields, used to evaluate 25 MLLMs.") | arXiv 2025 | - | - |
| 2025.03 | **AstroChart** | [DomainCQA: Crafting Knowledge-Intensive QA from Domain-Specific Charts](https://arxiv.org/abs/2503.19498 "AstroChart provides 1,690 question-answer pairs over 482 astronomy charts and is used to evaluate 21 MLLMs on perception, numerical reasoning and domain knowledge.") | AAAI 2026 | - | [Data](https://huggingface.co/datasets/yangjing0128/AstroChart) |

### Text and Reasoning Evaluation

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.10 | **Astro2Method** | [Astro2Method: Benchmarking LLMs on Machine Learning Method Selection in Astronomy](https://arxiv.org/abs/2610.30282 "500 expert-reviewed binary questions from 346 astronomy papers asking which machine learning method performs better for a stated problem.") | arXiv 2026 | - | [Data](https://huggingface.co/datasets/Xingzhongfan/Astro2Method) |
| 2026.06 | **ALeRCE Text-to-SQL** | [Querying an Astronomical Database Using Large Language Models: The ALeRCE Text-to-SQL System](https://arxiv.org/abs/2606.18108 "Evaluates thirteen LLMs on translating natural-language requests into SQL queries over the ALeRCE alert broker database, comparing direct and step-by-step generation.") | A&A 2026 | - | - |
| 2025.10 | **IOAA** | [Large Language Models Achieve Gold Medal Performance at the International Olympiad on Astronomy & Astrophysics (IOAA)](https://arxiv.org/abs/2510.05016 "Evaluates five LLMs on 49 theory and 8 data analysis problems from the 2022 to 2025 IOAA exams.") | arXiv 2025 | - | - |
| 2025.10 | **ReplicationBench** | [ReplicationBench: Can AI Agents Replicate Astrophysics Research Papers?](https://arxiv.org/abs/2510.24591 "111 tasks derived from 20 astrophysics papers that test whether agents can reproduce published results, with the best models scoring about 20 percent.") | arXiv 2025 | - | - |
| 2025.07 | **CosmoPaperQA** | [Evaluating Retrieval-Augmented Generation Agents for Autonomous Scientific Discovery in Astrophysics](https://arxiv.org/abs/2507.07155 "105 expert-written question-answer pairs from cosmology papers for comparing retrieval-augmented generation agents against human evaluation.") | arXiv 2025 | - | [Data](https://huggingface.co/datasets/ASTROANTS/CosmoPaperQA) |
| 2025.05 | **AstroVisBench** | [AstroVisBench: A Code Benchmark for Scientific Computing and Visualization in Astronomy](https://arxiv.org/abs/2505.20538 "864 processing and visualization tasks from 110 NOIRLab and STScI notebooks, scored by execution and a VLM judge.") | NeurIPS 2025 (Datasets and Benchmarks) | [Code](https://github.com/SebaJoe/AstroVisBench) | [Project](https://astrovisbench.github.io) |
| 2025 | **Astro-QA** | [An Astronomical Question Answering Dataset for Evaluating Large Language Models](https://doi.org/10.1038/s41597-025-04613-9 "3,082 English and Chinese questions of six types across astrophysics, astrometry, celestial mechanics, history and techniques, evaluated on 27 LLMs.") | Scientific Data 2025 | - | [Data](https://figshare.com/articles/dataset/Astro-QA/28235639) |
| 2024.07 | **AstroMLab 1** | [AstroMLab 1: Who Wins Astronomy Jeopardy!?](https://arxiv.org/abs/2407.11194 "4,425 multiple-choice questions curated from the Annual Review of Astronomy and Astrophysics for evaluating LLM knowledge recall.") | Astron. Comput. 2025 | - | - |

## Galaxies

### Morphology and Catalogues

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2025.03 |  | [Euclid Q1: Exploring Galaxy Morphology across Cosmic Time through Sersic Fits](https://arxiv.org/abs/2503.15309 "Euclid Q1 morphology study listed among Zoobot applications.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: First Visual Morphology Catalogue](https://arxiv.org/abs/2503.15310 "First Euclid visual morphology catalogue produced with Galaxy Zoo volunteers and Zoobot.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: A First Look at the Fraction of Bars in Massive Galaxies at z \< 1](https://arxiv.org/abs/2503.15311 "Bar fraction measurement in Euclid Q1 using machine learning morphology.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: A Census of Dwarf Galaxies across a Range of Distances and Environments](https://arxiv.org/abs/2503.15335 "Dwarf galaxy census in Euclid Q1 listed among Zoobot applications.") | arXiv 2025 | - | - |
| 2024.06 |  | [Galaxy Zoo DESI: Large-scale Bars as a Secular Mechanism for Triggering AGN](https://arxiv.org/abs/2406.20096 "Uses Galaxy Zoo DESI deep learning morphologies to study bars and AGN.") | arXiv 2024 | - | - |
| 2024.05 |  | [Galaxy Zoo: Stronger Bars Facilitate Quenching in Star-forming Galaxies](https://arxiv.org/abs/2405.05960 "Uses deep learning bar classifications to study the link between bar strength and quenching.") | arXiv 2024 | - | - |
| 2024.04 |  | [Uncovering Tidal Treasures: Automated Classification of Faint Tidal Features in DECaLS Data](https://arxiv.org/abs/2404.06487 "Classification of faint tidal features in DECaLS images using pretrained morphology models.") | arXiv 2024 | - | - |
| 2024.02 |  | [Euclid Preparation. Measuring Detailed Galaxy Morphologies for Euclid with Machine Learning](https://arxiv.org/abs/2402.10187 "Zoobot trained to predict detailed morphology for Euclid imaging.") | arXiv 2024 | - | - |
| 2023.12 |  | [Transfer Learning for Galaxy Feature Detection: Finding Giant Star-forming Clumps in Low Redshift Galaxies Using Faster R-CNN](https://arxiv.org/abs/2312.03503 "Object detection of star-forming clumps in galaxy images with transfer learning.") | arXiv 2023 | - | - |
| 2023.04 | **Astroformer** | [Astroformer: More Data Might Not be All You Need for Classification](https://arxiv.org/abs/2304.05350 "Hybrid transformer and convolutional classifier trained in the low-data regime on Galaxy10 DECals.") | arXiv 2023 | [Code](https://github.com/Rishit-dagli/Astroformer) | - |
| 2023.03 |  | [Harnessing the Hubble Space Telescope Archives: A Catalogue of 21,926 Interacting Galaxies](https://arxiv.org/abs/2303.00366 "Zoobot-based search of the HST archive for interacting galaxies.") | arXiv 2023 | - | - |
| 2023.02 | **DeepAstroUDA** | [DeepAstroUDA: Semi-Supervised Universal Domain Adaptation for Cross-Survey Galaxy Morphology Classification and Anomaly Detection](https://arxiv.org/abs/2302.02005 "Universal domain adaptation between SDSS, DECaLS and LSST mock images that also clusters unknown classes.") | MLST 2023 | [Code](https://github.com/deepskies/DeepAstroUDA) | - |
| 2021.11 |  | [A Comparison of Deep Learning Architectures for Optical Galaxy Morphology Classification](https://arxiv.org/abs/2111.04353 "Compares deep learning architectures for optical galaxy morphology classification using the Zoobot library.") | ICECET 2021 | - | [Journal](https://doi.org/10.1109/ICECET52533.2021.9698414) |
| 2021.02 | **GZ DECaLS** | [Galaxy Zoo DECaLS: Detailed Visual Morphology Measurements from Volunteers and Deep Learning for 314,000 Galaxies](https://arxiv.org/abs/2102.08414 "7.5M volunteer classifications and Bayesian CNN posteriors for 314k DECaLS galaxies.") | MNRAS 2022 | [Code](https://github.com/mwalmsley/zoobot) | [Data](https://doi.org/10.5281/zenodo.4196266) [Journal](https://doi.org/10.1093/mnras/stab2093) |
| 2020.06 | **GaMorNet** | [Galaxy Morphology Network: A Convolutional Neural Network Used to Study Morphology and Quenching in ~100,000 SDSS and ~20,000 CANDELS Galaxies](https://arxiv.org/abs/2006.14639 "CNN pretrained on simulated galaxies and transferred to SDSS and CANDELS bulge-to-total classification.") | ApJ 2020 | [Code](https://github.com/aritraghsh09/GaMorNet) | - |

### Anomaly Detection

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.08 |  | [Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN](https://arxiv.org/abs/2608.23688 "DINOv2 light-curve embeddings, isolation forests and multimodal LLM agents that vet anomaly candidates.") | arXiv 2026 | - | - |
| 2026.02 | **astromorph** | [astromorph: Self-supervised Machine Learning Pipeline for Astronomical Morphology Analysis](https://arxiv.org/abs/2602.09223 "BYOL-based embedding pipeline applied to ALMA protoplanetary disks and infrared dark clouds.") | arXiv 2026 | - | - |
| 2025.10 |  | [Re-envisioning Euclid Galaxy Morphology: Identifying and Interpreting Features with Sparse Autoencoders](https://arxiv.org/abs/2510.23749 "Sparse autoencoders on Zoobot and masked-autoencoder embeddings of Euclid Q1 galaxies to surface interpretable features.") | arXiv 2025 | - | - |
| 2025.05 | **AnomalyMatch** | [AnomalyMatch: Discovering Rare Objects of Interest with Semi-supervised and Active Learning](https://arxiv.org/abs/2505.03509 "FixMatch with EfficientNet and a user-in-the-loop active learning interface, integrated into ESA Datalabs.") | arXiv 2025 | - | - |
| 2025.05 | **AnomalyMatch HLA** | [Identifying Astrophysical Anomalies in 99.6 Million Source Cutouts from the Hubble Legacy Archive Using AnomalyMatch](https://arxiv.org/abs/2505.03508 "Applies AnomalyMatch to the full Hubble Legacy Archive and reports 1,176 new anomalies across 19 classes.") | A&A 2025 | - | - |
| 2025 | **Coniferest** | [Coniferest: A Complete Active Anomaly Detection Framework](https://doi.org/10.1016/j.ascom.2025.100960 "Isolation-forest based active anomaly detection with expert feedback, used by the SNAD team on ZTF data.") | Astron. Comput. 2025 | [Code](https://github.com/snad-space/coniferest) | - |
| 2023.11 |  | [Enabling Unsupervised Discovery in Astronomical Images through Self-Supervised Representations](https://arxiv.org/abs/2311.14157 "Self-supervised features with clustering, artefact removal, anomaly detection and similarity search on survey images.") | arXiv 2023 | - | - |
| 2023.09 |  | [Astronomaly at Scale: Searching for Anomalies Amongst 4 Million Galaxies](https://arxiv.org/abs/2309.08660 "Applies Astronomaly to about 4M galaxies using pretrained Zoobot representations.") | arXiv 2023 | - | - |
| 2021.11 | **DeepAdversaries** | [DeepAdversaries: Examining the Robustness of Deep Learning Models for Galaxy Morphology Classification](https://arxiv.org/abs/2111.00961 "Studies the robustness of galaxy morphology classifiers to image perturbations.") | arXiv 2021 | [Code](https://github.com/AleksCipri/DeepAdversaries) | - |
| 2021.05 | **HSC Anomalies** | [Anomaly Detection in Hyper Suprime-Cam Galaxy Images with Generative Adversarial Networks](https://arxiv.org/abs/2105.02434 "Wasserstein GAN anomaly scores for HSC galaxy images.") | MNRAS 2021 | [Code](https://github.com/kstoreyf/anomalies-GAN-HSC) | [Workshop Version](https://arxiv.org/abs/2012.08082) |
| 2020.10 | **Astronomaly** | [Astronomaly: Personalised Active Anomaly Detection in Astronomical Data](https://arxiv.org/abs/2010.11202 "Active learning framework that combines anomaly scores with user feedback to rank interesting objects.") | arXiv 2020 | [Code](https://github.com/MichelleLochner/astronomaly) | [Protege](https://arxiv.org/abs/2411.04188) |
| 2020.06 | **Sequencer** | [Extracting the Main Trend in a Dataset: the Sequencer Algorithm](https://arxiv.org/abs/2006.13948 "Unsupervised ordering algorithm that recovers one-dimensional trends in spectra and other datasets.") | arXiv 2020 | [Code](https://github.com/dalya/Sequencer) | - |
| 2016.11 | **Weirdest Galaxies** | [The Weirdest SDSS Galaxies: Results from an Outlier Detection Algorithm](https://arxiv.org/abs/1611.07526 "Unsupervised random forest outlier scores for about two million SDSS galaxy spectra.") | MNRAS 2017 | [Code](https://github.com/dalya/WeirdestGalaxies) | [Journal](https://doi.org/10.1093/mnras/stw3021) |

### Physical Properties and Photometric Redshifts

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.02 | **PITA** | [Optimizing Deep Learning Photometric Redshifts for the Roman Space Telescope with HST/CANDELS](https://arxiv.org/abs/2602.10207 "Semi-supervised network that combines contrastive, color and redshift losses on CANDELS images.") | arXiv 2026 | - | - |
| 2025.07 |  | [Template-Fitting Meets Deep Learning: Redshift Estimation Using Physics-Guided Neural Networks](https://arxiv.org/abs/2507.00866 "Multimodal network with cross-attention and Bayesian layers that integrates SED templates on HSC PDR3 data.") | arXiv 2025 | - | - |
| 2025.07 |  | [Deep Learning Improves Photometric Redshifts in All Regions of Color Space](https://arxiv.org/abs/2507.06299 "Self-organizing map analysis showing lower scatter and attenuation bias for image-based photo-z on SDSS.") | arXiv 2025 | - | - |
| 2025.05 | **RAIL** | [Redshift Assessment Infrastructure Layers (RAIL): Rubin-era Photometric Redshift Stress-testing and At-scale Production](https://arxiv.org/abs/2505.02928 "LSST DESC framework for training, evaluating and running photometric redshift estimators.") | arXiv 2025 | [Code](https://github.com/LSSTDESC/rail) | - |
| 2025.01 | **Hybrid-z** | [Hybrid-z: Enhancing the Kilo-Degree Survey Bright Galaxy Sample Photometric Redshifts with Deep Learning](https://arxiv.org/abs/2501.01942 "Inception CNN on four-band images combined with an MLP on nine-band magnitudes for 1.2 million KiDS-Bright galaxies.") | A&A 2025 | - | - |
| 2024.10 | **CLAP** | [CLAP. I. Resolving Miscalibration for Deep Learning-based Galaxy Photometric Redshift Estimation](https://arxiv.org/abs/2410.19390 "Supervised contrastive learning with adaptive KNN to calibrate photometric redshift probability densities.") | arXiv 2024 | - | - |
| 2024.06 |  | [Galaxy Spectroscopy without Spectra: Galaxy Properties from Photometric Images with Conditional Diffusion Models](https://arxiv.org/abs/2406.18175 "Diffusion model with contrastive networks that predicts optical spectra and photometric redshifts from SDSS images.") | arXiv 2024 | - | - |
| 2024.05 | **pzflow** | [Probabilistic Forward Modeling of Galaxy Catalogs with Normalizing Flows](https://arxiv.org/abs/2405.04740 "Normalizing flows for modeling galaxy catalogs and photometric redshift posteriors.") | AJ 2024 | [Code](https://github.com/jfcrenshaw/pzflow) | - |
| 2023.04 | **SBI++** | [SBI++: Flexible, Ultra-fast Likelihood-free Inference Customized for Astronomical Applications](https://arxiv.org/abs/2304.05281 "Neural posterior estimation for galaxy SED fitting that handles missing data and out-of-distribution noise.") | ApJL 2023 | [Code](https://github.com/wangbingjie/sbi_pp) | - |
| 2022.10 | **Mangrove** | [Mangrove: Learning Galaxy Properties from Merger Trees](https://arxiv.org/abs/2210.13473 "Graph neural networks on dark matter merger trees that emulate semi-analytic galaxy properties.") | ApJ 2022 | [Code](https://github.com/astrockragh/Mangrove) | - |
| 2022.07 | **GaMPEN** | [GaMPEN: A Machine-learning Framework for Estimating Bayesian Posteriors of Galaxy Morphological Parameters](https://arxiv.org/abs/2207.05107 "Bayesian CNN that predicts posteriors of bulge-to-total ratio, effective radius and flux.") | ApJ 2022 | [Code](https://github.com/aritraghsh09/GaMPEN) | - |
| 2022.03 | **SEDflow** | [Accelerated Bayesian SED Modeling Using Amortized Neural Posterior Estimation](https://arxiv.org/abs/2203.07391 "Amortized neural posterior estimation of 12 SED parameters in about one second per galaxy.") | ApJ 2022 | [Code](https://github.com/changhoonhahn/SEDflow) | [Journal](https://doi.org/10.3847/1538-4357/ac7b84) |
| 2022.02 | **PROVABGS** | [The DESI PRObabilistic Value-Added Bright Galaxy Survey (PROVABGS) Mock Challenge](https://arxiv.org/abs/2202.01809 "Bayesian SED modeling pipeline for DESI BGS that uses neural emulators for speed.") | arXiv 2022 | [Code](https://github.com/changhoonhahn/provabgs) | - |
| 2019.11 | **speculator** | [SPECULATOR: Emulating Stellar Population Synthesis for Fast and Accurate Galaxy Spectra and Photometry](https://arxiv.org/abs/1911.11778 "Neural network emulator of stellar population synthesis for fast SED fitting.") | ApJS 2020 | [Code](https://github.com/justinalsing/speculator) | [Journal](https://doi.org/10.3847/1538-4365/ab917f) |
| 2019 | **dense\_basis** | [Nonparametric Star Formation History Reconstruction with Gaussian Processes. I. Counting Major Episodes of Star Formation](https://doi.org/10.3847/1538-4357/ab2052 "Gaussian process representation of galaxy star formation histories for SED fitting.") | ApJ 2019 | [Code](https://github.com/kartheikiyer/dense_basis) | - |
| 2018.06 | **Pasquet Photo-z** | [Photometric Redshifts from SDSS Images Using a Convolutional Neural Network](https://arxiv.org/abs/1806.06607 "CNN that predicts redshift probability densities directly from multiband SDSS images.") | A&A 2019 | [Code](https://github.com/jpasquet/photoz) | - |
| 2016.12 | **Delight** | [Data-driven, Interpretable Photometric Redshifts Trained on Heterogeneous and Unrepresentative Data](https://arxiv.org/abs/1612.00847 "Gaussian process photometric redshifts that combine templates with data-driven flux modeling.") | ApJ 2017 | [Code](https://github.com/ixkael/Delight) | - |
| 2015.07 | **ANNz2** | [ANNz2: Photometric Redshift and Probability Distribution Function Estimation Using Machine Learning](https://arxiv.org/abs/1507.00490 "Ensembles of neural networks and boosted decision trees for photometric redshift PDFs.") | PASP 2016 | [Code](https://github.com/IftachSadeh/ANNZ) | - |

## Gravitational Lensing

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2025.11 |  | [Euclid Quick Data Release (Q1). Searching for Giant Gravitational Arcs in Galaxy Clusters with Mask Region-based Convolutional Neural Networks](https://arxiv.org/abs/2511.03064 "Mask R-CNN instance segmentation of cluster-scale lensed arcs trained on Euclidised HST simulations.") | arXiv 2025 | - | - |
| 2025.05 | **GLUE I** | [Gravitational Lenses in UNIONS and Euclid (GLUE) I: A Search for Strong Gravitational Lenses in UNIONS with Subaru, CFHT, and Pan-STARRS Data](https://arxiv.org/abs/2505.05032 "ResNet lens finder based on CMU-DeepLens applied to 8 million UNIONS galaxies.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: The Strong Lensing Discovery Engine A, System Overview and Lens Catalogue](https://arxiv.org/abs/2503.15324 "Overview of the Euclid Q1 strong lens search combining volunteers and machine learning.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: The Strong Lensing Discovery Engine C, Finding Lenses with Machine Learning](https://arxiv.org/abs/2503.15326 "Machine learning lens finders applied to Euclid Q1.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: The Strong Lensing Discovery Engine D, Double-Source-Plane Lens Candidates](https://arxiv.org/abs/2503.15327 "Double-source-plane lens candidates from the Euclid Q1 search.") | arXiv 2025 | - | - |
| 2025.03 |  | [Euclid Q1: The Strong Lensing Discovery Engine E, Ensemble Classification of Strong Gravitational Lenses](https://arxiv.org/abs/2503.15328 "Ensemble classification of lens candidates and lessons for Euclid DR1.") | arXiv 2025 | - | - |
| 2025.03 | **LEMON** | [Euclid Quick Data Release (Q1). LEMON -- Lens Modelling with Neural Networks. Automated and Fast Modelling of Euclid Gravitational Lenses with a Singular Isothermal Ellipsoid Mass Profile](https://arxiv.org/abs/2503.15329 "Bayesian neural network that predicts lens mass and light parameters and initialises classical lens modelling.") | arXiv 2025 | - | - |
| 2025.02 |  | [Euclid: Finding Strong Gravitational Lenses in the Early Release Observations Using Convolutional Neural Networks](https://arxiv.org/abs/2502.09802 "Five CNN lens finders applied to 13 Euclid ERO fields, followed by visual inspection and spectroscopic confirmation.") | arXiv 2025 | - | - |
| 2024.06 | **caustics** | [Caustics: A Python Package for Accelerated Strong Gravitational Lensing Simulations](https://arxiv.org/abs/2406.15542 "Differentiable, GPU-accelerated lensing simulator for machine learning workflows.") | JOSS 2024 | [Code](https://github.com/Ciela-Institute/caustics) | - |
| 2022.11 | **Score Lensing** | [Posterior Samples of Source Galaxies in Strong Gravitational Lenses with Score-Based Priors](https://arxiv.org/abs/2211.03812 "Score-based generative priors for lensed source reconstruction.") | arXiv 2022 | [Code](https://github.com/AlexandreAdam/score_models) | - |
| 2022.03 | **paltas** | [From Images to Dark Matter: End-to-end Inference of Substructure from Hundreds of Strong Gravitational Lenses](https://arxiv.org/abs/2203.00690 "Simulation-based inference of subhalo mass function parameters from many lenses.") | ApJ 2023 | [Code](https://github.com/swagnercarena/paltas) | - |
| 2022.02 | **GIGA-Lens** | [GIGA-Lens: Fast Bayesian Inference for Strong Gravitational Lens Modeling](https://arxiv.org/abs/2202.07663 "GPU-accelerated lens modeling with gradient-based optimization, variational inference and HMC.") | ApJ 2022 | [Code](https://github.com/giga-lens/gigalens) | - |
| 2021.10 | **Lens Mining** | [Mining for Strong Gravitational Lenses with Self-supervised Learning](https://arxiv.org/abs/2110.00023 "Self-supervised representations of DESI Legacy Survey images used to find new strong lens candidates.") | arXiv 2021 | [Code](https://github.com/georgestein/ssl-legacysurvey) | - |
| 2021.02 | **deeplenstronomy** | [deeplenstronomy: A Dataset Simulation Package for Strong Gravitational Lensing](https://arxiv.org/abs/2102.02830 "Configuration-driven simulation of strong lensing training sets for deep learning.") | JOSS 2021 | [Code](https://github.com/deepskies/deeplenstronomy) | [Journal](https://doi.org/10.21105/joss.02854) |
| 2020.12 | **h0rton** | [Large-scale Gravitational Lens Modeling with Bayesian Neural Networks for Accurate and Precise Inference of the Hubble Constant](https://arxiv.org/abs/2012.00042 "Bayesian neural network lens modeling for time-delay cosmography.") | ApJ 2021 | [Code](https://github.com/jiwoncpark/h0rton) | - |
| 2020.10 | **ovejero** | [Hierarchical Inference with Bayesian Neural Networks: An Application to Strong Gravitational Lensing](https://arxiv.org/abs/2010.13787 "Bayesian neural networks for population-level lens parameter inference.") | ApJ 2021 | [Code](https://github.com/swagnercarena/ovejero) | - |
| 2020 | **DeepLense** | [Deep Learning the Morphology of Dark Matter Substructure](https://doi.org/10.3847/1538-4357/ab7925 "Classifies strong lensing images by dark matter substructure type with deep learning.") | ApJ 2020 | [Code](https://github.com/ML4SCI/DeepLense) | - |
| 2019.09 | **Substructure Mining** | [Mining for Dark Matter Substructure: Inferring Subhalo Population Properties from Strong Lenses with Machine Learning](https://arxiv.org/abs/1909.02005 "Likelihood-ratio estimation with neural networks for subhalo population inference from lensed images.") | arXiv 2019 | [Code](https://github.com/smsharma/mining-for-substructure-lens) | - |
| 2019.08 | **DeepMass** | [Deep Learning Dark Matter Map Reconstructions from DES SV Weak Lensing Data](https://arxiv.org/abs/1908.00543 "U-Net mass mapping of Dark Energy Survey Science Verification weak lensing data.") | MNRAS 2020 | [Code](https://github.com/NiallJeffrey/DeepMass) | - |
| 2017.03 | **CMU DeepLens** | [CMU DeepLens: Deep Learning for Automatic Image-based Galaxy-Galaxy Strong Lens Finding](https://arxiv.org/abs/1703.02642 "Residual network strong lens finder.") | MNRAS 2018 | [Code](https://github.com/McWilliamsCenter/CMUDeepLens) | - |

## Source Detection, Deblending and Image Simulation

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.04 |  | [Diffusion-based Galaxy Simulations for the Roman High Latitude Survey](https://arxiv.org/abs/2604.22917 "DDPM trained on JWST JADES imaging to generate Roman-like multi-band galaxy stamps for weak lensing.") | arXiv 2026 | - | - |
| 2026 | **scarlet2** | [scarlet2: Astronomical Scene Modeling in JAX](https://doi.org/10.21105/joss.09646 "JAX scene modeling for multi-band, multi-epoch and multi-instrument data with neural network priors.") | JOSS 2026 | [Code](https://github.com/pmelchior/scarlet2) | - |
| 2025.06 | **GalaxySD** | [Can AI Dream of Unseen Galaxies? Conditional Diffusion Model for Galaxy Morphology Augmentation](https://arxiv.org/abs/2506.16233 "Stable Diffusion fine-tuned on Galaxy Zoo 2 morphology prompts to augment classifiers and find rare dusty early-type galaxies.") | arXiv 2025 | - | - |
| 2025.06 | **GalCatDiff** | [Category-based Galaxy Image Generation via Diffusion Models](https://arxiv.org/abs/2506.16255 "Class-conditioned diffusion model with residual attention blocks trained on Galaxy10 DECaLS categories.") | arXiv 2025 | - | - |
| 2025.04 |  | [Denoising Diffusion Probabilistic Model for Realistic and Fast Generated Euclid-like Data for Weak Lensing Analysis](https://arxiv.org/abs/2504.07183 "DDPM trained on CANDELS images that generates Euclid-like galaxies for shear calibration.") | arXiv 2025 | - | - |
| 2025 | **BTK** | [The Blending ToolKit: A Simulation Framework for Evaluation of Galaxy Detection and Deblending](https://doi.org/10.33232/001c.129699 "Simulation and metrics framework for benchmarking detection and deblending algorithms.") | OJAp 2025 | [Code](https://github.com/LSSTDESC/BlendingToolKit) | - |
| 2024.07 | **MuyGPs Stellar Blends** | [Stellar Blend Image Classification Using Computationally Efficient Gaussian Processes](https://arxiv.org/abs/2407.19297 "Scalable Gaussian process classification of blended stellar images.") | arXiv 2024 | [Code](https://github.com/LLNL/MuyGPyS) | - |
| 2022.03 | **WaveDiff** | [Rethinking Data-driven Point Spread Function Modeling with a Differentiable Optical Model](https://arxiv.org/abs/2203.04908 "Differentiable wavefront-based PSF model that captures chromatic variations for Euclid-like telescopes.") | Inverse Problems 2023 | [Code](https://github.com/CosmoStat/wf-psf) | - |
| 2021.11 | **astroddpm** | [Realistic Galaxy Image Simulation via Score-Based Generative Models](https://arxiv.org/abs/2111.01713 "Denoising diffusion models that generate realistic galaxy images.") | MNRAS 2022 | [Code](https://github.com/Smith42/astroddpm) | - |
| 2021.07 | **MuyGPs Blends** | [Gaussian Process Classification of Galaxy Blend Identification in LSST](https://arxiv.org/abs/2107.09246 "Gaussian process classifiers that flag blended galaxies in simulated LSST images.") | arXiv 2021 | [Code](https://github.com/LLNL/MuyGPyS) | - |
| 2021.05 | **MuyGPs Star-Galaxy Images** | [Star-Galaxy Image Separation with Computationally Efficient Gaussian Process Classification](https://arxiv.org/abs/2105.01106 "Scalable local Gaussian process classification of star and galaxy image cutouts.") | arXiv 2021 | [Code](https://github.com/LLNL/MuyGPyS) | - |
| 2020.12 | **PS1 Point Source Catalog II** | [A Morphological Classification Model to Identify Unresolved PanSTARRS1 Sources II: Update to the PS1 Point Source Catalog](https://arxiv.org/abs/2012.01544 "Random forest star and galaxy separation for Pan-STARRS1 sources.") | PASP 2021 | [Code](https://github.com/adamamiller/PS1_star_galaxy) | - |
| 2020.10 | **MuyGPs Star-Galaxy** | [Star-Galaxy Separation via Gaussian Processes with Model Reduction](https://arxiv.org/abs/2010.06094 "Gaussian process classification of stars and galaxies with dimensionality reduction.") | arXiv 2020 | [Code](https://github.com/LLNL/MuyGPyS) | - |
| 2020.08 | **galsim-hub** | [Deep Generative Models for Galaxy Image Simulations](https://arxiv.org/abs/2008.03833 "Conditional generative models of galaxy light profiles integrated with GalSim.") | MNRAS 2021 | [Code](https://github.com/McWilliamsCenter/galsim_hub) | - |
| 2020.05 | **DeblenderVAE** | [Deblending Galaxies with Variational Autoencoders: A Joint Multi-band, Multi-instrument Approach](https://arxiv.org/abs/2005.12039 "VAE-based deblender trained jointly on ground and space-based simulated images.") | arXiv 2020 | [Code](https://github.com/LSSTDESC/DeblenderVAE) [Updated Code](https://github.com/astrodeepnet/debvader) | - |
| 2019 | **Astro R-CNN** | [Deblending and Classifying Astronomical Sources with Mask R-CNN Deep Learning](https://doi.org/10.1093/mnras/stz2845 "Instance segmentation for joint detection, deblending and star-galaxy classification.") | MNRAS 2019 | [Code](https://github.com/burke86/astro_rcnn) | - |
| 2018.02 | **scarlet** | [scarlet: Source Separation in Multi-band Images by Constrained Matrix Factorization](https://arxiv.org/abs/1802.10157 "Constrained matrix factorization deblender for multiband survey images.") | Astron. Comput. 2018 | [Code](https://github.com/pmelchior/scarlet) | [Journal](https://doi.org/10.1016/j.ascom.2018.07.001) |

## Stars and Stellar Spectroscopy

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.04 | **ASTRAFier** | [ASTRAFier: A Novel and Scalable Transformer-based Stellar Variability Classifier](https://arxiv.org/abs/2604.07437 "BiLSTM, attention and CNN classifier applied to about 2.8 million TESS light curves.") | arXiv 2026 | - | - |
| 2026.03 |  | [A Generalist Model Including Evolved Star Mass and Age](https://arxiv.org/abs/2603.03732 "Extends a transformer stellar foundation model to infer mass and age of giants from Gaia XP spectra.") | arXiv 2026 | - | - |
| 2025.10 | **EBOP MAVEN** | [EBOP MAVEN: A Machine Learning Model to Estimate the Input Parameters for Analytic Fitting of Detached Eclipsing Binary Light Curves](https://arxiv.org/abs/2510.21465 "CNN that predicts detached eclipsing binary parameters from phase-folded TESS light curves to initialise JKTEBOP fits.") | arXiv 2025 | - | - |
| 2025.08 |  | [The Use of Conditional Variational Autoencoders in Generating Stellar Spectra](https://arxiv.org/abs/2508.17059 "CVAE that generates stellar spectra over a grid of atmospheric parameters, rotation and instrumental resolution.") | arXiv 2025 | - | - |
| 2025.07 |  | [Millions of Main-Sequence Binary Stars from Gaia BP/RP Spectra](https://arxiv.org/abs/2507.09622 "Neural spectral emulator of single stars used to identify more than 14 million binary candidates from XP spectra.") | arXiv 2025 | - | - |
| 2025.05 | **UA-CSNet** | [Metallicities of 20 Million Giant Stars Based on Gaia XP Spectra](https://arxiv.org/abs/2505.05281 "Uncertainty-aware cost-sensitive network that estimates metallicities down to [Fe/H] about -4 for giants.") | arXiv 2025 | - | - |
| 2024.11 |  | [Mapping the Milky Way with Gaia Bp/Rp Spectra I: Systematic Flux Corrections and Atmospheric Parameters for 68 Million Stars](https://arxiv.org/abs/2411.19105 "APOGEE-trained network that corrects XP flux systematics before model-atmosphere fitting.") | arXiv 2024 | - | - |
| 2024.10 |  | [Predicting Metallicities and Carbon Abundances from Gaia XP Spectra for (Carbon-enhanced) Metal-poor Stars](https://arxiv.org/abs/2410.11077 "Heteroscedastic neural network ensemble that predicts [Fe/H] and [C/Fe] for more than 10 million XP stars.") | arXiv 2024 | - | - |
| 2024.07 | **LightPred** | [Accurate and Robust Stellar Rotation Periods Catalog for 82771 Kepler Stars Using Deep Learning](https://arxiv.org/abs/2407.06858 "LSTM and transformer model pretrained contrastively on Kepler light curves and trained on spot-model simulations.") | arXiv 2024 | - | - |
| 2020.05 | **Blancato CNN** | [Data-driven Derivation of Stellar Properties from Photometric Time Series Data Using Convolutional Neural Networks](https://arxiv.org/abs/2005.09682 "CNNs that infer stellar rotation and surface gravity from Kepler light curves.") | ApJ 2022 | [Code](https://github.com/kblancato/theia-net) | - |
| 2020 | **stella** | [stella: Convolutional Neural Networks for Flare Identification in TESS](https://doi.org/10.21105/joss.02347 "CNN flare detection in TESS two-minute light curves.") | JOSS 2020 | [Code](https://github.com/afeinstein20/stella) | - |
| 2018.08 | **astroNN** | [Deep Learning of Multi-element Abundances from High-resolution Spectroscopic Data](https://arxiv.org/abs/1808.04428 "Bayesian neural networks for stellar parameters and abundances from APOGEE spectra.") | MNRAS 2019 | [Code](https://github.com/henrysky/astroNN) | [Journal](https://doi.org/10.1093/mnras/sty3217) |

## Time-Domain Astronomy and Transients

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.07 | **NAPTIME** | [NAPTIME: A Neural-Process Framework for Rubin Alert Classification](https://arxiv.org/abs/2607.19236 "Neural process that jointly reconstructs and classifies sparse multiband light curves on ELAsTiCC2 and MALLORN.") | arXiv 2026 | - | - |
| 2026.06 | **PIE-ADA** | [PIE-ADA: Physics-Informed Ensemble with Adaptive Data Augmentation for Photometric Transient Classification](https://arxiv.org/abs/2606.29367 "Physics-motivated light-curve augmentation for rare classes combined with gradient boosted ensembles.") | arXiv 2026 | - | - |
| 2025.02 |  | [Real-Time Active Learning for Optimised Spectroscopic Follow-up: Enhancing Early SN Ia Classification with the Fink Broker](https://arxiv.org/abs/2502.19555 "Active learning loop on the Fink stream that selects spectroscopic targets to improve early SN Ia classifiers.") | arXiv 2025 | - | - |
| 2025.01 | **ORACLE** | [ORACLE: A Real-Time, Hierarchical, Deep-Learning Photometric Classifier for the LSST](https://arxiv.org/abs/2501.01496 "Hierarchical recurrent classifier for real-time LSST alert streams.") | arXiv 2025 | [Code](https://github.com/uiucsn/ORACLE) | - |
| 2025.01 | **AMPEL** | [AMPEL Workflows for LSST: Modular and Reproducible Real-time Photometric Classification](https://arxiv.org/abs/2501.16511 "SNGuess, FollowMe and FinalBet classification channels for ELAsTiCC alerts.") | arXiv 2025 | - | - |
| 2024.04 | **CATS** | [Transient Classifiers for Fink](https://arxiv.org/abs/2404.08798 "Tree-based and deep learning classifiers in the Fink broker evaluated on ELAsTiCC, including the CATS architecture.") | arXiv 2024 | - | - |
| 2024.01 | **BTSbot** | [The Zwicky Transient Facility Bright Transient Survey. III. BTSbot: Automated Identification and Follow-up of Bright Transients with Deep Learning](https://arxiv.org/abs/2401.15167 "Multimodal CNN that selects bright transients for automated spectroscopic follow-up.") | arXiv 2024 | [Code](https://github.com/nabeelre/BTSbot) | [Follow-up](https://arxiv.org/abs/2512.11957) |
| 2023.11 |  | [Identifying Light-curve Signals with a Deep-learning-based Object Detection Algorithm. II. A General Light-curve Classification Framework](https://arxiv.org/abs/2311.08080 "Object-detection based classifier on light curves and power spectra from Kepler, TESS and ZTF.") | arXiv 2023 | - | - |
| 2022.08 | **MuyGPs Light Curves** | [Light Curve Completion and Forecasting Using Fast and Scalable Gaussian Processes (MuyGPs)](https://arxiv.org/abs/2208.14592 "Scalable Gaussian processes for filling gaps in and forecasting light curves.") | arXiv 2022 | [Code](https://github.com/LLNL/MuyGPyS) | - |
| 2021.11 | **ACAI** | [Phenomenological Classification of the Zwicky Transient Facility Astronomical Event Alerts](https://arxiv.org/abs/2111.12142 "Multi-label deep learning classifiers for ZTF alert phenomenology.") | arXiv 2021 | [Code](https://github.com/dmitryduev/acai) | - |
| 2021.06 | **SCONE** | [SCONE: Supernova Classification with a Convolutional Neural Network](https://arxiv.org/abs/2106.04370 "CNN on wavelength-time heatmaps of supernova light curves.") | AJ 2021 | [Code](https://github.com/helenqu/scone) | [Early-time Paper](https://arxiv.org/abs/2111.05539) |
| 2021.05 | **Time-Series Transformer** | [Paying Attention to Astronomical Transients: Introducing the Time-series Transformer for Photometric Classification](https://arxiv.org/abs/2105.06178 "Transformer classifier for multiband transient light curves evaluated on PLAsTiCC.") | RASTI 2024 | [Code](https://github.com/tallamjr/astronet) | - |
| 2021.02 | **SCoPe** | [The ZTF Source Classification Project: I. Methods and Infrastructure](https://arxiv.org/abs/2102.11304 "Modular machine learning framework for classifying variable sources in ZTF light curves.") | AJ 2021 | [Code](https://github.com/ZwickyTransientFacility/scope) | [Journal](https://doi.org/10.3847/1538-3881/abe853) |
| 2021 | **Roman Microlensing NPE** | [Real-time Likelihood-free Inference of Roman Binary Microlensing Events with Amortized Neural Posterior Estimation](https://doi.org/10.3847/1538-3881/abf42e "ResNet-GRU featurizer and normalizing flow that infer binary microlensing parameters in real time.") | AJ 2021 | [Code](https://github.com/kmzzhang/nbi) | - |
| 2020.11 | **Cyclic-Permutation Networks** | [Classification of Periodic Variable Stars with Novel Cyclic-permutation Invariant Neural Networks](https://arxiv.org/abs/2011.01243 "Phase-folded light-curve classifiers that are invariant to cyclic permutations.") | MNRAS 2021 | [Code](https://github.com/kmzzhang/periodicnetwork) | - |
| 2019.07 | **braai** | [Real-bogus Classification for the Zwicky Transient Facility Using Deep Learning](https://arxiv.org/abs/1907.11259 "CNN real-bogus classifier deployed in the ZTF alert pipeline.") | MNRAS 2019 | [Code](https://github.com/dmitryduev/braai) | - |
| 2019.04 | **DeepStreaks** | [DeepStreaks: Identifying Fast-moving Objects in the Zwicky Transient Facility Data with Deep Learning](https://arxiv.org/abs/1904.05920 "CNN ensemble that identifies streaks from fast-moving near-Earth objects in ZTF images.") | MNRAS 2019 | [Code](https://github.com/dmitryduev/DeepStreaks) | - |
| 2019.01 | **SuperNNova** | [SuperNNova: An Open-Source Framework for Bayesian, Neural Network Based Supernova Classification](https://arxiv.org/abs/1901.06384 "Recurrent and Bayesian neural networks for light-curve classification.") | MNRAS 2020 | [Code](https://github.com/supernnova/SuperNNova) | [Journal](https://doi.org/10.1093/mnras/stz3312) |
| 2016.03 | **snmachine** | [Photometric Supernova Classification with Machine Learning](https://arxiv.org/abs/1603.00882 "Feature extraction and classifier pipeline for photometric supernova typing.") | ApJS 2016 | [Code](https://github.com/LSSTDESC/snmachine) | [Rubin Study](https://arxiv.org/abs/2107.07531) |

## Exoplanets

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.04 | **ExoNet** | [ExoNet: Calibrated Multimodal Deep Learning for TESS Exoplanet Candidate Vetting Using Phase-Folded Light Curves, Stellar Parameters, and Multi-Head Attention](https://arxiv.org/abs/2604.15560 "Late fusion of light-curve CNN features with attention and stellar parameters, calibrated by temperature scaling.") | arXiv 2026 | - | - |
| 2026.03 | **RAVEN** | [Automatic Search for Transiting Planets in TESS-SPOC FFIs with RAVEN: Over 100 Newly Validated Planets and Over 2000 Vetted Candidates](https://arxiv.org/abs/2603.22597 "Machine learning classifiers trained on injected simulations combined with statistical validation for TESS FFI candidates.") | arXiv 2026 | - | - |
| 2025.11 | **WATSON-Net** | [WATSON-Net: Vetting, Validation, and Analysis of Transits from Space Observations with Neural Networks](https://arxiv.org/abs/2511.08768 "Multi-branch network for transit vetting integrated into the SHERLOCK pipeline.") | arXiv 2025 | - | - |
| 2025.09 |  | [Exoplanetary Atmospheres Retrieval via a Quantum Extreme Learning Machine](https://arxiv.org/abs/2509.03617 "Quantum extreme learning machine retrieval executed on IBM quantum hardware.") | arXiv 2025 | - | - |
| 2025.09 |  | [Identifying Exoplanets with Deep Learning: A CNN and RNN Classifier for Kepler DR25 and Candidate Vetting](https://arxiv.org/abs/2509.04793 "CNN, bidirectional LSTM and attention classifier for Kepler DR25 transit signals.") | arXiv 2025 | - | - |
| 2025.08 |  | [Towards the Habitable Worlds Observatory: Retrieval of Reflection Spectra from Evolving Earth Analogues Using 1D CNNs](https://arxiv.org/abs/2508.00076 "1D CNN retrieval of composition and planetary properties from HWO-like reflected-light spectra.") | arXiv 2025 | - | - |
| 2025.08 |  | [Supervised Machine Learning Methods with Uncertainty Quantification for Exoplanet Atmospheric Retrievals from Transmission Spectroscopy](https://arxiv.org/abs/2508.04982 "Benchmark of PLS, SVM, KNN, tree ensembles and XGBoost on Ariel-like transmission spectra.") | arXiv 2025 | - | - |
| 2025.06 | **DART-Vetter** | [DART-Vetter: A Deep LeARning Tool for Automatic Triage of Exoplanet Candidates](https://arxiv.org/abs/2506.05556 "Compact CNN on phase-folded light curves that triages TESS and Kepler threshold crossing events.") | arXiv 2025 | - | - |
| 2025.02 | **FASTER** | [Near-instantaneous Atmospheric Retrievals and Model Comparison with FASTER](https://arxiv.org/abs/2502.18045 "Neural ratio estimation for marginal posteriors and amortized Bayesian model comparison, applied to WASP-39b.") | arXiv 2025 | - | - |
| 2025.02 |  | [Exoplanet Transit Candidate Identification in TESS Full-Frame Images via a Transformer-Based Algorithm](https://arxiv.org/abs/2502.07542 "Convolutional embeddings and transformer encoder applied to flux, centroid and background series of 4.1 million light curves.") | arXiv 2025 | - | - |
| 2024.10 | **FMPE Retrieval** | [Flow Matching for Atmospheric Retrieval of Exoplanets: Where Reliability Meets Adaptive Noise Levels](https://arxiv.org/abs/2410.21477 "Flow matching posterior estimation with importance sampling to verify retrievals and estimate the evidence.") | arXiv 2024 | - | - |
| 2024.01 | **FlopPITy** | [FlopPITy: Enabling Self-consistent Exoplanet Atmospheric Retrievals with Machine Learning](https://arxiv.org/abs/2401.04168 "Sequential neural posterior estimation with neural spline flows for self-consistent atmospheric retrievals.") | arXiv 2024 | - | - |
| 2023.11 | **AESTRA** | [AESTRA: Deep Learning for Precise Radial Velocity Estimation in the Presence of Stellar Activity](https://arxiv.org/abs/2311.18326 "Self-supervised spectrum autoencoder and RV estimator that separate Doppler shifts from activity-induced line-profile changes.") | AJ 2024 | [Code](https://github.com/yanliang-astro/aestra) | [Journal](https://doi.org/10.3847/1538-3881/ad0e01) [Paper II](https://arxiv.org/abs/2606.13574) |
| 2023.01 | **SBI-EAR** | [Neural Posterior Estimation for Exoplanetary Atmospheric Retrieval](https://arxiv.org/abs/2301.06575 "Normalizing-flow posterior estimation for exoplanet atmospheric retrieval.") | A&A 2023 | [Code](https://github.com/MalAstronomy/sbi-ear) | - |
| 2022.04 | **HSR4HCI** | [Half-sibling Regression Meets Exoplanet Imaging: PSF Modeling and Subtraction Using a Flexible, Domain Knowledge-driven, Causal Framework](https://arxiv.org/abs/2204.03439 "Data-driven PSF subtraction for high-contrast imaging based on half-sibling regression.") | A&A 2022 | [Code](https://github.com/timothygebhard/hsr4hci) | - |
| 2021.11 | **ExoMiner** | [ExoMiner: A Highly Accurate and Explainable Deep Learning Classifier that Validates 301 New Exoplanets](https://arxiv.org/abs/2111.10009 "Multi-branch network that mimics expert vetting diagnostics and validates 301 Kepler planets.") | ApJ 2022 | [Code](https://github.com/nasa/ExoMiner) | [Journal](https://doi.org/10.3847/1538-4357/ac4399) |
| 2021.01 | **BNN Chaos** | [A Bayesian Neural Network Predicts the Dissolution of Compact Planetary Systems](https://arxiv.org/abs/2101.04117 "Bayesian neural network that predicts instability times of compact planetary systems.") | PNAS 2021 | [Code](https://github.com/MilesCranmer/bnn_chaos_model) | - |
| 2021 | **MARGE** | [Accurate Machine-learning Atmospheric Retrieval via a Neural-network Surrogate Model for Radiative Transfer](https://doi.org/10.3847/PSJ/abe3fd "Neural surrogate for radiative transfer that accelerates exoplanet atmospheric retrieval.") | PSJ 2021 | [Code](https://github.com/exosports/MARGE) | - |
| 2020.07 | **SPOCK** | [Predicting the Long-term Stability of Compact Multiplanet Systems](https://arxiv.org/abs/2007.06521 "Gradient boosted classifier on short N-body integrations that predicts multiplanet stability.") | PNAS 2020 | [Code](https://github.com/dtamayo/spock) | [Follow-up](https://arxiv.org/abs/2408.08873) |
| 2019.04 | **Astronet-Triage** | [Identifying Exoplanets with Deep Learning III: Automated Triage and Vetting of TESS Candidates](https://arxiv.org/abs/1904.02726 "Neural networks for triage and vetting of TESS transit signals.") | AJ 2019 | [Code](https://github.com/yuliang419/Astronet-Triage) | [Journal](https://doi.org/10.3847/1538-3881/ab21d6) |
| 2019.03 | **AstroNet-K2** | [Identifying Exoplanets with Deep Learning II: Two New Super-Earths Uncovered by a Neural Network in K2 Data](https://arxiv.org/abs/1903.10507 "AstroNet adapted to K2 light curves.") | AJ 2019 | [Code](https://github.com/aedattilo/models_K2) | - |
| 2018.06 | **HELA** | [Supervised Machine Learning for Analysing Spectra of Exoplanetary Atmospheres](https://arxiv.org/abs/1806.03944 "Random forest atmospheric retrieval for exoplanet transmission spectra.") | Nature Astronomy 2018 | [Code](https://github.com/exoclime/HELA) | - |
| 2018.06 | **ExoGAN** | [ExoGAN: Retrieving Exoplanetary Atmospheres Using Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1806.02906 "Generative adversarial network for atmospheric retrieval.") | AJ 2018 | [Code](https://github.com/ucl-exoplanets/ExoGAN_public) | - |
| 2018 | **AstroNet** | [Identifying Exoplanets with Deep Learning: A Five-planet Resonant Chain around Kepler-80 and an Eighth Planet around Kepler-90](https://doi.org/10.3847/1538-3881/aa9e09 "CNN transit classifier for Kepler threshold crossing events.") | AJ 2018 | [Code](https://github.com/google-research/exoplanet-ml) | - |
| 2017.06 | **Pearson Exoplanet AI** | [Searching for Exoplanets Using Artificial Intelligence](https://arxiv.org/abs/1706.04319 "Neural networks that detect transit signals in simulated and Kepler light curves.") | MNRAS 2018 | [Code](https://github.com/pearsonkyle/Exoplanet-Artificial-Intelligence) | - |

## Cosmology and Large-Scale Structure

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.07 |  | [From Dark Matter to Galaxies: Halo-Free Mock Generation via Conditional Point-Cloud Diffusion](https://arxiv.org/abs/2607.19808 "Point-cloud diffusion that generates galaxy positions and star formation rates from IllustrisTNG dark matter fields.") | arXiv 2026 | - | - |
| 2026.06 |  | [Dark Energy Survey Year 3 Results: Optimized wCDM Simulation-based Inference with Weak Lensing Map-level Hybrid Statistics](https://arxiv.org/abs/2606.11309 "Hybrid power spectrum and neural summaries that compress DES Y3 lensing maps to seven statistics.") | arXiv 2026 | - | - |
| 2026.06 |  | [Field-level Weak Lensing Cosmology with 60 Simulations Using Multifidelity Simulation-based Inference](https://arxiv.org/abs/2606.23346 "Pretraining on lognormal mocks and fine-tuning on 60 N-body simulations for KiDS-Legacy field-level inference.") | arXiv 2026 | - | - |
| 2026.06 |  | [Simulation-Based Inference for Cluster Cosmology with Set-Based Neural Network Architectures](https://arxiv.org/abs/2606.27439 "Set-based networks and autoregressive flows on eRASS1-like cluster catalogues.") | arXiv 2026 | - | - |
| 2025.11 |  | [Dark Energy Survey Year 3 Results: Simulation-based wCDM Inference from Weak Lensing and Galaxy Clustering Maps with Deep Learning. I. Analysis Design](https://arxiv.org/abs/2511.04681 "Graph CNN compression of spherical lensing and clustering maps with normalizing-flow likelihoods.") | arXiv 2025 | - | - |
| 2025.11 |  | [Fast End-to-End Framework for Cosmological Parameter Inference from CMB Data Using Machine Learning](https://arxiv.org/abs/2511.01291 "Combines analytical blind separation of foregrounds with neural network parameter inference.") | arXiv 2025 | - | - |
| 2025.11 |  | [Deep-learning Mitigation of Foregrounds and Beam Effects in 21-cm Intensity Mapping Using Hybrid Frequency Differencing and PCA](https://arxiv.org/abs/2511.15072 "Two-channel UNet with frequency-differenced and PCA-cleaned inputs for HI reconstruction under realistic beams.") | arXiv 2025 | - | - |
| 2025.09 | **21cmLSTM / 21cmKAN** | [Emulating Global 21 cm Cosmology Observations from the Lunar Far Side to Achieve Quick and Reliable Physical Constraints](https://arxiv.org/abs/2509.00976 "LSTM and Kolmogorov-Arnold network emulators of the global 21-cm signal for Bayesian inference.") | arXiv 2025 | [Code](https://github.com/jdorigojones/21cmKAN) | - |
| 2025.09 |  | [Exploring the Early Universe with Deep Learning](https://arxiv.org/abs/2509.22018 "Benchmark of deep learning models that recover the neutral hydrogen fraction from 2D 21-cm power spectra.") | arXiv 2025 | - | - |
| 2025.06 |  | [Dark Energy Survey Year 3 Results: wCDM Cosmology from Simulation-based Inference with Persistent Homology on the Sphere](https://arxiv.org/abs/2506.13439 "Spherical persistent homology summaries with neural compression and likelihood estimation on DES Y3 lensing maps.") | arXiv 2025 | - | - |
| 2025.01 | **Effort.jl** | [Effort.jl: A Fast and Differentiable Emulator for the Effective Field Theory of the Large Scale Structure of the Universe](https://arxiv.org/abs/2501.04639 "Differentiable neural emulator of EFTofLSS galaxy power spectra.") | arXiv 2025 | [Code](https://github.com/CosmologicalEmulators/Effort.jl) | - |
| 2024.12 |  | [Nonlinear Reconstruction of 21cm Global Signal from 21cm Power Spectrum with Artificial Neural Networks](https://arxiv.org/abs/2412.20862 "Neural network that predicts the global 21-cm signal from power spectrum measurements under SKA-like noise.") | arXiv 2024 | - | - |
| 2024.09 |  | [Simulation-based Inference Benchmark for Weak Lensing Cosmology](https://arxiv.org/abs/2409.17975 "Compares simulation budgets of explicit and implicit full-field inference for LSST Y10-like convergence maps.") | arXiv 2024 | - | - |
| 2024.07 |  | [Optimal Neural Summarisation for Full-Field Weak Lensing Cosmological Implicit Inference](https://arxiv.org/abs/2407.10877 "Compares neural compression losses against an HMC full-field reference with a differentiable lognormal simulator.") | arXiv 2024 | [Code](https://github.com/DifferentiableUniverseInitiative/sbi_lens) | - |
| 2023.09 | **21cmEMU** | [21cmEMU: An Emulator of 21cmFAST Summary Observables](https://arxiv.org/abs/2309.05697 "Neural emulator of 21cmFAST power spectra and global signals.") | MNRAS 2024 | [Code](https://github.com/21cmfast/21cmEMU) | - |
| 2023.07 | **Capse.jl** | [Capse.jl: Efficient and Auto-differentiable CMB Power Spectra Emulation](https://arxiv.org/abs/2307.14339 "Julia neural emulator of CMB power spectra for gradient-based samplers.") | arXiv 2023 | [Code](https://github.com/CosmologicalEmulators/Capse.jl) | - |
| 2023.06 |  | [In Search of Global 21-cm Signal Using Artificial Neural Network in Light of ARCADE 2](https://arxiv.org/abs/2306.02039 "Neural network that extracts global 21-cm parameters from antenna temperatures with foregrounds and ionospheric distortion.") | arXiv 2023 | - | - |
| 2023.05 | **CosmoPower-JAX** | [CosmoPower-JAX: High-dimensional Bayesian Inference with Differentiable Cosmological Emulators](https://arxiv.org/abs/2305.06347 "JAX version of CosmoPower for gradient-based samplers.") | arXiv 2023 | [Code](https://github.com/dpiras/cosmopower-jax) | - |
| 2022.05 | **CONNECT** | [CONNECT: A Neural Network Based Framework for Emulating Cosmological Observables and Cosmological Parameter Inference](https://arxiv.org/abs/2205.15726 "Iteratively trained emulators of CLASS observables for MCMC.") | JCAP 2023 | [Code](https://github.com/AarhusCosmology/connect_public) | - |
| 2022.04 | **CosmoGraphNet** | [Learning Cosmology and Clustering with Cosmic Graphs](https://arxiv.org/abs/2204.13713 "Graph neural networks on galaxy catalogues for cosmological parameter inference.") | arXiv 2022 | [Code](https://github.com/PabloVD/CosmoGraphNet) | - |
| 2022.03 | **DeepLSS** | [DeepLSS: Breaking Parameter Degeneracies in Large-scale Structure with Deep Learning Analysis of Combined Probes](https://arxiv.org/abs/2203.09616 "Deep learning analysis of combined weak lensing and galaxy clustering maps.") | PRX 2022 | [Code](https://github.com/tomaszkacprzak/deeplss) | - |
| 2022.03 | **LINNA** | [LINNA: Likelihood Inference Neural Network Accelerator](https://arxiv.org/abs/2203.05583 "Neural network emulation of the likelihood for accelerated cosmological parameter inference.") | arXiv 2022 | [Code](https://github.com/chto/linna) | - |
| 2022 | **21cmVAE** | [21cmVAE: A Very Accurate Emulator of the 21 cm Global Signal](https://doi.org/10.3847/1538-4357/ac6424 "Variational autoencoder emulator of the global 21-cm signal.") | ApJ 2022 | [Code](https://github.com/christianhbye/21cmVAE) | - |
| 2021.11 | **HaloGraphNet** | [Inferring Halo Masses with Graph Neural Networks](https://arxiv.org/abs/2111.08683 "Graph neural networks trained on CAMELS to infer halo masses from galaxy properties.") | ApJ 2022 | [Code](https://github.com/PabloVD/HaloGraphNet) | - |
| 2021.11 | **harmonic** | [Machine Learning Assisted Bayesian Model Comparison: Learnt Harmonic Mean Estimator](https://arxiv.org/abs/2111.12720 "Learned harmonic mean estimator of the Bayesian evidence from posterior samples.") | arXiv 2021 | [Code](https://github.com/astro-informatics/harmonic) | [Flow Version](https://arxiv.org/abs/2307.00048) |
| 2021.11 | **DeepMass CMB** | [Single Frequency CMB B-mode Inference with Realistic Foregrounds from a Single Training Image](https://arxiv.org/abs/2111.01138 "Moment networks trained on a single foreground image for CMB B-mode inference.") | MNRAS Letters 2021 | [Code](https://github.com/NiallJeffrey/DeepMass) | - |
| 2021.07 | **FieldIMNNs** | [Lossless, Scalable Implicit Likelihood Inference for Cosmological Fields](https://arxiv.org/abs/2107.07405 "Information maximising neural network compression of Gaussian and lognormal fields followed by simulation-based inference.") | JCAP 2021 | [Code](https://github.com/tlmakinen/FieldIMNNs) | [Journal](https://doi.org/10.1088/1475-7516/2021/11/049) |
| 2021.06 | **CosmoPower** | [CosmoPower: Emulating Cosmological Power Spectra for Accelerated Bayesian Inference from Next-generation Surveys](https://arxiv.org/abs/2106.03846 "Neural emulators of CMB and matter power spectra.") | MNRAS 2022 | [Code](https://github.com/alessiospuriomancini/cosmopower) | [Journal](https://doi.org/10.1093/mnras/stac064) |
| 2021.04 | **globalemu** | [GLOBALEMU: A Novel and Robust Approach for Emulating the Sky-averaged 21-cm Signal from the Cosmic Dawn and Epoch of Reionization](https://arxiv.org/abs/2104.04336 "Neural network emulator of the global 21-cm signal.") | MNRAS 2021 | [Code](https://github.com/htjb/globalemu) | - |
| 2020.12 | **DeepSphere** | [DeepSphere: A Graph-based Spherical CNN](https://arxiv.org/abs/2012.15000 "Graph convolutions on spherical sky maps such as HEALPix.") | ICLR 2020 | [Code](https://github.com/deepsphere/deepsphere-pytorch) | - |
| 2020.11 | **Stellar Streams SBI** | [Towards Constraining Warm Dark Matter with Stellar Streams through Neural Simulation-based Inference](https://arxiv.org/abs/2011.14923 "Neural ratio estimation for dark matter constraints from stream density variations.") | arXiv 2020 | [Code](https://github.com/JoeriHermans/constraining-dark-matter-with-stellar-streams-and-ml) | - |
| 2020.11 | **Moment Networks** | [Solving High-dimensional Parameter Inference: Marginal Posterior Densities & Moment Networks](https://arxiv.org/abs/2011.05991 "Networks that estimate marginal posterior moments for high-dimensional inference.") | arXiv 2020 | [Code](https://github.com/NiallJeffrey/MomentNetworks) | - |
| 2020.11 | **ForSE** | [ForSE: A GAN-based Algorithm for Extending CMB Foreground Models to Subdegree Angular Scales](https://arxiv.org/abs/2011.02221 "GAN that adds small-scale non-Gaussian structure to Galactic dust foreground maps.") | ApJ 2021 | [Code](https://github.com/ai4cmb/ForSE) | [Journal](https://doi.org/10.3847/1538-4357/abe71c) |
| 2020.10 | **FlowPM** | [FlowPM: Distributed TensorFlow Implementation of the FastPM Cosmological N-body Solver](https://arxiv.org/abs/2010.11847 "Differentiable particle-mesh N-body simulation for gradient-based inference and hybrid ML models.") | Astron. Comput. 2021 | [Code](https://github.com/DifferentiableUniverseInitiative/flowpm) | - |
| 2020.10 | **LDL** | [Learning Effective Physical Laws for Generating Cosmological Hydrodynamics with Lagrangian Deep Learning](https://arxiv.org/abs/2010.02926 "Learned displacement layers that map dark matter simulations to baryonic fields.") | PNAS 2021 | [Code](https://github.com/biweidai/LDL) | - |
| 2020.10 | **deep21** | [deep21: A Deep Learning Method for 21cm Foreground Removal](https://arxiv.org/abs/2010.15843 "3D UNet ensemble that separates cosmological HI signal from radio foregrounds.") | JCAP 2021 | [Code](https://github.com/tlmakinen/deep21) | [Journal](https://doi.org/10.1088/1475-7516/2021/04/081) |
| 2020.06 | **Symbolic DL** | [Discovering Symbolic Models from Deep Learning with Inductive Biases](https://arxiv.org/abs/2006.11287 "Graph networks distilled into symbolic expressions, including a dark matter halo example.") | NeurIPS 2020 | [Code](https://github.com/MilesCranmer/symbolic_deep_learning) | - |
| 2019.08 | **3DcosmoGAN** | [Cosmological N-body Simulations: A Challenge for Scalable Generative Models](https://arxiv.org/abs/1908.05519 "Scalable 3D GAN for N-body density fields.") | arXiv 2019 | [Code](https://github.com/nperraud/3DcosmoGAN) | - |
| 2019 | **NNhealpix** | [Convolutional Neural Networks on the HEALPix Sphere: A Pixel-based Algorithm and Its Application to CMB Data Analysis](https://doi.org/10.1051/0004-6361/201935211 "Pixel-based convolutions on HEALPix maps applied to CMB analysis.") | A&A 2019 | [Code](https://github.com/ai4cmb/NNhealpix) | - |
| 2018 | **IMNN** | [Automatic Physical Inference with Information Maximizing Neural Networks](https://doi.org/10.1103/PhysRevD.97.083004 "Neural compression that maximises Fisher information for downstream inference.") | PRD 2018 | [Code](https://github.com/tomcharnock/IMNN) | - |
| 2017.06 | **CosmoGAN** | [Creating Virtual Universes Using Generative Adversarial Networks](https://arxiv.org/abs/1706.02390 "GAN that generates weak lensing convergence maps.") | arXiv 2017 | [Code](https://github.com/MustafaMustafa/cosmoGAN) | - |

## Simulation-Based Inference

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2024.02 | **LtU-ILI** | [LtU-ILI: An All-in-One Framework for Implicit Inference in Astrophysics and Cosmology](https://arxiv.org/abs/2402.05137 "Unified interface over sbi, pydelfi and lampe with validation and calibration tools.") | OJAp 2024 | [Code](https://github.com/maho3/ltu-ili) | [Journal](https://doi.org/10.33232/001c.120559) |
| 2023.12 | **nbi** | [nbi: The Astronomer's Package for Neural Posterior Estimation](https://arxiv.org/abs/2312.03824 "Neural posterior estimation package with featurizers for light curves and spectra.") | NeurIPS 2023 Workshop (DLIP) | [Code](https://github.com/kmzzhang/nbi) | - |
| 2023.06 | **nautilus** | [nautilus: Boosting Bayesian Importance Nested Sampling with Deep Learning](https://arxiv.org/abs/2306.16923 "Importance nested sampling with neural network emulation of the likelihood contours.") | arXiv 2023 | [Code](https://github.com/johannesulf/nautilus) | - |
| 2023.02 | **TARP** | [Sampling-Based Accuracy Testing of Posterior Estimators for General Inference](https://arxiv.org/abs/2302.03026 "Coverage test that checks generative posterior estimators using samples alone.") | ICML 2023 | [Code](https://github.com/Ciela-Institute/tarp) | - |
| 2022.11 | **GPry** | [Fast and Robust Bayesian Inference Using Gaussian Processes with GPry](https://arxiv.org/abs/2211.02045 "Active-learning Gaussian process surrogate of the posterior for expensive cosmological likelihoods.") | JCAP 2023 | [Code](https://github.com/jonaselgammal/GPry) | [Journal](https://doi.org/10.1088/1475-7516/2023/10/021) |
| 2022.07 | **pocoMC** | [Accelerating Astronomical and Cosmological Inference with Preconditioned Monte Carlo](https://arxiv.org/abs/2207.05660 "Sequential Monte Carlo sampler preconditioned with normalizing flows.") | arXiv 2022 | [Code](https://github.com/minaskar/pocomc) | - |
| 2022.05 | **margarine** | [Marginal Post Processing of Bayesian Inference Products with Normalizing Flows and Kernel Density Estimators](https://arxiv.org/abs/2205.12841 "Normalizing flows and KDEs that learn nuisance-free marginal posteriors for marginal KL divergences and emulation.") | MNRAS 2023 | [Code](https://github.com/htjb/margarine) | - |
| 2021.11 | **swyft TMNRE** | [Fast and Credible Likelihood-Free Cosmology with Truncated Marginal Neural Ratio Estimation](https://arxiv.org/abs/2111.08030 "Truncated marginal neural ratio estimation applied to CMB cosmological inference.") | arXiv 2021 | [Code](https://github.com/undark-lab/swyft) | - |
| 2021.07 | **swyft** | [Truncated Marginal Neural Ratio Estimation](https://arxiv.org/abs/2107.01214 "Simulation-efficient marginal posterior estimation with prior truncation.") | NeurIPS 2021 | [Code](https://github.com/undark-lab/swyft) | - |
| 2019.03 | **pydelfi** | [Fast Likelihood-free Cosmology with Neural Density Estimators and Active Learning](https://arxiv.org/abs/1903.00007 "Density-estimation likelihood-free inference with active simulation acquisition.") | MNRAS 2019 | [Code](https://github.com/justinalsing/pydelfi) | - |

## High-Energy Astrophysics and Astroparticle Physics

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2025.10 |  | [Multivariate Time Series Classification of Fermi-Detected Gamma-Ray Transients Using Convolutional-Recurrent Neural Networks](https://arxiv.org/abs/2510.22412 "CNN-LSTM classifiers that separate GRBs, TGFs, solar flares and SGRs in Fermi-GBM light curves and flag outliers.") | arXiv 2025 | - | - |
| 2025.09 |  | [Unsupervised Machine Learning Classification of Gamma-ray Bursts Based on the Rest-frame Prompt Emission Parameters](https://arxiv.org/abs/2509.08224 "Unsupervised clustering of GRBs into types using rest-frame prompt emission properties.") | arXiv 2025 | - | - |
| 2025.09 | **ASID** | [Towards a Foundation Model for Astrophysical Source Detection: An End-to-End Gamma-Ray Data Analysis Pipeline Using Deep Learning](https://arxiv.org/abs/2509.25128 "U-Net detection with CNN classification and deep-ensemble flux estimation on Fermi-LAT and CTAO simulations.") | arXiv 2025 | - | - |
| 2025.05 |  | [A Robust Neural Determination of the Source-count Distribution of the Fermi-LAT Sky at High Latitudes](https://arxiv.org/abs/2505.02906 "Neural ratio estimation with spherical convolutions on 14 years of high-latitude Fermi-LAT photon maps.") | arXiv 2025 | - | - |
| 2024.01 | **DeepGRB** | [Deep Learning for Gamma-Ray Bursts: A Data Driven Event Framework for X/Gamma-Ray Analysis in Space Telescopes](https://arxiv.org/abs/2401.15632 "Neural background estimation with FOCuS-Poisson trigger search on Fermi-GBM count rates.") | arXiv 2024 | - | - |
| 2022.09 | **GraphNeT IceCube** | [Graph Neural Networks for Low-Energy Event Classification & Reconstruction in IceCube](https://arxiv.org/abs/2209.03042 "Point-cloud GNN that classifies and reconstructs GeV-scale neutrino events in IceCube.") | JINST 2022 | [Code](https://github.com/graphnet-team/graphnet) | [Journal](https://doi.org/10.1088/1748-0221/17/11/P11003) |
| 2021.10 | **Fermi GCE SBI** | [A Neural Simulation-based Inference Approach for Characterizing the Galactic Center γ-ray Excess](https://arxiv.org/abs/2110.06931 "Normalizing-flow posterior estimation on spherical Fermi-LAT maps with graph neural network summaries.") | arXiv 2021 | [Code](https://github.com/smsharma/fermi-gce-flows) | - |
| 2021.07 | **GCE SCD** | [Extracting the Galactic Center Excess' Source-count Distribution with Neural Nets](https://arxiv.org/abs/2107.09070 "Neural networks that estimate source-count distributions and flux fractions of gamma-ray templates.") | PRD 2021 | [Code](https://github.com/FloList/GCE_NN) | [Journal](https://doi.org/10.1103/PhysRevD.104.123022) |
| 2020.06 | **GCE BGCNN** | [Galactic Center Excess in a New Light: Disentangling the γ-Ray Sky with Bayesian Graph Convolutional Neural Networks](https://arxiv.org/abs/2006.12504 "Bayesian graph CNNs on HEALPix maps that separate point-source and smooth contributions to the Fermi Galactic Center Excess.") | PRL 2020 | [Code](https://github.com/FloList/GCE_NN) | [Journal](https://doi.org/10.1103/PhysRevLett.125.241102) |

## Gravitational Waves

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.11 |  | [Deep-Learning-Assisted Bayesian Inference for Extreme-Mass-Ratio Inspirals](https://arxiv.org/abs/2611.11922 "Deep learning acceleration of Bayesian parameter inference for EMRI signals.") | arXiv 2026 | - | - |
| 2026.10 |  | [Scalable and Sequential Inference of the Neutron Star Equation of State with the Einstein Telescope](https://arxiv.org/abs/2610.07975 "Normalizing-flow stacking of single-event posteriors with GPU sequential Monte Carlo for EOS inference.") | arXiv 2026 | - | - |
| 2026.07 |  | [AI-enabled Gravitational-waves Searches for Binary Neutron Stars at Optimal Sensitivity](https://arxiv.org/abs/2607.01372 "Neural network BNS search with heterodyned inputs that runs in real time on a single GPU.") | arXiv 2026 | - | - |
| 2024.09 |  | [A Binary Neutron Star Merger Search Pipeline Powered by Deep Learning](https://arxiv.org/abs/2409.06266 "CNN on matched-filter SNR time series that detects BNS mergers and is robust to glitches.") | arXiv 2024 | - | - |
| 2024.08 |  | [A Machine-learning Classifier for the Postmerger Remnant of Binary Neutron Stars](https://arxiv.org/abs/2408.10678 "Gradient boosted trees trained on numerical-relativity simulations predict BNS merger outcomes from inspiral parameters.") | arXiv 2024 | - | - |
| 2024.07 | **DINGO-BNS** | [Real-time Inference for Binary Neutron Star Mergers Using Machine Learning](https://arxiv.org/abs/2407.09602 "Prior-conditioned neural posterior estimation that infers all BNS parameters in about one second, including before merger.") | Nature 2025 | [Code](https://github.com/dingo-gw/dingo) | - |
| 2024.03 | **Aframe** | [A Machine-learning Pipeline for Real-time Detection of Gravitational Waves from Compact Binary Coalescences](https://arxiv.org/abs/2403.18661 "Low-latency neural network search pipeline used in O4.") | arXiv 2024 | [Code](https://github.com/ML4GW/aframe) | - |
| 2024 | **GWAK** | [GWAK: Gravitational-Wave Anomalous Knowledge with Recurrent Autoencoders](https://doi.org/10.1088/2632-2153/ad3a31 "Semi-supervised anomaly detection for unmodeled gravitational-wave transients.") | MLST 2024 | [Code](https://github.com/ML4GW/gwak) | - |
| 2023.04 | **Peregrine** | [Peregrine: Sequential Simulation-based Inference for Gravitational Wave Signals](https://arxiv.org/abs/2304.02035 "Truncated marginal neural ratio estimation for compact binary parameter estimation.") | arXiv 2023 | [Code](https://github.com/PEREGRINE-GW/peregrine) | - |
| 2022.11 | **flowMC** | [flowMC: Normalizing Flow Enhanced Sampling Package for Probabilistic Inference in JAX](https://arxiv.org/abs/2211.06397 "MCMC with normalizing-flow global proposals, used for gravitational-wave parameter estimation.") | arXiv 2022 | [Code](https://github.com/kazewong/flowMC) | - |
| 2021.06 | **DINGO** | [Real-time Gravitational-wave Science with Neural Posterior Estimation](https://arxiv.org/abs/2106.12594 "Normalizing-flow posteriors for binary black hole events with inference times of about a minute.") | PRL 2021 | [Code](https://github.com/dingo-gw/dingo) | [Journal](https://doi.org/10.1103/PhysRevLett.127.241103) |
| 2021.02 | **nessai** | [Nested Sampling with Normalizing Flows for Gravitational-wave Inference](https://arxiv.org/abs/2102.11056 "Nested sampler that uses normalizing flows to propose new live points.") | PRD 2021 | [Code](https://github.com/mj-will/nessai) | [Importance Nested Sampling](https://arxiv.org/abs/2302.08526) |
| 2020.05 | **DeepClean** | [Noise Reduction in Gravitational-wave Data via Deep Learning](https://arxiv.org/abs/2005.06534 "Neural network for low-frequency noise subtraction in gravitational-wave detectors.") | arXiv 2020 | [Code](https://github.com/ML4GW/DeepClean) | - |
| 2019.09 | **VItamin** | [Bayesian Parameter Estimation Using Conditional Variational Autoencoders for Gravitational-wave Astronomy](https://arxiv.org/abs/1909.06296 "Conditional VAE for rapid compact binary parameter estimation.") | Nature Physics 2022 | [Code](https://github.com/hagabbar/vitamin_c) | - |
| 2019.04 | **Magic Bullet** | [Convolutional Neural Networks: A Magic Bullet for Gravitational-wave Detection?](https://arxiv.org/abs/1904.08693 "Critical evaluation of CNN-based gravitational-wave detection.") | PRD 2019 | [Code](https://github.com/timothygebhard/magic-bullet) | - |

## Solar Physics and Heliophysics

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.04 |  | [Predicting Associations between Solar Flares and Coronal Mass Ejections Using SDO/HMI Magnetograms and a Hybrid Neural Network](https://arxiv.org/abs/2604.10016 "ViT and LSTM hybrid that predicts whether upcoming flares will be eruptive or confined.") | arXiv 2026 | - | - |
| 2026.02 |  | [Prediction of Major Solar Flares Using Interpretable Class-dependent Reward Framework with Active Region Magnetograms and Domain Knowledge](https://arxiv.org/abs/2602.16264 "CNN, CNN-BiLSTM and transformer models with class-dependent rewards for imbalanced M-class flare prediction.") | arXiv 2026 | - | - |
| 2025.11 | **JW-Flare** | [JW-Flare: Accurate Solar Flare Forecasting Method Based on Multimodal Large Language Models](https://arxiv.org/abs/2511.08970 "Multimodal LLM fine-tuned with LoRA on magnetograms and textual magnetic parameters for 24-hour flare forecasts.") | arXiv 2025 | - | - |
| 2025.10 |  | [Solar Flare Forecasting with Foundational Transformer Models across Image, Video, and Time-series Modalities](https://arxiv.org/abs/2510.23400 "Compares SigLIP2, VideoMAE and Moirai2 on SDO/HMI magnetograms and GOES X-ray fluxes.") | arXiv 2025 | - | - |
| 2025.08 | **Surya** | [Surya: Foundation Model for Heliophysics](https://arxiv.org/abs/2508.14112 "366M-parameter spatiotemporal model trained on eight AIA channels and five HMI products at native resolution.") | arXiv 2025 | [Code](https://github.com/NASA-IMPACT/Surya) | - |
| 2023 | **NF2** | [Probing the Solar Coronal Magnetic Field with Physics-informed Neural Networks](https://doi.org/10.1038/s41550-023-02030-9 "Physics-informed neural network extrapolation of force-free coronal magnetic fields from photospheric magnetograms.") | Nature Astronomy 2023 | [Code](https://github.com/RobertJaro/NF2) | [Multi-height](https://doi.org/10.3847/2041-8213/ad2450) |
| 2020.06 | **Unsupervised MFBD** | [Learning to Do Multiframe Blind Deconvolution Unsupervisedly](https://arxiv.org/abs/2006.01438 "Unsupervised neural multiframe blind deconvolution of solar observations.") | A&A 2021 | [Code](https://github.com/aasensio/unsupervisedMFBD) | - |
| 2019.05 | **Slic** | [Fast Solar Image Classification Using Deep Learning and Its Importance for Automation in Solar Physics](https://arxiv.org/abs/1905.13575 "CNN classification of solar features in H-alpha images.") | Solar Physics 2019 | [Code](https://github.com/rhero12/Slic) | - |
| 2019.04 | **SICON** | [Stokes Inversion Based on Convolutional Neural Networks](https://arxiv.org/abs/1904.03714 "Fully convolutional networks that invert Hinode Stokes maps into 3D thermodynamic and magnetic cubes.") | A&A 2019 | [Code](https://github.com/aasensio/sicon) | - |
| 2019.03 | **SDOML** | [A Machine-learning Data Set Prepared from the NASA Solar Dynamics Observatory Mission](https://arxiv.org/abs/1903.04538 "Curated 6.5 TB AIA, HMI and EVE dataset with baselines for EUV irradiance forecasting and instrument translation.") | ApJS 2019 | [Code](https://github.com/fluxtransport/SDOML) | [Journal](https://doi.org/10.3847/1538-4365/ab1005) |
| 2017.06 | **Enhance** | [Enhancing SDO/HMI Images Using Deep Learning](https://arxiv.org/abs/1706.02933 "Deconvolution and super-resolution of HMI continuum images and magnetograms.") | A&A 2018 | [Code](https://github.com/cdiazbas/enhance) | - |
| 2017.03 | **DeepVel** | [DeepVel: Deep Learning for the Estimation of Horizontal Velocities at the Solar Surface](https://arxiv.org/abs/1703.05128 "End-to-end network that estimates horizontal velocity fields from pairs of granulation images.") | A&A 2017 | [Code](https://github.com/aasensio/deepvel) | - |

## Radio Astronomy

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.08 | **YOLO-Chars** | [Radio Galaxies Detection and Characterization Using Deep Learning Techniques](https://arxiv.org/abs/2608.21474 "Two-stage YOLO detection and characterisation network for flux, size and position angle on SKA SDC1 images.") | MNRAS 2026 | - | - |
| 2025.09 | **YOLO-CIANNA** | [YOLO-CIANNA: Galaxy Detection with Deep Learning in Radio Data](https://arxiv.org/abs/2509.12082 "3D CNN detector for HI sources in SKA SDC2 hyperspectral cubes, extending the method that won SDC2.") | arXiv 2025 | - | - |
| 2025.06 |  | [Simulating Realistic Radio Continuum Survey Maps with Diffusion Models](https://arxiv.org/abs/2506.11715 "Diffusion-generated radio galaxies assembled into sky models and imaged to mimic LoTSS pointings.") | arXiv 2025 | - | - |
| 2025.03 |  | [Classification of Radio Sources Through Self-Supervised Learning](https://arxiv.org/abs/2503.19111 "Self-supervised pretraining and deep clustering that classify LoTSS-DR2 radio galaxies into 12 morphology classes.") | arXiv 2025 | - | - |
| 2024.10 |  | [Simulating Images of Radio Galaxies with Diffusion Models](https://arxiv.org/abs/2410.07794 "Continuous-time diffusion model that generates radio galaxy images with control over flux and morphology.") | arXiv 2024 | - | - |
| 2024.03 | **R2D2** | [The R2D2 Deep Neural Network Series Paradigm for Fast Precision Imaging in Radio Astronomy](https://arxiv.org/abs/2403.05452 "Series of residual networks for radio interferometric imaging.") | ApJS 2024 | [Code](https://github.com/basp-group/R2D2-RI) | [Journal](https://doi.org/10.3847/1538-4365/ad46f5) |
| 2023.12 | **AIRI** | [Plug-and-play Imaging with Model Uncertainty Quantification in Radio Astronomy](https://arxiv.org/abs/2312.07137 "Learned denoisers in proximal algorithms for radio-interferometric imaging with uncertainty quantification.") | arXiv 2023 | [Code](https://github.com/basp-group/AIRI) | - |
| 2023.05 | **Radio Galaxy Zoo FM** | [Radio Galaxy Zoo: Building a Multipurpose Foundation Model for Radio Astronomy with Self-supervised Learning](https://arxiv.org/abs/2305.16127 "BYOL pretraining on unlabelled radio galaxy images for downstream classification.") | arXiv 2023 | [Code](https://github.com/inigoval/byol) | - |
| 2022 | **radionets** | [Deep Learning-based Imaging in Radio Interferometry](https://doi.org/10.1051/0004-6361/202142113 "Neural networks that reconstruct radio images from incomplete visibility data.") | A&A 2022 | [Code](https://github.com/radionets-project/radionets) | - |
| 2021.11 | **POLISH** | [Deep Radio-interferometric Imaging with POLISH: DSA-2000 and Weak Lensing](https://arxiv.org/abs/2111.03249 "Super-resolution network for radio interferometric image reconstruction.") | MNRAS 2022 | [Code](https://github.com/liamconnor/polish-pub) | - |
| 2020.12 | **Attention Gating** | [Attention-gating for Improved Radio Galaxy Classification](https://arxiv.org/abs/2012.01248 "Attention-gated CNNs for FRI and FRII radio galaxy classification.") | MNRAS 2021 | [Code](https://github.com/mb010/AstroAttention) | - |
| 2020.10 | **Pulsar SGAN** | [Pulsar Candidate Identification Using Semi-supervised Generative Adversarial Networks](https://arxiv.org/abs/2010.07457 "Semi-supervised GAN classifier for pulsar candidates with few labelled examples.") | MNRAS 2021 | [Code](https://github.com/vishnubk/sgan) | [Journal](https://doi.org/10.1093/mnras/stab1308) |
| 2019.02 | **FETCH** | [FETCH: A Deep-learning Based Classifier for Fast Transient Classification](https://arxiv.org/abs/1902.06343 "CNN classifier for fast radio burst and single-pulse candidates.") | MNRAS 2020 | [Code](https://github.com/devanshkv/fetch) | - |
| 2019 | **ClaRAN** | [Radio Galaxy Zoo: ClaRAN, a Deep Learning Classifier for Radio Morphologies](https://doi.org/10.1093/mnras/sty2646 "Faster R-CNN detection and classification of radio source morphologies.") | MNRAS 2019 | [Code](https://github.com/chenwuperth/rgz_rcnn) | - |

## Planetary Science and Small Bodies

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2026.06 |  | [Deep Learning-Based Lunar Crater Terrain Relative Navigation](https://arxiv.org/abs/2606.14776 "U-Net++ crater detector coupled with an extended Kalman filter for lunar landing navigation.") | arXiv 2026 | - | - |
| 2026.03 | **LLaVA-LE** | [LLaVA-LE: Large Language-and-Vision Assistant for Lunar Exploration](https://arxiv.org/abs/2603.24696 "LLaVA adapted to lunar remote sensing with LUCID, 96k panchromatic images paired with scientific captions and question-answer pairs.") | arXiv 2026 | - | - |
| 2026.01 |  | [Vision-Language Model for Accurate Crater Detection](https://arxiv.org/abs/2601.07795 "OWLv2 vision transformer fine-tuned on LRO images for lunar crater detection.") | arXiv 2026 | - | - |
| 2026 | **Lunar-Bench** | [Lunar-Bench: Towards Evaluating Task-Oriented Reasoning of LLMs in Lunar Exploration Scenarios](https://aclanthology.org/2026.findings-acl.83/ "3,000 tasks derived from lunar mission procedures with Environmental Scenario Indicators for safety, efficiency, integrity and alignment; the best of 36 models reaches 47.8% against 65.1% for human experts.") | ACL Findings 2026 | - | - |
| 2026 | **Lunar-R1** | [Lunar-R1: Efficient Reasoning of Large Language Models for Lunar Exploration via Reinforcement Learning](https://aclanthology.org/2026.emnlp-industry.5/ "8B reasoning model trained by continued pretraining, SFT and RL, with Latent Difficulty Perception that cuts chain-of-thought tokens by 38.9%, the Lunar-QA benchmark and RK3588 NPU deployment.") | EMNLP 2026 Industry | - | - |
| 2025.08 |  | [Deep Learning Framework for Crater Detection and Identification on the Moon and Mars](https://arxiv.org/abs/2508.03920 "Two-stage YOLO detection and CNN or ResNet-50 size classification of craters with an annotated dataset.") | arXiv 2025 | [Code](https://github.com/sydney-machine-learning/crater-identification) | - |
| 2025 | **Lunar Twins** | [Lunar Twins: We Choose to Go to the Moon with Large Language Models](https://aclanthology.org/2025.findings-acl.69/ "Earth-Moon collaborative Chang'e large model with Yutu-Text and Yutu-VL small models, the Lunar_GenData multi-agent instruction workflow built on Chang'e mission data, and the Lunar_Eval suite.") | ACL Findings 2025 | - | - |
| 2023.04 |  | [Deep Learning Universal Crater Detection Using Segment Anything Model (SAM)](https://arxiv.org/abs/2304.07764 "Zero-shot crater segmentation with SAM on lunar and Martian images and DEMs.") | arXiv 2023 | - | - |
| 2022.08 | **AstroVision** | [AstroVision: Towards Autonomous Feature Detection and Description for Missions to Small Bodies Using Deep Learning](https://arxiv.org/abs/2208.02053 "115,970 annotated real images of 16 small bodies for keypoint detection and description benchmarks.") | Acta Astronaut. 2023 | - | [Data](https://huggingface.co/datasets/travisdriver/astrovision-data) [Journal](https://doi.org/10.1016/j.actaastro.2023.01.009) |
| 2018.03 | **DeepMoon** | [Lunar Crater Identification via Deep Learning](https://arxiv.org/abs/1803.02192 "CNN crater detection on lunar digital elevation maps, transferred to Mercury.") | Icarus 2019 | [Code](https://github.com/silburt/DeepMoon) | [Data](https://doi.org/10.5281/zenodo.1133969) |

## Datasets

### Observational Datasets

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2024.12 | **Multimodal Universe** | [The Multimodal Universe: Enabling Large-Scale Machine Learning with 100 TB of Astronomical Scientific Data](https://arxiv.org/abs/2412.02527 "Images, spectra, time series and catalogs for hundreds of millions of objects, distributed as Hugging Face datasets with benchmark tasks.") | NeurIPS 2024 (Datasets and Benchmarks) | [Code](https://github.com/MultimodalUniverse/MultimodalUniverse) | - |
| 2021 | **Galaxy10 DECaLS** | [Galaxy10 DECaLS](https://github.com/henrysky/Galaxy10 "17,736 DECaLS g, r, z galaxy images in 10 morphology classes with Galaxy Zoo labels.") | Dataset 2021 | [Code](https://github.com/henrysky/Galaxy10) | [Data](https://doi.org/10.5281/zenodo.10845026) |
| 2018.10 | **PLAsTiCC** | [The Photometric LSST Astronomical Time-series Classification Challenge (PLAsTiCC): Data Set](https://arxiv.org/abs/1810.00001 "Simulated LSST multi-band light curves for transient and variable classification.") | arXiv 2018 | - | [Kaggle](https://www.kaggle.com/c/PLAsTiCC-2018) |

### Simulation Datasets

| Date | Name | Title | Venue | Code | Links |
|:--|:--|:--|:--|:--|:--|
| 2024.12 | **The Well** | [The Well: A Large-Scale Collection of Diverse Physics Simulations for Machine Learning](https://arxiv.org/abs/2412.00568 "15 TB across 16 physics simulation datasets, including MHD and supernova explosion simulations.") | NeurIPS 2024 (Datasets and Benchmarks) | [Code](https://github.com/PolymathicAI/the_well) | - |
| 2020.10 | **CAMELS** | [The CAMELS Project: Cosmology and Astrophysics with MachinE Learning Simulations](https://arxiv.org/abs/2010.00619 "4,233 cosmological simulations varying cosmological and feedback parameters, designed for training ML models.") | ApJ 2021 | [Code](https://github.com/franciscovillaescusa/CAMELS) | [Project](https://www.camel-simulations.org) |
| 2019.09 | **Quijote** | [The Quijote Simulations](https://arxiv.org/abs/1909.05273 "44,100 N-body simulations spanning more than 7,000 cosmological models, designed for information quantification and ML training.") | ApJS 2020 | - | [Journal](https://doi.org/10.3847/1538-4365/ab9d82) |

## Tools and Libraries

| Name | Description |
|:--|:--|
| [AspGap](https://github.com/jiadonglee/aspgap) | infers red giant stellar parameters and abundances from Gaia XP spectra. |
| [astroML](https://github.com/astroML/astroML) | provides machine learning and statistics routines for astronomy. |
| [astrorapid](https://github.com/daniel-muthukrishna/astrorapid) | classifies transients in real time with recurrent neural networks. |
| [avocado](https://github.com/kboone/avocado) | classifies photometric transients with Gaussian process augmentation and boosted trees. |
| [BLISS](https://github.com/prob-ml/bliss) | performs Bayesian light source separation with amortized variational inference. |
| [ctlearn](https://github.com/ctlearn-project/ctlearn) | trains deep learning models for imaging atmospheric Cherenkov telescope event reconstruction. |
| [D3M](https://github.com/siyucosmo/ML-Recon) | emulates N-body displacement fields with deep learning. |
| [DASH](https://github.com/daniel-muthukrishna/astrodash) | classifies supernova spectra with deep learning. |
| [Deep-HiTS](https://github.com/guille-c/Deep-HiTS) | classifies HiTS transient candidates with convolutional neural networks. |
| [deep-potential](https://github.com/gregreen/deep-potential) | recovers gravitational potentials from phase-space snapshots with normalizing flows. |
| [DeepBench](https://github.com/deepskies/DeepBench) | generates simple physics and astronomy benchmark datasets for machine learning. |
| [DeepDISC](https://github.com/grantmerz/deepdisc) | applies Detectron2 instance segmentation to astronomical source detection. |
| [DeepMerge](https://github.com/deepskies/deepmerge-public) | classifies high-redshift merging galaxies with CNNs. |
| [DeepSource](https://github.com/vafaei-ar/deepsource) | detects point sources in radio images with deep learning. |
| [E2CNNRadGal](https://github.com/as595/E2CNNRadGal) | classifies radio galaxies with group-equivariant CNNs. |
| [fink-science](https://github.com/astrolabsoftware/fink-science) | hosts the science modules and classifiers run on the Fink alert stream. |
| [Fink](https://github.com/astrolabsoftware/fink-broker) | is an LSST alert broker with machine learning classification modules. |
| [FLEET](https://github.com/gmzsebastian/FLEET) | selects superluminous supernova and tidal disruption event candidates for follow-up. |
| [FlexCode](https://github.com/tpospisi/FlexCode) | estimates conditional densities for photometric redshifts. |
| [Galaxy Zoo Bayesian CNN](https://github.com/mwalmsley/galaxy-zoo-bayesian-cnn) | trains Bayesian CNNs with active learning on Galaxy Zoo labels. |
| [galaxy-datasets](https://github.com/mwalmsley/galaxy-datasets) | loads Galaxy Zoo datasets for PyTorch training. |
| [GalaxyGAN](https://github.com/SpaceML/GalaxyGAN_python) | recovers features from degraded galaxy images with GANs. |
| [GPz](https://github.com/OxfordML/GPz) | estimates photometric redshifts with sparse Gaussian processes. |
| [Gravity Spy](https://github.com/Gravity-Spy/GravitySpy) | classifies LIGO detector glitches with citizen science and machine learning. |
| [herculens](https://github.com/Herculens/herculens) | performs differentiable strong lens modeling in JAX. |
| [InstrumentToInstrument](https://github.com/RobertJaro/InstrumentToInstrument) | translates solar observations between instruments. |
| [IrregularTimeSeriesAutoencoder](https://github.com/bnaul/IrregularTimeSeriesAutoencoderPaper) | learns recurrent autoencoder features from irregularly sampled light curves. |
| [jax-cosmo](https://github.com/DifferentiableUniverseInitiative/jax_cosmo) | provides differentiable cosmology computations in JAX. |
| [jax-lensing](https://github.com/CosmoStat/jax-lensing) | implements probabilistic mass mapping with neural score estimation ([paper](https://arxiv.org/abs/2011.08271)). |
| [JaxPM](https://github.com/DifferentiableUniverseInitiative/JaxPM) | implements a differentiable particle-mesh N-body solver in JAX. |
| [jim](https://github.com/kazewong/jim) | performs gravitational-wave parameter estimation in JAX with flow-enhanced sampling. |
| [lampe](https://github.com/probabilists/lampe) | implements neural ratio and posterior estimation for likelihood-free inference in PyTorch. |
| [lc\_classifier](https://github.com/alercebroker/lc_classifier) | classifies light curves in the ALeRCE broker. |
| [LIA](https://github.com/dgodinez77/LIA) | classifies microlensing events with random forests. |
| [light-curve](https://github.com/light-curve/light-curve-python) | extracts light-curve features for transient and variable classification. |
| [magnify](https://github.com/jiwoncpark/magnify) | models AGN light curves with Gaussian process and neural network tools. |
| [map2map](https://github.com/eelregit/map2map) | trains field-to-field neural networks on cosmological simulations. |
| [MCCD](https://github.com/CosmoStat/mccd) | models the PSF across multiple CCDs with data-driven methods. |
| [ml4gw](https://github.com/ML4GW/ml4gw) | provides PyTorch utilities for gravitational-wave machine learning. |
| [ML\_GBT\_SETI](https://github.com/PetchMa/ML_GBT_SETI) | searches Green Bank Telescope data for technosignatures with machine learning. |
| [MLZ](https://github.com/mgckind/MLZ) | estimates photometric redshifts with TPZ random forests. |
| [Morpheus](https://github.com/morpheus-project/morpheus) | performs pixel-level morphological classification of astronomical images. |
| [MuyGPyS](https://github.com/LLNL/MuyGPyS) | provides scalable Gaussian process estimation used for star-galaxy separation. |
| [ParSNIP](https://github.com/kboone/parsnip) | builds generative models of transient light curves with physics-enabled deep learning. |
| [PICS](https://github.com/zhuww/ubc_AI) | classifies pulsar candidates with image pattern recognition. |
| [pmwd](https://github.com/eelregit/pmwd) | implements differentiable particle-mesh N-body simulation in JAX. |
| [PySR](https://github.com/MilesCranmer/PySR) | performs symbolic regression for interpretable scientific models ([paper](https://arxiv.org/abs/2305.01582)). |
| [QuasarNET](https://github.com/ngbusca/QuasarNET) | classifies quasar spectra and estimates redshifts with a convolutional network. |
| [ramjet](https://github.com/golmschenk/ramjet) | detects transits and microlensing events in light curves with neural networks. |
| [RESSPECT](https://github.com/COINtoolbox/RESSPECT) | applies active learning to supernova spectroscopic follow-up. |
| [sbi](https://github.com/sbi-dev/sbi) | implements neural posterior, likelihood and ratio estimation ([JOSS](https://doi.org/10.21105/joss.02505)). |
| [ShapeDeconv](https://github.com/CosmoStat/ShapeDeconv) | deconvolves galaxy images with deep learning for shape measurement. |
| [SimBIG](https://github.com/changhoonhahn/simbig) | performs simulation-based inference of galaxy clustering. |
| [single\_pulse\_ml](https://github.com/liamconnor/single_pulse_ml) | classifies single-pulse and fast radio burst candidates with deep learning. |
| [star-galaxy CNN](https://github.com/EdwardJKim/dl4astro) | separates stars and galaxies with CNNs. |
| [StarNet](https://github.com/astroai/starnet) | infers stellar parameters from spectra with CNNs. |
| [sunbird](https://github.com/florpi/sunbird) | emulates galaxy clustering summary statistics with neural networks. |
| [Superphot+](https://github.com/VTDA-Group/superphot-plus) | fits and classifies supernova light curves. |
| [Superphot](https://github.com/griffin-h/superphot) | classifies supernovae from photometric light curves. |
| [SuperRAENN](https://github.com/villrv/SuperRAENN) | classifies supernova light curves with recurrent autoencoder features. |
| [The Cannon](https://github.com/andycasey/AnniesLasso) | provides a data-driven model for stellar labels from spectra. |
| [The Payne](https://github.com/tingyuansen/The_Payne) | fits stellar spectra with neural network spectral emulators. |
| [transomaly](https://github.com/daniel-muthukrishna/transomaly) | detects anomalous transients in real time. |
| [xVal](https://github.com/PolymathicAI/xVal) | encodes real numbers as continuous embeddings for language models on scientific data. |

## Communities and Groups

| Name | Description |
|:--|:--|
| [Polymathic AI](https://polymathic-ai.org) | develops AstroCLIP, AION-1, MPP, the Multimodal Universe and The Well. |
| [UniverseTBD](https://universetbd.org) | develops AstroLLaMA, AstroPT and AstroLLaVA. |
| [AstroMLab](https://huggingface.co/AstroMLab) | develops the AstroMLab benchmark and the AstroSage models. |
| [ML4GW](https://github.com/ML4GW) | develops machine learning pipelines for gravitational-wave astronomy. |

## Related Awesome Lists

| Name | Description |
|:--|:--|
| [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy) | covers general resources for professional astronomers. |
| [awesome-astro-datascience](https://github.com/mpi-astronomy/awesome-astro-datascience) | covers astronomical data science resources. |
| [awesome-astrodata](https://github.com/gully/awesome-astrodata) | covers data and tools for machine learning in astronomy. |
| [taotie](https://github.com/dr-guangtou/taotie) | covers resources for astrophysical research. |
| [awesome-space](https://github.com/orbitalindex/awesome-space) | covers space-related packages and resources. |
| [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) | covers scientific language models across domains. |

## Contributing

Pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
