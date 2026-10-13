<!-- Repeated links provide sources in multiple sections. -->
<!--lint disable double-link-->

# Awesome EmbeddingGemma [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 用 Google **EmbeddingGemma2** 构建本地多模态搜索。

[English](README.md) · [贡献指南](CONTRIBUTING.md)

EmbeddingGemma2 将文本、代码、图片、视频和音频映射到共享向量空间。本清单聚焦明确支持**第二代**的资源（区别于 EmbeddingGemma 300M 与 Gemini Embedding 2）。

核查日期：**2026-10-12**；新增社区条目于 **2026-10-13** 核查。已核对来源，未本地实测。

## 目录

- [热门应用](#热门应用)
- [社区应用](#社区应用)
- [微调与决策模型](#微调与决策模型)
- [决策应用示例](#决策应用示例)
- [从这里开始](#从这里开始)
- [模型速览](#模型速览)
- [教程与示例](#教程与示例)
- [模型与运行时](#模型与运行时)
- [推理框架与服务](#推理框架与服务)
- [使用要点](#使用要点)
- [评测](#评测)

## 热门应用

基于 EmbeddingGemma2 的应用。Stars 由 Shields.io 动态获取，可能有缓存延迟。

| 项目                                                                            | Stars                                                                  | 用途与支持依据                                                                                                               |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [DigUp](https://github.com/ARahim3/DigUp)                                     | ![Stars](https://img.shields.io/github/stars/ARahim3/DigUp?style=flat) | [本地搜索文档、图片、音频和视频；Apple silicon、macOS 14+](https://github.com/ARahim3/DigUp).                                          |

## 社区应用

- [Local Search](https://github.com/btroussel/SemanticSearchMCP) - macOS 本地文件搜索，通过 MCP 供编程助手检索；应用尚未公证，发送给云端助手的文件片段会离开设备。
- [Recall](https://github.com/pdstn12/Recall) - Linux 本地多模态文件搜索，基于 Rust、GTK 4 和 llama.cpp；早期项目。
- [VectorDash](https://github.com/ampersandru/VectorDash) - Windows 11 本地搜索文档、图片、音频和视频，支持跳转页码与时间点；基于 llama.cpp，安装包尚未签名。

## 微调与决策模型

- [EG2 Typed Decision](https://huggingface.co/mrm8488/embeddinggemma-2-ft-typed-decision) - 基于 EmbeddingGemma2 文本编码器和约 0.5M 参数决策头，输出 `choice`、`noul`（布尔）与 `score` 及概率；提供权重、推理代码和继续微调示例。
- [Typed Decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - 上述模型的训练与评测数据，覆盖 Agent 检查、客服、发票和安全事件；指标衡量与教师标签的一致性。

模型作者披露调参时查看过测试集；其微调结果不能与数据集的零样本榜单直接比较。

## 决策应用示例

- [EmbeddingGemma2 Jeff](https://github.com/karimtn/embeddingGemma2-jeff) - 基于 Transformers.js 与 ONNX 向量的 Node.js 示例，用于客服意图分类、垃圾信息识别和任务分流；通过余弦相似度匹配带标签的示例，无需微调，也没有训练决策头。

## 从这里开始

- [官方模型主页](https://deepmind.google/models/gemma/embeddinggemma/) - Google DeepMind 模型介绍与资源入口。
- [模型卡](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2) - 架构、评测、输入约束与局限。
- [原始权重](https://huggingface.co/google/embeddinggemma-2) - Google 官方权重与配置。
- [开发者指南](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/) - 架构概览、模块化加载与应用示例。

## 模型速览

| 项目   | 内容                                           |
| ---- | -------------------------------------------- |
| 输入   | 文本/代码、图片、视频、音频及混合输入                          |
| 参数量  | 纯文本 270M；文本 + 视觉 440M；文本 + 音频 570M；完整模型 740M |
| 上下文  | 各模态共享 8,192 token                            |
| 向量维度 | 原生 768（支持截短至 512 / 256 / 128）                |
| 模型许可 | Apache-2.0（请查阅权重许可及相关政策）                     |

来源：[模型卡](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)、[开发者指南](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/)。

## 教程与示例

- [Sentence Transformers 文本教程](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers) - 官方 Python 文本检索指南。
- [Sentence Transformers 多模态教程](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers) - 媒体与混合输入官方示例。
- [Transformers 模型文档](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2) - 底层模型与处理器 API。
- [最小多模态搜索示例](https://github.com/ranjankndev/embeddinggemma2-search) - 用少量 Python 文件和 NumPy 向量实现本地文本、图片、音频与视频检索，无需数据库或 UI。

Sentence Transformers 教程要求 **6.1.0+**。

## 模型与运行时

| 资源                                                                                                         | 使用路线                                 | 注意事项                          |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------- |
| [Google 原始权重](https://huggingface.co/google/embeddinggemma-2)                                              | Sentence Transformers / Transformers | 参考权重；小工作负载可关闭未使用的编码器。         |
| [ONNX Community 转换](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)                           | Transformers.js                      | 包含浏览器/Node.js 示例及后端/dtype 说明。 |
| [LiteRT 纯文本 270M](https://huggingface.co/litert-community/embeddinggemma-2-text-270m-litert-lm)            | LiteRT-LM                            | 纯文本模型文件。                      |
| [LiteRT 文本 + 视觉 440M](https://huggingface.co/litert-community/embeddinggemma-2-text-vision-440m-litert-lm) | LiteRT-LM                            | 视觉模型文件；输入范围见模型卡。              |
| [LiteRT 完整模型 740M](https://huggingface.co/litert-community/embeddinggemma-2-740m-litert-lm)                | LiteRT-LM                            | 完整多模态文件与部署说明。                 |
| [MLX Community 合集](https://huggingface.co/collections/mlx-community/embeddinggemma-2)                      | Apple silicon                        | 转换版本合集；运行时与模态支持须查阅各模型卡。       |


## 推理框架与服务

已确认第二代支持；Stars 由 Shields.io 动态获取，可能有缓存延迟。

| 项目                                                                            | Stars                                                                                      | 用途与支持依据                                                                                                               |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)                      | ![Stars](https://img.shields.io/github/stars/google-ai-edge/LiteRT-LM?style=flat)          | [端侧推理；0.18.0 加入支持](https://github.com/google-ai-edge/LiteRT-LM).                                                      |
| [llama.cpp](https://github.com/ggml-org/llama.cpp)                            | ![Stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat)                | [原生 C/C++；文本、视觉、音频支持已合并](https://github.com/ggml-org/llama.cpp/pull/30054).                                           |
| [MLX-VLM](https://github.com/Blaizzy/mlx-vlm)                                 | ![Stars](https://img.shields.io/github/stars/Blaizzy/mlx-vlm?style=flat)                   | [Apple silicon 原生 MLX 多模态向量](https://github.com/Blaizzy/mlx-vlm/blob/main/mlx_vlm/models/embedding_gemma2/README.md). |
| [oMLX](https://github.com/jundot/omlx)                                        | ![Stars](https://img.shields.io/github/stars/jundot/omlx?style=flat)                       | [Apple silicon 推理服务，已列出第二代支持](https://github.com/jundot/omlx).                                                        |
| [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | ![Stars](https://img.shields.io/github/stars/huggingface/sentence-transformers?style=flat) | [Python 向量接口；官方教程要求 6.1.0+](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/).                 |
| [Transformers](https://github.com/huggingface/transformers)                   | ![Stars](https://img.shields.io/github/stars/huggingface/transformers?style=flat)          | [Python 模型与预处理 API](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2).                             |
| [Transformers.js](https://github.com/huggingface/transformers.js)             | ![Stars](https://img.shields.io/github/stars/huggingface/transformers.js?style=flat)       | [浏览器 / Node.js；4.3.1 加入支持](https://github.com/huggingface/transformers.js/releases/tag/4.3.1).                        |

- [embeddinggemma.c](https://github.com/QuixiAI/embeddinggemma.c) - 原生嵌入服务，第二代 profile 支持 CPU 与 Metal（文本、图片、音频、视频采样帧及混合输入）。第二代 CUDA、ROCm 与 XPU 支持仍待实现；已发布的 300M 评测反映第一代。

## 使用要点

- 按[模型卡](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)使用任务前缀，检索查询和文档前缀不同。
- 截短向量后重新归一化，查询与文档维度保持一致。多模态检索使用 128 维需仔细验证。
- 参考权重使用 BF16 或 FP32（避免 FP16）。转换运行时参见各自的 [dtype 说明](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)。
- 各模态共享 8,192 token 预算。音频分段与视频采样前请查阅[多模态预处理说明](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers)。

## 评测

[官方评测表](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results)包含文本、代码、图片、视觉文档、视频、音频及截短维度结果（发布方数据，未在本地复现）。社区评测提交要求详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 参与贡献

欢迎提交第二代相关资源。详情见[贡献指南](CONTRIBUTING.md)。
