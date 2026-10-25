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
| [MemPalace](https://github.com/MemPalace/mempalace) | ![Stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=flat) | [本地 Agent 记忆与文本/代码检索，v3.11.0 可选启用 EG2；实验性图片、音频和视频检索返回整文件引用，不支持片段定位。需要 Python 3.10+ 和可选依赖，切换模型须重新嵌入已有索引。](https://github.com/MemPalace/mempalace/blob/v3.11.0/docs/embeddinggemma2.md) |

DigUp [v0.7.0-beta.3](https://github.com/ARahim3/DigUp/releases/tag/v0.7.0-beta.3) 面向 Windows 10/11 x64 与 Linux x64，新增表格与演示文稿（xlsx、pptx、ods、odp）及 Typst 文档的文本索引，并同步 Mac [v0.6.2](https://github.com/ARahim3/DigUp/releases/tag/v0.6.2) 的共享修复。Linux 闲置十分钟后退出搜索进程，下次搜索启动会稍慢。Windows 安装包仍未签名；这两个测试版尚无截图文字 OCR，并跳过旧版 Word .doc、RAW 和 SVG 文件。

## 社区应用

- [Code Déjà Vu](https://github.com/shashankbudem/code-dejavu) - 本地跨仓库查找函数，并通过 Git pre-commit hook 提醒相似实现，不阻止提交；支持 TypeScript、JavaScript、Python 和 Rust 中至少五行的函数，跳过测试文件，需要 Python 3.10+ 并下载模型。
- [Daemon](https://github.com/iamartyaa/daemon) - macOS 14+ Apple silicon 应用，用快捷键保存选中文字、截图、文件和语音笔记，再按语义找回；基于本地 llama.cpp，发布包尚未公证。
- [drive-lens](https://github.com/xcspl/drive-lens) - 用本地 EmbeddingGemma2 向量搜索 Google Drive 共享照片、视频预览和 PDF，提供 Windows/macOS/Linux 桌面端；文件夹须设为持链接可访问，描述生成另需视觉大模型，使用云端模型时会发送预览图给服务商。
- [GemSearch](https://github.com/IndigoJay/GemSearch) - Linux 本地照片与截图搜索，支持文字、图片及图片加文字的组合查询，提供 CLI 和浏览器界面；默认使用 NVIDIA CUDA，也可选 CPU，离线使用前需先下载模型。
- [Local Search](https://github.com/btroussel/SemanticSearchMCP) - macOS 本地文件搜索，通过 MCP 供编程助手检索；应用尚未公证，发送给云端助手的文件片段会离开设备。
- [MediaIndex](https://github.com/harsheetamorey/mediaindex) - macOS 13+ Apple silicon 应用，用 EmbeddingGemma2 本地搜索图片、音频和视频，另用其他模型做物体计数与图片编辑；应用未签名，编辑功能需额外下载模型。
- [Mitsuke](https://github.com/kanaworksai-hue/mitsuke) - 在 Apple silicon Mac 上通过 MLX 本地搜索图片和视频镜头，支持文字、示例图片及组合查询，覆盖 RAW、PSD、EXR/HDR 素材库，提供网页、CLI 和 MCP；首次使用需下载模型。
- [omafind](https://github.com/radimsem/omafind) - Omarchy 4 本地文档、PDF、图片、视频和音频搜索插件，基于 EmbeddingGemma2 与 llama-server，支持跳转到页码和时间点；安装时构建引擎并下载模型，索引与缩略图在本机未加密保存。
- [photosearch](https://github.com/mumit/photosearch) - 在 Mac 上用文字或图片搜索 Apple Photos 图库，并定位视频片段，提供浏览器界面；索引使用本地预览图，iCloud 原尺寸照片和仅存云端的视频需下载。
- [Recall](https://github.com/pdstn12/Recall) - Linux 本地多模态文件搜索，基于 Rust、GTK 4 和 llama.cpp；早期项目。
- [rummage](https://github.com/av/rummage) - 基于 llama.cpp 的本地多模态文件搜索，提供 CLI、网页、HTTP API 及页码和时间点跳转，支持 CPU、CUDA、ROCm 或 Vulkan；Linux 安装包要求 glibc 2.39+ 和 x86-64-v3，模型另行下载，视频需 FFmpeg，PDF 页面图像需 Poppler。
- [sift-it](https://github.com/jwa91/sift-it) - 基于 Rust、EmbeddingGemma2 和 llama.cpp 的终端文档、图片、录音、视频与代码搜索，支持页码、时间点、行号跳转、JSON 输出及 JSON Lines 前端接口；需要 Apple silicon、macOS 14+ 并下载模型，转写文本检索使用独立语音模型。
- [Sonicproof](https://github.com/kanaworksai-hue/sonicproof) - 本地检查生成音频与提示词的匹配程度、筛选多个生成结果及搜索音效库，提供 CLI、网页和 MCP，支持 CPU、CUDA 或 Apple silicon；相似度评分仍需试听确认，短促声音尤其容易混淆。
- [Trawl](https://github.com/Crane-AI-Labs/trawl) - 在 Android 11+、64 位手机上通过 EmbeddingGemma2 本地搜索照片、文档、视频和语音笔记；模型需另下载，搜索以英语效果为优先，转写使用独立的英语语音识别模型。32 位 Go 版不提供语义搜索。
- [VectorDash](https://github.com/ampersandru/VectorDash) - Windows 本地文档、图片、音频和视频搜索，通过 llama.cpp 支持页码与时间点跳转；安装包未签名。[0.3.42 版](https://github.com/ampersandru/VectorDash/releases/tag/v0.3.42) 新增测试版以图搜图，覆盖已索引文件和保留的剪贴板图片，需要兼容的视觉向量（不含仅 Quick 或仅 OCR 条目），并提供可选的 AI 本地检索。远端图片查询会发送图片给配置的向量服务器，AI 本地检索会发送检索片段给配置的 AI 服务器。Windows 10 x64 2004+ 与可选 RAW 支持（默认关闭，仅用于 Full 来源）仍为测试版，Windows 11 为主要测试平台。
- [Vault Semantic Search](https://github.com/TheBrainAir/vault-semantic-search) - Obsidian 桌面端本地笔记混合搜索、相关笔记与图片搜索插件，使用 WebGPU 或本地 Ollama 服务；尚无安装包，需从源码构建。

- [video-grep](https://github.com/madhusoodhans/video-grep) - 在终端或 SSH 会话中用 EmbeddingGemma2 搜索视频，返回时间点与片段导出命令；需要 Python 3.10+、FFmpeg 并首次下载模型。仅搜索六秒片段的视觉内容，不搜索音频或 OCR 文字；作者测试覆盖 macOS 与英语查询，Linux 和 CUDA 尚未测试。

## 微调与决策模型

- [EG2 Typed Decision](https://huggingface.co/mrm8488/embeddinggemma-2-ft-typed-decision) - 基于 EmbeddingGemma2 文本编码器和约 0.5M 参数决策头，输出 `choice`、`noul`（布尔）与 `score` 及概率；提供权重、推理代码和继续微调示例。
- [Typed Decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - 上述模型的训练与评测数据，覆盖 Agent 检查、客服、发票和安全事件；指标衡量与教师标签的一致性。
- [Typed Decision GGUF](https://huggingface.co/cstr/embeddinggemma-2-ft-typed-decision-GGUF) - 完整微调编码器与决策头的 FP32/Q8 GGUF 转换版；需要 CrispEmbed，不能直接用于标准 llama.cpp，作者仅报告小规模数值对齐验证。
- [Typed Decision Core ML](https://github.com/mikolaj92/embeddinggemma-typed-decisions-coreml) - 同一微调模型的 macOS 15+ Apple silicon 适配，无重新训练；需本地转换，Core ML 编码器使用 CPU/Neural Engine，原 FP32 决策头运行于 CPU，采用固定 token 桶并拒绝超长输入。

模型作者披露调参时查看过测试集；其微调结果不能与数据集的零样本榜单直接比较。

Core ML 适配于 **2026-10-14** 核对文档与实现；作者报告的数值对齐检查不代表任务准确率，也不证明全部计算都在 Neural Engine 执行。

- [Multimodal Typed Decision](https://huggingface.co/Danny-Dasilva/embeddinggemma-2-multimodal-typed-decision) - EmbeddingGemma2 微调模型，支持文字、图片和视频的选择、布尔判断与等级评分，以及可选的目标框定位；需配套运行时代码，主要面向英语。开发中重复使用了评测集，部分训练数据限非商业、仅供研究或未声明许可。

- [Bharat-Embed 270M](https://huggingface.co/eulogik/bharat-embed-270m-gemma2) - 面向印地语和印英混合语检索的纯文本 LoRA 微调模型，提供[训练与导出代码](https://github.com/eulogik/Bharat-Embed)；按 256 token 训练，长文档效果尚未评测。
- [EmbeddingGemma2 Korean](https://huggingface.co/jonpark0/embeddinggemma-2-ko) - 面向韩语检索的微调模型，与基础权重混合并保留多模态输入；需要 Sentence Transformers 6.1+、Transformers 5.18+，作者报告韩语文本到语音检索效果小幅下降。
- [eg2-transcribe](https://github.com/john-rocky/eg2-transcribe) - 用冻结的 EmbeddingGemma2 音频编码器和训练后的读取器做英语转写，提供 Android 8+ arm64 的 LiteRT 实现及 iOS/macOS 27 的 Core AI 实现；需自行构建应用并另下载模型，仅用英语朗读语音训练，输出不带标点或大写。
- [eg2-transcribe-zh-en-ja-ko](https://github.com/TimHu950112/eg2-transcribe-zh-en-ja-ko) - 用冻结的 EmbeddingGemma2 音频编码器、字符级 CTC 读取器及分语言 n-gram 做中英日韩离线转写，支持标点、中文繁简输出，提供 Core ML/LiteRT 模型与 Swift/Kotlin 解码器；模型需另下载，n-gram 语言包采用 CC BY-SA 4.0。
- [Embed2ASR](https://github.com/tc3oliver/embed2asr) - 冻结 EmbeddingGemma2 音频编码器，训练 9.66M 参数的 GRU-CTC 读取器，用于普通话、英语与中英混合转写，提供[读取器权重](https://huggingface.co/tc3oliver/Embed2ASR-v1)；需另行下载基础编码器，仅支持离线转写，不支持流式。
- [KolStream](https://huggingface.co/MaorB/embeddinggemma-2-asr-hebrew-english-streaming) - 基于部分微调的 EmbeddingGemma2 音频编码器、流式读取器与 Transducer 头，支持希伯来语和英语的文件及流式转写；提供权重与推理代码，需另下载基础编码器，输出不带标点或大写。
- [norsk-asr](https://github.com/ahdrage/norsk-asr) - 基于 EmbeddingGemma2 音频编码器和 CTC 读取器的挪威语 Bokmål 识别模型，提供[权重](https://huggingface.co/ahdrage/norsk-asr)；仅录音转写，输出小写且无标点，可选 KenLM 文件采用 CC BY-SA 4.0。
- [sea-asr](https://github.com/PixelML/sea-asr) - 基于 EmbeddingGemma2 的 CTC 语音识别，提供[印尼语](https://huggingface.co/PixelML/sea-asr-id)和 [Tagalog／Taglish](https://huggingface.co/PixelML/sea-asr-ph) 权重、词级时间戳及 SRT/VTT 字幕导出，支持 CPU 或 CUDA；需另下载基础编码器，输出小写文本且无标点。
- [Turkish STT](https://huggingface.co/mstkyvz/embeddinggemma2-turkish-stt) - 基于 EmbeddingGemma2、字符级 CTC 读取器、可拆卸 LoRA 和可选 KenLM 的土耳其语转写，提供 CC BY-SA 4.0 权重与语言模型，以及 Apache-2.0 训练代码；需基础模型，不支持流式，输出小写且无标点，使用原始向量能力时须关闭 LoRA。
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
- [官方多模态微调教程](https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-multimodal-embeddinggemma-with-sentence-transformers) - 用跨模态三元组与 Sentence Transformers 训练文本到图片检索，包含训练前后评估；需要支持 BF16 的 GPU。
- [Transformers 模型文档](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2) - 底层模型与处理器 API。
- [最小多模态搜索示例](https://github.com/ranjankndev/embeddinggemma2-search) - 用少量 Python 文件和 NumPy 向量实现本地文本、图片、音频与视频检索，无需数据库或 UI。
- [Gemma-Lens](https://github.com/johnrobinsn/gemma-lens) - 用文字、麦克风录音或图片检索 COCO 图片与 ESC-50 音频的示例，直接计算余弦相似度，附[实现教程](https://www.storminthecastle.com/posts/gemma_lens/)；支持 CPU 或 CUDA，ESC-50 音频限非商业使用。
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
| [EverPaper Core AI](https://huggingface.co/EverPaper/embeddinggemma-2-coreai) | macOS 27+ / Apple silicon | 文本、图片和音频转换版，提供 Swift/Python 接口；支持 Neural Engine/GPU 路线，文本上限 2,048 token，音频按 30 秒窗口处理。 |

- [CowboyCoder Core AI ANE](https://huggingface.co/cowboycoderhq/EmbeddingGemma-2-FP16-M6-ANE) - macOS 27+ / Apple silicon: 纯文本 FP16 转换版，提供 [Python 运行时与转换代码](https://github.com/cowboycoderhq/EmbeddingGemma-2-16GB-M6-ANE)；面向 Neural Engine，词元查表在主机侧完成，使用固定的 128/512 token 输入形状，超出 512 token 会截断。作者测试设备为 16 GB M6 Mac mini。


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

- [GemmaEmbed](https://github.com/maralski/gemma-embed-swift) - 使用自带 Metal 内核的 Swift 包，在进程内生成 EmbeddingGemma2 文本、图片及图文混合向量；需要 Apple silicon、macOS 14+、Swift 6，并另下载 Q8_0 GGUF 权重（图片还需投影器），不支持音频。

- [OpenVLCLIP](https://github.com/kotadymo/openvlclip) - 非官方 Python 库，通过 Transformers 在 CPU 或 CUDA 上提供 EmbeddingGemma2 图片、文本编码及可选视频帧搜索；接口借鉴 OpenCLIP，但不能直接替换它，需要 Python 3.12–3.14（不含 3.14.1）。 原名 openclip-gemma；[迁移指南](https://github.com/kotadymo/openvlclip/blob/main/docs/migration-v0.5.0.md)要求更换包名与导入名，不提供旧导入名兼容。

- [ComfyUI-EmbeddingGemma2](https://github.com/hiroki-abe-58/ComfyUI-EmbeddingGemma2) - 非官方 ComfyUI 节点包，用于文本、图片、视频和音频相似度比较及图片排序；需要 V3 节点 API 和单独下载模型，音频仅取前 30 秒、视频最多取 32 帧，依赖可能与要求 huggingface-hub 2.x 的节点冲突。

- [embeddinggemma2-rocm](https://github.com/anjn/embeddinggemma2-rocm) - 通过 HIP、MIGraphX 和 LibTorch 在 Linux AMD GPU 上生成 EmbeddingGemma2 图片与文本向量，提供 C/C++、Python 和 HTTP 接口；需要可用的 ROCm 驱动，并单独准备与 GPU、软件环境匹配的模型包。作者测试覆盖 Radeon 890M（gfx1150），其他 GPU 需自行编译与验证。

- [embeddinggemma2-rust](https://github.com/Dalailalama/embeddinggemma2-rust) - 非官方 Rust 文本、图片、音频和视频向量实现，支持 CPU 或 CUDA，提供 CLI 与兼容 OpenAI 的 HTTP 服务；需另下载权重，GPU 运行需 CUDA 13.x 库，音频文件输入限 WAV，MP4 解码需 FFmpeg。

- [Rust Embedding Runtime](https://github.com/A-K-6/rust-embedding-runtime) - 自托管的纯 CPU EmbeddingGemma2 文本向量服务，提供兼容 OpenAI 的 API 及内置模型的 Linux AMD64/ARM64 Docker 镜像；每条输入限 1,024 token，任务前缀需自行添加，ARM64 需支持 NEON/FP16 指令。

- [EmbeddingGemma2 for Unity](https://github.com/ayutaz/unity-embeddinggemma-2) - 通过 Unity 6000.3.21f1 和 Sentis 2.6.1 GPUCompute 提供文本、图片与音频向量；仅支持 Windows Editor/Player，模型另行下载，媒体输入尺寸或长度固定，无自动 CPU 回退；首版支持配置为 64 GB RAM、16 GB VRAM。

## 使用要点

- 按[模型卡](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)使用任务前缀，检索查询和文档前缀不同。
- 截短向量后重新归一化，查询与文档维度保持一致。多模态检索使用 128 维需仔细验证。
- 参考权重使用 BF16 或 FP32（避免 FP16）。转换运行时参见各自的 [dtype 说明](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)。
- 各模态共享 8,192 token 预算。音频分段与视频采样前请查阅[多模态预处理说明](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers)。

## 评测

[官方评测表](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results)包含文本、代码、图片、视觉文档、视频、音频及截短维度结果（发布方数据，未在本地复现）。社区评测提交要求详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 参与贡献

欢迎提交第二代相关资源。详情见[贡献指南](CONTRIBUTING.md)。
