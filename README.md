<!-- Repeated links provide sources in multiple sections. -->
<!--lint disable double-link-->

# Awesome EmbeddingGemma [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Local multimodal search with Google’s **EmbeddingGemma2**.

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md)

EmbeddingGemma2 maps text, code, images, video, and audio into a shared embedding space. This list covers resources supporting the **second generation** (distinct from EmbeddingGemma 300M and Gemini Embedding 2).

Last checked: **2026-10-12**. Sources reviewed; runtimes not tested locally.

## Contents

- [Popular Applications](#popular-applications)
- [Community Applications](#community-applications)
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

- [Recall](https://github.com/pdstn12/Recall) - Early-stage Linux file search with Rust, GTK 4, and llama.cpp.

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

The Sentence Transformers tutorials require **6.1.0+**.

## Models and runtimes

| Resource                                                                                                          | Route                                | Notes                                                                    |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------ |
| [Google checkpoint](https://huggingface.co/google/embeddinggemma-2)                                               | Sentence Transformers / Transformers | Reference weights; disable unused encoders for smaller workloads.        |
| [ONNX Community conversion](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)                          | Transformers.js                      | Browser/Node.js examples and backend/dtype guidance.                     |
| [LiteRT text, 270M](https://huggingface.co/litert-community/embeddinggemma-2-text-270m-litert-lm)                 | LiteRT-LM                            | Text-only artifact.                                                      |
| [LiteRT text + vision, 440M](https://huggingface.co/litert-community/embeddinggemma-2-text-vision-440m-litert-lm) | LiteRT-LM                            | Vision-enabled artifact; see supported-input table.                      |
| [LiteRT full model, 740M](https://huggingface.co/litert-community/embeddinggemma-2-740m-litert-lm)                | LiteRT-LM                            | Full multimodal artifact and deployment instructions.                    |
| [MLX Community collection](https://huggingface.co/collections/mlx-community/embeddinggemma-2)                     | Apple silicon                        | Conversion collection; inspect model cards for runtime/modality support. |


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

- [embeddinggemma.c](https://github.com/QuixiAI/embeddinggemma.c) - Native embedding server supporting EmbeddingGemma2 on CPU and Metal (text, image, audio, sampled video, mixed inputs). CUDA, ROCm, and XPU support for v2 is pending; published benchmarks reflect the first-generation 300M model.

## Practical notes

- Use task-specific prefixes from the [model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2); query and document prefixes differ.
- Re-normalize truncated vectors and maintain matching query/document dimensions. Validate 128d carefully for multimodal retrieval.
- Use BF16 or FP32 (not FP16) for reference weights. See [dtype guidance](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX) for converted runtimes.
- Modalities share the 8,192-token budget. Follow [multimodal preprocessing](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers) before chunking audio or sampling video.

## Evaluation

The [official benchmark tables](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results) report publisher results for text, code, image, visual-document, video, audio, and truncated dimensions. Community benchmark submission requirements are detailed in [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to suggest second-generation resources or benchmarks.
