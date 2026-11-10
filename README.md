# Awesome AI for Astronomy

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/Xin-YuXiao/Awesome-AI-for-Astronomy)

A curated list of foundation models, language models, agents, benchmarks, datasets and tools for artificial intelligence in astronomy and astrophysics.

Existing lists such as [awesome-astronomy](https://github.com/jonathansick/awesome-astronomy) cover general astronomy resources, and [awesome-astro-datascience](https://github.com/mpi-astronomy/awesome-astro-datascience) covers classical astronomical data science. This list focuses on work since 2021 on pretrained models for astronomical observations, language models and agents for astronomical research, and the benchmarks and ML-ready datasets used to evaluate them.

**Notes**

1. Entries are sorted chronologically within each subsection. The date follows the first arXiv version when one exists, otherwise the journal or proceedings version.
2. The venue tag shows the peer-reviewed venue when one is confirmed. Otherwise it shows `arXiv` and the year.
3. An entry is included when it has a public paper and at least one public artifact (code, weights, data or a hosted service). Every link in this list is checked before merging.
4. Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry template.

## Contents

- [Surveys and Reviews](#surveys-and-reviews)
- [Foundation Models for Observations](#foundation-models-for-observations)
  - [Images](#images)
  - [Spectra](#spectra)
  - [Time Series](#time-series)
  - [Multimodal](#multimodal)
- [Language and Vision-Language Models](#language-and-vision-language-models)
- [Agents and Retrieval Systems](#agents-and-retrieval-systems)
- [Benchmarks](#benchmarks)
- [Datasets](#datasets)
  - [Observational Datasets](#observational-datasets)
  - [Simulation Datasets](#simulation-datasets)
- [Tools and Libraries](#tools-and-libraries)
- [Communities and Groups](#communities-and-groups)
- [Related Awesome Lists](#related-awesome-lists)

## Surveys and Reviews

- *The Dawes Review 10: The Impact of Deep Learning for the Analysis of Galaxy Surveys* `PASA 2023`  
  [[Paper](https://arxiv.org/abs/2210.01813)] [[Journal](https://doi.org/10.1017/pasa.2022.55)]  
  Review of deep learning applications to galaxy surveys covering classification, property estimation, discovery and cosmological inference.

- *Astronomia ex machina: A History, Primer and Outlook on Neural Networks in Astronomy* `R. Soc. Open Sci. 2023`  
  [[Paper](https://arxiv.org/abs/2211.03796)] [[Journal](https://doi.org/10.1098/rsos.221454)]  
  Historical review of neural networks in astronomy with a primer on deep learning and an outlook on astronomical foundation models.

## Foundation Models for Observations

### Images

- **(Zoobot)** *Zoobot: Adaptable Deep Learning Models for Galaxy Morphology* `JOSS 2023`  
  [[GitHub](https://github.com/mwalmsley/zoobot)] [[PyPI](https://pypi.org/project/zoobot/)]  
  Pretrained galaxy morphology encoders trained on Galaxy Zoo volunteer labels, designed for finetuning on new tasks.

- **(Galaxy Scaling Laws)** *Scaling Laws for Galaxy Images* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2404.02973)]  
  Supervised scaling study on 840k galaxy images with over 100M Galaxy Zoo annotations.

- **(AstroPT)** *AstroPT: Scaling Large Observation Models for Astronomy* `ICML 2024 Workshop (AI4Science)`  
  [[Paper](https://arxiv.org/abs/2405.14930)] [[GitHub](https://github.com/Smith42/astroPT)] [[Model](https://huggingface.co/Smith42/astroPT_v2.0)]  
  Autoregressive transformers from 1M to 2.1B parameters pretrained on 8.6M DESI Legacy Survey galaxy images.

### Spectra

- **(SpectraFM)** *SpectraFM: Tuning into Stellar Foundation Models* `NeurIPS 2024 Workshop (FM4Science)`  
  [[Paper](https://arxiv.org/abs/2411.04750)]  
  Transformer pretrained on synthetic stellar spectra and transferred to real spectra across wavelength ranges.

### Time Series

- **(ASTROMER)** *ASTROMER: A Transformer-Based Embedding for the Representation of Light Curves* `A&A 2023`  
  [[Paper](https://arxiv.org/abs/2205.01677)] [[GitHub](https://github.com/astromer-science)] [[Journal](https://doi.org/10.1051/0004-6361/202243928)]  
  Self-supervised light-curve encoder pretrained with masked magnitude prediction on MACHO R-band data.

- **(Maven)** *Maven: A Multimodal Foundation Model for Supernova Science* `MLST 2024`  
  [[Paper](https://arxiv.org/abs/2408.16829)]  
  Contrastive alignment of supernova photometry and spectroscopy, pretrained on 0.5M synthetic events and finetuned on ZTF.

### Multimodal

- **(AstroCLIP)** *AstroCLIP: A Cross-Modal Foundation Model for Galaxies* `MNRAS 2024`  
  [[Paper](https://arxiv.org/abs/2310.03024)] [[GitHub](https://github.com/PolymathicAI/AstroCLIP)] [[Journal](https://doi.org/10.1093/mnras/stae1450)]  
  Contrastive alignment of DESI galaxy images and spectra in a shared embedding space.

- **(PAPERCLIP)** *PAPERCLIP: Associating Astronomical Observations and Natural Language with Multi-Modal Models* `COLM 2024`  
  [[Paper](https://arxiv.org/abs/2403.08851)]  
  CLIP finetuned on Hubble Space Telescope observations paired with observing proposal abstracts.

- **(AstroM3)** *AstroM3: A Self-Supervised Multimodal Model for Astronomy* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2411.08842)]  
  Trimodal CLIP-style pretraining on variable-star light curves, spectra and metadata.

- **(AION-1)** *AION-1: Omnimodal Foundation Model for Astronomical Sciences* `NeurIPS 2025`  
  [[Paper](https://arxiv.org/abs/2510.17960)] [[GitHub](https://github.com/PolymathicAI/AION)] [[Model](https://huggingface.co/polymathic-ai/aion-base)]  
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

- **(AstroLLaMA-2-70B)** *AstroMLab 2: AstroLLaMA-2-70B Model and Benchmarking Specialised LLMs for Astronomy* `SC 2024 Workshop (AI4S)`  
  [[Paper](https://arxiv.org/abs/2409.19750)] [[Model](https://huggingface.co/AstroMLab)]  
  Releases AstroLLaMA-3-8B and AstroLLaMA-2-70B and reports that the 7B AstroLLaMA series underperforms its base model.

- **(AstroSage-8B)** *AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a Specialized 8B-Parameter Large Language Model* `Sci. Rep. 2025`  
  [[Paper](https://arxiv.org/abs/2411.09012)] [[Model](https://huggingface.co/AstroMLab/AstroSage-8B)] [[Journal](https://doi.org/10.1038/s41598-025-97131-y)]  
  Llama-3.1-8B with continued pretraining on about 250k astro-ph and gr-qc preprints, SFT and model merging. Scores 80.9% on AstroMLab 1.

- **(AstroLLaVA)** *AstroLLaVA: Towards the Unification of Astronomical Data and Natural Language* `ICLR 2025 Workshop (SCI-FM)`  
  [[Paper](https://arxiv.org/abs/2504.08583)]  
  LLaVA finetuned on about 30k captioned images from APOD, ESO and Hubble for astronomical visual question answering.

## Agents and Retrieval Systems

- **(pathfinder)** *pathfinder: A Semantic Framework for Literature Review and Knowledge Discovery in Astronomy* `ApJS 2024`  
  [[Paper](https://arxiv.org/abs/2408.01556)] [[Demo](https://pfdr.app)]  
  Retrieval-augmented literature search and synthesis over about 350k ADS papers with time and citation weighting.

- **(Mephisto)** *Mephisto: Self-Improving Large Language Model-Based Agents for Automated Interpretation of Multi-band Galaxy Observations* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.08354)] [[Short Paper](https://arxiv.org/abs/2409.14807)] [[Code](https://zenodo.org/records/15589045)]  
  Multi-agent tree search over CIGALE SED models with a self-updating knowledge base, applied to JWST Little Red Dots.

- **(cmbagent)** *Multi-Agent System for Cosmological Parameter Analysis* `arXiv 2024`  
  [[Paper](https://arxiv.org/abs/2412.00431)] [[Follow-up](https://arxiv.org/abs/2507.07257)] [[GitHub](https://github.com/CMBAgents/cmbagent)]  
  Planning and control system of about 30 LLM agents for autonomous cosmological data analysis.

- **(StarWhisper Telescope)** *StarWhisper Telescope: An AI Framework for Automating End-to-End Astronomical Observations* `Commun. Eng. 2025`  
  [[Paper](https://arxiv.org/abs/2412.06412)] [[Journal](https://doi.org/10.1038/s44172-025-00520-4)]  
  LLM agent that plans observations, controls a 10-telescope network and runs transient detection for the Nearby Galaxy Supernovae Survey.

- **(Denario)** *The Denario Project: Deep Knowledge AI Agents for Scientific Discovery* `arXiv 2025`  
  [[Paper](https://arxiv.org/abs/2510.26887)] [[GitHub](https://github.com/AstroPilot-AI/Denario)] [[Demo](https://huggingface.co/spaces/astropilot-ai/Denario)]  
  Modular multi-agent research assistant for idea generation, analysis and paper drafting, using cmbagent as its analysis backend.

## Benchmarks

- **(AstroMLab 1)** *AstroMLab 1: Who Wins Astronomy Jeopardy!?* `Astron. Comput. 2025`  
  [[Paper](https://arxiv.org/abs/2407.11194)]  
  4,425 multiple-choice questions curated from the Annual Review of Astronomy and Astrophysics for evaluating LLM knowledge recall.

- **(AstroVisBench)** *AstroVisBench: A Code Benchmark for Scientific Computing and Visualization in Astronomy* `NeurIPS 2025 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2505.20538)] [[Project](https://astrovisbench.github.io)]  
  864 processing and visualization tasks from 110 NOIRLab and STScI notebooks, scored by execution and a VLM judge.

## Datasets

### Observational Datasets

- **(PLAsTiCC)** *The Photometric LSST Astronomical Time-series Classification Challenge (PLAsTiCC): Data Set* `arXiv 2018`  
  [[Paper](https://arxiv.org/abs/1810.00001)] [[Kaggle](https://www.kaggle.com/c/PLAsTiCC-2018)]  
  Simulated LSST multi-band light curves for transient and variable classification.

- **(Galaxy10 DECaLS)** *Galaxy10 DECaLS* `Dataset 2021`  
  [[GitHub](https://github.com/henrysky/Galaxy10)] [[Zenodo](https://doi.org/10.5281/zenodo.10845026)]  
  17,736 DECaLS g, r, z galaxy images in 10 morphology classes with Galaxy Zoo labels.

- **(Multimodal Universe)** *The Multimodal Universe: Enabling Large-Scale Machine Learning with 100 TB of Astronomical Scientific Data* `NeurIPS 2024 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2412.02527)] [[GitHub](https://github.com/MultimodalUniverse/MultimodalUniverse)]  
  Images, spectra, time series and catalogs for hundreds of millions of objects, distributed as Hugging Face datasets with benchmark tasks.

### Simulation Datasets

- **(CAMELS)** *The CAMELS Project: Cosmology and Astrophysics with MachinE Learning Simulations* `ApJ 2021`  
  [[Paper](https://arxiv.org/abs/2010.00619)] [[Project](https://www.camel-simulations.org)]  
  4,233 cosmological simulations varying cosmological and feedback parameters, designed for training ML models.

- **(The Well)** *The Well: A Large-Scale Collection of Diverse Physics Simulations for Machine Learning* `NeurIPS 2024 (Datasets and Benchmarks)`  
  [[Paper](https://arxiv.org/abs/2412.00568)] [[GitHub](https://github.com/PolymathicAI/the_well)]  
  15 TB across 16 physics simulation datasets, including MHD and supernova explosion simulations.

## Tools and Libraries

- **(sbi)** *sbi: A Toolkit for Simulation-Based Inference* `JOSS 2020`  
  [[GitHub](https://github.com/sbi-dev/sbi)] [[Journal](https://doi.org/10.21105/joss.02505)]  
  PyTorch package for neural posterior, likelihood and ratio estimation.

- **(LtU-ILI)** *LtU-ILI: An All-in-One Framework for Implicit Inference in Astrophysics and Cosmology* `OJAp 2024`  
  [[Paper](https://arxiv.org/abs/2402.05137)] [[GitHub](https://github.com/maho3/ltu-ili)]  
  Unified interface over sbi, pydelfi and lampe with validation and calibration tools.

## Communities and Groups

- [Polymathic AI](https://polymathic-ai.org) develops AstroCLIP, AION-1, the Multimodal Universe and The Well.
- [UniverseTBD](https://universetbd.org) develops AstroLLaMA, AstroPT and AstroLLaVA.
- [AstroMLab](https://huggingface.co/AstroMLab) develops the AstroMLab benchmark and the AstroSage models.

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
