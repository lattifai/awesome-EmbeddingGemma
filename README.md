<!-- Repeated links provide sources in multiple sections. -->
<!--lint disable double-link-->

# Awesome EmbeddingGemma [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Local multimodal search with Google’s **EmbeddingGemma2**.

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md)

EmbeddingGemma2 maps text, code, images, video, and audio into a shared embedding space. This list covers resources supporting the **second generation** (distinct from EmbeddingGemma 300M and Gemini Embedding 2).

Last checked: **2026-10-12**; new and updated community entries checked **2026-10-13**. Sources reviewed; runtimes not tested locally.

## Contents

- [Popular Applications](#popular-applications)
- [Community Applications](#community-applications)
- [Fine-tuning and Decision Models](#fine-tuning-and-decision-models)
- [Decision Application Examples](#decision-application-examples)
- [Start here](#start-here)
- [Model at a glance](#model-at-a-glance)
- [Guides and examples](#guides-and-examples)
- [Models and runtimes](#models-and-runtimes)
- [Inference Frameworks and Servers](#inference-frameworks-and-servers)
- [Practical notes](#practical-notes)
- [Evaluation](#evaluation)

## Popular Applications

Applications built with EmbeddingGemma2. Stars update via Shields.io and may be cached.

| Project                                                                       | Stars                                                                  | Use and support evidence                                                                                                                     |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [DigUp](https://github.com/ARahim3/DigUp)                                     | ![Stars](https://img.shields.io/github/stars/ARahim3/DigUp?style=flat) | [Local file search across documents, images, audio, and video; Apple silicon, macOS 14+](https://github.com/ARahim3/DigUp).                  |

## Community Applications

- [Local Search](https://github.com/btroussel/SemanticSearchMCP) - macOS local file search with MCP access for coding assistants; the app is not notarized, and snippets sent to cloud assistants leave the device.
- [Recall](https://github.com/pdstn12/Recall) - Early-stage Linux file search with Rust, GTK 4, and llama.cpp.
- [VectorDash](https://github.com/ampersandru/VectorDash) - Windows 11 local search across documents, images, audio, and video with page and timestamp jumps; uses llama.cpp and ships an unsigned installer.

## Fine-tuning and Decision Models

- [EG2 Typed Decision](https://huggingface.co/mrm8488/embeddinggemma-2-ft-typed-decision) - EmbeddingGemma2 text encoder with a roughly 0.5M-parameter head for `choice`, `noul` (Boolean), and `score` decisions with probabilities; includes weights, inference code, and further fine-tuning examples.
- [Typed Decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - Training and evaluation data used by the model above, covering agent checks, support tickets, invoices, and security incidents; metrics measure agreement with teacher labels.
- [Typed Decision GGUF](https://huggingface.co/cstr/embeddinggemma-2-ft-typed-decision-GGUF) - Complete fine-tuned encoder and decision head in FP32/Q8 GGUF; requires CrispEmbed rather than stock llama.cpp, with only small-scale numerical parity checks reported.
- [Typed Decision Core ML](https://github.com/mikolaj92/embeddinggemma-typed-decisions-coreml) - Adaptation of the same fine-tuned model for macOS 15+ Apple silicon, without retraining; locally converted Core ML encoder uses CPU/Neural Engine with the original FP32 decision head on CPU, fixed token buckets, and overlength rejection.

The model author selected hyperparameters while inspecting the test split; its fine-tuned results are not directly comparable with the dataset's zero-shot leaderboard.

Core ML adaptation checked **2026-10-14** against its documentation and implementation; author-reported parity checks do not establish task accuracy or exclusive Neural Engine execution.

## Decision Application Examples

- [EmbeddingGemma2 Jeff](https://github.com/karimtn/embeddingGemma2-jeff) - Node.js examples for support intent classification, spam detection, and triage using Transformers.js and ONNX embeddings; matches labeled examples by cosine similarity without fine-tuning or a trained decision head.

## Start here

- [Official model page](https://deepmind.google/models/gemma/embeddinggemma/) - DeepMind overview and entry points.
- [Model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2) - Architecture, evaluation, input constraints, and limitations.
- [Original checkpoint](https://huggingface.co/google/embeddinggemma-2) - Model weights and configuration.
- [Developer guide](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/) - Architecture, modular loading, and examples.

## Model at a glance

| Property             | Details                                                           |
| -------------------- | ----------------------------------------------------------------- |
| Inputs               | Text/code, images, video, audio, and mixed inputs                 |
| Parameters           | 270M text; 440M text + vision; 570M text + audio; 740M full model |
| Context              | 8,192 tokens shared across modalities                             |
| Embedding dimensions | 768 (truncatable to 512 / 256 / 128)                              |
| Model license        | Apache-2.0 (consult checkpoint license and policies)              |

Sources: [model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2), [developer guide](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/).

## Guides and examples

- [Text embeddings with Sentence Transformers](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers) - Official text retrieval walkthrough.
- [Multimodal embeddings with Sentence Transformers](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers) - Media and mixed-input examples.
- [Transformers model documentation](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2) - Lower-level model and processor APIs.
- [Minimal multimodal search](https://github.com/ranjankndev/embeddinggemma2-search) - A small Python example for local text, image, audio, and video retrieval using NumPy vectors, without a database or UI.
- [UI Search](https://github.com/sai-prakash/ui-screenshot-search) - Browser demo using Transformers.js to find UI components by text or screenshot; limited to 19 sample components, with no screenshot retrieval accuracy evaluation yet.

The Sentence Transformers tutorials require **6.1.0+**.

## Models and runtimes

| Resource                                                                                                          | Route                                | Notes                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| [Google checkpoint](https://huggingface.co/google/embeddinggemma-2)                                               | Sentence Transformers / Transformers | Reference weights; disable unused encoders for smaller workloads.                                                                  |
| [ONNX Community conversion](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)                          | Transformers.js                      | Browser/Node.js examples and backend/dtype guidance.                                                                               |
| [LiteRT text, 270M](https://huggingface.co/litert-community/embeddinggemma-2-text-270m-litert-lm)                 | LiteRT-LM                            | Text-only artifact.                                                                                                                |
| [LiteRT text + vision, 440M](https://huggingface.co/litert-community/embeddinggemma-2-text-vision-440m-litert-lm) | LiteRT-LM                            | Vision-enabled artifact; see supported-input table.                                                                                |
| [LiteRT full model, 740M](https://huggingface.co/litert-community/embeddinggemma-2-740m-litert-lm)                | LiteRT-LM                            | Full multimodal artifact and deployment instructions.                                                                              |
| [MLX Community collection](https://huggingface.co/collections/mlx-community/embeddinggemma-2)                     | Apple silicon                        | Conversion collection; inspect model cards for runtime/modality support.                                                           |
| [FluidInference Core ML](https://huggingface.co/FluidInference/embeddinggemma-2-coreml)                           | Apple Neural Engine / GPU            | Text on Neural Engine, image/audio on GPU; macOS 15 / iOS 18+, text limited to 512 tokens and audio to 10-second windows.          |
| [Påmin INT8 ONNX](https://huggingface.co/pamin-labs/embeddinggemma-2-text-int8-onnx)                              | ONNX Runtime CPU                     | Text only; example truncates at 512 tokens, longest tested input is 471 tokens; pin the runtime version when maintaining an index. |

Påmin conversion checked **2026-10-14** against its model card and published files; limits and numerical checks are author-reported, not locally reproduced.


## Inference Frameworks and Servers

Confirmed second-generation support. Stars update via Shields.io and may be cached.

| Project                                                                       | Stars                                                                                      | Use and support evidence                                                                                                                     |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)                      | ![Stars](https://img.shields.io/github/stars/google-ai-edge/LiteRT-LM?style=flat)          | [On-device inference; added support in 0.18.0](https://github.com/google-ai-edge/LiteRT-LM).                                                 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp)                            | ![Stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat)                | [Native C/C++; text, vision, and audio support merged](https://github.com/ggml-org/llama.cpp/pull/30054).                                    |
| [MLX-VLM](https://github.com/Blaizzy/mlx-vlm)                                 | ![Stars](https://img.shields.io/github/stars/Blaizzy/mlx-vlm?style=flat)                   | [Native MLX multimodal embeddings on Apple silicon](https://github.com/Blaizzy/mlx-vlm/blob/main/mlx_vlm/models/embedding_gemma2/README.md). |
| [oMLX](https://github.com/jundot/omlx)                                        | ![Stars](https://img.shields.io/github/stars/jundot/omlx?style=flat)                       | [Apple silicon inference server; lists EmbeddingGemma2 support](https://github.com/jundot/omlx).                                             |
| [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | ![Stars](https://img.shields.io/github/stars/huggingface/sentence-transformers?style=flat) | [Python embeddings; official guide requires 6.1.0+](https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/).                |
| [Transformers](https://github.com/huggingface/transformers)                   | ![Stars](https://img.shields.io/github/stars/huggingface/transformers?style=flat)          | [Python model and processor APIs](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2).                                      |
| [Transformers.js](https://github.com/huggingface/transformers.js)             | ![Stars](https://img.shields.io/github/stars/huggingface/transformers.js?style=flat)       | [Browser / Node.js; added support in 4.3.1](https://github.com/huggingface/transformers.js/releases/tag/4.3.1).                              |
| [vLLM](https://github.com/vllm-project/vllm)                                  | ![Stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat)                 | [Multimodal embedding serving via the pooling runner; support merged into main](https://github.com/vllm-project/vllm/pull/60254).            |

vLLM support checked **2026-10-14** against the merged PR and model implementation; no local runtime test.

- [embeddinggemma.c](https://github.com/QuixiAI/embeddinggemma.c) - Native embedding server supporting EmbeddingGemma2 on CPU, Metal, and [CUDA](https://github.com/QuixiAI/embeddinggemma.c/commit/6f4c2e713ed1d71519334ce159c57f5e592f76e1) (text, image, audio, sampled video, mixed inputs); v2 ROCm/XPU support is pending, and 300M benchmarks describe the first generation.

## Practical notes

- Use task-specific prefixes from the [model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2); query and document prefixes differ.
- Re-normalize truncated vectors and maintain matching query/document dimensions. Validate 128d carefully for multimodal retrieval.
- Use BF16 or FP32 (not FP16) for reference weights. See [dtype guidance](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX) for converted runtimes.
- Modalities share the 8,192-token budget. Follow [multimodal preprocessing](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers) before chunking audio or sampling video.

## Evaluation

The [official benchmark tables](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results) report publisher results for text, code, image, visual-document, video, audio, and truncated dimensions. Community benchmark submission requirements are detailed in [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to suggest second-generation resources or benchmarks.
