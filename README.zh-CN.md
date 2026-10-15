<!-- Repeated links provide sources in multiple sections. -->
<!--lint disable double-link-->

# Awesome EmbeddingGemma [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 用 Google **EmbeddingGemma2** 构建本地多模态搜索。

[English](README.md) · [贡献指南](CONTRIBUTING.md)

EmbeddingGemma2 将文本、代码、图片、视频和音频映射到共享向量空间。本清单聚焦明确支持**第二代**的资源（区别于 EmbeddingGemma 300M 与 Gemini Embedding 2）。

核查日期：**2026-10-12**；新增及更新社区条目于 **2026-10-13** 核查。已核对来源，未本地实测。

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
| [DigUp](https://github.com/ARahim3/DigUp)                                     | ![Stars](https://img.shields.io/github/stars/ARahim3/DigUp?style=flat) | [本地多模态文件搜索；Apple silicon macOS 14+，另有 Windows/Linux 测试版](https://github.com/ARahim3/DigUp).                                          |
| [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) | ![Stars](https://img.shields.io/github/stars/google-ai-edge/gallery?style=flat) | [端侧图片搜索与视频片段定位；Android 12+ / iOS 17+，实验性测试版](https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2/). |

DigUp [v0.7.0-beta.1](https://github.com/ARahim3/DigUp/releases/tag/v0.7.0-beta.1) 新增 Windows 10/11 x64 与 Linux x64 安装包；Windows 安装包未签名。这两个测试版尚无截图文字 OCR，并跳过旧版 Word .doc、RAW 和 SVG 文件。

## 社区应用

- [Local Search](https://github.com/btroussel/SemanticSearchMCP) - macOS 本地文件搜索，通过 MCP 供编程助手检索；应用尚未公证，发送给云端助手的文件片段会离开设备。
- [Recall](https://github.com/pdstn12/Recall) - Linux 本地多模态文件搜索，基于 Rust、GTK 4 和 llama.cpp；早期项目。
- [VectorDash](https://github.com/ampersandru/VectorDash) - Windows 11 本地搜索文档、图片、音频和视频，支持跳转页码与时间点；基于 llama.cpp，安装包尚未签名。

## 微调与决策模型

- [EG2 Typed Decision](https://huggingface.co/mrm8488/embeddinggemma-2-ft-typed-decision) - 基于 EmbeddingGemma2 文本编码器和约 0.5M 参数决策头，输出 `choice`、`noul`（布尔）与 `score` 及概率；提供权重、推理代码和继续微调示例。
- [Typed Decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - 上述模型的训练与评测数据，覆盖 Agent 检查、客服、发票和安全事件；指标衡量与教师标签的一致性。
- [Typed Decision GGUF](https://huggingface.co/cstr/embeddinggemma-2-ft-typed-decision-GGUF) - 完整微调编码器与决策头的 FP32/Q8 GGUF 转换版；需要 CrispEmbed，不能直接用于标准 llama.cpp，作者仅报告小规模数值对齐验证。
- [Typed Decision Core ML](https://github.com/mikolaj92/embeddinggemma-typed-decisions-coreml) - 同一微调模型的 macOS 15+ Apple silicon 适配，无重新训练；需本地转换，Core ML 编码器使用 CPU/Neural Engine，原 FP32 决策头运行于 CPU，采用固定 token 桶并拒绝超长输入。

模型作者披露调参时查看过测试集；其微调结果不能与数据集的零样本榜单直接比较。

Core ML 适配于 **2026-10-14** 核对文档与实现；作者报告的数值对齐检查不代表任务准确率，也不证明全部计算都在 Neural Engine 执行。

- [Bharat-Embed 270M](https://huggingface.co/eulogik/bharat-embed-270m-gemma2) - 面向印地语和印英混合语检索的纯文本 LoRA 微调模型，提供[训练与导出代码](https://github.com/eulogik/Bharat-Embed)；按 256 token 训练，长文档效果尚未评测。
- [EmbeddingGemma2 Korean](https://huggingface.co/jonpark0/embeddinggemma-2-ko) - 面向韩语检索的微调模型，与基础权重混合并保留多模态输入；需要 Sentence Transformers 6.1+、Transformers 5.18+，作者报告韩语文本到语音检索效果小幅下降。
- [norsk-asr](https://github.com/ahdrage/norsk-asr) - 基于 EmbeddingGemma2 音频编码器和 CTC 读取器的挪威语 Bokmål 识别模型，提供[权重](https://huggingface.co/ahdrage/norsk-asr)；仅录音转写，输出小写且无标点，可选 KenLM 文件采用 CC BY-SA 4.0。
- [African speech-retrieval LoRA](https://huggingface.co/naijaml/embeddinggemma-2-african-speech-lora) - 在六种非洲语言上训练的同语种语音与文本检索适配器；需要基础模型，不提供转写或翻译。

Bharat-Embed 于 **2026-10-14** 核对模型卡、配置与已发布文件；未本地复现作者评测。

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
- [UI Search](https://github.com/sai-prakash/ui-screenshot-search) - 在浏览器中用文字或截图搜索示例组件、IBM Carbon 和 GitHub Primer，提供可复用的 Storybook 索引脚本；截图检索准确率尚未评测。

Sentence Transformers 教程要求 **6.1.0+**。

## 模型与运行时

| 资源                                                                                                         | 使用路线                                 | 注意事项                                                                          |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------- |
| [Google 原始权重](https://huggingface.co/google/embeddinggemma-2)                                              | Sentence Transformers / Transformers | 参考权重；小工作负载可关闭未使用的编码器。                                                         |
| [ONNX Community 转换](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)                           | Transformers.js                      | 包含浏览器/Node.js 示例及后端/dtype 说明。                                                 |
| [LiteRT 纯文本 270M](https://huggingface.co/litert-community/embeddinggemma-2-text-270m-litert-lm)            | LiteRT-LM                            | 纯文本模型文件。                                                                      |
| [LiteRT 文本 + 视觉 440M](https://huggingface.co/litert-community/embeddinggemma-2-text-vision-440m-litert-lm) | LiteRT-LM                            | 视觉模型文件；输入范围见模型卡。                                                              |
| [LiteRT 完整模型 740M](https://huggingface.co/litert-community/embeddinggemma-2-740m-litert-lm)                | LiteRT-LM                            | 完整多模态文件与部署说明。                                                                 |
| [LiteRT 文本 + 音频，570M](https://huggingface.co/Luigi/embeddinggemma-2-570m-text-audio-litert-lm) | LiteRT-LM | 移除视觉编码器的社区重打包版本，仅支持文本与音频，附构建配置。 |
| [MLX Community 合集](https://huggingface.co/collections/mlx-community/embeddinggemma-2)                      | Apple silicon                        | 转换版本合集；运行时与模态支持须查阅各模型卡。                                                       |
| [FluidInference Core ML](https://huggingface.co/FluidInference/embeddinggemma-2-coreml)                    | Apple Neural Engine / GPU            | 文本走 Neural Engine，图片/音频走 GPU；macOS 15 / iOS 18 起，文本最多 512 token，音频按 10 秒窗口处理。 |
| [Påmin INT8 ONNX](https://huggingface.co/pamin-labs/embeddinggemma-2-text-int8-onnx)                       | ONNX Runtime CPU                     | 仅文本；示例截断至 512 token，最长实测输入为 471 token；维护索引时须固定运行时版本。                          |
| [EverPaper Core AI](https://huggingface.co/EverPaper/embeddinggemma-2-coreai) | macOS 27+ / Apple silicon | 文本、图片和音频转换版，提供 Swift/Python 接口；支持 Neural Engine/GPU 路线，文本上限 2,048 token，音频按 30 秒窗口处理。 |

Påmin 转换版于 **2026-10-14** 核对模型卡与已发布文件；限制及数值检查来自作者，未本地复现。

EverPaper 转换版于 **2026-10-15** 核对模型卡与已发布文件；未本地运行，也未复现作者的数值检查。


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
| [vLLM](https://github.com/vllm-project/vllm)                                  | ![Stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat)                 | [通过 pooling runner 提供多模态向量服务；支持已合并至 main](https://github.com/vllm-project/vllm/pull/60254)。                           |

vLLM 支持于 **2026-10-14** 核对已合并 PR 与模型实现；未本地运行验证。

- [embeddinggemma.c](https://github.com/QuixiAI/embeddinggemma.c) - 原生嵌入服务，第二代支持 CPU、Metal 与 [CUDA](https://github.com/QuixiAI/embeddinggemma.c/commit/6f4c2e713ed1d71519334ce159c57f5e592f76e1)（文本、图片、音频、视频采样帧及混合输入）；第二代 ROCm/XPU 支持仍待实现，300M 评测反映第一代。
- [eg2npu](https://github.com/daaku/eg2npu) - 基于 OpenVINO 的 Intel NPU 文本向量服务，读取 EmbeddingGemma2 GGUF 权重并提供兼容 llama-server 的 API；不支持图片或音频，打包的系统服务仅支持最多 64 token 的查询。

## 使用要点

- 按[模型卡](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)使用任务前缀，检索查询和文档前缀不同。
- 截短向量后重新归一化，查询与文档维度保持一致。多模态检索使用 128 维需仔细验证。
- 参考权重使用 BF16 或 FP32（避免 FP16）。转换运行时参见各自的 [dtype 说明](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)。
- 各模态共享 8,192 token 预算。音频分段与视频采样前请查阅[多模态预处理说明](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers)。

## 评测

[官方评测表](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results)包含文本、代码、图片、视觉文档、视频、音频及截短维度结果（发布方数据，未在本地复现）。社区评测提交要求详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 参与贡献

欢迎提交第二代相关资源。详情见[贡献指南](CONTRIBUTING.md)。
