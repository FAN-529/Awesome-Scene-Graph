#!/usr/bin/env python3
"""Build the public Awesome list and reading notes from data/papers.json.

Uses only Python's standard library. Run with --check to validate a contribution
and confirm that committed Markdown matches the structured catalogue.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
REPO = "FAN-529/Awesome-Scene-Graph"
EVIDENCE = {
    "construction": "Graph construction or evaluation",
    "predicted": "Predicted graphs evaluated on selected downstream tasks",
    "gt": "Ground-truth or manually provided graphs in downstream experiments",
    "payload": "Visual or geometric features retained in the representation",
    "joint": "Graphs used together with the original visual input",
    "generation": "Graph-conditioned image or video generation",
    "uncertain": "Incomplete review or evidence assessment",
    "survey": "Survey rather than an independent downstream experiment",
}
EVIDENCE_ZH = {
    "construction": "以构图或评测为主",
    "predicted": "预测图用于限定的下游任务",
    "gt": "下游实验使用人工或真值图",
    "payload": "图内保留视觉或几何特征",
    "joint": "图与原始视觉输入共同使用",
    "generation": "图条件图像或视频生成",
    "uncertain": "阅读或证据评估尚不完整",
    "survey": "综述，不是独立的下游验证实验",
}
STATUS_ZH = {"published": "已发表", "accepted": "已接收", "preprint": "预印本", "workshop": "研讨会论文"}
DATASETS = [
    ("visualgenome2017", "Visual Genome", "Dense object, attribute and relationship annotations for image scene graphs."),
    ("vidvrd", "VidVRD", "Video visual relationship detection with temporal object relations."),
    ("action_genome", "Action Genome", "Human-object interactions represented as spatiotemporal scene graphs."),
    ("psg2022", "PSG", "Panoptic scene graphs with object and background-region masks."),
    ("pvsg", "PVSG", "Panoptic video scene graphs with object tracks and temporal relations."),
    ("G02", "3DSSG", "Semantic scene graphs associated with 3D indoor reconstructions."),
    ("easg", "EASG", "Action scene graphs for long-form egocentric video understanding."),
    ("cat_sg", "CAT-SG", "Fine-grained dynamic scene graph annotations for cataract surgery."),
    ("4d_or", "4D-OR", "Multiview operating-room data with semantic scene graphs."),
    ("mm_or", "MM-OR", "Multimodal operating-room scenes and semantic annotations."),
    ("egoexor", "EgoExOR", "Ego-exocentric operating-room data for surgical activity understanding."),
    ("ssg_vqa", "SSG-VQA", "Surgical visual question answering informed by scene graph knowledge."),
    ("llmbenchmark2025", "LLM Meets Scene Graph", "A benchmark for language-model scene graph understanding and generation."),
]
TOOLS = [
    ("psg2022", "OpenPSG", "Panoptic scene graph generation baselines and evaluation."),
    ("pvsg", "OpenPVSG", "Panoptic video scene graph annotations and baselines."),
    ("sttran", "STTran", "Dynamic scene graph generation with spatial-temporal transformers."),
    ("reltr2023", "RelTR", "Transformer-based image scene graph generation."),
    ("tde2020", "Scene-Graph-Benchmark", "Image scene graph baselines and debiasing methods."),
    ("G05", "Hydra", "3D scene graph construction for robotic spatial perception."),
    ("G06", "ConceptGraphs", "Open-vocabulary 3D scene graphs for perception and planning."),
    ("G09", "Open3DSG", "Open-vocabulary objects and relations in 3D scene graphs."),
    ("ssg_vqa", "SSG-VQA", "Surgical QA resources and the released baseline interface."),
    ("sg2vid", "SG2VID", "Surgical graph-conditioned video generation resources."),
]
STARTERS = ["johnson2015", "visualgenome2017", "imp2017", "motifs2018", "psg2022", "action_genome", "pvsg", "G02", "surg2020_graph", "ssg_vqa"]


def load_data():
    return json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))


def anchor(paper):
    return "paper-" + paper["id"].lower().replace("_", "-")


def ordered(papers):
    return sorted(papers, key=lambda p: (-p["year"], p["title"].casefold()))


def source_links(paper, include_notes=True):
    links = [f'[[paper]]({paper["paper_url"]})']
    for field, label in (("repository_url", "repo"), ("project_url", "project")):
        if paper.get(field):
            if field == "repository_url":
                label = {"data": "data repo", "dataset": "data repo", "data-tool": "data tool", "framework": "framework"}.get(paper.get("repository_resource_type"), label)
            links.append(f'[[{label}]]({paper[field]})')
    if include_notes:
        links.append(f'[[notes]](docs/reading-guide.zh-CN.md#{anchor(paper)})')
    return " ".join(links)


def label(paper):
    base = f'{paper["venue"]} {paper["year"]}'
    if paper["publication_status"] == "accepted":
        base += "; accepted"
    elif paper["publication_status"] == "preprint":
        base += "; preprint"
    return base


def make_readme(data):
    papers = ordered(data["papers"])
    by_id = {p["id"]: p for p in papers}
    topics = data["topics"]
    counts = Counter(p["review_status"] for p in papers)
    lines = [
        "# Awesome Scene Graph", "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        f"[![GitHub Stars](https://img.shields.io/github/stars/{REPO}?style=social)](https://github.com/{REPO})", "",
        "A curated collection of papers, datasets and implementations on scene graphs: image scene graph generation, panoptic and open-vocabulary representations, temporal graphs, 3D spatial reasoning, and surgical applications.", "",
        f'**{len(papers)} entries from 2015 to 2026.** Literature snapshot: **{data["literature_snapshot"]}**. Repository updated: **{data["repository_updated_on"]}**.', "",
        "[中文说明](README.zh-CN.md) · [中文逐篇阅读笔记](docs/reading-guide.zh-CN.md) · [Structured catalogue](data/papers.json) · [BibTeX](references.bib)", "",
        "The list covers selected milestones and related applications rather than every scene graph paper. Published papers, accepted papers, workshops and preprints are labelled separately. A `repo` link means a public repository is available; it does not certify complete code, released checkpoints, permissive licensing or reproduced results.", "",
        "## Contents", "",
        "- [Start here](#start-here)",
        "- [Papers by year](#papers-by-year)",
        "- [Papers by topic](#papers-by-topic)",
        "- [Datasets and benchmarks](#datasets-and-benchmarks)",
        "- [Surveys](#surveys)",
        "- [Tools and implementations](#tools-and-implementations)",
        "- [Reading notes and citations](#reading-notes-and-citations)",
        "- [Under review](#under-review)",
        "- [Contributing](#contributing)",
        "- [Acknowledgements](#acknowledgements)",
        "- [License](#license)", "",
        "## Start here", "",
        "For a first pass, follow the progression from objects, attributes and relationships to automatic generation, time, geometry and surgical use:", "",
    ]
    for i, paper_id in enumerate(STARTERS, 1):
        p = by_id[paper_id]
        lines.append(f'{i}. [{p["title"]}](#{anchor(p)}) ({p["year"]}).')
    lines.extend(["", "A scene graph may contain symbolic labels, visual features, geometry or several of these together. Downstream experiments using human annotations or the original video should not be read as evidence that an automatically predicted symbolic graph can replace the video.", "", "## Papers by year", ""])
    for year in sorted({p["year"] for p in papers}, reverse=True):
        lines.extend([f"### {year}", ""])
        for p in papers:
            if p["year"] != year:
                continue
            extra = " **Abstract reviewed only.**" if p["review_status"] == "abstract_only" else ""
            if p["entry_type"] == "journal_extension":
                extra += " Journal extension."
            lines.append(f'- <a id="{anchor(p)}"></a>[{label(p)}] **{p["title"]}** {source_links(p)}{extra}')
        lines.append("")
    lines.extend(["## Papers by topic", "", "Each paper has one primary topic below. Dataset, reasoning and generation papers can also be found through the resource sections.", ""])
    for topic in topics:
        subset = [p for p in papers if p["topic"] == topic["id"]]
        lines.extend([f'### {topic["name"]}', ""])
        for p in subset:
            lines.append(f'- [{p["title"]}](#{anchor(p)}) ({p["year"]}).')
        lines.append("")
    lines.extend(["## Datasets and benchmarks", "", "Follow each source for access requirements, annotation scope and dataset terms. A paper or repository link does not imply that every raw video, image or annotation is available without conditions.", ""])
    for paper_id, name, description in DATASETS:
        p = by_id[paper_id]
        lines.append(f'- **{name}** — {description} {source_links(p, include_notes=False)}')
    lines.extend(["", "## Surveys", ""])
    for p in papers:
        if p["entry_type"] == "survey":
            lines.append(f'- [{label(p)}] **{p["title"]}** {source_links(p)}')
    lines.extend(["", "## Tools and implementations", "", "Selected author repositories. Their dependencies, checkpoints and licenses differ; consult each release before choosing a baseline. Repository availability was checked on the date recorded in [repository-checks.json](data/repository-checks.json). These checks are not reproduction results.", ""])
    for paper_id, name, description in TOOLS:
        p = by_id[paper_id]
        if p.get("repository_url"):
            lines.append(f'- [{name}]({p["repository_url"]}) — {description}')
    lines.extend([
        "", "## Reading notes and citations", "",
        f'- [Chinese reading notes](docs/reading-guide.zh-CN.md) explain what each paper does, its contribution and its limitations. Selected sections were reviewed for {counts["paper_sections_reviewed"]} entries; the SGT++ entry is explicitly limited to its abstract and metadata.',
        "- [papers.json](data/papers.json) is the source of truth for the generated lists and notes. It also records publication status and the type of downstream evidence.",
        "- [references.bib](references.bib) contains 87 citations obtained from source metadata. It is a partial export: no author names or missing citations were invented to match the catalogue size. An arXiv citation may use its preprint year while the list uses the final publication year.",
        "- The collection links to original publications; it does not redistribute paper PDFs, extracted full text, model weights or datasets.",
        "", "## Under review", "",
        "[watchlist.json](data/watchlist.json) keeps one publication outside the main list pending further assessment of its methodological and experimental claims. Its presence is not a recommendation or a reproduced result.",
        "", "## Contributing", "",
        "Suggestions, corrections and new papers are welcome through issues or pull requests. Please follow [CONTRIBUTING.md](CONTRIBUTING.md), cite an original source, and distinguish a repository link from a verified runnable release.",
        "", "## Acknowledgements", "",
        "The catalogue layout was inspired by [Awesome AI Agents for Healthcare](https://github.com/FAN-529/Awesome-AI-Agents-for-Healthcare) and [Awesome Radiology Report Generation](https://github.com/FAN-529/Awesome-Radiology-Report-Generation), with thanks to their upstream maintainers [AgenticHealthAI](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) and [mk-runner](https://github.com/mk-runner/Awesome-Radiology-Report-Generation). All linked research belongs to its respective authors.",
        "", "## License", "",
        "Original catalogue text, reading notes and maintenance scripts are provided under the [MIT License](LICENSE). Linked papers, implementations, datasets and model weights retain their own copyrights and licenses.", "",
    ])
    return "\n".join(lines)


def make_notes(data):
    lines = ["# Scene Graph 逐篇阅读笔记", "",
        "这份笔记按公开论文整理，说明每篇做了什么、主要贡献和适用边界。它是阅读辅助，不能替代原文或模型复现。", "",
        f'文献快照：{data["literature_snapshot"]}。共 {len(data["papers"])} 条主目录记录，含一条仅根据摘要和元数据整理的 SGT++；待核条目另见 [watchlist.json](../data/watchlist.json)。', "",
        "[返回英文首页](../README.md) · [中文仓库说明](../README.zh-CN.md) · [结构化目录](../data/papers.json)", "",
        "## 如何理解下游证据", "",
        "图内是否保留视觉特征、是否使用人工图、是否同时输入原视频，会影响下游实验能够支持的结论。生成一个外观合理的视频，也不能直接证明图保存了原视频的全部信息。", "",
    ]
    for key, value in EVIDENCE_ZH.items():
        lines.append(f"- **{key}**：{value}。")
    lines.append("")
    for topic in data["topics"]:
        lines.extend([f'## {topic["name"]}', ""])
        for p in ordered(data["papers"]):
            if p["topic"] != topic["id"]:
                continue
            lines.extend([f'<a id="{anchor(p)}"></a>', "", f'### {p["title"]}', "",
                f'{p["venue"]} {p["year"]} · {STATUS_ZH[p["publication_status"]]} · [原文]({p["paper_url"]})', ""])
            if p["review_status"] == "abstract_only":
                lines.extend(["**阅读范围：仅摘要与原始元数据，未阅读全文。**", ""])
            if p.get("publication_note"):
                lines.extend([f'出版说明：{p["publication_note"]}。', ""])
            n = p["notes_zh"]
            lines.extend([f'**做了什么：** {n["summary"]}', "", f'**主要贡献：** {n["innovation"]}', "", f'**局限与边界：** {n["limitation"]}', "", f'**下游证据类型：** {EVIDENCE_ZH[p["downstream_evidence_type"]]}。', ""])
    return "\n".join(lines)


def make_chinese(data):
    counts = Counter(p["topic"] for p in data["papers"])
    lines = ["# Awesome Scene Graph", "", "[English](README.md) · [逐篇阅读笔记](docs/reading-guide.zh-CN.md) · [BibTeX](references.bib)", "",
        "一个持续整理的 Scene Graph 论文与资源目录，覆盖图像、视频、三维、开放词汇以及手术场景中的表示、生成、推理和应用。", "",
        f'目前主目录有 **{len(data["papers"])} 条记录**，年份覆盖 **2015—2026**。文献快照为 **{data["literature_snapshot"]}**，仓库整理日期为 **{data["repository_updated_on"]}**。这是一份经过选择的阅读目录，不是全部 Scene Graph 论文的穷尽列表。', "",
        "## 阅读入口", "",
        "- [按年份浏览](README.md#papers-by-year)：年份倒序列出论文、原文和已有仓库链接。",
        "- [按主题浏览](README.md#papers-by-topic)：从静态图、时序图、三维图或手术应用进入。",
        "- [数据集与 benchmark](README.md#datasets-and-benchmarks)：查看代表性标注集和评测任务。",
        "- [中文逐篇笔记](docs/reading-guide.zh-CN.md)：每篇说明做了什么、主要贡献及局限。",
        "- [结构化目录](data/papers.json)：用于搜索、二次整理以及自动生成首页。", "",
        "## 主题覆盖", "",
    ]
    for topic in data["topics"]:
        lines.append(f'- **{topic["name"]}**：{counts[topic["id"]]} 条。')
    lines.extend(["", "## 收录和核查口径", "",
        "正式发表、已接收、研讨会论文和预印本分开标记。SGT++ 仅阅读了摘要和元数据，因此不发布未经全文核实的方法或性能结论。另有一条待核论文放在 [watchlist.json](data/watchlist.json)，不计入主目录。", "",
        "`repo` 表示该公开 GitHub 仓库的地址已经检查，不代表代码、数据、权重或许可证全部齐全，也不表示我们完成了复现。资源实际可用范围以作者仓库和原始数据条款为准。", "",
        "中文笔记区分人工图、预测图、含视觉或几何特征的图、图加原始视觉输入以及图条件生成。只有先看清输入条件，才能判断某项实验是否说明图足以支持特定下游任务。", "",
        "论文以原文链接提供。BibTeX 为有原始来源的部分导出，共 87 条；部分记录尚无引用导出，后续可根据原始出版信息补充。", "",
        "## 参与维护", "", "欢迎通过 Issue 或 Pull Request 补充论文、纠正元数据和报告失效链接。更新方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。", "",
        "## 许可", "", "本仓库原创目录文字、阅读笔记和维护脚本使用 [MIT License](LICENSE)。链接到的论文、代码、数据和模型仍遵循各自的版权与许可。", "",
    ])
    return "\n".join(lines)


def validate(data):
    papers = data["papers"]
    topics = {t["id"] for t in data["topics"]}
    seen = set()
    titles = set()
    urls = set()
    for p in papers:
        assert re.fullmatch(r"[A-Za-z0-9_]+", p["id"]), p["id"]
        assert p["id"] not in seen, f'Duplicate id: {p["id"]}'
        assert p["title"].casefold() not in titles, f'Duplicate title: {p["title"]}'
        assert p["paper_url"] not in urls, f'Duplicate paper URL: {p["paper_url"]}'
        seen.add(p["id"]); titles.add(p["title"].casefold()); urls.add(p["paper_url"])
        assert isinstance(p["year"], int) and 1900 <= p["year"] <= 2100
        assert p["topic"] in topics
        assert p["publication_status"] in STATUS_ZH
        assert p["downstream_evidence_type"] in EVIDENCE
        assert p["review_status"] in {"paper_sections_reviewed", "abstract_only"}
        assert not re.search(r"[\u4e00-\u9fff]", p["venue"]), p["venue"]
        for field in ("paper_url", "repository_url", "project_url", "pdf_url"):
            if p.get(field):
                url = urlparse(p[field])
                assert url.scheme == "https" and url.netloc, (p["id"], field)
                if field == "repository_url":
                    assert url.netloc == "github.com", p[field]
        assert all(p["notes_zh"].get(k) for k in ("summary", "innovation", "limitation"))
    watchlist = json.loads((ROOT / "data/watchlist.json").read_text(encoding="utf-8"))
    assert all(p["id"] not in seen for p in watchlist)
    checks = json.loads((ROOT / "data/repository-checks.json").read_text(encoding="utf-8"))
    available = {(c["paper_id"], c["url"]) for c in checks if c["http_status"] == 200}
    assert all((p["id"], p["repository_url"]) in available for p in papers if p.get("repository_url")), "Repository URL missing its availability record"


def validate_local_links(outputs):
    anchors = {}
    for filename, text in outputs.items():
        ids = re.findall(r'<a id="([^"]+)"></a>', text)
        for heading in re.findall(r"^#{1,6} (.+)$", text, flags=re.M):
            slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
            ids.append(slug)
        anchors[filename] = set(ids)
        assert len(re.findall(r'<a id="([^"]+)"></a>', text)) == len(set(re.findall(r'<a id="([^"]+)"></a>', text))), f"Duplicate explicit anchor in {filename}"
    for filename, text in outputs.items():
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://")):
                continue
            path, _, fragment = target.partition("#")
            dest = str((Path(filename).parent / path).as_posix()) if path else filename
            # Normalise ../ segments without allowing a link outside the repo.
            resolved = (ROOT / dest).resolve()
            assert resolved.is_relative_to(ROOT), (filename, target)
            canonical = resolved.relative_to(ROOT).as_posix()
            assert canonical in outputs or resolved.is_file(), (filename, target)
            if fragment and canonical in anchors:
                assert fragment in anchors[canonical], (filename, target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without changing files")
    args = parser.parse_args()
    data = load_data()
    validate(data)
    outputs = {"README.md": make_readme(data), "README.zh-CN.md": make_chinese(data), "docs/reading-guide.zh-CN.md": make_notes(data)}
    validate_local_links(outputs)
    stale = []
    for name, text in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
    if stale:
        print("Generated files need updating: " + ", ".join(stale), file=sys.stderr)
        return 1
    print(f'Validated {len(data["papers"])} catalogue entries, repository records, local links and generated Markdown.')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
