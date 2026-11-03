# Scene Graphs in Surgery

[Back to the main catalogue](../README.md)

**Updated: 2026-11-03. 52 selected entries:** 47 journal/main-conference publications (including one review), four workshop papers and one accepted conference paper. Two preprints without verified journal/conference publication are linked separately as a watchlist and are not counted in this selection or added to the main catalogue.

This topic prioritizes papers published in **IEEE TMI, Medical Image Analysis, CVPR, NeurIPS, MICCAI, ICRA, IEEE RA-L, TCSVT, JBHI, Information Fusion and npj Digital Medicine**. Closely related **IJCARS/IPCAI** publications are included as specialist references. Workshop papers and accepted-but-not-yet-presented work have their own section; venue inclusion is not a claim that every paper has equal evidence or reproducibility.

The starting point is Henriques et al.'s *Decoding the Surgical Scene*, especially Section 2.3 and Appendix A, supplemented with primary publication pages and author repositories. The review's 52-study scope includes isolated action-triplet recognition and other relational task models. Our 52-entry selection is a different set: it omits peripheral/lower-priority references and includes later published work. **It is not a transcription of all 52 studies and is not claimed exhaustive.**

## Contents

- [Review and scope](#review-and-scope)
- [Internal-view graph construction and context](#internal-view-graph-construction-and-context)
- [Temporal graphs, workflow and transfer](#temporal-graphs-workflow-and-transfer)
- [Reports, questions and referring segmentation](#reports-questions-and-referring-segmentation)
- [Graph-conditioned generation and state dynamics](#graph-conditioned-generation-and-state-dynamics)
- [External-view operating-room graphs](#external-view-operating-room-graphs)
- [Related action-triplet methods and benchmarks](#related-action-triplet-methods-and-benchmarks)
- [Workshop papers and accepted work](#workshop-papers-and-accepted-work)
- [Datasets and evaluation](#datasets-and-evaluation)
- [Release checks](#release-checks)
- [Reading routes](#reading-routes)
- [Preprint watchlist](#preprint-watchlist)
- [Curation notes](#curation-notes)

## How to read the list

- **Internal view** means endoscopic, robotic or microscope video of the operative field; **external view** means people/equipment across the operating room. Their sensing and labels differ substantially.
- **Instance scene graphs** connect observed objects; **concept/knowledge graphs** connect prior concepts; **latent multimodal graphs** connect learned features. These representations should not be treated as interchangeable.
- **Action-triplet recognition** can predict instrument-verb-target presence without locating each target or connecting all instances. It is listed as related task work where appropriate.
- **Graph-conditioned generation** can synthesize plausible images/videos without recovering the original video. Reconstruction fidelity and downstream utility answer different questions.
- **Public source** means inspected repository files, not a successfully reproduced experiment. Unless stated otherwise, this update did not install models, download large checkpoints or run these papers.

## Review and scope

<a id="paper-surg-scoping"></a>

- **Decoding the Surgical Scene: A Scoping Review of Scene Graphs in Surgery** — Medical Image Analysis 2026. [[paper]](https://doi.org/10.1016/j.media.2026.104083)

  Maps surgical scene-graph construction, uses and limitations, including internal-view interactions and external-view OR modeling. Its broad scope also includes isolated triplets and other relational task models.

  **Data/task:** 52 studies mapped in the supplied review. **Release:** Published MedIA review; reference and appendix entries were independently screened before inclusion here.

## Internal-view graph construction and context

<a id="paper-surg2020-graph"></a>

- **Learning and Reasoning with the Graph Structure Representation in Robotic Surgery** — MICCAI 2020. [[paper]](https://arxiv.org/abs/2007.03357) [[repo]](https://github.com/mobarakol/Surgical_SceneGraph_Generation)

  Introduces visual-semantic graph reasoning over surgical instruments and a region of interest to predict tool-tissue interactions. An early surgical scene graph baseline.

  **Data/task:** Robotic surgery; annotated EndoVis 2018. **Release:** Source and training/evaluation entries present; no root license file found.

<a id="paper-global-mtl"></a>

- **Global-Reasoned Multi-Task Learning Model for Surgical Scene Understanding** — IEEE RA-L 2022. [[paper]](https://doi.org/10.1109/LRA.2022.3146544) [[repo]](https://github.com/lalithjets/Global-reasoned-multi-task-model)

  Shares visual features between instrument segmentation and interaction-graph prediction, adding global reasoning to local node-pair reasoning. Useful precedent for retaining context beyond isolated objects.

  **Data/task:** EndoVis 2018. **Release:** Source and evaluation instructions present; preprocessing/instrument labels remain marked to be released; no root license file found.

<a id="paper-gradient-features"></a>

- **Rethinking Feature Extraction: Gradient-Based Localized Feature Extraction for End-To-End Surgical Downstream Tasks** — IEEE RA-L 2022. [[paper]](https://doi.org/10.1109/LRA.2022.3221310)

  Uses gradient-based localization to extract local features for surgical downstream models, reducing dependence on a separate detector and feature-extraction pipeline. A graph-construction reference, rather than a new complete graph dataset.

  **Data/task:** Surgical interaction recognition and report generation. **Release:** No author implementation verified in this update.

<a id="paper-task-aware-mtl"></a>

- **Task-Aware Asynchronous Multi-Task Model with Class Incremental Contrastive Learning for Surgical Scene Understanding** — IJCARS 2023. [[paper]](https://doi.org/10.1007/s11548-022-02800-2)

  Jointly predicts tool-tissue interactions and surgical reports with asynchronous task optimization and class-incremental contrastive learning. Relevant to adaptation across instruments and surgical domains.

  **Data/task:** EndoVis 2018 and a target robotic-surgery domain, including TORS. **Release:** No author implementation verified in this update.

<a id="paper-lg-cvs"></a>

- **Latent Graph Representations for Critical View of Safety Assessment** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2023.3333034) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph)

  Encodes object appearance, semantics and spatial relations in a latent graph for assessing the three critical-view-of-safety criteria. The released implementation also retains a pooled global image feature.

  **Data/task:** Endoscapes; laparoscopic cholecystectomy. **Release:** Shared SurgLatentGraph source/configs available; final task checkpoints are still advertised as coming soon in the upstream README.

<a id="paper-concept-graph"></a>

- **Concept Graph Neural Networks for Surgical Video Understanding** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2023.3299518)

  Combines a prior concept/knowledge graph with temporal visual analysis for CVS assessment, surgical difficulty grading and action-triplet recognition. Its nodes represent concepts; this is different from an exported graph of all observed object instances.

  **Data/task:** CVS100, Parkland grading and action-triplet benchmarks. **Release:** No author implementation verified in this update.

<a id="paper-itidnet"></a>

- **Instrument-Tissue Interaction Detection Framework for Surgical Video Understanding** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2024.3381209)

  Extends an interaction to a five-part record: instrument class and box, tissue class and box, and action class. Uses snippet context, spatial correspondence and temporal graph connections to model interactions across frames.

  **Data/task:** PhacoQ cataract and CholecQ cholecystectomy datasets. **Release:** No author implementation verified in this update.

<a id="paper-landmark-graph"></a>

- **Knowledge-Driven Framework for Anatomical Landmark Annotation in Laparoscopic Surgery** — IEEE TMI 2025. [[paper]](https://doi.org/10.1109/TMI.2025.3529294)

  Encodes tool-anatomy topology, explainable node attributes and temporal landmark-state changes in a graph. Attention-based message passing supports landmark annotation and tracking under changing tissue appearance.

  **Data/task:** Clinical laparoscopic cholecystectomy dataset. **Release:** No author implementation verified in this update.

<a id="paper-holistic-surgical"></a>

- **Towards Holistic Surgical Scene Graph** — MICCAI 2025. [[paper]](https://papers.miccai.org/miccai-2025/paper/2642_paper.pdf) [[repo]](https://github.com/ailab-kyunghee/SSG-Com)

  Adds refined instrument categories, instrument-verb-target relations and hand identity to Endoscapes, and learns a more detailed surgical scene graph. A close comparison for enriching the existing LG-CVS representation.

  **Data/task:** Endoscapes-SG201. **Release:** Source and additional annotation download linked; no root license file found and one advertised triplet configuration is missing. See release checks.

## Temporal graphs, workflow and transfer

<a id="paper-surg-stlg"></a>

- **Encoding Surgical Videos as Latent Spatiotemporal Graphs for Object and Anatomy-Driven Reasoning** — MICCAI 2023. [[paper]](https://arxiv.org/abs/2312.06829) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph)

  Links latent frame graphs over time for object- and anatomy-aware surgical reasoning. Supplies graph-based routes to CVS assessment, phase recognition and triplet recognition in the same codebase.

  **Data/task:** Endoscapes, Cholec80 and CholecT50. **Release:** Source, temporal configs and saved-graph dataset interfaces present in SurgLatentGraph; upstream final checkpoints not confirmed released.

<a id="paper-surg-dg"></a>

- **Optimizing Latent Graph Representations of Surgical Scenes for Unseen Domain Generalization** — IPCAI / IJCARS 2024. [[paper]](https://doi.org/10.1007/s11548-024-03121-2) [[repo]](https://github.com/CAMMA-public/SurgLatentGraph)

  Optimizes latent graph representations to improve generalization to unseen domains. Relevant to learning reusable object/context features and evaluating procedure or institution shifts.

  **Data/task:** Surgical-scene domain-generalization experiments. **Release:** Shared SurgLatentGraph source/configs present; check paper-specific target protocol and data access.

<a id="paper-cat-sg"></a>

- **CAT-SG: A Large Dynamic Scene Graph Dataset for Fine-Grained Understanding of Cataract Surgery** — MICCAI 2025. [[paper]](https://papers.miccai.org/miccai-2025/0133-Paper1687.html) [[repo]](https://github.com/felixholm/CAT-SG)

  Introduces fine-grained dynamic graphs for cataract surgery, including entities, spatial/semantic relations, step and technique labels. Geometry is derived from segmentation predictions and includes pseudolabels.

  **Data/task:** 50 CATARACTS videos; graph annotations at 5 fps. **Release:** Annotations and a PyTorch Geometric loader present; the checked repository does not contain the full CatSGG/GATv2 training pipelines.

<a id="paper-protoflow"></a>

- **ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes** — IPCAI / IJCARS 2026. [[paper]](https://doi.org/10.1007/s11548-026-03697-x)

  Learns recurring dynamic-graph prototypes with self-supervised graph representation learning and prototype-based fine-tuning, making workflow patterns easier to inspect.

  **Data/task:** CAT-SG; cataract workflow and technique analysis. **Release:** No author implementation verified in this update.

<a id="paper-instrument-anticipation"></a>

- **Towards Multimodal Graph Neural Networks for Surgical Instrument Anticipation** — IJCARS 2024. [[paper]](https://doi.org/10.1007/s11548-024-03226-8)

  Builds a multimodal knowledge graph from imaging and non-imaging signals, then uses a spatiotemporal GNN to anticipate instruments. Useful for defining node state and multimodal temporal context.

  **Data/task:** In-house laparoscopic surgery data. **Release:** No author implementation verified in this update.

<a id="paper-grad-workflow"></a>

- **Multimodal Graph Representation Learning for Robust Surgical Workflow Recognition with Adversarial Feature Disentanglement** — Information Fusion 2025. [[paper]](https://doi.org/10.1016/j.inffus.2025.103290)

  Combines vision and robotic kinematics through graph message modeling, adversarial modality alignment and a contextual decoder for robust workflow recognition. A multimodal latent-graph reference, not a dataset of fully named visual relations.

  **Data/task:** MISAW and CUHK-MRG. **Release:** Publication verified; no author implementation verified in this update.

## Reports, questions and referring segmentation

<a id="paper-sgt"></a>

- **SGT: Scene Graph-Guided Transformer for Surgical Report Generation** — MICCAI 2022. [[paper]](https://conferences.miccai.org/2022/papers/463-Paper2204.html) [[repo]](https://github.com/ccccchenllll/SGT_master)

  Uses relation-driven attention and graph-induced local attention to improve surgical report generation. A downstream reference for converting structured relationships into language.

  **Data/task:** Robotic nephrectomy reports derived from surgical images. **Release:** Training/evaluation code and a weight link present; processed data require contacting the author; no root license file found.

<a id="paper-dynamic-report"></a>

- **Dynamic Interactive Relation Capturing via Scene Graph Learning for Robotic Surgical Report Generation** — ICRA 2023. [[paper]](https://doi.org/10.1109/ICRA48891.2023.10160647)

  Learns interactive relationships through relational exploration and interaction-perception modules, then uses them to generate surgical reports.

  **Data/task:** Robotic surgical report generation. **Release:** No author implementation verified in this update.

<a id="paper-sgt-plus-plus"></a>

- **SGT++: Improved Scene Graph-Guided Transformer for Surgical Report Generation** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2023.3335909) **Abstract reviewed only.**

  Extends scene-graph-guided report generation by learning explicit and implicit instrument-tissue interactions. Retained as a published downstream reference; the original catalogue had only reviewed its abstract.

  **Data/task:** Robotic surgery report generation. **Release:** Publisher abstract checked; no author implementation verified in this update. The SGT repository is not automatically evidence of an SGT++ release.

<a id="paper-ssg-vqa"></a>

- **Advancing Surgical VQA with Scene Graph Knowledge** — IPCAI / IJCARS 2024. [[paper]](https://doi.org/10.1007/s11548-024-03141-y) [[repo]](https://github.com/CAMMA-public/SSG-VQA)

  Builds surgical QA pairs using scene graphs and incorporates geometric scene knowledge into a VQA model. Useful for spatial/action questions; the released model also consumes image-derived visual features.

  **Data/task:** SSG-VQA; Cholec80-derived scenes. **Release:** Source, QA/graph downloads and feature-extraction scripts present. A graph-only replacement requires an adapter and a separate experiment.

<a id="paper-vis-net"></a>

- **Video-Instrument Synergistic Network for Referring Video Instrument Segmentation in Robotic Surgery** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2024.3426953) [[repo]](https://github.com/whq-xxh/RSVIS)

  Combines video-level and instrument-level information, including relation-aware modeling, for segmenting the instrument referred to by a text description. This is a related downstream task with dense spatial output.

  **Data/task:** EndoVis-RS17 and EndoVis-RS18. **Release:** Preliminary source release present; processed datasets require author-approved access. Dense segmentation cannot be assumed recoverable from symbolic triples alone.

## Graph-conditioned generation and state dynamics

<a id="paper-surgrid"></a>

- **SurGrID: Controllable Surgical Simulation via Scene Graph to Image Diffusion** — IPCAI / IJCARS 2025. [[paper]](https://doi.org/10.1007/s11548-025-03397-y) [[repo]](https://github.com/MECLabTUDA/SurGrID)

  Pretrains graph embeddings against local/global image and segmentation information, then conditions diffusion on scene graphs for controllable surgical image synthesis.

  **Data/task:** CaDIS cataract surgery. **Release:** Source/configs and hosted data/checkpoint links present; license file present. Downloaded weights and complete execution were not checked.

<a id="paper-sg2vid"></a>

- **SG2VID: Scene Graphs Enable Fine-Grained Control for Video Synthesis** — MICCAI 2025. [[paper]](https://papers.miccai.org/miccai-2025/0828-Paper0234.html) [[repo]](https://github.com/MECLabTUDA/SG2VID)

  Uses graph conditioning to control surgical video layout, object size and motion, and demonstrates generated-data use for phase recognition. Supports graph-only and graph-plus-initial-frame generation configurations.

  **Data/task:** CATARACTS, Cataract-1K and Cholec80. **Release:** Graph encoder, training/sampling source and hosted data/checkpoint links present. Generation fidelity is not a proof that all original video information was retained.

<a id="paper-swomo"></a>

- **SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation** — MICCAI 2026. [[paper]](https://papers.miccai.org/miccai-2026/1023-Paper2681.html) [[repo]](https://github.com/MECLabTUDA/SWoMo)

  Combines a rule-based simulator and scene graphs for motion/tool-tissue dynamics with diffusion for realistic visual synthesis. A reference for representing state changes and constraining generated interactions.

  **Data/task:** Cataract-1K and cataract-surgery simulation. **Release:** Source/configs and hosted data/checkpoint links present; real-video manual masks and extra annotations require author contact; no root license file found.

<a id="paper-hierasurg"></a>

- **HieraSurg: Hierarchy-Aware Diffusion Model for Surgical Video Generation** — MICCAI 2025. [[paper]](https://papers.miccai.org/miccai-2025/0412-Paper0550.html) [[repo]](https://github.com/DiegoBiagini/HieraSurg)

  Separates semantic evolution from appearance: phase/triplet information guides future segmentation maps, which a second diffusion stage turns into video. An adjacent hierarchy/layout reference, rather than a full scene graph generator.

  **Data/task:** Cholec80 and CholecT50. **Release:** Real source files present, but README training/inference documentation and weights retain TODOs. The advertised scripts/train.py and scripts/infer.py paths are absent.

## External-view operating-room graphs

<a id="paper-4d-or"></a>

- **4D-OR: Semantic Scene Graphs for OR Domain Modeling** — MICCAI 2022. [[paper]](https://arxiv.org/abs/2203.11937) [[repo]](https://github.com/egeozsoy/4D-OR)

  Introduces multiview RGB-D operating-room data and semantic graphs of people, tools and equipment. Establishes external-view OR scene graph prediction.

  **Data/task:** 4D-OR; simulated surgical procedures. **Release:** Source/annotations and data-access instructions present; raw data have a separate access process.

<a id="paper-labrad-or"></a>

- **LABRAD-OR: Lightweight Memory Scene Graphs for Accurate Bimodal Reasoning in Dynamic Operating Rooms** — MICCAI 2023. [[paper]](https://arxiv.org/abs/2303.13293) [[repo]](https://github.com/egeozsoy/LABRAD-OR)

  Adds lightweight memory to bimodal OR scene graph reasoning, using temporal context to improve prediction in dynamic, occluded scenes.

  **Data/task:** 4D-OR. **Release:** Public source and model/data instructions; RGB-D/point-cloud dependencies require a separate environment.

<a id="paper-holistic-or"></a>

- **Holistic OR domain modeling: a semantic scene graph approach** — IJCARS 2024. [[paper]](https://doi.org/10.1007/s11548-023-03022-w) [[repo]](https://github.com/egeozsoy/4D-OR) Journal extension.

  Journal extension of the 4D-OR line, using semantic scene graphs for holistic operating-room domain modeling. Keep its relationship to the conference paper explicit.

  **Data/task:** 4D-OR. **Release:** Shares the 4D-OR author repository; a journal extension is not an independent dataset.

<a id="paper-oracle"></a>

- **ORacle: Large Vision-Language Models for Knowledge-Guided Holistic OR Domain Modeling** — MICCAI 2024. [[paper]](https://arxiv.org/abs/2404.07031) [[repo]](https://github.com/egeozsoy/ORacle)

  Uses a large vision-language model with surgical knowledge for holistic OR scene graph prediction. A reference for combining language priors with visual evidence.

  **Data/task:** 4D-OR. **Release:** Public source with LLaVA-based training/inference components; data, model and third-party terms remain separate.

<a id="paper-tritemp-or"></a>

- **Tri-modal Confluence with Temporal Dynamics for Scene Graph Generation in Operating Rooms** — MICCAI 2024. [[paper]](https://papers.miccai.org/miccai-2024/802-Paper0281.html) [[repo]](https://github.com/RascalGdd/TriTemp-OR)

  Fuses images, point clouds and language together with temporal dynamics to generate OR graphs. Relevant when additional modalities can resolve ambiguous relationships.

  **Data/task:** 4D-OR. **Release:** Source and train/infer commands present; processed data and pretrained DETR are externally hosted; no root license file found.

<a id="paper-s2former-or"></a>

- **S²Former-OR: Single-Stage Bi-Modal Transformer for Scene Graph Generation in OR** — IEEE TMI 2025; early access 2024. [[paper]](https://doi.org/10.1109/TMI.2024.3444279) [[repo]](https://github.com/PJLallen/S2Former-OR)

  Uses a single-stage bimodal transformer for OR scene graph generation, combining RGB appearance and 3D information to reduce the cost of a multistage pipeline.

  **Data/task:** 4D-OR. **Release:** Source and train/infer commands present; requires PointNet++ and processed RGB/point-cloud data. Journal issue year is 2025; early access was 2024.

<a id="paper-mm-or"></a>

- **MM-OR: A Large Multimodal Operating Room Dataset for Semantic Understanding of High-Intensity Surgical Environments** — CVPR 2025. [[paper]](https://arxiv.org/abs/2503.02579) [[repo]](https://github.com/egeozsoy/MM-OR)

  Adds RGB-D, detailed views, audio, speech, robot logs and tracking to an OR benchmark, with semantic graphs and downstream labels. MM2SG uses multiple modalities to predict scene graphs.

  **Data/task:** MM-OR; simulated OR procedures. **Release:** Source, downstream-data generation commands and hosted checkpoint links present; raw-data access follows the authors' procedure.

<a id="paper-egoexor"></a>

- **EgoExOR: An Ego-Exo-Centric Operating Room Dataset for Surgical Activity Understanding** — NeurIPS Datasets and Benchmarks 2025. [[paper]](https://proceedings.neurips.cc/paper_files/paper/2025/file/5e3ffa2c53dce23986ca0f8d1d2bbc7e-Paper-Datasets_and_Benchmarks_Track.pdf) [[repo]](https://github.com/ardamamur/EgoExOR)

  Combines first- and third-person OR observations with graph annotations of entities and relationships. Extends graph understanding to complementary viewpoints and wearable sensing.

  **Data/task:** EgoExOR; emulated spine procedures. **Release:** Annotations, source and hosted model links present; an HQ dataset update is linked separately.

<a id="paper-topoor"></a>

- **TopoOR: A Unified Topological Scene Representation for the Operating Room** — MICCAI 2026. [[paper]](https://papers.miccai.org/miccai-2026/1068-Paper2412.html) [[repo]](https://github.com/wngTn/TopoOR)

  Replaces exclusively pairwise relationships with higher-order topological cells that can represent group interactions while retaining modality structure. Evaluates sterility breaches, robot phases and next actions.

  **Data/task:** MM-OR. **Release:** Model/data modules, training/evaluation scripts and a packed-data/checkpoint download script present; MM-OR data access remains separate.

<a id="paper-orqa"></a>

- **Specialized Foundation Models for Intelligent Operating Rooms** — npj Digital Medicine 2026. [[paper]](https://doi.org/10.1038/s41746-026-02631-4) [[repo]](https://github.com/egeozsoy/ORQA)

  Unifies visual, auditory and structured OR data in a question-answering foundation model. Relevant to graph-grounded multimodal questions, but its published input is broader than an exported graph alone.

  **Data/task:** Multiple OR datasets and ORQA benchmark. **Release:** Source, benchmark and model links present; adapting enhanced surgical graphs would require an explicit input interface.

<a id="paper-or-action"></a>

- **OR-Action: Multi-Role Video Understanding with Fine-Grained Actions** — MICCAI 2026. [[paper]](https://papers.miccai.org/miccai-2026/0741-Paper4727.html)

  Derives fine-grained, role-specific temporal action segments from ground-truth graph changes and benchmarks graph-based versus video-based understanding. Reports limitations of current graph temporal modeling; useful for choosing action-level evaluation.

  **Data/task:** Ego-exocentric OR activity data. **Release:** Official conference page has no code/dataset link; no author implementation verified in this update. Its main proposed action model is vision based.

## Related action-triplet methods and benchmarks

<a id="paper-tripnet"></a>

- **Recognition of Instrument-Tissue Interactions in Endoscopic Videos via Action Triplets** — MICCAI 2020. [[paper]](https://doi.org/10.1007/978-3-030-59716-0_35)

  Formalizes instrument-verb-target action-triplet recognition in endoscopic video. Establishes the vocabulary and task that later graph methods extend.

  **Data/task:** CholecT40. **Release:** Task/dataset source verified; no separate author implementation verified in this update.

<a id="paper-rendezvous"></a>

- **Rendezvous: Attention Mechanisms for the Recognition of Surgical Action Triplets in Endoscopic Videos** — Medical Image Analysis 2022. [[paper]](https://doi.org/10.1016/j.media.2022.102433) [[repo]](https://github.com/CAMMA-public/rendezvous)

  Models dependencies between instruments, verbs and targets using attention to recognize surgical action triplets. A strong published task reference; a list of predicted triplets is not automatically a connected full scene graph.

  **Data/task:** CholecT50. **Release:** PyTorch and TensorFlow implementations present; the decoder expects visual spatial/component features, not an arbitrary graph vector.

<a id="paper-sirnet"></a>

- **SIRNet: Fine-Grained Surgical Interaction Recognition** — IEEE RA-L 2022. [[paper]](https://doi.org/10.1109/LRA.2022.3148454) [[repo]](https://github.com/cynerelee/SIRNet)

  Uses fine-grained interaction modeling to recognize surgical action triplets. Included as a related relation-recognition baseline, rather than a full graph export method.

  **Data/task:** Laparoscopic action-triplet recognition. **Release:** Model/training/test source and a license file present; README gives only minimal environment guidance.

<a id="paper-forest-gcn"></a>

- **Forest Graph Convolutional Network for Surgical Action Triplet Recognition in Endoscopic Videos** — IEEE TCSVT 2022. [[paper]](https://doi.org/10.1109/TCSVT.2022.3191838)

  Combines a classification forest and GCN to model associations within and between action triplets, addressing fine-grained multilabel recognition and class imbalance.

  **Data/task:** Endoscopic surgical action-triplet recognition. **Release:** No author implementation verified in this update.

<a id="paper-mt-fist"></a>

- **MT-FiST: A Multi-Task Fine-Grained Spatial-Temporal Framework for Surgical Action Triplet Recognition** — IEEE JBHI 2023. [[paper]](https://doi.org/10.1109/JBHI.2023.3299321) [[repo]](https://github.com/Lycus99/MT-FiST)

  Uses multitask fine-grained spatial/temporal modeling to recognize action triplets. Useful for temporal task-head design and comparison with relational representations.

  **Data/task:** CholecT50. **Release:** Source and externally hosted model/feature links present; no root license file found.

<a id="paper-rit"></a>

- **Rendezvous in Time: An Attention-Based Temporal Fusion Approach for Surgical Triplet Recognition** — IPCAI / IJCARS 2023. [[paper]](https://doi.org/10.1007/s11548-023-02914-1) [[repo]](https://github.com/CAMMA-public/rendezvous-in-time)

  Adds attention-based temporal fusion to Rendezvous, emphasizing current/past-frame evidence for verbs and smoother triplet predictions.

  **Data/task:** CholecT45 cross-validation protocol. **Release:** Training/evaluation source and scripts present; data access and matching split are required.

<a id="paper-mcit-ig"></a>

- **Surgical Action Triplet Detection by Mixed Supervised Learning of Instrument-Tissue Interactions** — MICCAI 2023. [[paper]](https://conferences.miccai.org/2023/papers/629-Paper2331.html) [[repo]](https://github.com/CAMMA-public/mcit-ig)

  Associates localized instruments with targets and verbs using a two-stage transformer and interaction graph, learning from mixed weak/pseudo supervision.

  **Data/task:** CholecT50; localized action-triplet detection. **Release:** The checked author repository has only four files and no training/model implementation, despite README commands. Private localization-test labels are also listed as unreleased.

<a id="paper-mt4mtl-kd"></a>

- **MT4MTL-KD: A Multi-Teacher Knowledge Distillation Framework for Triplet Recognition** — IEEE TMI 2024. [[paper]](https://doi.org/10.1109/TMI.2023.3345736)

  Distills knowledge from multiple teachers into a multitask action-triplet recognizer. A reference for learning a smaller downstream model; this is not scene graph generation by itself.

  **Data/task:** Surgical action-triplet recognition. **Release:** No author implementation verified in this update.

<a id="paper-itg-trip"></a>

- **Instrument-Tissue-Guided Surgical Action Triplet Detection via Textual-Temporal Trail Exploration** — IEEE TMI 2025. [[paper]](https://doi.org/10.1109/TMI.2025.3590457) [[repo]](https://github.com/PJLallen/ITG-Trip)

  Uses instrument/tissue pseudo-localization, visual-language priors and a Mamba/Transformer temporal decoder to detect localized surgical triplets. Relevant to richer action edges and rare interactions.

  **Data/task:** CholecT50. **Release:** Model, dataset and training files present; custom hoi_annotation-format data conversion and causal-conv/Mamba dependencies require inspection before reproduction.

<a id="paper-cholectriplet2021"></a>

- **CholecTriplet2021: A Benchmark Challenge for Surgical Action Triplet Recognition** — Medical Image Analysis 2023. [[paper]](https://doi.org/10.1016/j.media.2023.102803) [[repo]](https://github.com/CAMMA-public/cholect50)

  Benchmarks instrument-verb-target presence recognition and provides common evaluation context for triplet methods. Included as a benchmark paper, not a new general-purpose scene graph representation.

  **Data/task:** CholecTriplet2021. **Release:** Official CholecT50 repository documents dataset versions, access forms and challenge resources.

<a id="paper-cholectriplet2022"></a>

- **CholecTriplet2022: Show Me a Tool and Tell Me the Triplet - An Endoscopic Vision Challenge for Surgical Action Triplet Detection** — Medical Image Analysis 2023. [[paper]](https://doi.org/10.1016/j.media.2023.102888) [[repo]](https://github.com/CAMMA-public/cholect50)

  Moves the benchmark toward localized triplet detection: recognizing an action must be associated with the correct instrument instance. Useful for testing whether graph edges preserve instance-specific information.

  **Data/task:** CholecTriplet2022. **Release:** Official repository describes access and annotation differences; challenge test annotations must not be assumed fully public.

## Workshop papers and accepted work

<a id="paper-dynamic-surgical"></a>

- **Dynamic Scene Graph Representation for Surgical Video** — ICCV Workshops (SG2RL) 2023. [[paper]](https://openaccess.thecvf.com/content/ICCV2023W/SG2RL/html/Holm_Dynamic_Scene_Graph_Representation_for_Surgical_Video_ICCVW_2023_paper.html)

  Represents surgical videos as dynamic graphs and studies temporal graph information for cataract workflow prediction. A directly relevant workshop precursor to later cataract graph datasets.

  **Data/task:** CaDIS and CATARACTS. **Release:** Workshop paper verified; no author implementation verified in this update.

<a id="paper-sangria"></a>

- **SANGRIA: Surgical Video Scene Graph Optimization for Surgical Workflow Prediction** — GRAIL @ MICCAI 2024. [[paper]](https://arxiv.org/abs/2407.20214)

  Optimizes surgical video scene graphs with weak supervision for workflow prediction. Relevant to improving graph quality without densely annotating every relationship.

  **Data/task:** CATARACTS. **Release:** GRAIL/MICCAI workshop paper, not the MICCAI main track; no author implementation verified in this update.

<a id="paper-visage"></a>

- **VISAGE: Video Synthesis Using Action Graphs for Surgery** — MICCAI Workshops 2024; proceedings 2025. [[paper]](https://doi.org/10.1007/978-3-031-77610-6_14)

  Conditions future surgical video synthesis on an initial frame and action-graph triplets. An earlier graph-conditioned video-generation reference.

  **Data/task:** Laparoscopic cholecystectomy video. **Release:** MICCAI 2024 workshop paper, published in the 2025 proceedings; no author implementation verified in this update.

<a id="paper-sg-nca"></a>

- **Sterilizable Scene Graph Generation for Operating Rooms** — SafeSurg @ MICCAI Workshops 2026. [[paper]](https://papers.miccai.org/miccai-2026-sat/SafeSurg_001.html) [[repo]](https://github.com/MECLabTUDA/SG-NCA)

  Uses lightweight neural cellular automata for surgical scene graph generation with deployment on low-power devices. Relevant to efficient graph extraction.

  **Data/task:** Cataract and cholecystectomy data. **Release:** SafeSurg/MICCAI workshop paper; source and analysis scripts present; no root license file found. Its title does not mean it detects sterile-field breaches.

<a id="paper-sage-or"></a>

- **SAGE-OR: Semi-supervised Adaptive Scene Graph Generation for Operating Rooms** — BMVC 2026; accepted. [[paper]](https://arxiv.org/abs/2608.15336) [[repo]](https://github.com/TheFourthKaramazov/SAGE-OR)

  Caches frozen foundation-model features and trains a lightweight graph transformer for OR relational reasoning. Prompt-based extra context entities are particularly relevant to enriching a detection-limited graph.

  **Data/task:** 4D-OR; RGB-driven graph generation. **Release:** BMVC 2026 accepted; programme lists 25 November. Source/cache/checkpoint links present; DINOv3 access is gated. Reported graph-head speed excludes offline feature extraction.

## Datasets and evaluation

- **Endoscapes** — object/segmentation labels and three CVS criteria, including a temporal release. It does not supply a dense, clinically complete relation graph. [Official data](https://github.com/CAMMA-public/Endoscapes). The temporal release is at 1 fps, whereas CVS labels are sampled every five seconds.
- **Endoscapes-SG201** — refined instrument labels, triplets and operator/assistant hand identities. [Author release](https://github.com/ailab-kyunghee/SSG-Com#-dataset-endoscapes-sg201). Additional labels are valuable, but the implementation caveats below still apply.
- **CAT-SG** — dynamic cataract graphs plus workflow/technique labels. [Annotations and loader](https://github.com/felixholm/CAT-SG). Underlying CATARACTS videos are acquired separately. Frame geometry contains segmentation-derived pseudolabels; step/technique answers must not be included as model inputs when predicting those same labels.
- **CholecT40/T45/T50 and CholecTriplet challenges** — distinguish frame-level triplet presence, instrument boxes and box-triplet associations. [Formats and access](https://github.com/CAMMA-public/cholect50). A benchmark's complete private test set is not guaranteed by the public training-data release.
- **SSG-VQA** — graph-informed surgical QA and image-derived features. [Resources](https://github.com/CAMMA-public/SSG-VQA). Keep graph construction independent of the questions/answers used for evaluation.
- **4D-OR / MM-OR / EgoExOR** — external-view multiview/multimodal graphs. [4D-OR](https://github.com/egeozsoy/4D-OR), [MM-OR](https://github.com/egeozsoy/MM-OR), [EgoExOR](https://github.com/ardamamur/EgoExOR). These sources include simulated/emulated procedures, and should not be described as broad prospective clinical validation.
- **Procedure transfer** — CAT-SG offers an eye-surgery graph domain; [AutoLaparo](https://autolaparo.github.io/) offers hysterectomy phase data, with a [MICCAI 2022 paper and author repository](https://github.com/ziyiwangx/AutoLaparo). AutoLaparo is an auxiliary downstream dataset, not already an annotated scene graph benchmark. Anatomy labels/task heads need adaptation.

**Overlap matters.** Endoscapes, Cholec80 and CholecT50 contain overlapping procedures. Use [CAMMA's overlap inventory](https://github.com/CAMMA-public/camma_dataset_overlaps) before a cross-dataset claim. For example, Endoscapes training cases 1, 2, 3, 4 and 7, and validation case 121, overlap videos in the canonical Cholec80 test set. Removing leakage may require retraining the source encoder, not just changing the target head.

For a reusable graph dataset, report graph-generation quality, downstream task performance, actual serialized storage and the exact information allowed at inference. Evaluate on a frozen predicted graph export; compare separately with human graphs and graphs extracted using ground-truth masks. A downstream model originally consuming RGB features needs an adapter or retraining before it can evaluate a different graph representation.

## Release checks

The author repositories below were inspected on **2026-11-03**. Checks cover README instructions, repository trees, license-file presence and selected model/data interfaces. They are source-release observations, not end-to-end reproduction certificates. External Drive/Hugging Face links were found in the source; their full binary contents and download permissions were not validated here.

- **LG-CVS / SV2LSTG / LG-DG** — Model, dataset and task configuration files are present. The README still marks final task checkpoints as coming soon. Uses MMDetection/MMEngine/DGL and image-derived node/edge/global features; task-specific graph inference is not a universal adapter. Sources: [README.md](https://github.com/CAMMA-public/SurgLatentGraph/blob/8e521f07ffe431926ae00f273dce649ebf0cdbfa/README.md), [model/lg.py](https://github.com/CAMMA-public/SurgLatentGraph/blob/8e521f07ffe431926ae00f273dce649ebf0cdbfa/model/lg.py), [datasets/custom_loading.py](https://github.com/CAMMA-public/SurgLatentGraph/blob/8e521f07ffe431926ae00f273dce649ebf0cdbfa/datasets/custom_loading.py).

- **SSG-Com / Endoscapes-SG201** — Additional annotation link and real model/config files are present. The README calls configs/models/faster_rcnn/lg_ds_faster_rcnn_pplus_triplet_full.py, which is absent; the tree contains lg_ds_faster_rcnn_ssg201_triplet.py instead. This does not establish equivalence between those configs. No root license file was found. Sources: [README.md](https://github.com/ailab-kyunghee/SSG-Com/blob/40522803ca75304a9dbf2c7759d1525eed931235/README.md).

- **CAT-SG** — The checked release contains JSON graph annotations and dataloader.py. It does not contain complete CatSGG or GATv2 baseline training/evaluation source. The README states CC BY-NC 4.0 for the dataset; no separate root LICENSE file was found. Sources: [README.md](https://github.com/felixholm/CAT-SG/blob/bf626d7038b2764c86a78e0e56519682287d4b9c/README.md), [dataloader.py](https://github.com/felixholm/CAT-SG/blob/bf626d7038b2764c86a78e0e56519682287d4b9c/dataloader.py).

- **SSG-VQA** — Training/test code, graph/QA downloads and visual-feature extraction are present. The inspected loader opens image-derived HDF5 visual features, and test.py passes visual_features to the model. Graph-to-VQA adaptation requires engineering and training. Sources: [test.py](https://github.com/CAMMA-public/SSG-VQA/blob/e242fae711b6889e6e73c3580432514c83a3ecf8/test.py), [utils/dataloaderClassification.py](https://github.com/CAMMA-public/SSG-VQA/blob/e242fae711b6889e6e73c3580432514c83a3ecf8/utils/dataloaderClassification.py).

- **Rendezvous** — Published task implementation with PyTorch/TensorFlow alternatives. The PyTorch network works on spatial visual features and component activations, so pooled graph nodes cannot be substituted without an interface change. Sources: [README.md](https://github.com/CAMMA-public/rendezvous/blob/f80f35d007c9ee30dfca321bae596af8f29cff59/README.md), [pytorch/network.py](https://github.com/CAMMA-public/rendezvous/blob/f80f35d007c9ee30dfca321bae596af8f29cff59/pytorch/network.py).

- **Rendezvous in Time** — Training/evaluation instructions are present; the paper comparison uses cholect45-crossval. Preserve the temporal sampling and split when using the release. Sources: [README.md](https://github.com/CAMMA-public/rendezvous-in-time/blob/73b7daad113796e7bcc0f1b6630551759344e602/README.md).

- **MCIT-IG** — Only four repository files were present. No main/model/train.sh implementation was found, pseudo-triplet generation is marked Coming Soon, and the README describes a private localization-test set. Literature reference only for now. Sources: [README.md](https://github.com/CAMMA-public/mcit-ig/blob/6c71a35ac3ca2fbcab6e4ff04a57e32d1f690f99/README.md).

- **ITG-Trip** — Actual model/dataset/training source and LICENSE are present. The dataset loader expects hoi_annotation and annotations structures; conversion from public CholecT50 labels is not established by the minimal README. Mamba and causal-convolution installation also need attention. Sources: [README.md](https://github.com/PJLallen/ITG-Trip/blob/2b22355193fc1e7d05d262c3e484c854dfecec3a/README.md), [datasets/hico.py](https://github.com/PJLallen/ITG-Trip/blob/2b22355193fc1e7d05d262c3e484c854dfecec3a/datasets/hico.py).

- **SGT** — Training/evaluation source and a weight link are present. README says processed data require author contact; no root license file was found. Do not attribute this release to SGT++ without further evidence. Sources: [README.md](https://github.com/ccccchenllll/SGT_master/blob/f88a11864441d609a711f33dc3e0bb8e7aaa222e/README.md).

- **VIS-Net / RSVIS** — Source is described as a preliminary release. Dataset access requires an affiliation-matched application; raw EndoVis video access is separate. This is not a ready-made graph-only inference experiment. Sources: [README.md](https://github.com/whq-xxh/RSVIS/blob/b6b7fbcda7750b98d0f1d42fefc1b20e5b5b59d2/README.md).

- **S2Former-OR** — Source, LICENSE and train/infer commands present. Requires processed 4D-OR and PointNet++/PyG dependencies; README links DETR initialization rather than establishing access to every final task checkpoint. Sources: [README.md](https://github.com/PJLallen/S2Former-OR/blob/500cb42bd2318b8ae97b4b6b95db1b587e226b94/README.md).

- **TriTemp-OR** — Source and train/infer commands present, with externally hosted processed data. No root license file was found; do not infer a license from the upstream frameworks. Sources: [README.md](https://github.com/RascalGdd/TriTemp-OR/blob/69f217e296f326230936466fa4c61edb251a6fb4/README.md).

- **TopoOR** — Real topology/model/data modules and evaluators present; scripts/download.sh links packed modalities and checkpoints. The task module uses a TemporalSuperGraph and modality-specific inputs; it is not a drop-in decoder for endoscopic LG-CVS graphs. Sources: [README.md](https://github.com/wngTn/TopoOR/blob/d285bc268fe31adc7a41a8ad5eaff30de022aa76/README.md), [src/models/modules/workflow_recognition.py](https://github.com/wngTn/TopoOR/blob/d285bc268fe31adc7a41a8ad5eaff30de022aa76/src/models/modules/workflow_recognition.py).

- **MM-OR** — Source includes multimodal scene graph training and downstream dataset-generation instructions. Raw data and model weights are separate resources; matching its multimodal graph schema is necessary. Sources: [README.md](https://github.com/egeozsoy/MM-OR/blob/defe55b855d603a3a64b219bfee2d3b729875a6d/README.md).

- **ORQA** — Benchmark construction/evaluation and multimodal training source are present, with hosted model links. A published QA framework does not guarantee acceptance of arbitrary serialized scene graphs. Sources: [README.md](https://github.com/egeozsoy/ORQA/blob/12c97f985aa865f72263d7095ed062cf6a8bc7e0/README.md).

- **EgoExOR** — Graph annotations/model source and model links present; the repository also documents the 2026 high-quality data update. Procedures are emulated spine surgery. Sources: [README.md](https://github.com/ardamamur/EgoExOR/blob/38291c71d6d204590b636fe8ba0382237251edd5/README.md).

- **SurGrID** — Graph encoder, sampler/trainer configs, LICENSE.txt and hosted data/checkpoint links present. Dataset-specific classes and paths require adaptation. Sources: [README.md](https://github.com/MECLabTUDA/SurGrID/blob/4fa39bdc0a4b78707ce2a12c2a2b3579ae3226f9/README.md).

- **SG2VID** — Graph encoder, sampling/training source, LICENSE.txt and hosted data/checkpoint links present. Separate graph-only versus graph-plus-image conditioning configurations when reporting results. Sources: [README.md](https://github.com/MECLabTUDA/SG2VID/blob/d2571f02583cb88f9ea3f28f10b44341c822120b/README.md), [sg2vid/graph_encoder/graph_segclip_masked.py](https://github.com/MECLabTUDA/SG2VID/blob/d2571f02583cb88f9ea3f28f10b44341c822120b/sg2vid/graph_encoder/graph_segclip_masked.py).

- **SWoMo** — Substantial source/config release and data/checkpoint links present. Real-video manual masks and additional labels require author contact. No root license file was found. Sources: [README.md](https://github.com/MECLabTUDA/SWoMo/blob/ddb52edc852f52a0056fca01789bbbff99014947/README.md).

- **HieraSurg** — Actual finetuning/labeling source is present, but README retains TODOs for weights/training/inference. Its example scripts/train.py and scripts/infer.py are absent. A noncommercial license is described in README, but the referenced root LICENSE file was not found. Sources: [README.md](https://github.com/DiegoBiagini/HieraSurg/blob/fd22698daf62b7e4eb1766b58fda5355656241ba/README.md).

- **SAGE-OR** — Source, LICENSE and cache/checkpoint links present. DINOv3 is gated for regenerating features; pinned SAM3 and cached features are part of the protocol. Separate graph-head runtime/storage from the offline perception stage. Accepted BMVC 2026, not yet presented on the check date. Sources: [README.md](https://github.com/TheFourthKaramazov/SAGE-OR/blob/e7e5d2f959182297ee0e22bd4e3c394d3b8202af/README.md).

- **SG-NCA** — Training, inference and analysis scripts present, including low-power deployment material. No root license file was found. Keep its SafeSurg workshop status explicit. Sources: [README.md](https://github.com/MECLabTUDA/SG-NCA/blob/09fafe3c6c2705a0190a1a845f56b96503ae4e5e/README.md).

- **Global-reasoned MTL** — Real source and model/evaluation-data links present. Some preprocessing/instrument labels are still marked to be released; old Torch/DGL dependencies and missing root license complicate reuse. Sources: [README.md](https://github.com/lalithjets/Global-reasoned-multi-task-model/blob/daf196c7fae5e98492dbfc604d7814616b6deffe/README.md).

- **Surgical graph reasoning (2020)** — Graph model and training/evaluation entries present. Feature-extraction instructions point to the extended work; no root license file was found. Sources: [README.md](https://github.com/mobarakol/Surgical_SceneGraph_Generation/blob/037760f714b0801340d129da2ffa226dc23cc593/README.md).

- **SIRNet** — Model, trainer/test files and LICENSE present; README supplies a minimal dependency list, so data/checkpoint setup still needs work. Sources: [README.md](https://github.com/cynerelee/SIRNet/blob/c03d7ace0c396095a32ff057b1b0e51fc8b5963b/README.md).

- **MT-FiST** — Real training/test/model files and externally hosted weights/features are linked. No root license file was found; release is not a complete reproduction guarantee. Sources: [README.md](https://github.com/Lycus99/MT-FiST/blob/399328b826341cec4145774ba877953f71d47d3c/README.md).

## Reading routes

- **Enhance an LG-CVS graph:** LG-CVS → ITIDNet → SSG-Com → CAT-SG → SV2LSTG. Compare object attributes, target geometry, hand identity, action edges and temporal links.
- **Preserve context and learn compact features:** global-reasoned multitask learning → concept graphs → SurGrID/SG2VID graph pretraining → SAGE-OR. These are precedents to examine before claiming that global features, masked graph pretraining or offline feature caching are new.
- **Transfer and robustness:** LG-DG → task-aware incremental learning → GRAD → CAT-SG/AutoLaparo as different-procedure targets. Multimodal latent graphs and explicit anatomical scene graphs need different adapters.
- **Identify graph-only downstream interfaces:** start with the saved-graph paths in SurgLatentGraph; then inspect CAT-SG graph loaders and TopoOR task modules. SSG-VQA, Rendezvous, VIS-Net and ORQA require their actual image/feature/modality dependencies to be handled explicitly.
- **Understand richer structure:** 4D-OR → LABRAD-OR → TriTemp-OR/S2Former-OR → MM-OR/EgoExOR → TopoOR. OR-Action is useful for examining temporal information current graphs may lose.

## Preprint watchlist

These are discovery leads, not verified top-venue publications or required implementation dependencies, and are not included in the counts above.

- **STSG-VQA: Evidence-Grounded Temporal Question Answering from Surgical Spatio-Temporal Scene Graphs** — arXiv 2026. [Preprint](https://arxiv.org/abs/2609.08543). Relevant to temporal graph QA; no main-conference/journal publication or reproducible author release established in this update.
- **SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs** — arXiv 2026. [Preprint](https://arxiv.org/abs/2609.25651). Relevant to geometry-grounded quantitative graphs; no main-conference/journal publication or reproducible author release established in this update.

## Curation notes

- Titles and venue/year labels were checked against publisher/conference records or primary author records. DOI years can differ from journal issue years: S2Former-OR is TMI 2025 with early access in 2024; LG-CVS is TMI 2024 with a 2023 DOI.
- The LG-DG published title is **Optimizing latent graph representations of surgical scenes for unseen domain generalization**. The previous zero-shot-domain-transfer wording was corrected.
- The supplied review's Appendix A has mismatched summaries for W. Lin et al. (2024) and C. Lin et al. (2024). Their original papers identify **ITIDNet** with localized interaction quintuples and **SGT++** with report generation, respectively. The catalogue follows the original papers.
- The review lists the early 2025 foundation-model work; the final 2026 **ORQA** publication and author repository are linked here. This update also adds later MICCAI 2026 work.
- General surgical VLM papers, segmentation-only methods and unrelated medical/radiology graphs are not automatically included because they appear in the review's references. HieraSurg, VIS-Net, concept graphs and action-triplet recognizers are explicitly identified as related methods rather than complete scene graph datasets.
- The main-conference/journal selection and the workshop/accepted section are different evidence groups. No metric table here combines results from different splits, human versus predicted graphs or different access to RGB inputs.
- Original catalogue text is covered by the repository license. Paper, code, data and model licenses remain those of their respective authors. A missing root license file does not prove there are no terms elsewhere; it means an explicit reusable-code license was not established by this check.
