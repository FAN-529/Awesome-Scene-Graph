# Awesome Scene Graph

[English](README.md) · [逐篇阅读笔记](docs/reading-guide.zh-CN.md) · [BibTeX](references.bib)

一个持续整理的 Scene Graph 论文与资源目录，覆盖图像、视频、三维、开放词汇以及手术场景中的表示、生成、推理和应用。

目前主目录有 **94 条记录**，年份覆盖 **2015—2026**。文献快照为 **2026-10-12**，仓库整理日期为 **2026-10-14**。这是一份经过选择的阅读目录，不是全部 Scene Graph 论文的穷尽列表。

## 阅读入口

- [按年份浏览](README.md#papers-by-year)：年份倒序列出论文、原文和已有仓库链接。
- [按主题浏览](README.md#papers-by-topic)：从静态图、时序图、三维图或手术应用进入。
- [数据集与 benchmark](README.md#datasets-and-benchmarks)：查看代表性标注集和评测任务。
- [中文逐篇笔记](docs/reading-guide.zh-CN.md)：每篇说明做了什么、主要贡献及局限。
- [结构化目录](data/papers.json)：用于搜索、二次整理以及自动生成首页。

## 主题覆盖

- **Foundations and Image Scene Graph Generation**：20 条。
- **Panoptic, Open-Vocabulary and Multimodal Scene Graphs**：20 条。
- **Video and Temporal Scene Graphs**：13 条。
- **3D Scene Graphs and Robotics**：14 条。
- **Surgical Scene Graphs**：15 条。
- **Operating-Room Scene Graphs**：11 条。
- **Surveys**：1 条。

## 收录和核查口径

正式发表、已接收、研讨会论文和预印本分开标记。SGT++ 仅阅读了摘要和元数据，因此不发布未经全文核实的方法或性能结论。另有一条待核论文放在 [watchlist.json](data/watchlist.json)，不计入主目录。

`repo` 表示该公开 GitHub 仓库的地址已经检查，不代表代码、数据、权重或许可证全部齐全，也不表示我们完成了复现。资源实际可用范围以作者仓库和原始数据条款为准。

中文笔记区分人工图、预测图、含视觉或几何特征的图、图加原始视觉输入以及图条件生成。只有先看清输入条件，才能判断某项实验是否说明图足以支持特定下游任务。

论文以原文链接提供。BibTeX 为有原始来源的部分导出，共 87 条；部分记录尚无引用导出，后续可根据原始出版信息补充。

## 参与维护

欢迎通过 Issue 或 Pull Request 补充论文、纠正元数据和报告失效链接。更新方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

本仓库原创目录文字、阅读笔记和维护脚本使用 [MIT License](LICENSE)。链接到的论文、代码、数据和模型仍遵循各自的版权与许可。
