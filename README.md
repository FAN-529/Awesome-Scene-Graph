# Awesome Scene Graph

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/FAN-529/Awesome-Scene-Graph?style=social)](https://github.com/FAN-529/Awesome-Scene-Graph)

A curated collection of papers, datasets and implementations on scene graphs: image scene graph generation, panoptic and open-vocabulary representations, temporal graphs, 3D spatial reasoning, and surgical applications.

**94 entries from 2015 to 2026.** Literature snapshot: **2026-10-12**. Repository updated: **2026-10-14**.

[中文说明](README.zh-CN.md) · [中文逐篇阅读笔记](docs/reading-guide.zh-CN.md) · [Structured catalogue](data/papers.json) · [BibTeX](references.bib)

The list covers selected milestones and related applications rather than every scene graph paper. Published papers, accepted papers, workshops and preprints are labelled separately. A `repo` link means a public repository is available; it does not certify complete code, released checkpoints, permissive licensing or reproduced results.

## Contents

- [Start here](#start-here)
- [Papers by year](#papers-by-year)
- [Papers by topic](#papers-by-topic)
- [Datasets and benchmarks](#datasets-and-benchmarks)
- [Surveys](#surveys)
- [Tools and implementations](#tools-and-implementations)
- [Reading notes and citations](#reading-notes-and-citations)
- [Under review](#under-review)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Start here

For a first pass, follow the progression from objects, attributes and relationships to automatic generation, time, geometry and surgical use:

1. [Image Retrieval Using Scene Graphs](#paper-johnson2015) (2015).
2. [Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations](#paper-visualgenome2017) (2017).
3. [Scene Graph Generation by Iterative Message Passing](#paper-imp2017) (2017).
4. [Neural Motifs: Scene Graph Parsing with Global Context](#paper-motifs2018) (2018).
5. [Panoptic Scene Graph Generation](#paper-psg2022) (2022).
6. [Action Genome: Actions As Compositions of Spatio-Temporal Scene Graphs](#paper-action-genome) (2020).
7. [Panoptic Video Scene Graph Generation](#paper-pvsg) (2023).
8. [Learning 3D Semantic Scene Graphs from 3D Indoor Reconstructions](#paper-g02) (2020).
9. [Learning and Reasoning with the Graph Structure Representation in Robotic Surgery](#paper-surg2020-graph) (2020).
10. [Advancing Surgical VQA with Scene Graph Knowledge](#paper-ssg-vqa) (2024).

A scene graph may contain symbolic labels, visual features, geometry or several of these together. Downstream experiments using human annotations or the original video should not be read as evidence that an automatically predicted symbolic graph can replace the video.

## Papers by year

### 2026

- <a id="paper-surg-scoping"></a>[Medical Image Analysis 2026] **Decoding the Surgical Scene: A Scoping Review of Scene Graphs in Surgery** [[paper]](https://doi.org/10.1016/j.media.2026.104083) [[notes]](docs/reading-guide.zh-CN.md#paper-surg-scoping)
- <a id="paper-ego-sg"></a>[arXiv 2026; preprint] **Graph it first! Enabling Reasoning on Long-form Egocentric Videos through Scene Graphs** [[paper]](https://arxiv.org/abs/2606.25842) [[notes]](docs/reading-guide.zh-CN.md#paper-ego-sg)
- <a id="paper-graphthinker"></a>[arXiv 2026; preprint] **GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking** [[paper]](https://arxiv.org/abs/2602.17555) [[notes]](docs/reading-guide.zh-CN.md#paper-graphthinker)
- <a id="paper-g13"></a>[NeurIPS 2026; accepted] **GraphWrit3R: End-to-End 3D Scene Graph Writing** [[paper]](https://arxiv.org/abs/2609.31595) [[repo]](https://github.com/insait-institute/GraphWrit3R) [[notes]](docs/reading-guide.zh-CN.md#paper-g13)
- <a id="paper-or-action"></a>[MICCAI 2026] **OR-Action: Multi-Role Video Understanding with Fine-Grained Actions** [[paper]](https://papers.miccai.org/miccai-2026/0741-Paper4727.html) [[notes]](docs/reading-guide.zh-CN.md#paper-or-action)
- <a id="paper-probabilistic2026"></a>[arXiv 2026; preprint] **Probabilistic Scene Graphs: Hierarchical Representation and Real-time System** [[paper]](https://arxiv.org/abs/2609.23144) [[notes]](docs/reading-guide.zh-CN.md#paper-probabilistic2026)
- <a id="paper-protoflow"></a>[IPCAI / IJCARS 2026] **ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes** [[paper]](https://arxiv.org/abs/2512.14092) [[notes]](docs/reading-guide.zh-CN.md#paper-protoflow)
- <a id="paper-relationr1-2026"></a>[AAAI 2026] **Relation-R1: Progressively Cognitive Chain-of-Thought Guided Reinforcement Learning for Unified Relation Comprehension** [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/37557) [[repo]](https://github.com/HKUST-LongGroup/Relation-R1) [[notes]](docs/reading-guide.zh-CN.md#paper-relationr1-2026)
- <a id="paper-sage-or"></a>[BMVC 2026; accepted] **SAGE-OR: Semi-supervised Adaptive Scene Graph Generation for Operating Rooms** [[paper]](https://arxiv.org/abs/2608.15336) [[repo]](https://github.com/TheFourthKaramazov/SAGE-OR) [[notes]](docs/reading-guide.zh-CN.md#paper-sage-or)
- <a id="paper-sage2026"></a>[ICML 2026] **Scene Graph Thinking: Reinforcing Structured Visual Reasoning for Multimodal Large Language Models** [[paper]](https://proceedings.mlr.press/v306/yang26ck.html) [[repo]](https://github.com/zwyang6/SaGe) [[notes]](docs/reading-guide.zh-CN.md#paper-sage2026)
- <a id="paper-sggr3-2026"></a>[Findings of ACL 2026] **SGG-R3: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation** [[paper]](https://aclanthology.org/2026.findings-acl.992/) [[notes]](docs/reading-guide.zh-CN.md#paper-sggr3-2026)
- <a id="paper-sg-nca"></a>[SafeSurg @ MICCAI Workshops 2026] **Sterilizable Scene Graph Generation for Operating Rooms** [[paper]](https://arxiv.org/abs/2608.16469) [[repo]](https://github.com/MECLabTUDA/SG-NCA) [[notes]](docs/reading-guide.zh-CN.md#paper-sg-nca)
- <a id="paper-topoor"></a>[MICCAI 2026] **TopoOR: A Unified Topological Scene Representation for the Operating Room** [[paper]](https://papers.miccai.org/miccai-2026/1068-Paper2412.html) [[notes]](docs/reading-guide.zh-CN.md#paper-topoor)
- <a id="paper-uno"></a>[WACV 2026] **UNO: Unifying One-stage Video Scene Graph Generation via Object-Centric Visual Representation Learning** [[paper]](https://openaccess.thecvf.com/content/WACV2026/html/Le_UNO_Unifying_One-stage_Video_Scene_Graph_Generation_via_Object-Centric_Visual_WACV_2026_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-uno)

### 2025

- <a id="paper-cat-sg"></a>[MICCAI 2025] **CAT-SG: A Large Dynamic Scene Graph Dataset for Fine-Grained Understanding of Cataract Surgery** [[paper]](https://arxiv.org/abs/2506.21813) [[repo]](https://github.com/felixholm/CAT-SG) [[notes]](docs/reading-guide.zh-CN.md#paper-cat-sg)
- <a id="paper-conformal2025"></a>[CVPR 2025] **Conformal Prediction and MLLM aided Uncertainty Quantification in Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Nag_Conformal_Prediction_and_MLLM_aided_Uncertainty_Quantification_in_Scene_Graph_CVPR_2025_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-conformal2025)
- <a id="paper-copasg2025"></a>[ICCV Workshops (SG2RL) 2025] **CoPa-SG: Dense Scene Graphs with Parametric and Proto-Relations** [[paper]](https://openaccess.thecvf.com/content/ICCV2025W/SG2RL/html/Lorenz_CoPa-SG_Dense_Scene_Graphs_with_Parametric_and_Proto-Relations_ICCVW_2025_paper.html) [[project]](https://lorjul.github.io/copasg/) [[notes]](docs/reading-guide.zh-CN.md#paper-copasg2025)
- <a id="paper-diffvsgg"></a>[CVPR 2025] **DiffVsgg: Diffusion-Driven Online Video Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_DiffVsgg_Diffusion-Driven_Online_Video_Scene_Graph_Generation_CVPR_2025_paper.html) [[repo]](https://github.com/kagawa588/DiffVsgg) [[notes]](docs/reading-guide.zh-CN.md#paper-diffvsgg)
- <a id="paper-egoexor"></a>[NeurIPS Datasets and Benchmarks 2025] **EgoExOR: An Ego-Exo-Centric Operating Room Dataset for Surgical Activity Understanding** [[paper]](https://arxiv.org/abs/2505.24287) [[repo]](https://github.com/ardamamur/EgoExOR) [[notes]](docs/reading-guide.zh-CN.md#paper-egoexor)
- <a id="paper-esca2025"></a>[NeurIPS 2025] **ESCA: Contextualizing Embodied Agents via Scene-Graph Generation** [[paper]](https://proceedings.nips.cc/paper_files/paper/2025/hash/0418973e545b932939302cb605d06f43-Abstract-Conference.html) [[repo]](https://github.com/video-fm/ESCA) [[notes]](docs/reading-guide.zh-CN.md#paper-esca2025)
- <a id="paper-g12"></a>[IROS 2025] **FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction** [[paper]](https://doi.org/10.1109/IROS60139.2025.11247555) [[repo]](https://github.com/dennisrotondi/FunGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-g12)
- <a id="paper-llavaspace2025"></a>[WACV 2025] **LLaVA-SpaceSGG: Visual Instruct Tuning for Open-Vocabulary Scene Graph Generation with Enhanced Spatial Relations** [[paper]](https://openaccess.thecvf.com/content/WACV2025/html/Xu_LLaVA-SpaceSGG_Visual_Instruct_Tuning_for_Open-Vocabulary_Scene_Graph_Generation_with_WACV_2025_paper.html) [[repo]](https://github.com/Endlinc/LLaVA-SpaceSGG) [[notes]](docs/reading-guide.zh-CN.md#paper-llavaspace2025)
- <a id="paper-llmbenchmark2025"></a>[ACL 2025] **LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs? A Benchmark and Empirical Study** [[paper]](https://aclanthology.org/2025.acl-long.1036/) [[notes]](docs/reading-guide.zh-CN.md#paper-llmbenchmark2025)
- <a id="paper-mm-or"></a>[CVPR 2025] **MM-OR: A Large Multimodal Operating Room Dataset for Semantic Understanding of High-Intensity Surgical Environments** [[paper]](https://arxiv.org/abs/2503.02579) [[repo]](https://github.com/egeozsoy/MM-OR) [[notes]](docs/reading-guide.zh-CN.md#paper-mm-or)
- <a id="paper-g11"></a>[CVPR 2025] **Open-Vocabulary Functional 3D Scene Graphs for Real-World Indoor Spaces** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Open-Vocabulary_Functional_3D_Scene_Graphs_for_Real-World_Indoor_Spaces_CVPR_2025_paper.html) [[repo]](https://github.com/ZhangCYG/OpenFunGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-g11)
- <a id="paper-g10"></a>[CVPR 2025] **RelationField: Relate Anything in Radiance Fields** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Koch_RelationField_Relate_Anything_in_Radiance_Fields_CVPR_2025_paper.html) [[repo]](https://github.com/boschresearch/RelationField) [[notes]](docs/reading-guide.zh-CN.md#paper-g10)
- <a id="paper-sg2vid"></a>[MICCAI 2025] **SG2VID: Scene Graphs Enable Fine-Grained Control for Video Synthesis** [[paper]](https://arxiv.org/abs/2506.03082) [[repo]](https://github.com/MECLabTUDA/SG2VID) [[notes]](docs/reading-guide.zh-CN.md#paper-sg2vid)
- <a id="paper-surgrid"></a>[IPCAI / IJCARS 2025] **SurGrID: Controllable Surgical Simulation via Scene Graph to Image Diffusion** [[paper]](https://arxiv.org/abs/2502.07945) [[notes]](docs/reading-guide.zh-CN.md#paper-surgrid)
- <a id="paper-holistic-surgical"></a>[MICCAI 2025] **Towards Holistic Surgical Scene Graph** [[paper]](https://arxiv.org/abs/2507.15541) [[repo]](https://github.com/ailab-kyunghee/SSG-Com) [[notes]](docs/reading-guide.zh-CN.md#paper-holistic-surgical)
- <a id="paper-vsdd"></a>[CVPR 2025] **Unbiased Video Scene Graph Generation via Visual and Semantic Dual Debiasing** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Unbiased_Video_Scene_Graph_Generation_via_Visual_and_Semantic_Dual_CVPR_2025_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-vsdd)
- <a id="paper-usg2025"></a>[CVPR 2025] **Universal Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Universal_Scene_Graph_Generation_CVPR_2025_paper.html) [[repo]](https://github.com/ChocoWu/USG) [[notes]](docs/reading-guide.zh-CN.md#paper-usg2025)
- <a id="paper-vlirm2025"></a>[ICCV 2025] **Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-vlirm2025)

### 2024

- <a id="paper-fairpsg2024"></a>[ECCV 2024] **A Fair Ranking and New Model for Panoptic Scene Graph Generation** [[paper]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7817_ECCV_2024_paper.php) [[repo]](https://github.com/lorjul/panoptic-scene-graph-generation) [[notes]](docs/reading-guide.zh-CN.md#paper-fairpsg2024)
- <a id="paper-easg"></a>[CVPR 2024] **Action Scene Graphs for Long-Form Understanding of Egocentric Videos** [[paper]](https://openaccess.thecvf.com/content/CVPR2024/html/Rodin_Action_Scene_Graphs_for_Long-Form_Understanding_of_Egocentric_Videos_CVPR_2024_paper.html) [[repo]](https://github.com/fpv-iplab/EASG) [[notes]](docs/reading-guide.zh-CN.md#paper-easg)
- <a id="paper-ssg-vqa"></a>[IPCAI / IJCARS 2024] **Advancing Surgical VQA with Scene Graph Knowledge** [[paper]](https://arxiv.org/abs/2312.10251) [[repo]](https://github.com/CAMMA-public/SSG-VQA) [[notes]](docs/reading-guide.zh-CN.md#paper-ssg-vqa)
- <a id="paper-g08"></a>[IEEE Robotics and Automation Letters 2024] **Clio: Real-time Task-Driven Open-Set 3D Scene Graphs** [[paper]](https://doi.org/10.1109/LRA.2024.3451395) [[repo]](https://github.com/MIT-SPARK/Clio) [[notes]](docs/reading-guide.zh-CN.md#paper-g08)
- <a id="paper-g06"></a>[ICRA 2024] **ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning** [[paper]](https://concept-graphs.github.io/) [[repo]](https://github.com/concept-graphs/concept-graphs) [[notes]](docs/reading-guide.zh-CN.md#paper-g06)
- <a id="paper-ovsgtr2024"></a>[ECCV 2024] **Expanding Scene Graph Boundaries: Fully Open-Vocabulary Scene Graph Generation via Visual-Concept Alignment and Retention** [[paper]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8290_ECCV_2024_paper.php) [[repo]](https://github.com/gpt4vision/OvSGTR) [[notes]](docs/reading-guide.zh-CN.md#paper-ovsgtr2024)
- <a id="paper-pixels2024"></a>[CVPR 2024] **From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models** [[paper]](https://openaccess.thecvf.com/content/CVPR2024/html/Li_From_Pixels_to_Graphs_Open-Vocabulary_Scene_Graph_Generation_with_Vision-Language_CVPR_2024_paper.html) [[repo]](https://github.com/SHTUPLUS/Pix2Grp_CVPR2024) [[notes]](docs/reading-guide.zh-CN.md#paper-pixels2024)
- <a id="paper-holistic-or"></a>[IJCARS 2024] **Holistic OR domain modeling: a semantic scene graph approach** [[paper]](https://doi.org/10.1007/s11548-023-03022-w) [[repo]](https://github.com/egeozsoy/4D-OR) [[notes]](docs/reading-guide.zh-CN.md#paper-holistic-or) Journal extension.
- <a id="paper-g07"></a>[Robotics Science and Systems 2024] **Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic SLAM in Dynamic Environments** [[paper]](https://www.roboticsproceedings.org/rss20/p081.html) [[repo]](https://github.com/MIT-SPARK/Khronos) [[notes]](docs/reading-guide.zh-CN.md#paper-g07)
- <a id="paper-lg-cvs"></a>[IEEE TMI 2024] **Latent Graph Representations for Critical View of Safety Assessment** [[paper]](https://arxiv.org/abs/2212.04155) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-lg-cvs)
- <a id="paper-llm4sgg2024"></a>[CVPR 2024] **LLM4SGG: Large Language Models for Weakly Supervised Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_LLM4SGG_Large_Language_Models_for_Weakly_Supervised_Scene_Graph_Generation_CVPR_2024_paper.html) [[repo]](https://github.com/rlqja1107/torch-LLM4SGG) [[notes]](docs/reading-guide.zh-CN.md#paper-llm4sgg2024)
- <a id="paper-oed"></a>[CVPR 2024] **OED: Towards One-stage End-to-End Dynamic Scene Graph Generation** [[paper]](https://arxiv.org/abs/2405.16925) [[repo]](https://github.com/guanw-pku/OED) [[notes]](docs/reading-guide.zh-CN.md#paper-oed)
- <a id="paper-g09"></a>[CVPR 2024] **Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships** [[paper]](https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html) [[repo]](https://github.com/boschresearch/Open3DSG) [[notes]](docs/reading-guide.zh-CN.md#paper-g09)
- <a id="paper-openpsg2024"></a>[ECCV 2024] **OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models** [[paper]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1552_ECCV_2024_paper.php) [[repo]](https://github.com/franciszzj/OpenPSG) [[notes]](docs/reading-guide.zh-CN.md#paper-openpsg2024)
- <a id="paper-surg-dg"></a>[IPCAI / IJCARS 2024] **Optimizing Latent Graph Representations of Surgical Scenes for Zero-Shot Domain Transfer** [[paper]](https://arxiv.org/abs/2403.06953) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-surg-dg)
- <a id="paper-oracle"></a>[MICCAI 2024] **ORacle: Large Vision-Language Models for Knowledge-Guided Holistic OR Domain Modeling** [[paper]](https://arxiv.org/abs/2404.07031) [[notes]](docs/reading-guide.zh-CN.md#paper-oracle)
- <a id="paper-sangria"></a>[GRAIL @ MICCAI 2024] **SANGRIA: Surgical Video Scene Graph Optimization for Surgical Workflow Prediction** [[paper]](https://arxiv.org/abs/2407.20214) [[notes]](docs/reading-guide.zh-CN.md#paper-sangria)
- <a id="paper-sgt-plus-plus"></a>[IEEE TMI 2024] **SGT++: Improved Scene Graph-Guided Transformer for Surgical Report Generation** [[paper]](https://doi.org/10.1109/TMI.2023.3335909) [[notes]](docs/reading-guide.zh-CN.md#paper-sgt-plus-plus) **Abstract reviewed only.**
- <a id="paper-s2former-or"></a>[IEEE TMI 2024] **S²Former-OR: Single-Stage Bi-Modal Transformer for Scene Graph Generation in OR** [[paper]](https://arxiv.org/abs/2402.14461) [[notes]](docs/reading-guide.zh-CN.md#paper-s2former-or)
- <a id="paper-asmv2-2024"></a>[ECCV 2024] **The All-Seeing Project V2: Towards General Relation Comprehension of the Open World** [[paper]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04939.pdf) [[repo]](https://github.com/OpenGVLab/all-seeing) [[notes]](docs/reading-guide.zh-CN.md#paper-asmv2-2024)
- <a id="paper-tritemp-or"></a>[MICCAI 2024] **Tri-modal Confluence with Temporal Dynamics for Scene Graph Generation in Operating Rooms** [[paper]](https://arxiv.org/abs/2404.09231) [[notes]](docs/reading-guide.zh-CN.md#paper-tritemp-or)

### 2023

- <a id="paper-dynamic-surgical"></a>[ICCV Workshops (SG2RL) 2023] **Dynamic Scene Graph Representation for Surgical Video** [[paper]](https://openaccess.thecvf.com/content/ICCV2023W/SG2RL/html/Holm_Dynamic_Scene_Graph_Representation_for_Surgical_Video_ICCVW_2023_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-dynamic-surgical)
- <a id="paper-surg-stlg"></a>[MICCAI 2023] **Encoding Surgical Videos as Latent Spatiotemporal Graphs for Object and Anatomy-Driven Reasoning** [[paper]](https://arxiv.org/abs/2312.06829) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-surg-stlg)
- <a id="paper-dsg-detr"></a>[WACV 2023] **Exploiting Long-Term Dependencies for Generating Dynamic Scene Graphs** [[paper]](https://arxiv.org/abs/2112.09828) [[repo]](https://github.com/Shengyu-Feng/DSG-DETR) [[notes]](docs/reading-guide.zh-CN.md#paper-dsg-detr)
- <a id="paper-labrad-or"></a>[MICCAI 2023] **LABRAD-OR: Lightweight Memory Scene Graphs for Accurate Bimodal Reasoning in Dynamic Operating Rooms** [[paper]](https://arxiv.org/abs/2303.13293) [[repo]](https://github.com/egeozsoy/LABRAD-OR) [[notes]](docs/reading-guide.zh-CN.md#paper-labrad-or)
- <a id="paper-vs3-2023"></a>[CVPR 2023] **Learning To Generate Language-Supervised and Open-Vocabulary Scene Graph Using Pre-Trained Visual-Semantic Space** [[paper]](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_Learning_To_Generate_Language-Supervised_and_Open-Vocabulary_Scene_Graph_Using_Pre-Trained_CVPR_2023_paper.html) [[repo]](https://github.com/gitzyong812/VS3_CVPR23) [[notes]](docs/reading-guide.zh-CN.md#paper-vs3-2023)
- <a id="paper-pvsg"></a>[CVPR 2023] **Panoptic Video Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_Panoptic_Video_Scene_Graph_Generation_CVPR_2023_paper.html) [[repo]](https://github.com/LilyDaytoy/OpenPVSG) [[notes]](docs/reading-guide.zh-CN.md#paper-pvsg)
- <a id="paper-reltr2023"></a>[IEEE TPAMI 2023] **RelTR: Relation Transformer for Scene Graph Generation** [[paper]](https://arxiv.org/abs/2201.11460) [[repo]](https://github.com/yrcong/RelTR) [[notes]](docs/reading-guide.zh-CN.md#paper-reltr2023)
- <a id="paper-tempura"></a>[CVPR 2023] **Unbiased Scene Graph Generation in Videos** [[paper]](https://arxiv.org/abs/2304.00733) [[repo]](https://github.com/sayaknag/unbiasedSGG) [[notes]](docs/reading-guide.zh-CN.md#paper-tempura)

### 2022

- <a id="paper-4d-or"></a>[MICCAI 2022] **4D-OR: Semantic Scene Graphs for OR Domain Modeling** [[paper]](https://arxiv.org/abs/2203.11937) [[repo]](https://github.com/egeozsoy/4D-OR) [[notes]](docs/reading-guide.zh-CN.md#paper-4d-or)
- <a id="paper-g05"></a>[Robotics Science and Systems 2022] **Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization** [[paper]](https://www.roboticsproceedings.org/rss18/p050.html) [[repo]](https://github.com/MIT-SPARK/Hydra) [[notes]](docs/reading-guide.zh-CN.md#paper-g05)
- <a id="paper-informative2022"></a>[CVPR 2022] **Not All Relations Are Equal: Mining Informative Labels for Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2022/html/Goel_Not_All_Relations_Are_Equal_Mining_Informative_Labels_for_Scene_CVPR_2022_paper.html) [[repo]](https://github.com/VICO-UoE/NARE) [[notes]](docs/reading-guide.zh-CN.md#paper-informative2022)
- <a id="paper-psg2022"></a>[ECCV 2022] **Panoptic Scene Graph Generation** [[paper]](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/222_ECCV_2022_paper.php) [[repo]](https://github.com/Jingkang50/OpenPSG) [[notes]](docs/reading-guide.zh-CN.md#paper-psg2022)
- <a id="paper-sgt"></a>[MICCAI 2022] **SGT: Scene Graph-Guided Transformer for Surgical Report Generation** [[paper]](https://conferences.miccai.org/2022/papers/463-Paper2204.html) [[repo]](https://github.com/ccccchenllll/SGT_master) [[notes]](docs/reading-guide.zh-CN.md#paper-sgt)
- <a id="paper-sgtr2022"></a>[CVPR 2022] **SGTR: End-to-End Scene Graph Generation With Transformer** [[paper]](https://openaccess.thecvf.com/content/CVPR2022/html/Li_SGTR_End-to-End_Scene_Graph_Generation_With_Transformer_CVPR_2022_paper.html) [[repo]](https://github.com/Scarecrow0/SGTR) [[notes]](docs/reading-guide.zh-CN.md#paper-sgtr2022)
- <a id="paper-ssrcnn2022"></a>[CVPR 2022] **Structured Sparse R-CNN for Direct Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2022/html/Teng_Structured_Sparse_R-CNN_for_Direct_Scene_Graph_Generation_CVPR_2022_paper.html) [[repo]](https://github.com/MCG-NJU/Structured-Sparse-RCNN) [[notes]](docs/reading-guide.zh-CN.md#paper-ssrcnn2022)
- <a id="paper-nice2022"></a>[CVPR 2022] **The Devil Is in the Labels: Noisy Label Correction for Robust Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2022/html/Li_The_Devil_Is_in_the_Labels_Noisy_Label_Correction_for_CVPR_2022_paper.html) [[repo]](https://github.com/muktilin/NICE) [[notes]](docs/reading-guide.zh-CN.md#paper-nice2022)
- <a id="paper-ovprompt2022"></a>[ECCV 2022] **Towards Open-Vocabulary Scene Graph Generation with Prompt-Based Finetuning** [[paper]](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6652_ECCV_2022_paper.php) [[notes]](docs/reading-guide.zh-CN.md#paper-ovprompt2022)

### 2021

- <a id="paper-bgnn2021"></a>[CVPR 2021] **Bipartite Graph Network with Adaptive Message Passing for Unbiased Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Bipartite_Graph_Network_With_Adaptive_Message_Passing_for_Unbiased_Scene_CVPR_2021_paper.html) [[repo]](https://github.com/SHTUPLUS/PySGG) [[notes]](docs/reading-guide.zh-CN.md#paper-bgnn2021)
- <a id="paper-ebm2021"></a>[CVPR 2021] **Energy-Based Learning for Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2021/html/Suhail_Energy-Based_Learning_for_Scene_Graph_Generation_CVPR_2021_paper.html) [[repo]](https://github.com/mods333/energy-based-scene-graph) [[notes]](docs/reading-guide.zh-CN.md#paper-ebm2021)
- <a id="paper-fcsgg2021"></a>[CVPR 2021] **Fully Convolutional Scene Graph Generation** [[paper]](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_Fully_Convolutional_Scene_Graph_Generation_CVPR_2021_paper.html) [[repo]](https://github.com/liuhengyue/fcsgg) [[notes]](docs/reading-guide.zh-CN.md#paper-fcsgg2021)
- <a id="paper-g04"></a>[CVPR 2021] **SceneGraphFusion: Incremental 3D Scene Graph Prediction from RGB-D Sequences** [[paper]](https://openaccess.thecvf.com/content/CVPR2021/html/Wu_SceneGraphFusion_Incremental_3D_Scene_Graph_Prediction_From_RGB-D_Sequences_CVPR_2021_paper.html) [[repo]](https://github.com/ShunChengWu/SceneGraphFusion) [[notes]](docs/reading-guide.zh-CN.md#paper-g04)
- <a id="paper-sttran"></a>[ICCV 2021] **Spatial-Temporal Transformer for Dynamic Scene Graph Generation** [[paper]](https://arxiv.org/abs/2107.12309) [[repo]](https://github.com/yrcong/STTran) [[notes]](docs/reading-guide.zh-CN.md#paper-sttran)

### 2020

- <a id="paper-g03"></a>[Robotics Science and Systems 2020] **3D Dynamic Scene Graphs: Actionable Spatial Perception with Places, Objects, and Humans** [[paper]](https://www.roboticsproceedings.org/rss16/p079.html) [[framework]](https://github.com/MIT-SPARK/Kimera) [[notes]](docs/reading-guide.zh-CN.md#paper-g03)
- <a id="paper-action-genome"></a>[CVPR 2020] **Action Genome: Actions As Compositions of Spatio-Temporal Scene Graphs** [[paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Ji_Action_Genome_Actions_As_Compositions_of_Spatio-Temporal_Scene_Graphs_CVPR_2020_paper.html) [[repo]](https://github.com/JingweiJ/ActionGenome) [[notes]](docs/reading-guide.zh-CN.md#paper-action-genome)
- <a id="paper-g02"></a>[CVPR 2020] **Learning 3D Semantic Scene Graphs from 3D Indoor Reconstructions** [[paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Wald_Learning_3D_Semantic_Scene_Graphs_From_3D_Indoor_Reconstructions_CVPR_2020_paper.html) [[data repo]](https://github.com/3DSSG/3DSSG.github.io) [[notes]](docs/reading-guide.zh-CN.md#paper-g02)
- <a id="paper-surg2020-graph"></a>[MICCAI 2020] **Learning and Reasoning with the Graph Structure Representation in Robotic Surgery** [[paper]](https://arxiv.org/abs/2007.03357) [[repo]](https://github.com/mobarakol/Surgical_SceneGraph_Generation) [[notes]](docs/reading-guide.zh-CN.md#paper-surg2020-graph)
- <a id="paper-pcpl2020"></a>[ACM Multimedia 2020] **PCPL: Predicate-Correlation Perception Learning for Unbiased Scene Graph Generation** [[paper]](https://doi.org/10.1145/3394171.3413722) [[notes]](docs/reading-guide.zh-CN.md#paper-pcpl2020)
- <a id="paper-tde2020"></a>[CVPR 2020] **Unbiased Scene Graph Generation from Biased Training** [[paper]](https://arxiv.org/abs/2002.11949) [[repo]](https://github.com/KaihuaTang/Scene-Graph-Benchmark.pytorch) [[notes]](docs/reading-guide.zh-CN.md#paper-tde2020)

### 2019

- <a id="paper-g01"></a>[ICCV 2019] **3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera** [[paper]](https://openaccess.thecvf.com/content_ICCV_2019/html/Armeni_3D_Scene_Graph_A_Structure_for_Unified_Semantics_3D_Space_ICCV_2019_paper.html) [[repo]](https://github.com/StanfordVL/3DSceneGraph) [[notes]](docs/reading-guide.zh-CN.md#paper-g01)
- <a id="paper-gcl2019"></a>[CVPR 2019] **Graphical Contrastive Losses for Scene Graph Parsing** [[paper]](https://openaccess.thecvf.com/content_CVPR_2019/html/Zhang_Graphical_Contrastive_Losses_for_Scene_Graph_Parsing_CVPR_2019_paper.html) [[repo]](https://github.com/NVIDIA/ContrastiveLosses4VRD) [[notes]](docs/reading-guide.zh-CN.md#paper-gcl2019)
- <a id="paper-kern2019"></a>[CVPR 2019] **Knowledge-Embedded Routing Network for Scene Graph Generation** [[paper]](https://arxiv.org/abs/1903.03326) [[repo]](https://github.com/yuweihao/KERN) [[notes]](docs/reading-guide.zh-CN.md#paper-kern2019)
- <a id="paper-vctree2019"></a>[CVPR 2019] **Learning to Compose Dynamic Tree Structures for Visual Contexts** [[paper]](https://arxiv.org/abs/1812.01880) [[repo]](https://github.com/KaihuaTang/VCTree-Scene-Graph-Generation) [[notes]](docs/reading-guide.zh-CN.md#paper-vctree2019)

### 2018

- <a id="paper-graphrcnn2018"></a>[ECCV 2018] **Graph R-CNN for Scene Graph Generation** [[paper]](https://arxiv.org/abs/1808.00191) [[repo]](https://github.com/jwyang/graph-rcnn.pytorch) [[notes]](docs/reading-guide.zh-CN.md#paper-graphrcnn2018)
- <a id="paper-motifs2018"></a>[CVPR 2018] **Neural Motifs: Scene Graph Parsing with Global Context** [[paper]](https://arxiv.org/abs/1711.06640) [[repo]](https://github.com/rowanz/neural-motifs) [[notes]](docs/reading-guide.zh-CN.md#paper-motifs2018)

### 2017

- <a id="paper-imp2017"></a>[CVPR 2017] **Scene Graph Generation by Iterative Message Passing** [[paper]](https://openaccess.thecvf.com/content_cvpr_2017/html/Xu_Scene_Graph_Generation_CVPR_2017_paper.html) [[repo]](https://github.com/danfeiX/scene-graph-TF-release) [[notes]](docs/reading-guide.zh-CN.md#paper-imp2017)
- <a id="paper-phrase2017"></a>[ICCV 2017] **Scene Graph Generation from Objects, Phrases and Region Captions** [[paper]](https://openaccess.thecvf.com/content_iccv_2017/html/Li_Scene_Graph_Generation_ICCV_2017_paper.html) [[repo]](https://github.com/yikang-li/MSDN) [[notes]](docs/reading-guide.zh-CN.md#paper-phrase2017)
- <a id="paper-vidvrd"></a>[ACM Multimedia 2017] **Video Visual Relation Detection** [[paper]](https://doi.org/10.1145/3123266.3123380) [[repo]](https://github.com/VRU-NExT/Video-Relation-Detection) [[notes]](docs/reading-guide.zh-CN.md#paper-vidvrd)
- <a id="paper-visualgenome2017"></a>[IJCV 2017] **Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations** [[paper]](https://doi.org/10.1007/s11263-016-0981-7) [[data tool]](https://github.com/ranjaykrishna/visual_genome_python_driver) [[notes]](docs/reading-guide.zh-CN.md#paper-visualgenome2017)
- <a id="paper-vtranse2017"></a>[CVPR 2017] **Visual Translation Embedding Network for Visual Relation Detection** [[paper]](https://arxiv.org/abs/1702.08319) [[repo]](https://github.com/zawlin/cvpr17_vtranse) [[notes]](docs/reading-guide.zh-CN.md#paper-vtranse2017)

### 2016

- <a id="paper-lu2016"></a>[ECCV 2016] **Visual Relationship Detection with Language Priors** [[paper]](https://arxiv.org/abs/1608.00187) [[repo]](https://github.com/Prof-Lu-Cewu/Visual-Relationship-Detection) [[notes]](docs/reading-guide.zh-CN.md#paper-lu2016)

### 2015

- <a id="paper-johnson2015"></a>[CVPR 2015] **Image Retrieval Using Scene Graphs** [[paper]](https://openaccess.thecvf.com/content_cvpr_2015/html/Johnson_Image_Retrieval_Using_2015_CVPR_paper.html) [[notes]](docs/reading-guide.zh-CN.md#paper-johnson2015)

## Papers by topic

Each paper has one primary topic below. Dataset, reasoning and generation papers can also be found through the resource sections.

### Foundations and Image Scene Graph Generation

- [RelTR: Relation Transformer for Scene Graph Generation](#paper-reltr2023) (2023).
- [Not All Relations Are Equal: Mining Informative Labels for Scene Graph Generation](#paper-informative2022) (2022).
- [Structured Sparse R-CNN for Direct Scene Graph Generation](#paper-ssrcnn2022) (2022).
- [The Devil Is in the Labels: Noisy Label Correction for Robust Scene Graph Generation](#paper-nice2022) (2022).
- [Bipartite Graph Network with Adaptive Message Passing for Unbiased Scene Graph Generation](#paper-bgnn2021) (2021).
- [Energy-Based Learning for Scene Graph Generation](#paper-ebm2021) (2021).
- [Fully Convolutional Scene Graph Generation](#paper-fcsgg2021) (2021).
- [PCPL: Predicate-Correlation Perception Learning for Unbiased Scene Graph Generation](#paper-pcpl2020) (2020).
- [Unbiased Scene Graph Generation from Biased Training](#paper-tde2020) (2020).
- [Graphical Contrastive Losses for Scene Graph Parsing](#paper-gcl2019) (2019).
- [Knowledge-Embedded Routing Network for Scene Graph Generation](#paper-kern2019) (2019).
- [Learning to Compose Dynamic Tree Structures for Visual Contexts](#paper-vctree2019) (2019).
- [Graph R-CNN for Scene Graph Generation](#paper-graphrcnn2018) (2018).
- [Neural Motifs: Scene Graph Parsing with Global Context](#paper-motifs2018) (2018).
- [Scene Graph Generation by Iterative Message Passing](#paper-imp2017) (2017).
- [Scene Graph Generation from Objects, Phrases and Region Captions](#paper-phrase2017) (2017).
- [Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations](#paper-visualgenome2017) (2017).
- [Visual Translation Embedding Network for Visual Relation Detection](#paper-vtranse2017) (2017).
- [Visual Relationship Detection with Language Priors](#paper-lu2016) (2016).
- [Image Retrieval Using Scene Graphs](#paper-johnson2015) (2015).

### Panoptic, Open-Vocabulary and Multimodal Scene Graphs

- [Relation-R1: Progressively Cognitive Chain-of-Thought Guided Reinforcement Learning for Unified Relation Comprehension](#paper-relationr1-2026) (2026).
- [Scene Graph Thinking: Reinforcing Structured Visual Reasoning for Multimodal Large Language Models](#paper-sage2026) (2026).
- [SGG-R3: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation](#paper-sggr3-2026) (2026).
- [Conformal Prediction and MLLM aided Uncertainty Quantification in Scene Graph Generation](#paper-conformal2025) (2025).
- [CoPa-SG: Dense Scene Graphs with Parametric and Proto-Relations](#paper-copasg2025) (2025).
- [ESCA: Contextualizing Embodied Agents via Scene-Graph Generation](#paper-esca2025) (2025).
- [LLaVA-SpaceSGG: Visual Instruct Tuning for Open-Vocabulary Scene Graph Generation with Enhanced Spatial Relations](#paper-llavaspace2025) (2025).
- [LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs? A Benchmark and Empirical Study](#paper-llmbenchmark2025) (2025).
- [Universal Scene Graph Generation](#paper-usg2025) (2025).
- [Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation](#paper-vlirm2025) (2025).
- [A Fair Ranking and New Model for Panoptic Scene Graph Generation](#paper-fairpsg2024) (2024).
- [Expanding Scene Graph Boundaries: Fully Open-Vocabulary Scene Graph Generation via Visual-Concept Alignment and Retention](#paper-ovsgtr2024) (2024).
- [From Pixels to Graphs: Open-Vocabulary Scene Graph Generation with Vision-Language Models](#paper-pixels2024) (2024).
- [LLM4SGG: Large Language Models for Weakly Supervised Scene Graph Generation](#paper-llm4sgg2024) (2024).
- [OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models](#paper-openpsg2024) (2024).
- [The All-Seeing Project V2: Towards General Relation Comprehension of the Open World](#paper-asmv2-2024) (2024).
- [Learning To Generate Language-Supervised and Open-Vocabulary Scene Graph Using Pre-Trained Visual-Semantic Space](#paper-vs3-2023) (2023).
- [Panoptic Scene Graph Generation](#paper-psg2022) (2022).
- [SGTR: End-to-End Scene Graph Generation With Transformer](#paper-sgtr2022) (2022).
- [Towards Open-Vocabulary Scene Graph Generation with Prompt-Based Finetuning](#paper-ovprompt2022) (2022).

### Video and Temporal Scene Graphs

- [Graph it first! Enabling Reasoning on Long-form Egocentric Videos through Scene Graphs](#paper-ego-sg) (2026).
- [GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking](#paper-graphthinker) (2026).
- [UNO: Unifying One-stage Video Scene Graph Generation via Object-Centric Visual Representation Learning](#paper-uno) (2026).
- [DiffVsgg: Diffusion-Driven Online Video Scene Graph Generation](#paper-diffvsgg) (2025).
- [Unbiased Video Scene Graph Generation via Visual and Semantic Dual Debiasing](#paper-vsdd) (2025).
- [Action Scene Graphs for Long-Form Understanding of Egocentric Videos](#paper-easg) (2024).
- [OED: Towards One-stage End-to-End Dynamic Scene Graph Generation](#paper-oed) (2024).
- [Exploiting Long-Term Dependencies for Generating Dynamic Scene Graphs](#paper-dsg-detr) (2023).
- [Panoptic Video Scene Graph Generation](#paper-pvsg) (2023).
- [Unbiased Scene Graph Generation in Videos](#paper-tempura) (2023).
- [Spatial-Temporal Transformer for Dynamic Scene Graph Generation](#paper-sttran) (2021).
- [Action Genome: Actions As Compositions of Spatio-Temporal Scene Graphs](#paper-action-genome) (2020).
- [Video Visual Relation Detection](#paper-vidvrd) (2017).

### 3D Scene Graphs and Robotics

- [GraphWrit3R: End-to-End 3D Scene Graph Writing](#paper-g13) (2026).
- [Probabilistic Scene Graphs: Hierarchical Representation and Real-time System](#paper-probabilistic2026) (2026).
- [FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction](#paper-g12) (2025).
- [Open-Vocabulary Functional 3D Scene Graphs for Real-World Indoor Spaces](#paper-g11) (2025).
- [RelationField: Relate Anything in Radiance Fields](#paper-g10) (2025).
- [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](#paper-g08) (2024).
- [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](#paper-g06) (2024).
- [Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic SLAM in Dynamic Environments](#paper-g07) (2024).
- [Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships](#paper-g09) (2024).
- [Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization](#paper-g05) (2022).
- [SceneGraphFusion: Incremental 3D Scene Graph Prediction from RGB-D Sequences](#paper-g04) (2021).
- [3D Dynamic Scene Graphs: Actionable Spatial Perception with Places, Objects, and Humans](#paper-g03) (2020).
- [Learning 3D Semantic Scene Graphs from 3D Indoor Reconstructions](#paper-g02) (2020).
- [3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera](#paper-g01) (2019).

### Surgical Scene Graphs

- [ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes](#paper-protoflow) (2026).
- [Sterilizable Scene Graph Generation for Operating Rooms](#paper-sg-nca) (2026).
- [CAT-SG: A Large Dynamic Scene Graph Dataset for Fine-Grained Understanding of Cataract Surgery](#paper-cat-sg) (2025).
- [SG2VID: Scene Graphs Enable Fine-Grained Control for Video Synthesis](#paper-sg2vid) (2025).
- [SurGrID: Controllable Surgical Simulation via Scene Graph to Image Diffusion](#paper-surgrid) (2025).
- [Towards Holistic Surgical Scene Graph](#paper-holistic-surgical) (2025).
- [Advancing Surgical VQA with Scene Graph Knowledge](#paper-ssg-vqa) (2024).
- [Latent Graph Representations for Critical View of Safety Assessment](#paper-lg-cvs) (2024).
- [Optimizing Latent Graph Representations of Surgical Scenes for Zero-Shot Domain Transfer](#paper-surg-dg) (2024).
- [SANGRIA: Surgical Video Scene Graph Optimization for Surgical Workflow Prediction](#paper-sangria) (2024).
- [SGT++: Improved Scene Graph-Guided Transformer for Surgical Report Generation](#paper-sgt-plus-plus) (2024).
- [Dynamic Scene Graph Representation for Surgical Video](#paper-dynamic-surgical) (2023).
- [Encoding Surgical Videos as Latent Spatiotemporal Graphs for Object and Anatomy-Driven Reasoning](#paper-surg-stlg) (2023).
- [SGT: Scene Graph-Guided Transformer for Surgical Report Generation](#paper-sgt) (2022).
- [Learning and Reasoning with the Graph Structure Representation in Robotic Surgery](#paper-surg2020-graph) (2020).

### Operating-Room Scene Graphs

- [OR-Action: Multi-Role Video Understanding with Fine-Grained Actions](#paper-or-action) (2026).
- [SAGE-OR: Semi-supervised Adaptive Scene Graph Generation for Operating Rooms](#paper-sage-or) (2026).
- [TopoOR: A Unified Topological Scene Representation for the Operating Room](#paper-topoor) (2026).
- [EgoExOR: An Ego-Exo-Centric Operating Room Dataset for Surgical Activity Understanding](#paper-egoexor) (2025).
- [MM-OR: A Large Multimodal Operating Room Dataset for Semantic Understanding of High-Intensity Surgical Environments](#paper-mm-or) (2025).
- [Holistic OR domain modeling: a semantic scene graph approach](#paper-holistic-or) (2024).
- [ORacle: Large Vision-Language Models for Knowledge-Guided Holistic OR Domain Modeling](#paper-oracle) (2024).
- [S²Former-OR: Single-Stage Bi-Modal Transformer for Scene Graph Generation in OR](#paper-s2former-or) (2024).
- [Tri-modal Confluence with Temporal Dynamics for Scene Graph Generation in Operating Rooms](#paper-tritemp-or) (2024).
- [LABRAD-OR: Lightweight Memory Scene Graphs for Accurate Bimodal Reasoning in Dynamic Operating Rooms](#paper-labrad-or) (2023).
- [4D-OR: Semantic Scene Graphs for OR Domain Modeling](#paper-4d-or) (2022).

### Surveys

- [Decoding the Surgical Scene: A Scoping Review of Scene Graphs in Surgery](#paper-surg-scoping) (2026).

## Datasets and benchmarks

Follow each source for access requirements, annotation scope and dataset terms. A paper or repository link does not imply that every raw video, image or annotation is available without conditions.

- **Visual Genome** — Dense object, attribute and relationship annotations for image scene graphs. [[paper]](https://doi.org/10.1007/s11263-016-0981-7) [[data tool]](https://github.com/ranjaykrishna/visual_genome_python_driver)
- **VidVRD** — Video visual relationship detection with temporal object relations. [[paper]](https://doi.org/10.1145/3123266.3123380) [[repo]](https://github.com/VRU-NExT/Video-Relation-Detection)
- **Action Genome** — Human-object interactions represented as spatiotemporal scene graphs. [[paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Ji_Action_Genome_Actions_As_Compositions_of_Spatio-Temporal_Scene_Graphs_CVPR_2020_paper.html) [[repo]](https://github.com/JingweiJ/ActionGenome)
- **PSG** — Panoptic scene graphs with object and background-region masks. [[paper]](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/222_ECCV_2022_paper.php) [[repo]](https://github.com/Jingkang50/OpenPSG)
- **PVSG** — Panoptic video scene graphs with object tracks and temporal relations. [[paper]](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_Panoptic_Video_Scene_Graph_Generation_CVPR_2023_paper.html) [[repo]](https://github.com/LilyDaytoy/OpenPVSG)
- **3DSSG** — Semantic scene graphs associated with 3D indoor reconstructions. [[paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Wald_Learning_3D_Semantic_Scene_Graphs_From_3D_Indoor_Reconstructions_CVPR_2020_paper.html) [[data repo]](https://github.com/3DSSG/3DSSG.github.io)
- **EASG** — Action scene graphs for long-form egocentric video understanding. [[paper]](https://openaccess.thecvf.com/content/CVPR2024/html/Rodin_Action_Scene_Graphs_for_Long-Form_Understanding_of_Egocentric_Videos_CVPR_2024_paper.html) [[repo]](https://github.com/fpv-iplab/EASG)
- **CAT-SG** — Fine-grained dynamic scene graph annotations for cataract surgery. [[paper]](https://arxiv.org/abs/2506.21813) [[repo]](https://github.com/felixholm/CAT-SG)
- **4D-OR** — Multiview operating-room data with semantic scene graphs. [[paper]](https://arxiv.org/abs/2203.11937) [[repo]](https://github.com/egeozsoy/4D-OR)
- **MM-OR** — Multimodal operating-room scenes and semantic annotations. [[paper]](https://arxiv.org/abs/2503.02579) [[repo]](https://github.com/egeozsoy/MM-OR)
- **EgoExOR** — Ego-exocentric operating-room data for surgical activity understanding. [[paper]](https://arxiv.org/abs/2505.24287) [[repo]](https://github.com/ardamamur/EgoExOR)
- **SSG-VQA** — Surgical visual question answering informed by scene graph knowledge. [[paper]](https://arxiv.org/abs/2312.10251) [[repo]](https://github.com/CAMMA-public/SSG-VQA)
- **LLM Meets Scene Graph** — A benchmark for language-model scene graph understanding and generation. [[paper]](https://aclanthology.org/2025.acl-long.1036/)

## Surveys

- [Medical Image Analysis 2026] **Decoding the Surgical Scene: A Scoping Review of Scene Graphs in Surgery** [[paper]](https://doi.org/10.1016/j.media.2026.104083) [[notes]](docs/reading-guide.zh-CN.md#paper-surg-scoping)

## Tools and implementations

Selected author repositories. Their dependencies, checkpoints and licenses differ; consult each release before choosing a baseline. Repository availability was checked on the date recorded in [repository-checks.json](data/repository-checks.json). These checks are not reproduction results.

- [OpenPSG](https://github.com/Jingkang50/OpenPSG) — Panoptic scene graph generation baselines and evaluation.
- [OpenPVSG](https://github.com/LilyDaytoy/OpenPVSG) — Panoptic video scene graph annotations and baselines.
- [STTran](https://github.com/yrcong/STTran) — Dynamic scene graph generation with spatial-temporal transformers.
- [RelTR](https://github.com/yrcong/RelTR) — Transformer-based image scene graph generation.
- [Scene-Graph-Benchmark](https://github.com/KaihuaTang/Scene-Graph-Benchmark.pytorch) — Image scene graph baselines and debiasing methods.
- [Hydra](https://github.com/MIT-SPARK/Hydra) — 3D scene graph construction for robotic spatial perception.
- [ConceptGraphs](https://github.com/concept-graphs/concept-graphs) — Open-vocabulary 3D scene graphs for perception and planning.
- [Open3DSG](https://github.com/boschresearch/Open3DSG) — Open-vocabulary objects and relations in 3D scene graphs.
- [SSG-VQA](https://github.com/CAMMA-public/SSG-VQA) — Surgical QA resources and the released baseline interface.
- [SG2VID](https://github.com/MECLabTUDA/SG2VID) — Surgical graph-conditioned video generation resources.

## Reading notes and citations

- [Chinese reading notes](docs/reading-guide.zh-CN.md) explain what each paper does, its contribution and its limitations. Selected sections were reviewed for 93 entries; the SGT++ entry is explicitly limited to its abstract and metadata.
- [papers.json](data/papers.json) is the source of truth for the generated lists and notes. It also records publication status and the type of downstream evidence.
- [references.bib](references.bib) contains 87 citations obtained from source metadata. It is a partial export: no author names or missing citations were invented to match the catalogue size. An arXiv citation may use its preprint year while the list uses the final publication year.
- The collection links to original publications; it does not redistribute paper PDFs, extracted full text, model weights or datasets.

## Under review

[watchlist.json](data/watchlist.json) keeps one publication outside the main list pending further assessment of its methodological and experimental claims. Its presence is not a recommendation or a reproduced result.

## Contributing

Suggestions, corrections and new papers are welcome through issues or pull requests. Please follow [CONTRIBUTING.md](CONTRIBUTING.md), cite an original source, and distinguish a repository link from a verified runnable release.

## Acknowledgements

The catalogue layout was inspired by [Awesome AI Agents for Healthcare](https://github.com/FAN-529/Awesome-AI-Agents-for-Healthcare) and [Awesome Radiology Report Generation](https://github.com/FAN-529/Awesome-Radiology-Report-Generation), with thanks to their upstream maintainers [AgenticHealthAI](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) and [mk-runner](https://github.com/mk-runner/Awesome-Radiology-Report-Generation). All linked research belongs to its respective authors.

## License

Original catalogue text, reading notes and maintenance scripts are provided under the [MIT License](LICENSE). Linked papers, implementations, datasets and model weights retain their own copyrights and licenses.
