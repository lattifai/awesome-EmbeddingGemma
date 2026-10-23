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

| Project                                                                       | Stars                                                                           | Use and support evidence                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DigUp](https://github.com/ARahim3/DigUp)                                     | ![Stars](https://img.shields.io/github/stars/ARahim3/DigUp?style=flat)          | [Local multimodal file search; Apple silicon macOS 14+, plus Windows/Linux beta](https://github.com/ARahim3/DigUp).                                                                                                                                                                                                                                       |
| [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery)           | ![Stars](https://img.shields.io/github/stars/google-ai-edge/gallery?style=flat) | [On-device photo search and video moment retrieval; Android 12+ / iOS 17+, experimental beta](https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2/).                                                                                                                                                                                   |
| [MemPalace](https://github.com/MemPalace/mempalace)                           | ![Stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=flat)    | [Local agent memory and text/code search with opt-in EG2 in v3.11.0; experimental image/audio/video retrieval returns whole-file references, without segment search. Requires Python 3.10+, optional dependencies, and re-embedding existing indexes when switching models.](https://github.com/MemPalace/mempalace/blob/v3.11.0/docs/embeddinggemma2.md) |

DigUp [v0.7.0-beta.3](https://github.com/ARahim3/DigUp/releases/tag/v0.7.0-beta.3) for Windows 10/11 x64 and Linux x64 adds text indexing for spreadsheets and presentations (xlsx, pptx, ods, odp) and Typst documents, bringing over shared fixes from Mac [v0.6.2](https://github.com/ARahim3/DigUp/releases/tag/v0.6.2). Linux releases the search process after ten idle minutes; the next search takes longer to start. The Windows installer remains unsigned. These beta ports lack screenshot OCR and skip legacy Word .doc, RAW, and SVG files.

## Community Applications

- [Code Déjà Vu](https://github.com/shashankbudem/code-dejavu) - Local cross-repository function search and similarity warnings through a non-blocking Git pre-commit hook; supports TypeScript, JavaScript, Python, and Rust functions of at least five lines, skips tests, and requires Python 3.10+ plus a model download.
- [Daemon](https://github.com/iamartyaa/daemon) - macOS 14+ Apple silicon app for capturing selected text, screenshots, files, and voice notes with a hotkey and recalling them by meaning; uses local llama.cpp, with unnotarized releases.
- [drive-lens](https://github.com/xcspl/drive-lens) - Search shared Google Drive photos, video previews, and PDFs with local EmbeddingGemma2 vectors and a Windows/macOS/Linux desktop app; requires an anyone-with-the-link folder and a separate vision LLM for descriptions, with previews sent to the provider when hosted.
- [GemSearch](https://github.com/IndigoJay/GemSearch) - Local photo and screenshot search for Linux with text, image, or combined image-and-text queries, a CLI, and a browser UI; defaults to NVIDIA CUDA with a CPU option, and needs an initial model download before offline use.
- [Local Search](https://github.com/btroussel/SemanticSearchMCP) - macOS local file search with MCP access for coding assistants; the app is not notarized, and snippets sent to cloud assistants leave the device.
- [MediaIndex](https://github.com/harsheetamorey/mediaindex) - macOS 13+ Apple silicon app for local image, audio, and video search with EmbeddingGemma2, plus object counting and photo editing via separate models; unsigned app, with extra model downloads for editing.
- [Mitsuke](https://github.com/kanaworksai-hue/mitsuke) - Local image and video-shot search on Apple silicon via MLX, using text, example images, or both; supports RAW, PSD, and EXR/HDR libraries with web UI, CLI, and MCP access, and requires an initial model download.
- [omafind](https://github.com/radimsem/omafind) - Omarchy 4 plugin for local document, PDF, image, video, and audio search with page and timestamp jumps using EmbeddingGemma2 and llama-server; setup builds the engine and downloads models, and indexes and thumbnails are stored unencrypted locally.
- [photosearch](https://github.com/mumit/photosearch) - Local Apple Photos text/image search and video moment retrieval on Mac, with a browser UI; indexes cached previews, while full-size iCloud photos and cloud-only videos require downloads.
- [Recall](https://github.com/pdstn12/Recall) - Early-stage Linux file search with Rust, GTK 4, and llama.cpp.
- [rummage](https://github.com/av/rummage) - Local multimodal file search with CLI, web UI, HTTP API, and page/timestamp jumps via llama.cpp on CPU, CUDA, ROCm, or Vulkan; Linux binaries require glibc 2.39+ and x86-64-v3, models download separately, video needs FFmpeg, and PDF page images need Poppler.
- [Sonicproof](https://github.com/kanaworksai-hue/sonicproof) - Local generated-audio prompt matching, take ranking, and sound-library search via CLI, web UI, or MCP on CPU, CUDA, or Apple silicon; similarity scores need listening checks, especially for short transient sounds.
- [Trawl](https://github.com/Crane-AI-Labs/trawl) - Local photo, document, video, and voice-note search on Android 11+ 64-bit phones using EmbeddingGemma2; requires a separate model download, works best in English, and uses a separate English-only speech recognizer. The 32-bit Go edition has no semantic search.
- [VectorDash](https://github.com/ampersandru/VectorDash) - Windows local search across documents, images, audio, and video with page and timestamp jumps; uses llama.cpp and ships an unsigned installer. [Version 0.3.41](https://github.com/ampersandru/VectorDash/releases/tag/v0.3.41) adds optional semantic search for clipboard images and OCR for screenshot text; Windows 10 x64 2004+ support remains in beta (Windows 11 is the primary tested platform) and RAW image support remains optional (beta, disabled by default, Full sources only).
- [Vault Semantic Search](https://github.com/TheBrainAir/vault-semantic-search) - Desktop Obsidian plugin for local hybrid note search, related notes, and image search using WebGPU or a local Ollama server; source build required, with no release package yet.

## Fine-tuning and Decision Models

- [EG2 Typed Decision](https://huggingface.co/mrm8488/embeddinggemma-2-ft-typed-decision) - EmbeddingGemma2 text encoder with a roughly 0.5M-parameter head for `choice`, `noul` (Boolean), and `score` decisions with probabilities; includes weights, inference code, and further fine-tuning examples.
- [Typed Decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - Training and evaluation data used by the model above, covering agent checks, support tickets, invoices, and security incidents; metrics measure agreement with teacher labels.
- [Typed Decision GGUF](https://huggingface.co/cstr/embeddinggemma-2-ft-typed-decision-GGUF) - Complete fine-tuned encoder and decision head in FP32/Q8 GGUF; requires CrispEmbed rather than stock llama.cpp, with only small-scale numerical parity checks reported.
- [Typed Decision Core ML](https://github.com/mikolaj92/embeddinggemma-typed-decisions-coreml) - Adaptation of the same fine-tuned model for macOS 15+ Apple silicon, without retraining; locally converted Core ML encoder uses CPU/Neural Engine with the original FP32 decision head on CPU, fixed token buckets, and overlength rejection.

The model author selected hyperparameters while inspecting the test split; its fine-tuned results are not directly comparable with the dataset's zero-shot leaderboard.

Core ML adaptation checked **2026-10-14** against its documentation and implementation; author-reported parity checks do not establish task accuracy or exclusive Neural Engine execution.

- [Multimodal Typed Decision](https://huggingface.co/Danny-Dasilva/embeddinggemma-2-multimodal-typed-decision) - EmbeddingGemma2 fine-tune for text, image, and video choice, Boolean, and ordinal decisions, with optional object-box localisation; requires the bundled runtime and is primarily English. Evaluation sets were reused during development, and some training data is non-commercial, research-only, or lacks a stated license.

- [Bharat-Embed 270M](https://huggingface.co/eulogik/bharat-embed-270m-gemma2) - Text-only LoRA fine-tune for Hindi and Hinglish retrieval, with [training and export code](https://github.com/eulogik/Bharat-Embed); trained at 256 tokens, with long-document behavior unmeasured.
- [EmbeddingGemma2 Korean](https://huggingface.co/jonpark0/embeddinggemma-2-ko) - Korean retrieval fine-tune blended with base weights, retaining multimodal inputs; requires Sentence Transformers 6.1+ and Transformers 5.18+, with a small Korean text-to-speech retrieval decline reported by the author.
- [eg2-transcribe](https://github.com/john-rocky/eg2-transcribe) - English speech transcription with a frozen EmbeddingGemma2 audio encoder and trained reader, targeting Android 8+ arm64 via LiteRT and iOS/macOS 27 via Core AI; requires building the app and downloading models separately, is trained on read English speech, and outputs no punctuation or capitalization.
- [Embed2ASR](https://github.com/tc3oliver/embed2asr) - Mandarin, English, and code-switching transcription using a frozen EmbeddingGemma2 audio encoder and a 9.66M-parameter GRU-CTC reader, with [reader weights](https://huggingface.co/tc3oliver/Embed2ASR-v1); requires the base encoder separately and supports offline transcription only, not streaming.
- [KolStream](https://huggingface.co/MaorB/embeddinggemma-2-asr-hebrew-english-streaming) - Hebrew and English file and streaming transcription using a partially fine-tuned EmbeddingGemma2 audio encoder, streaming reader, and transducer head; includes weights and inference code, requires the base encoder separately, and outputs no punctuation or capitalization.
- [norsk-asr](https://github.com/ahdrage/norsk-asr) - Norwegian Bokmål speech recognition using the EmbeddingGemma2 audio encoder and a CTC reader, with [weights](https://huggingface.co/ahdrage/norsk-asr); recordings only, lowercase unpunctuated output, optional KenLM files under CC BY-SA 4.0.
- [sea-asr](https://github.com/PixelML/sea-asr) - EmbeddingGemma2-based CTC speech recognition with [Indonesian](https://huggingface.co/PixelML/sea-asr-id) and [Tagalog/Taglish](https://huggingface.co/PixelML/sea-asr-ph) weights, word timestamps, and SRT/VTT export on CPU or CUDA; downloads the base encoder separately and outputs lowercase text without punctuation.
- [Turkish STT](https://huggingface.co/mstkyvz/embeddinggemma2-turkish-stt) - Turkish transcription using EmbeddingGemma2 with a character CTC reader, detachable LoRA, and optional KenLM; provides CC BY-SA 4.0 weights and language model with Apache-2.0 training code, requires the base model, has no streaming, and outputs lowercase text without punctuation; disable LoRA for original embedding behavior.
- [African speech-retrieval LoRA](https://huggingface.co/naijaml/embeddinggemma-2-african-speech-lora) - Adapter trained on six African languages for same-language speech/text retrieval; requires the base model and does not transcribe or translate.

Bharat-Embed checked **2026-10-14** against its model card, configuration, and published files; author evaluations were not reproduced locally.

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
- [Official multimodal fine-tuning guide](https://ai.google.dev/gemma/docs/embeddinggemma/fine-tuning-multimodal-embeddinggemma-with-sentence-transformers) - Text-to-image retrieval training with cross-modal triplets and Sentence Transformers, including before/after evaluation; requires a BF16-capable GPU.
- [Transformers model documentation](https://huggingface.co/docs/transformers/model_doc/embedding_gemma2) - Lower-level model and processor APIs.
- [Minimal multimodal search](https://github.com/ranjankndev/embeddinggemma2-search) - A small Python example for local text, image, audio, and video retrieval using NumPy vectors, without a database or UI.
- [Gemma-Lens](https://github.com/johnrobinsn/gemma-lens) - Text, microphone, and image-query demo over COCO images and ESC-50 audio using direct cosine search, with a [step-by-step article](https://www.storminthecastle.com/posts/gemma_lens/); runs on CPU or CUDA, and ESC-50 audio is non-commercial.
- [UI Search](https://github.com/sai-prakash/ui-screenshot-search) - Browser text/screenshot search across sample components, IBM Carbon, and GitHub Primer, with a reusable Storybook indexer; screenshot retrieval accuracy remains unmeasured.

The Sentence Transformers tutorials require **6.1.0+**.

## Models and runtimes

| Resource                                                                                                          | Route                                | Notes                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Google checkpoint](https://huggingface.co/google/embeddinggemma-2)                                               | Sentence Transformers / Transformers | Reference weights; disable unused encoders for smaller workloads.                                                                        |
| [ONNX Community conversion](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX)                          | Transformers.js                      | Browser/Node.js examples and backend/dtype guidance.                                                                                     |
| [LiteRT text, 270M](https://huggingface.co/litert-community/embeddinggemma-2-text-270m-litert-lm)                 | LiteRT-LM                            | Text-only artifact.                                                                                                                      |
| [LiteRT text + vision, 440M](https://huggingface.co/litert-community/embeddinggemma-2-text-vision-440m-litert-lm) | LiteRT-LM                            | Vision-enabled artifact; see supported-input table.                                                                                      |
| [LiteRT full model, 740M](https://huggingface.co/litert-community/embeddinggemma-2-740m-litert-lm)                | LiteRT-LM                            | Full multimodal artifact and deployment instructions.                                                                                    |
| [LiteRT text + audio, 570M](https://huggingface.co/Luigi/embeddinggemma-2-570m-text-audio-litert-lm)              | LiteRT-LM                            | Community repack of the full model without the vision encoder; text/audio only, with a build manifest.                                   |
| [MLX Community collection](https://huggingface.co/collections/mlx-community/embeddinggemma-2)                     | Apple silicon                        | Conversion collection; inspect model cards for runtime/modality support.                                                                 |
| [FluidInference Core ML](https://huggingface.co/FluidInference/embeddinggemma-2-coreml)                           | Apple Neural Engine / GPU            | Text on Neural Engine, image/audio on GPU; macOS 15 / iOS 18+, text limited to 512 tokens and audio to 10-second windows.                |
| [EverPaper Core AI](https://huggingface.co/EverPaper/embeddinggemma-2-coreai)                                     | macOS 27+ / Apple silicon            | Text, image, and audio conversion with Swift/Python runners; Neural Engine/GPU routes, 2,048-token text cap and 30-second audio windows. |


EverPaper conversion checked **2026-10-15** against its model card and published assets; runtime and author-reported numerical checks were not reproduced locally.


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
- [eg2npu](https://github.com/daaku/eg2npu) - OpenVINO text embedding server for Intel NPU using EmbeddingGemma2 GGUF weights and a llama-server-compatible API; no image/audio inputs, and the packaged system service is limited to 64-token queries.

- [OpenVLCLIP](https://github.com/kotadymo/openvlclip) - Unofficial Python library for EmbeddingGemma2 image/text encoding and optional video-frame search on CPU or CUDA through Transformers; offers an OpenCLIP-inspired API, not a drop-in replacement, and requires Python 3.12–3.14 excluding 3.14.1. Formerly openclip-gemma; the [migration guide](https://github.com/kotadymo/openvlclip/blob/main/docs/migration-v0.5.0.md) requires changing the package and imports, with no old import alias.

- [ComfyUI-EmbeddingGemma2](https://github.com/hiroki-abe-58/ComfyUI-EmbeddingGemma2) - Unofficial ComfyUI nodes for text, image, video, and audio similarity and image ranking; requires the V3 node API and separate model download, uses only the first 30 seconds of audio and at most 32 video frames, and may conflict with nodes requiring huggingface-hub 2.x.

- [embeddinggemma2-rust](https://github.com/Dalailalama/embeddinggemma2-rust) - Unofficial Rust text, image, audio, and video embeddings on CPU or CUDA, with CLI and OpenAI-compatible HTTP serving; requires separate weights, CUDA 13.x libraries for GPU use, WAV audio inputs, and FFmpeg for MP4 decoding.

- [EmbeddingGemma2 for Unity](https://github.com/ayutaz/unity-embeddinggemma-2) - Text, image, and audio embeddings via Unity 6000.3.21f1 and Sentis 2.6.1 GPUCompute; Windows Editor/Player only, separate model downloads, fixed media inputs, and no automatic CPU fallback; initial supported configuration uses 64 GB RAM and 16 GB VRAM.

## Practical notes

- Use task-specific prefixes from the [model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2); query and document prefixes differ.
- Re-normalize truncated vectors and maintain matching query/document dimensions. Validate 128d carefully for multimodal retrieval.
- Use BF16 or FP32 (not FP16) for reference weights. See [dtype guidance](https://huggingface.co/onnx-community/embeddinggemma-2-ONNX) for converted runtimes.
- Modalities share the 8,192-token budget. Follow [multimodal preprocessing](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers) before chunking audio or sampling video.

## Evaluation

The [official benchmark tables](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2#benchmark-results) report publisher results for text, code, image, visual-document, video, audio, and truncated dimensions. Community benchmark submission requirements are detailed in [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to suggest second-generation resources or benchmarks.
