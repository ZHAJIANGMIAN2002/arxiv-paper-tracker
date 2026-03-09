# VLN (Vision-and-Language Navigation) 论文追踪

> 自动从 Arxiv 抓取最新 VLN 相关论文，每日更新
> 
> 最后更新: 2026-03-09 11:24:44

---

## 2026-03-09 更新 (共 52 篇新论文)

### History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation

- **发布日期**: 2026-03-06
- **作者**: Qitong Wang, Yijun Liang, Ming Li, Tianyi Zhou, Christopher Rasmussen
- **分类**: cs.RO
- **Arxiv**: [2603.06480v1](http://arxiv.org/abs/2603.06480v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06480v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) enables robots to follow natural-language instructions in visually grounded environments, serving as a key capability for embodied robotic systems. Recent Vision-Language-Action (VLA) models have demonstrated strong navigation performance, but their high computational cost introduces latency that limits real-time deployment. We propose a training-free spatio-temporal vision token pruning framework tailored to VLA-based VLN. We apply spatial token selection to the current view, alongside spatio-temporal compression for historical memories, enabling efficient long-horizon inference while reducing redundant computation. Leveraging attention-based token importance and query-guided spatio-temporal filtering, the proposed approach preserves navigation-relevant information without retraining or modifying pretrained models, allowing plug-and-play integration into existing VLA systems. Through experiments on standard VLN benchmarks, we confirm that our method significantly outperforms existing pruning strategies. It successfully preserves superior navigation accuracy under extreme pruning scenarios, all while maintaining the highly competitive inference efficiency. Real-world deployment on a Unitree Go2 quadruped robot further validates reliable and low-latency instruction-following navigation under practical robotic constraints. We hope this work helps bridge the gap between large-scale multimodal modeling and efficient, real-time embodied deployment in robotic navigation systems.

**摘要 (中文翻译):**

> 视觉语言导航 (VLN) 使机器人能够在视觉环境中遵循自然语言指令，这是实体机器人系统的一项关键功能。最近的视觉-语言-动作（VLA）模型表现出了强大的导航性能，但其高计算成本会带来限制实时部署的延迟。我们提出了一个针对基于 VLA 的 VLN 量身定制的免训练时空视觉令牌修剪框架。我们将空间标记选择应用于当前视图，同时对历史记忆进行时空压缩，从而实现高效的长范围推理，同时减少冗余计算。利用基于注意力的标记重要性和查询引导的时空过滤，所提出的方法保留了导航相关信息，而无需重新训练或修改预训练模型，从而允许即插即用集成到现有的 VLA 系统中。通过对标准 VLN 基准的实验，我们确认我们的方法明显优于现有的剪枝策略。它成功地在极端剪枝场景下保持了卓越的导航精度，同时保持了极具竞争力的推理效率。在 Unitree Go2 四足机器人上的实际部署进一步验证了在实际机器人约束下的可靠且低延迟的指令跟踪导航。我们希望这项工作有助于弥合大规模多模态建模与机器人导航系统中高效、实时的具体部署之间的差距。

---

### REACT++: Efficient Cross-Attention for Real-Time Scene Graph Generation

- **发布日期**: 2026-03-06
- **作者**: Maëlic Neau, Zoe Falomir
- **分类**: cs.CV
- **Arxiv**: [2603.06386v1](http://arxiv.org/abs/2603.06386v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06386v1)

**Abstract (English):**

> Scene Graph Generation (SGG) is a task that encodes visual relationships between objects in images as graph structures. SGG shows significant promise as a foundational component for downstream tasks, such as reasoning for embodied agents. To enable real-time applications, SGG must address the trade-off between performance and inference speed. However, current methods tend to focus on one of the following: (1) improving relation prediction accuracy, (2) enhancing object detection accuracy, or (3) reducing latency, without aiming to balance all three objectives simultaneously. To address this limitation, we build on the powerful Real-time Efficiency and Accuracy Compromise for Tradeoffs in Scene Graph Generation (REACT) architecture and propose REACT++, a new state-of-the-art model for real-time SGG. By leveraging efficient feature extraction and subject-to-object cross-attention within the prototype space, REACT++ balances latency and representational power. REACT++ achieves the highest inference speed among existing SGG models, improving relation prediction accuracy without sacrificing object detection performance. Compared to the previous REACT version, REACT++ is 20% faster with a gain of 10% in relation prediction accuracy on average. The code is available at https://github.com/Maelic/SGG-Benchmark.

**摘要 (中文翻译):**

> 场景图生成（SGG）是将图像中对象之间的视觉关系编码为图结构的任务。 SGG 作为下游任务的基础组件显示出巨大的前景，例如实体代理的推理。为了实现实时应用程序，SGG 必须解决性能和推理速度之间的权衡。然而，当前的方法往往侧重于以下之一：（1）提高关系预测准确性，（2）提高对象检测准确性，或（3）减少延迟，而不是同时平衡所有三个目标。为了解决这个限制，我们建立在场景图生成（REACT）架构中强大的实时效率和准确性折衷权衡的基础上，并提出了 REACT++，这是一种新的最先进的实时 SGG 模型。通过在原型空间中利用高效的特征提取和主体到客体的交叉注意力，REACT++ 平衡了延迟和表征能力。 REACT++实现了现有SGG模型中最高的推理速度，在不牺牲目标检测性能的情况下提高了关系预测的准确性。与之前的 REACT 版本相比，REACT++ 速度提高了 20%，关系预测准确率平均提高了 10%。该代码可从 https://github.com/Maelic/SGG-Benchmark 获取。

---

### HiPP-Prune: Hierarchical Preference-Conditioned Structured Pruning for Vision-Language Models

- **发布日期**: 2026-03-06
- **作者**: Lincen Bai, Hedi Tabia, Raul Santos-Rodriguez
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2603.06270v1](http://arxiv.org/abs/2603.06270v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06270v1)

**Abstract (English):**

> Pruning vision-language models (VLMs) for efficient deployment is challenging because compression can affect not only task utility but also visual grounding, often amplifying object hallucinations even at the same sparsity level. We present HiPP-Prune, a hierarchical preference-conditioned structured pruning framework that treats pruning as conditional resource allocation under multiple objectives. HiPP-Prune makes plan-level decisions: a single policy invocation outputs a global pruning blueprint by factorizing decisions into an overall sparsity budget and a layer-wise allocation, enabling queryable trade-offs via a user-specified preference vector. To account for VLM-specific failure modes, our policy state integrates a visual sensitivity signal derived from attention flow between vision tokens and language hidden states, discouraging over-pruning of vision-critical layers that facilitate cross-modal fusion. We optimize pruning plans with plan-level Group Relative Policy Optimization (GRPO) under a multi-objective return that combines task utility, hallucination robustness (POPE), compression, and a synaptic-flow-inspired stability proxy to reduce unproductive exploration in high-sparsity regimes. Experiments on LLaVA with POPE and ScienceQA demonstrate that HiPP-Prune discovers diverse non-dominated pruning plans and provides controllable robustness--utility trade-offs under matched sparsity budgets.

**摘要 (中文翻译):**

> 修剪视觉语言模型（VLM）以实现高效部署具有挑战性，因为压缩不仅会影响任务效用，还会影响视觉基础，即使在相同的稀疏水平下，通常也会放大物体幻觉。我们提出了 HiPP-Prune，一种分层偏好条件结构化剪枝框架，它将剪枝视为多个目标下的条件资源分配。 HiPP-Prune 做出计划级决策：单个策略调用通过将决策分解为整体稀疏预算和分层分配来输出全局修剪蓝图，从而通过用户指定的偏好向量实现可查询的权衡。为了解决 VLM 特定的故障模式，我们的策略状态集成了从视觉标记和语言隐藏状态之间的注意力流派生的视觉敏感度信号，阻止对促进跨模式融合的视觉关键层的过度修剪。我们在多目标回报下使用计划级组相对策略优化（GRPO）来优化剪枝计划，该回报结合了任务效用、幻觉鲁棒性（POPE）、压缩和突触流启发的稳定性代理，以减少高稀疏状态下的无效探索。使用 POPE 和 ScienceQA 在 LLaVA 上进行的实验表明，HiPP-Prune 发现了多种非支配修剪计划，并提供了可控的鲁棒性——在匹配的稀疏预算下的效用权衡。

---

### DreamToNav: Generalizable Navigation for Robots via Generative Video Planning

- **发布日期**: 2026-03-06
- **作者**: Valerii Serpiva, Jeffrin Sam, Chidera Simon, Hajira Amjad, Iana Zhura, Artem Lykov, Dzmitry Tsetserukou
- **分类**: cs.RO
- **Arxiv**: [2603.06190v1](http://arxiv.org/abs/2603.06190v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06190v1)

**Abstract (English):**

> We present DreamToNav, a novel autonomous robot framework that uses generative video models to enable intuitive, human-in-the-loop control. Instead of relying on rigid waypoint navigation, users provide natural language prompts (e.g. ``Follow the person carefully''), which the system translates into executable motion. Our pipeline first employs Qwen 2.5-VL-7B-Instruct to refine vague user instructions into precise visual descriptions. These descriptions condition NVIDIA Cosmos 2.5, a state-of-the-art video foundation model, to synthesize a physically consistent video sequence of the robot performing the task. From this synthetic video, we extract a valid kinematic path using visual pose estimation, robot detection and trajectory recovery. By treating video generation as a planning engine, DreamToNav allows robots to visually "dream" complex behaviors before executing them, providing a unified framework for obstacle avoidance and goal-directed navigation without task-specific engineering. We evaluate the approach on both a wheeled mobile robot and a quadruped robot in indoor navigation tasks. DreamToNav achieves a success rate of 76.7%, with final goal errors typically within 0.05-0.10 m and trajectory tracking errors below 0.15 m. These results demonstrate that trajectories extracted from generative video predictions can be reliably executed on physical robots across different locomotion platforms.

**摘要 (中文翻译):**

> 我们推出了 DreamToNav，这是一种新颖的自主机器人框架，它使用生成视频模型来实现直观的人机交互控制。用户不再依赖严格的路径点导航，而是提供自然语言提示（例如“小心地跟随这个人”），系统将其转换为可执行的动作。我们的流程首先采用 Qwen 2.5-VL-7B-Instruct 将模糊的用户指令细化为精确的视觉描述。这些描述以最先进的视频基础模型 NVIDIA Cosmos 2.5 为条件，合成执行任务的机器人的物理一致的视频序列。从这个合成视频中，我们使用视觉姿态估计、机器人检测和轨迹恢复来提取有效的运动路径。通过将视频生成视为规划引擎，DreamToNav 允许机器人在执行复杂行为之前以视觉方式“想象”复杂行为，从而为避障和目标导向导航提供统一的框架，而无需特定于任务的工程。我们在室内导航任务中评估轮式移动机器人和四足机器人的方法。 DreamToNav 的成功率为 76.7%，最终目标误差通常在 0.05-0.10 m 以内，轨迹跟踪误差低于 0.15 m。这些结果表明，从生成视频预测中提取的轨迹可以在跨不同运动平台的物理机器人上可靠地执行。

---

### DeepSight: Bridging Depth Maps and Language with a Depth-Driven Multimodal Model

- **发布日期**: 2026-03-06
- **作者**: Hao Yang, Hongbo Zhang, Yanyan Zhao, Bing Qin
- **分类**: cs.CV, cs.CL
- **Arxiv**: [2603.06090v1](http://arxiv.org/abs/2603.06090v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06090v1)

**Abstract (English):**

> Multimodal large language models (MLLMs) have achieved impressive performance across various tasks such as image captioning and visual question answer(VQA); however, they often struggle to accurately interpret depth information inherent in visual data. In this work, we introduce DeepSight, the first dedicated depth MLLM designed to enhance three-dimensional scene understanding. Unlike conventional methods that align RGB image encodings with text, our approach takes advantage of the unique characteristics of depth images: single-channel grayscale images where the pixel values directly reflect depth cues to improve spatial reasoning. To address challenges associated with limited depth data and the inadequacy of simple channel replication, we construct a novel depth image-text pair dataset and a depth instruction dataset. Depth maps are generated from visual images using the GLPN model, and GPT-4 is employed to curate corresponding depth instructions, an approach validated by LLaVA. Additionally, we modify the ViT encoder in CLIP to incorporate local object information, thereby capturing the subtle continuous variations of depth more effectively. To evaluate the performance of our model, we develop a comprehensive depth question answer benchmark based on existing depth image datasets, which rigorously assesses understanding in typical depth map scenarios. Experimental results demonstrate that DeepSight significantly enhances depth perception and downstream task performance, marking a substantial step forward in multimodal three-dimensional understanding.

**摘要 (中文翻译):**

> 多模态大语言模型（MLLM）在图像字幕和视觉问答（VQA）等各种任务中取得了令人印象深刻的性能；然而，他们常常难以准确地解释视觉数据中固有的深度信息。在这项工作中，我们介绍了 DeepSight，这是第一个专用深度 MLLM，旨在增强三维场景理解。与将 RGB 图像编码与文本对齐的传统方法不同，我们的方法利用了深度图像的独特特征：单通道灰度图像，其中像素值直接反映深度线索，以改进空间推理。为了解决与有限深度数据和简单通道复制的不足相关的挑战，我们构建了一个新颖的深度图像文本对数据集和深度指令数据集。深度图是使用 GLPN 模型从视觉图像生成的，并采用 GPT-4 来管理相应的深度指令，这是一种经过 LLaVA 验证的方法。此外，我们修改了 CLIP 中的 ViT 编码器以合并局部对象信息，从而更有效地捕获深度的微妙连续变化。为了评估我们模型的性能，我们基于现有深度图像数据集开发了一个全面的深度问答基准，该基准严格评估对典型深度图场景的理解。实验结果表明，DeepSight 显着增强了深度感知和下游任务性能，标志着多模态三维理解向前迈出了实质性的一步。

---

### Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning

- **发布日期**: 2026-03-06
- **作者**: Cristiano Battistini, Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
- **分类**: cs.RO
- **Arxiv**: [2603.06084v1](http://arxiv.org/abs/2603.06084v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06084v1)

**Abstract (English):**

> Large and small language models have been widely used for robotic task planning. At the same time, vision-language models (VLMs) have successfully tackled problems such as image captioning, scene understanding, and visual question answering. In this work, we combine these two approaches by deploying a compact, open-source multimodal model to generate behavior trees for robotic task planning. The main obstacle to achieving this goal is the lack of an existing dataset that links visual observations and instructions to executable behavior trees. We propose a method to construct such a dataset starting from existing robotic episodes (i.e., Open X-Embodiment), in which a large model serves as a teacher in a multi-stage generation pipeline. We use this dataset to fine-tune VLMs ranging from 500M to 4B parameters via parameter-efficient fine-tuning (PEFT). The generated behavior trees, compatible with the BehaviorTree.CPP library, are evaluated both offline, using structural and lexical metrics, and online through the execution of household tasks in a state-of-the-art embodied simulator. Our results demonstrate that our fine-tuned 4B-parameter VLM approaches the performance of state-of-the-art closed-source models, achieving an 87\% success rate while requiring only a fraction of the computational resources.

**摘要 (中文翻译):**

> 大小语言模型已广泛用于机器人任务规划。与此同时，视觉语言模型（VLM）已经成功解决了图像字幕、场景理解和视觉问答等问题。在这项工作中，我们通过部署紧凑的开源多模式模型来结合这两种方法，以生成用于机器人任务规划的行为树。实现这一目标的主要障碍是缺乏将视觉观察和指令链接到可执行行为树的现有数据集。我们提出了一种从现有机器人情节（即 Open X-Embodiment）开始构建此类数据集的方法，其中大型模型充当多阶段生成管道中的教师。我们使用该数据集通过参数高效微调 (PEFT) 来微调 VLM，参数范围从 500M 到 4B。生成的行为树与BehaviorTree.CPP库兼容，可以使用结构和词汇指标进行离线评估，也可以通过在最先进的具体模拟器中执行家庭任务进行在线评估。我们的结果表明，我们经过微调的 4B 参数 VLM 接近最先进的闭源模型的性能，仅需要一小部分计算资源，即可实现 87% 的成功率。

---

### Lifelong Embodied Navigation Learning

- **发布日期**: 2026-03-06
- **作者**: Xudong Wang, Jiahua Dong, Baichen Liu, Qi Lyu, Lianqing Liu, Zhi Han
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2603.06073v1](http://arxiv.org/abs/2603.06073v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06073v1)

**Abstract (English):**

> Embodied navigation agents powered by large language models have shown strong performance on individual tasks but struggle to continually acquire new navigation skills, which suffer from catastrophic forgetting. We formalize this challenge as lifelong embodied navigation learning (LENL), where an agent is required to adapt to a sequence of navigation tasks spanning multiple scenes and diverse user instruction styles, while retaining previously learned knowledge. To tackle this problem, we propose Uni-Walker, a lifelong embodied navigation framework that decouples navigation knowledge into task-shared and task-specific components with Decoder Extension LoRA (DE-LoRA). To learn the shared knowledge, we design a knowledge inheritance strategy and an experts co-activation strategy to facilitate shared knowledge transfer and refinement across multiple navigation tasks. To learn the specific knowledge, we propose an expert subspace orthogonality constraint together and a navigation-specific chain-of-thought reasoning mechanism to capture specific knowledge and enhance instruction-style understanding. Extensive experiments demonstrate the superiority of Uni-Walker for building universal navigation agents with lifelong learning.

**摘要 (中文翻译):**

> 由大型语言模型支持的具体导航代理在单个任务上表现出了强大的性能，但很难不断获得新的导航技能，而这些技能会遭受灾难性的遗忘。我们将这一挑战形式化为终身体现导航学习（LENL），其中代理需要适应跨越多个场景和不同用户指令风格的一系列导航任务，同时保留以前学到的知识。为了解决这个问题，我们提出了 Uni-Walker，这是一个终身体现的导航框架，它通过解码器扩展 LoRA (DE-LoRA) 将导航知识解耦为任务共享和特定于任务的组件。为了学习共享知识，我们设计了知识继承策略和专家共同激活策略，以促进跨多个导航任务的共享知识转移和细化。为了学习特定知识，我们提出了专家子空间正交约束和导航特定的思想链推理机制，以捕获特定知识并增强指令式理解。大量实验证明了 Uni-Walker 在构建具有终身学习能力的通用导航代理方面的优越性。

---

### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

- **发布日期**: 2026-03-06
- **作者**: Ninghao Zhang, Bin Zhu, Shijie Zhou, Jingjing Chen
- **分类**: cs.RO, cs.AI, cs.CV
- **Arxiv**: [2603.06001v1](http://arxiv.org/abs/2603.06001v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.06001v1)

**Abstract (English):**

> Vision-Language-Action (VLA) models enable robots to perform manipulation tasks directly from natural language instructions and are increasingly viewed as a foundation for generalist robotic policies. However, their reliability under Out-of-Distribution (OOD) instructions remains underexplored. In this paper, we reveal a critical failure mode in which VLA policies continue executing visually plausible actions even when the language instruction contradicts the scene. We refer to this phenomenon as linguistic blindness, where VLA policies prioritize visual priors over instruction semantics during action generation. To systematically analyze this issue, we introduce ICBench, a diagnostic benchmark constructed from the LIBERO dataset that probes language-action coupling by injecting controlled OOD instruction contradictions while keeping the visual environment unchanged. Evaluations on three representative VLA architectures, including Pi0, Pi0.5 and OpenVLA OFT, show that these models frequently succeed at tasks despite logically impossible instructions, revealing a strong visual bias in action generation. To mitigate this issue, we propose Instruction-Guided Attention Recalibration (IGAR), a train-free inference-time mechanism that rebalances attention distributions to restore the influence of language instructions. IGAR operates without retraining or architectural modification and can be directly applied to existing VLA models. Experiments across 30 LIBERO tasks demonstrate that IGAR substantially reduces erroneous execution under OOD contradictory instructions while preserving baseline task performance. We additionally validate the approach on a real Franka robotic arm, where IGAR effectively prevents manipulation triggered by inconsistent instructions.

**摘要 (中文翻译):**

> 视觉-语言-动作（VLA）模型使机器人能够直接根据自然语言指令执行操作任务，并且越来越多地被视为通用机器人策略的基础。然而，它们在分发外 (OOD) 指令下的可靠性仍未得到充分研究。在本文中，我们揭示了一种严重的故障模式，其中即使语言指令与场景相矛盾，VLA 策略仍会继续执行视觉上合理的操作。我们将这种现象称为语言失明，其中 VLA 策略在动作生成过程中优先考虑视觉先验而不是指令语义。为了系统地分析这个问题，我们引入了 ICBench，这是一个根据 LIBERO 数据集构建的诊断基准，它通过注入受控的 OOD 指令矛盾来探测语言-动作耦合，同时保持视觉环境不变。对三种代表性 VLA 架构（包括 Pi0、Pi0.5 和 OpenVLA OFT）的评估表明，尽管逻辑上不可能的指令，这些模型经常成功完成任务，揭示了动作生成中的强烈视觉偏差。为了缓解这个问题，我们提出了指令引导注意力重新校准（IGAR），这是一种无需训练的推理时间机制，可以重新平衡注意力分布以恢复语言指令的影响。 IGAR 无需重新训练或架构修改即可运行，并且可以直接应用于现有的 VLA 模型。 30 个 LIBERO 任务的实验表明，IGAR 大大减少了 OOD 矛盾指令下的错误执行，同时保持基准任务性能。我们还在真正的 Franka 机械臂上验证了该方法，其中 IGAR 有效防止由不一致的指令触发的操作。

---

### MagRobot:An Open Simulator for Magnetically Navigated Robots

- **发布日期**: 2026-03-06
- **作者**: Heng Wang, Haoyu Song, Jiatao Zheng, Yuxiang Han, Kunli Wang
- **单位**: South China University of Technology
- **分类**: cs.RO
- **Arxiv**: [2603.05992v1](http://arxiv.org/abs/2603.05992v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05992v1)

**Abstract (English):**

> Magnetic navigation systems, including magnetic tracking systems and magnetic actuation systems, have shown great potential for occlusion-free localization and remote control of intracorporeal medical devices and robots in minimally invasive medicine, such as capsule endoscopy and cardiovascular intervention. However, the design of magnetically navigated robots remains heavily reliant on experimental prototyping, which is time-consuming and costly. Furthermore, there is a lack of a consistent experimental environment to compare and benchmark the hardware and algorithms across different magnetic navigation systems. To address these challenges, we propose the first universal open-source simulation platform to facilitate research, design and benchmarking of magnetically navigated robots. Our simulator features an intuitive graphical user interface that enables the user to efficiently design, visualize, and analyze magnetic navigation systems for both rigid and soft robots. The proposed simulator is versatile, which can simulate both magnetic actuation and magnetic tracking tasks in diverse medical applications that involve deformable anatomies. The proposed simulator provides an open development environment, where the user can load third-party anatomical models and customize both hardware and algorithms of magnetic navigation systems. The fidelity of the simulator is validated using both phantom and ex vivo experiments of magnetic navigation of a continuum robot and a capsule robot with diverse magnetic actuation setups. Three use cases of the simulator, i.e., bronchoscopy, endovascular intervention, and gastrointestinal endoscopy, are implemented to demonstrate the functionality of the simulator. It is shown that the configuration and algorithms of magnetic navigation systems can be flexibly designed and optimized for better performance using the simulator.

**摘要 (中文翻译):**

> 磁导航系统，包括磁跟踪系统和磁驱动系统，在胶囊内窥镜和心血管介入等微创医学中的体内医疗设备和机器人的无遮挡定位和远程控制方面显示出了巨大的潜力。然而，磁导航机器人的设计仍然严重依赖实验原型设计，这既耗时又昂贵。此外，缺乏一致的实验环境来比较和基准测试不同磁导航系统的硬件和算法。为了应对这些挑战，我们提出了第一个通用开源仿真平台，以促进磁导航机器人的研究、设计和基准测试。我们的模拟器具有直观的图形用户界面，使用户能够有效地设计、可视化和分析刚性和软体机器人的磁导航系统。所提出的模拟器是多功能的，可以模拟涉及可变形解剖结构的各种医疗应用中的磁驱动和磁跟踪任务。所提出的模拟器提供了一个开放的开发环境，用户可以加载第三方解剖模型并定制磁导航系统的硬件和算法。使用连续体机器人和具有不同磁驱动设置的胶囊机器人的磁导航的体模和离体实验来验证模拟器的保真度。模拟器的三个用例，即支气管镜检查、血管内介入和胃肠内窥镜检查，被用来演示模拟器的功能。结果表明，使用模拟器可以灵活设计和优化磁导航系统的配置和算法，以获得更好的性能。

---

### Improved hopping control on slopes for small robots using spring mass modeling

- **发布日期**: 2026-03-06
- **作者**: Heston Roberts, Pronoy Sarker, Sm Ashikul Islam, Min Gyu Kim
- **分类**: cs.RO, eess.SY
- **Arxiv**: [2603.05902v1](http://arxiv.org/abs/2603.05902v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05902v1)

**Abstract (English):**

> Hopping robots often lose balance on slopes because the tilted ground creates unwanted rotation at landing. This work analyzes that effect using a simple spring mass model and identifies how slope induced impulses destabilize the robot. To address this, we introduce two straightforward fixes, adjusting the bodys touchdown angle based on the slope and applying a small corrective torque before takeoff. Together, these steps effectively cancel the unwanted rotation caused by inclined terrain, allowing the robot to land smoothly and maintain stable hopping even on steep slopes. Moreover, the proposed method remains simple enough to implement on low cost robotic platforms without requiring complex sensing or computation. By combining this analytical model with minimal control actions, this approach provides a practical path toward reliable hopping on uneven terrain. The results from simulation confirm that even small slope aware adjustments can dramatically improve landing stability, making the technique suitable for future autonomous field robots that must navigate natural environments such as hills, rubble, and irregular outdoor landscapes.

**摘要 (中文翻译):**

> 跳跃机器人在斜坡上经常失去平衡，因为倾斜的地面在着陆时会产生不必要的旋转。这项工作使用简单的弹簧质量模型分析了这种影响，并确定了斜坡引起的脉冲如何使机器人不稳定。为了解决这个问题，我们引入了两个简单的修复方法，根据坡度调整机身的接地角度，并在起飞前施加一个小的校正扭矩。这些步骤共同有效地消除了倾斜地形引起的不必要的旋转，使机器人能够平稳着陆，即使在陡坡上也能保持稳定的跳跃。此外，所提出的方法仍然足够简单，可以在低成本机器人平台上实施，而不需要复杂的传感或计算。通过将该分析模型与最少的控制操作相结合，该方法提供了一条在不平坦地形上实现可靠跳跃的实用路径。仿真结果证实，即使是很小的坡度感知调整也可以显着提高着陆稳定性，使得该技术适用于必须在山丘、瓦砾和不规则户外景观等自然环境中导航的未来自主现场机器人。

---

### Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning

- **发布日期**: 2026-03-06
- **作者**: Xuan Li, Zhanke Zhou, Zongze Li, Jiangchao Yao, Yu Rong, Lu Zhang, Bo Han
- **分类**: cs.LG, cs.AI
- **Arxiv**: [2603.05900v1](http://arxiv.org/abs/2603.05900v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05900v1)

**Abstract (English):**

> Large language models (LLMs) benefit substantially from supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR) in reasoning tasks. However, these recipes perform poorly in instruction-based molecular optimization, where each data point typically provides only a single optimized reference molecule and no step-by-step optimization trajectory. We reveal that answer-only SFT on the reference molecules collapses reasoning, and RLVR provides sparse feedback under similarity constraints due to the model's lack of effective exploration, which slows learning and limits optimization. To encourage the exploration of new molecules while balancing the exploitation of the reference molecules, we introduce Reference-guided Policy Optimization (RePO), an optimization approach that learns from reference molecules without requiring trajectory data. At each update, RePO samples candidate molecules with their intermediate reasoning trajectories from the model and trains the model using verifiable rewards that measure property satisfaction under similarity constraints in an RL manner. Meanwhile, it applies reference guidance by keeping the policy's intermediate reasoning trajectory as context and training only the answer in a supervised manner. Together, the RL term promotes exploration, while the guidance term mitigates reward sparsity and stabilizes training by grounding outputs to references when many valid molecular edits exist. Across molecular optimization benchmarks, RePO consistently outperforms SFT and RLVR baselines (e.g., GRPO), achieving improvements on the optimization metric (Success Rate $\times$ Similarity), improving balance across competing objectives, and generalizing better to unseen instruction styles. Our code is publicly available at https://github.com/tmlr-group/RePO.

**摘要 (中文翻译):**

> 大型语言模型（LLM）从推理任务中的监督微调（SFT）和具有可验证奖励的强化学习（RLVR）中受益匪浅。然而，这些方法在基于指令的分子优化中表现不佳，其中每个数据点通常仅提供单个优化的参考分子，并且没有逐步的优化轨迹。我们发现，参考分子上的仅答案 SFT 会破坏推理，并且由于模型缺乏有效的探索，RLVR 在相似性约束下提供稀疏反馈，从而减慢了学习速度并限制了优化。为了鼓励探索新分子，同时平衡参考分子的利用，我们引入了参考引导策略优化（RePO），这是一种无需轨迹数据即可从参考分子中学习的优化方法。每次更新时，RePO 都会从模型中对候选分子及其中间推理轨迹进行采样，并使用可验证的奖励来训练模型，这些奖励以 RL 方式在相似性约束下测量属性满意度。同时，它通过将策略的中间推理轨迹作为上下文并以监督的方式仅训练答案来应用参考指导。总之，RL 术语促进探索，而指导术语则在存在许多有效的分子编辑时通过将输出接地到参考来减轻奖励稀疏性并稳定训练。在分子优化基准中，RePO 始终优于 SFT 和 RLVR 基线（例如 GRPO），实现了优化指标（成功率 $\times$ 相似度）的改进，改善了竞争目标之间的平衡，并更好地概括了未见过的指令风格。我们的代码可在 https://github.com/tmlr-group/RePO 上公开获取。

---

### Safe-SAGE: Social-Semantic Adaptive Guidance for Safe Engagement through Laplace-Modulated Poisson Safety Functions

- **发布日期**: 2026-03-05
- **作者**: Lizhi Yang, Ryan M. Bena, Meg Wilkinson, Gilbert Bahati, Andy Navarro Brenes, Ryan K. Cosner, Aaron D. Ames
- **分类**: cs.RO
- **Arxiv**: [2603.05497v2](http://arxiv.org/abs/2603.05497v2)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05497v2)

**Abstract (English):**

> Traditional safety-critical control methods, such as control barrier functions, suffer from semantic blindness, exhibiting the same behavior around obstacles regardless of contextual significance. This limitation leads to the uniform treatment of all obstacles, despite their differing semantic meanings. We present Safe-SAGE (Social-Semantic Adaptive Guidance for Safe Engagement), a unified framework that bridges the gap between high-level semantic understanding and low-level safety-critical control through a Poisson safety function (PSF) modulated using a Laplace guidance field. Our approach perceives the environment by fusing multi-sensor point clouds with vision-based instance segmentation and persistent object tracking to maintain up-to-date semantics beyond the camera's field of view. A multi-layer safety filter is then used to modulate system inputs to achieve safe navigation using this semantic understanding of the environment. This safety filter consists of both a model predictive control layer and a control barrier function layer. Both layers utilize the PSF and flux modulation of the guidance field to introduce varying levels of conservatism and multi-agent passing norms for different obstacles in the environment. Our framework enables legged robots to safely navigate semantically rich, dynamic environments with context-dependent safety margins.

**摘要 (中文翻译):**

> 传统的安全关键控制方法（例如控制屏障功能）存在语义盲目性，无论上下文的意义如何，在障碍物周围都会表现出相同的行为。这种限制导致对所有障碍的统一处理，尽管它们的语义含义不同。我们提出了 Safe-SAGE（安全参与的社会语义自适应指导），这是一个统一的框架，通过使用拉普拉斯指导场调制的泊松安全函数（PSF）来弥合高级语义理解和低级安全关键控制之间的差距。我们的方法通过将多传感器点云与基于视觉的实例分割和持久对象跟踪融合来感知环境，以保持相机视野之外的最新语义。然后使用多层安全过滤器来调制系统输入，以利用对环境的语义理解来实现安全导航。该安全过滤器由模型预测控制层和控制屏障功能层组成。这两层都利用制导场的 PSF 和通量调制来针对环境中的不同障碍物引入不同程度的保守性和多智能体通过规范。我们的框架使腿式机器人能够安全地导航语义丰富的动态环境，并具有上下文相关的安全裕度。

---

### OpenFrontier: General Navigation with Visual-Language Grounded Frontiers

- **发布日期**: 2026-03-05
- **作者**: Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum
- **分类**: cs.RO, cs.CV
- **Arxiv**: [2603.05377v1](http://arxiv.org/abs/2603.05377v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05377v1)

**Abstract (English):**

> Open-world navigation requires robots to make decisions in complex everyday environments while adapting to flexible task requirements. Conventional navigation approaches often rely on dense 3D reconstruction and hand-crafted goal metrics, which limits their generalization across tasks and environments. Recent advances in vision--language navigation (VLN) and vision--language--action (VLA) models enable end-to-end policies conditioned on natural language, but typically require interactive training, large-scale data collection, or task-specific fine-tuning with a mobile agent. We formulate navigation as a sparse subgoal identification and reaching problem and observe that providing visual anchoring targets for high-level semantic priors enables highly efficient goal-conditioned navigation. Based on this insight, we select navigation frontiers as semantic anchors and propose OpenFrontier, a training-free navigation framework that seamlessly integrates diverse vision--language prior models. OpenFrontier enables efficient navigation with a lightweight system design, without dense 3D mapping, policy training, or model fine-tuning. We evaluate OpenFrontier across multiple navigation benchmarks and demonstrate strong zero-shot performance, as well as effective real-world deployment on a mobile robot.

**摘要 (中文翻译):**

> 开放世界导航要求机器人在复杂的日常环境中做出决策，同时适应灵活的任务要求。传统的导航方法通常依赖于密集的 3D 重建和手工制定的目标指标，这限制了它们在任务和环境中的泛化。视觉-语言导航（VLN）和视觉-语言-动作（VLA）模型的最新进展使得能够以自然语言为条件的端到端策略成为可能，但通常需要交互式训练、大规模数据收集或使用移动代理进行特定于任务的微调。我们将导航制定为稀疏子目标识别和到达问题，并观察到为高级语义先验提供视觉锚定目标可以实现高效的目标条件导航。基于这一见解，我们选择导航前沿作为语义锚点，并提出了 OpenFrontier，这是一种免训练的导航框架，可以无缝集成不同的视觉-语言先验模型。 OpenFrontier 通过轻量级系统设计实现高效导航，无需密集 3D 映射、策略训练或模型微调。我们在多个导航基准测试中评估 OpenFrontier，并展示了强大的零射击性能，以及在移动机器人上的有效实际部署。

---

### Lightweight Visual Reasoning for Socially-Aware Robots

- **发布日期**: 2026-03-04
- **作者**: Alessio Galatolo, Ronald Cumbal, Alexandros Rouchitsas, Katie Winkle, Didem Gürdür Broo, Ginevra Castellano
- **分类**: cs.RO
- **Arxiv**: [2603.03942v1](http://arxiv.org/abs/2603.03942v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.03942v1)

**Abstract (English):**

> Robots operating in shared human environments must not only navigate, interact, and detect their surroundings, they must also interpret and respond to dynamic, and often unpredictable, human behaviours. Although recent advances have shown promise in enhancing robotic perception and instruction-following using Vision-Language Models (VLMs), they remain limited in addressing the complexities of multimodal human-robot interactions (HRI). Motivated by this challenge, we introduce a lightweight language-to-vision feedback module that closes the loop between an LLM and the vision encoder in VLMs. The module projects image-token hidden states through a gated Multi-Layer Perceptron (MLP) back into the encoder input, prompting a second pass that reinterprets the scene under text context. We evaluate this approach on three robotics-centred tasks: navigation in a simulated environment (Habitat), sequential scene description (Mementos-Robotics), and human-intention recognition (our HRI dataset). Results show that our method improves Qwen 2.5 (7B) by $3.3\%$ (less distance), $+0.057$ description score, and $+2.93\%$ accuracy, with less than $3\%$ extra parameters; Gemma 3 (4B) and LLaVA OV 1.5 (4B) show mixed navigation results but gains $+0.111,+0.055$ and $+10.81\%,+4.79\%$ on the latter two tasks. Code is available at https://github.com/alessioGalatolo/VLM-Reasoning-for-Robotics

**摘要 (中文翻译):**

> 在共享人类环境中运行的机器人不仅必须导航、交互和检测周围环境，还必须解释和响应动态且通常不可预测的人类行为。尽管最近的进展在使用视觉语言模型（VLM）增强机器人感知和指令遵循方面显示出了希望，但它们在解决多模式人机交互（HRI）的复杂性方面仍然有限。受这一挑战的推动，我们引入了一个轻量级的语言到视觉反馈模块，该模块闭合了 LLM 和 VLM 中的视觉编码器之间的循环。该模块通过门控多层感知器 (MLP) 将图像令牌隐藏状态投影回编码器输入，从而引发第二次传递，在文本上下文下重新解释场景。我们在三个以机器人为中心的任务上评估了这种方法：模拟环境（Habitat）中的导航、顺序场景描述（Mementos-Robotics）和人类意图识别（我们的 HRI 数据集）。结果表明，我们的方法将 Qwen 2.5 (7B) 提高了 $3.3\%$（距离更短）、$+0.057$ 描述分数和 $+2.93\%$ 准确度，并且额外参数少于 $3\%$； Gemma 3 (4B) 和 LLaVA OV 1.5 (4B) 显示混合导航结果，但在后两项任务中获得 $+0.111,+0.055$ 和 $+10.81\%,+4.79\%$。代码可在 https://github.com/alessioGalatolo/VLM-Reasoning-for-Robotics 获取

---

### RAGNav: A Retrieval-Augmented Topological Reasoning Framework for Multi-Goal Visual-Language Navigation

- **发布日期**: 2026-03-04
- **作者**: Ling Luo, Qiangian Bai
- **分类**: cs.AI, cs.RO
- **Arxiv**: [2603.03745v1](http://arxiv.org/abs/2603.03745v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.03745v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) is evolving from single-point pathfinding toward the more challenging Multi-Goal VLN. This task requires agents to accurately identify multiple entities while collaboratively reasoning over their spatial-physical constraints and sequential execution order. However, generic Retrieval-Augmented Generation (RAG) paradigms often suffer from spatial hallucinations and planning drift when handling multi-object associations due to the lack of explicit spatial modeling.To address these challenges, we propose RAGNav, a framework that bridges the gap between semantic reasoning and physical structure. The core of RAGNav is a Dual-Basis Memory system, which integrates a low-level topological map for maintaining physical connectivity with a high-level semantic forest for hierarchical environment abstraction. Building on this representation, the framework introduces an anchor-guided conditional retrieval and a topological neighbor score propagation mechanism. This approach facilitates the rapid screening of candidate targets and the elimination of semantic noise, while performing semantic calibration by leveraging the physical associations inherent in the topological neighborhood.This mechanism significantly enhances the capability of inter-target reachability reasoning and the efficiency of sequential planning. Experimental results demonstrate that RAGNav achieves state-of-the-art (SOTA) performance in complex multi-goal navigation tasks.

**摘要 (中文翻译):**

> 视觉语言导航 (VLN) 正在从单点寻路发展为更具挑战性的多目标 VLN。该任务要求智能体准确识别多个实体，同时对其空间物理约束和顺序执行顺序进行协作推理。然而，由于缺乏明确的空间建模，通用检索增强生成（RAG）范式在处理多对象关联时经常会出现空间幻觉和规划漂移。为了解决这些挑战，我们提出了 RAGNav，一个弥合语义推理和物理结构之间差距的框架。 RAGNav 的核心是双基内存系统，它集成了用于维护物理连接的低级拓扑图和用于分层环境抽象的高级语义森林。在此表示的基础上，该框架引入了锚引导条件检索和拓扑邻居分数传播机制。该方法有利于快速筛选候选目标并消除语义噪声，同时利用拓扑邻域固有的物理关联进行语义校准。该机制显着增强了目标间可达性推理的能力和顺序规划的效率。实验结果表明，RAGNav 在复杂的多目标导航任务中实现了最先进的 (SOTA) 性能。

---

### PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation

- **发布日期**: 2026-03-04
- **作者**: Zehua Fan, Wenqi Lyu, Wenxuan Song, Linge Zhao, Yifei Yang, Xi Wang, Junjie He, Lida Huang, Haiyan Liu, Bingchuan Sun et al. (共15位作者)
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2603.03739v1](http://arxiv.org/abs/2603.03739v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.03739v1)

**Abstract (English):**

> Multimodal large language models (MLLMs) have advanced zero-shot end-to-end Vision-Language Navigation (VLN), yet robust navigation requires not only semantic understanding but also predictive modeling of environment dynamics and spatial structure. We propose PROSPECT, a unified streaming navigation agent that couples a streaming Vision-Language-Action (VLA) policy with latent predictive representation learning. PROSPECT uses CUT3R as a streaming 3D foundation spatial encoder to produce long-context, absolute-scale spatial features, and fuses them with SigLIP semantic features via cross-attention. During training, we introduce learnable stream query tokens that query the streaming context and predict next-step 2D and 3D latent features (rather than pixels or explicit modalities), supervised in the latent spaces of frozen SigLIP and CUT3R teachers. The predictive branch shapes internal representations without inference overhead. Experiments on VLN-CE benchmarks and real-robot deployment demonstrate state-of-the-art performance and improved long-horizon robustness under diverse lighting. We will release code for the community soon.

**摘要 (中文翻译):**

> 多模态大语言模型（MLLM）具有先进的零样本端到端视觉语言导航（VLN），但强大的导航不仅需要语义理解，还需要环境动态和空间结构的预测建模。我们提出了 PROSPECT，一种统一的流式导航代理，它将流式视觉-语言-动作（VLA）策略与潜在预测表示学习相结合。 PROSPECT 使用 CUT3R 作为流式 3D 基础空间编码器来生成长上下文、绝对尺度的空间特征，并通过交叉注意力将它们与 SigLIP 语义特征融合。在训练期间，我们引入了可学习的流查询令牌，这些令牌查询流上下文并预测下一步的 2D 和 3D 潜在特征（而不是像素或显式模式），并在冻结的 SigLIP 和 CUT3R 教师的潜在空间中进行监督。 The predictive branch shapes internal representations without inference overhead. VLN-CE 基准测试和真实机器人部署的实验展示了最先进的性能，并在不同照明下提高了长视野鲁棒性。我们将很快向社区发布代码。

---

### MA-CoNav: A Master-Slave Multi-Agent Framework with Hierarchical Collaboration and Dual-Level Reflection for Long-Horizon Embodied VLN

- **发布日期**: 2026-03-03
- **作者**: Ling Luo, Qianqian Bai
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2603.03024v1](http://arxiv.org/abs/2603.03024v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.03024v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) aims to empower robots with the ability to perform long-horizon navigation in unfamiliar environments based on complex linguistic instructions. Its success critically hinges on establishing an efficient ``language-understanding -- visual-perception -- embodied-execution'' closed loop. Existing methods often suffer from perceptual distortion and decision drift in complex, long-distance tasks due to the cognitive overload of a single agent. Inspired by distributed cognition theory, this paper proposes MA-CoNav, a Multi-Agent Collaborative Navigation framework. This framework adopts a ``Master-Slave'' hierarchical agent collaboration architecture, decoupling and distributing the perception, planning, execution, and memory functions required for navigation tasks to specialized agents. Specifically, the Master Agent is responsible for global orchestration, while the Subordinate Agent group collaborates through a clear division of labor: an Observation Agent generates environment descriptions, a Planning Agent performs task decomposition and dynamic verification, an Execution Agent handles simultaneous mapping and action, and a Memory Agent manages structured experiences. Furthermore, the framework introduces a ``Local-Global'' dual-stage reflection mechanism to dynamically optimize the entire navigation pipeline. Empirical experiments were conducted using a real-world indoor dataset collected by a Limo Pro robot, with no scene-specific fine-tuning performed on the models throughout the process. The results demonstrate that MA-CoNav comprehensively outperforms existing mainstream VLN methods across multiple metrics.

**摘要 (中文翻译):**

> 视觉语言导航（VLN）旨在使机器人能够基于复杂的语言指令在陌生的环境中执行长视野导航。其成功关键在于建立一个高效的“语言理解——视觉感知——体现执行”闭环。由于单个智能体的认知超载，现有方法在复杂的长距离任务中经常会出现感知扭曲和决策漂移。受分布式认知理论的启发，本文提出了MA-CoNav，一种多智能体协作导航框架。该框架采用“主从”分层代理协作架构，将导航任务所需的感知、规划、执行和记忆功能解耦并分配给专门的代理。具体来说，主代理负责全局编排，而从属代理组通过明确的分工进行协作：观察代理生成环境描述，规划代理执行任务分解和动态验证，执行代理处理同步映射和操作，内存代理管理结构化体验。此外，该框架引入了“本地-全局”双阶段反射机制来动态优化整个导航管道。实证实验是使用 Limo Pro 机器人收集的真实室内数据集进行的，整个过程中没有对模型进行特定场景的微调。结果表明，MA-CoNav 在多个指标上全面优于现有主流 VLN 方法。

---

### TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation

- **发布日期**: 2026-03-03
- **作者**: Jiaxing Liu, Zexi Zhang, Xiaoyan Li, Boyue Wang, Yongli Hu, Baocai Yin
- **分类**: cs.CV, cs.RO
- **Arxiv**: [2603.02972v1](http://arxiv.org/abs/2603.02972v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.02972v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) presents a unique challenge for Large Vision-Language Models (VLMs) due to their inherent architectural mismatch: VLMs are primarily pretrained on static, disembodied vision-language tasks, which fundamentally clash with the dynamic, embodied, and spatially-structured nature of navigation. Existing large-model-based methods often resort to converting rich visual and spatial information into text, forcing models to implicitly infer complex visual-topological relationships or limiting their global action capabilities. To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an end-to-end framework that explicitly injects topological structures into the VLM backbone. To introduce topological edge information, Spatial Topology Aware Residual Attention (STAR-Att) directly integrates it into the VLM's self-attention mechanism, enabling intrinsic spatial reasoning while preserving pretrained knowledge. To enhance topological node information, an Interleaved Navigation Prompt strengthens node-level visual-text alignment. Finally, with the embedded topological graph, the model is capable of global action reasoning, allowing for robust path correction. On the R2R benchmark, TagaVLM achieves state-of-the-art performance among large-model-based methods, with a Success Rate (SR) of 51.09% and SPL of 47.18 in unseen environments, outperforming prior work by 3.39% in SR and 9.08 in SPL. This demonstrates that, for embodied spatial reasoning, targeted enhancements on smaller open-source VLMs can be more effective than brute-force model scaling. The code will be released upon publication.Project page: https://apex-bjut.github.io/Taga-VLM

**摘要 (中文翻译):**

> 由于其固有的架构不匹配，视觉语言导航 (VLN) 为大型视觉语言模型 (VLM) 带来了独特的挑战：VLM 主要针对静态、无实体的视觉语言任务进行预训练，这从根本上与导航的动态、具体和空间结构化性质相冲突。现有的基于大型模型的方法通常将丰富的视觉和空间信息转换为文本，迫使模型隐式推断复杂的视觉拓扑关系或限制其全局动作能力。为了弥补这一差距，我们提出了 TagaVLM（拓扑感知全局动作推理），这是一种端到端框架，可将拓扑结构明确地注入 VLM 主干。为了引入拓扑边缘信息，空间拓扑感知剩余注意力（STAR-Att）直接将其集成到 VLM 的自注意力机制中，在保留预训练知识的同时实现内在的空间推理。为了增强拓扑节点信息，交错导航提示增强了节点级视觉文本对齐。最后，通过嵌入的拓扑图，该模型能够进行全局动作推理，从而实现稳健的路径校正。在 R2R 基准上，TagaVLM 在基于大型模型的方法中实现了最先进的性能，在未见过的环境中成功率 (SR) 为 51.09%，SPL 为 47.18，比之前的工作在 SR 和 SPL 方面分别高出 3.39% 和 9.08。这表明，对于具体空间推理，对较小的开源 VLM 进行有针对性的增强可能比暴力模型扩展更有效。代码将在发布后发布。项目页面：https://apex-bjut.github.io/Taga-VLM

---

### CoFL: Continuous Flow Fields for Language-Conditioned Navigation

- **发布日期**: 2026-03-03
- **作者**: Haokun Liu, Zhaoqi Ma, Yicheng Chen, Masaki Kitagawa, Wentao Zhang, Jinjie Li, Moju Zhao
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2603.02854v1](http://arxiv.org/abs/2603.02854v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.02854v1)

**Abstract (English):**

> Language-conditioned navigation pipelines often rely on brittle modular components or costly action-sequence generation. To address these limitations, we present CoFL, an end-to-end policy that directly maps a bird's-eye view (BEV) observation and a language instruction to a continuous flow field for navigation. Instead of predicting discrete action tokens or sampling action chunks via iterative denoising, CoFL outputs instantaneous velocities that can be queried at arbitrary 2D projected locations. Trajectories are obtained by numerical integration of the predicted field, producing smooth motion that remains reactive under closed-loop execution. To enable large-scale training, we build a dataset of over 500k BEV image-instruction pairs, each procedurally annotated with a flow field and a trajectory derived from BEV semantic maps built on Matterport3D and ScanNet. By training on a mixed distribution, CoFL significantly outperforms modular Vision-Language Model (VLM)-based planners and generative policy baselines on strictly unseen scenes. Finally, we deploy CoFL zero-shot in real-world experiments with overhead BEV observations across multiple layouts, maintaining reliable closed-loop control and a high success rate.

**摘要 (中文翻译):**

> 语言调节的导航管道通常依赖于脆弱的模块化组件或昂贵的动作序列生成。为了解决这些限制，我们提出了 CoFL，这是一种端到端策略，可直接将鸟瞰图（BEV）观察和语言指令映射到连续流场以进行导航。 CoFL 不是通过迭代去噪来预测离散动作标记或采样动作块，而是输出可以在任意 2D 投影位置查询的瞬时速度。轨迹是通过预测场的数值积分获得的，产生在闭环执行下保持反应性的平滑运动。为了实现大规模训练，我们构建了超过 500k BEV 图像指令对的数据集，每个数据集都用流场和从基于 Matterport3D 和 ScanNet 构建的 BEV 语义图导出的轨迹进行程序注释。通过混合分布的训练，CoFL 在严格未见过的场景上显着优于基于模块化视觉语言模型 (VLM) 的规划器和生成策略基线。最后，我们在现实实验中部署了 CoFL 零样本，并在多个布局中进行头顶 BEV 观测，保持可靠的闭环控制和高成功率。

---

### SSMG-Nav: Enhancing Lifelong Object Navigation with Semantic Skeleton Memory Graph

- **发布日期**: 2026-03-02
- **作者**: Haochen Niu, Lantao Zhang, Xingwu Ji, Rendong Ying, Peilin Liu, Fei Wen
- **分类**: cs.RO
- **Arxiv**: [2603.01813v1](http://arxiv.org/abs/2603.01813v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.01813v1)

**Abstract (English):**

> Navigating to out-of-sight targets from human instructions in unfamiliar environments is a core capability for service robots. Despite substantial progress, most approaches underutilize reusable, persistent memory, constraining performance in lifelong settings. Many are additionally limited to single-modality inputs and employ myopic greedy policies, which often induce inefficient back-and-forth maneuvers (BFMs). To address such limitations, we introduce SSMG-Nav, a framework for object navigation built on a \textit{Semantic Skeleton Memory Graph} (SSMG) that consolidates past observations into a spatially aligned, persistent memory anchored by topological keypoints (e.g., junctions, room centers). SSMG clusters nearby entities into subgraphs, unifying entity- and space-level semantics to yield a compact set of candidate destinations. To support multimodal targets (images, objects, and text), we integrate a vision-language model (VLM). For each subgraph, a multimodal prompt synthesized from memory guides the VLM to infer a target belief over destinations. A long-horizon planner then trades off this belief against traversability costs to produce a visit sequence that minimizes expected path length, thereby reducing backtracking. Extensive experiments on challenging lifelong benchmarks and standard ObjectNav benchmarks demonstrate that, compared to strong baselines, our method achieves higher success rates and greater path efficiency, validating the effectiveness of SSMG-Nav.

**摘要 (中文翻译):**

> 在不熟悉的环境中根据人类指令导航到视线之外的目标是服务机器人的核心能力。尽管取得了实质性进展，但大多数方法都没有充分利用可重用的持久内存，从而限制了终生环境中的性能。许多人还仅限于单一模式输入并采用短视的贪婪政策，这通常会导致低效的来回操作（BFM）。为了解决这些限制，我们引入了 SSMG-Nav，这是一个基于 \textit{语义骨架记忆图} (SSMG) 构建的对象导航框架，它将过去的观察结果合并到由拓扑关键点（例如，交汇处、房间中心）锚定的空间对齐的持久记忆中。 SSMG 将附近的实体聚类为子图，统一实体和空间级别的语义，以生成一组紧凑的候选目的地。为了支持多模式目标（图像、对象和文​​本），我们集成了视觉语言模型（VLM）。对于每个子图，根据记忆合成的多模式提示会引导 VLM 推断出对目的地的目标信念。然后，长视野规划者会权衡这种信念与可遍历性成本，以产生最小化预期路径长度的访问序列，从而减少回溯。对具有挑战性的终身基准和标准 ObjectNav 基准的大量实验表明，与强基准相比，我们的方法实现了更高的成功率和更高的路径效率，验证了 SSMG-Nav 的有效性。

---

### SFCo-Nav: Efficient Zero-Shot Visual Language Navigation via Collaboration of Slow LLM and Fast Attributed Graph Alignment

- **发布日期**: 2026-03-02
- **作者**: Chaoran Xiong, Litao Wei, Xinhao Hu, Kehui Ma, Ziyi Xia, Zixin Jiang, Zhen Sun, Ling Pei
- **分类**: cs.RO
- **Arxiv**: [2603.01477v1](http://arxiv.org/abs/2603.01477v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.01477v1)

**Abstract (English):**

> Recent advances in large vision-language models (VLMs) and large language models (LLMs) have enabled zero-shot approaches to visual language navigation (VLN), where an agent follows natural language instructions using only ego perception and reasoning. However, existing zero-shot methods typically construct a naive observation graph and perform per-step VLM-LLM inference on it, resulting in high latency and computation costs that limit real-time deployment. To address this, we present SFCo-Nav, an efficient zero-shot VLN framework inspired by the principle of slow-fast cognitive collaboration. SFCo-Nav integrates three key modules: 1) a slow LLM-based planner that produces a strategic chain of subgoals, each linked to an imagined object graph; 2) a fast reactive navigator for real-time object graph construction and subgoal execution; and 3) a lightweight asynchronous slow-fast bridge aligns advanced structured, attributed imagined and perceived graphs to estimate navigation confidence, triggering the slow LLM planner only when necessary. To the best of our knowledge, SFCo-Nav is the first slow-fast collaboration zero-shot VLN system supporting asynchronous LLM triggering according to the internal confidence. Evaluated on the public R2R and REVERIE benchmarks, SFCo-Nav matches or exceeds prior state-of-the-art zero-shot VLN success rates while cutting total token consumption per trajectory by over 50% and running more than 3.5 times faster. Finally, we demonstrate SFCo-Nav on a legged robot in a hotel suite, showcasing its efficiency and practicality in indoor environments.

**摘要 (中文翻译):**

> 大型视觉语言模型（VLM）和大型语言模型（LLM）的最新进展使得视觉语言导航（VLN）的零样本方法成为可能，其中代理仅使用自我感知和推理来遵循自然语言指令。然而，现有的零样本方法通常构建一个朴素的观察图并对其执行每步VLM-LLM推理，导致高延迟和计算成本，限制了实时部署。为了解决这个问题，我们提出了 SFCo-Nav，这是一种高效的零样本 VLN 框架，其灵感来自慢速认知协作原则。 SFCo-Nav 集成了三个关键模块：1）一个基于 LLM 的缓慢规划器，它生成子目标的战略链，每个子目标都链接到一个想象的对象图； 2）用于实时对象图构建和子目标执行的快速反应导航器； 3) 轻量级异步慢-快桥将先进的结构化、归因想象和感知图表对齐以估计导航置信度，仅在必要时触发慢速 LLM 规划器。据我们所知，SFCo-Nav是第一个支持根据内部置信度异步LLM触发的慢速协作零样本VLN系统。根据公共 R2R 和 REVERIE 基准进行评估，SFCo-Nav 匹配或超过了之前最先进的零次 VLN 成功率，同时将每个轨迹的总代币消耗量减少了 50% 以上，运行速度提高了 3.5 倍以上。最后，我们在酒店套房的腿式机器人上演示了 SFCo-Nav，展示了其在室内环境中的效率和实用性。

---

### ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation

- **发布日期**: 2026-03-01
- **作者**: Wei Xue, Mingcheng Li, Xuecheng Wu, Jingqun Tang, Dingkang Yang, Lihua Zhang
- **分类**: cs.RO
- **Arxiv**: [2603.05530v1](http://arxiv.org/abs/2603.05530v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05530v1)

**Abstract (English):**

> Vision-and-Language Navigation (VLN) requires agents to accurately perceive complex visual environments and reason over navigation instructions and histories. However, existing methods passively process redundant visual inputs and treat all historical contexts indiscriminately, resulting in inefficient perception and unfocused reasoning. To address these challenges, we propose \textbf{ProFocus}, a training-free progressive framework that unifies \underline{Pro}active Perception and \underline{Focus}ed Reasoning through collaboration between large language models (LLMs) and vision-language models (VLMs). For proactive perception, ProFocus transforms panoramic observations into structured ego-centric semantic maps, enabling the orchestration agent to identify missing visual information needed for reliable decision-making, and to generate targeted visual queries with corresponding focus regions that guide the perception agent to acquire the required observations. For focused reasoning, we propose Branch-Diverse Monte Carlo Tree Search (BD-MCTS) to identify top-$k$ high-value waypoints from extensive historical candidates. The decision agent focuses reasoning on the historical contexts associated with these waypoints, rather than considering all historical waypoints equally. Extensive experiments validate the effectiveness of ProFocus, achieving state-of-the-art performance among zero-shot methods on R2R and REVERIE benchmarks.

**摘要 (中文翻译):**

> 视觉和语言导航（VLN）要求代理准确感知复杂的视觉环境并根据导航指令和历史进行推理。然而，现有的方法被动地处理冗余的视觉输入，并且不加区别地对待所有历史背景，导致感知效率低下和推理不集中。为了应对这些挑战，我们提出了 \textbf{ProFocus}，这是一种无需训练的渐进式框架，通过大语言模型（LLM）和视觉语言模型（VLM）之间的协作来统一 \underline{Pro}active Perception 和 \underline{Focus}ed Reasoning。对于主动感知，ProFocus 将全景观察转化为结构化的以自我为中心的语义图，使编排代理能够识别可靠决策所需的缺失视觉信息，并生成具有相应焦点区域的有针对性的视觉查询，引导感知代理获取所需的观察结果。为了进行集中推理，我们提出了分支多样化蒙特卡罗树搜索（BD-MCTS），以从广泛的历史候选中识别 top-$k$ 高价值路径点。决策代理将推理重点放在与这些航路点相关的历史背景上，而不是平等地考虑所有历史航路点。大量实验验证了 ProFocus 的有效性，在 R2R 和 REVERIE 基准测试中实现了零样本方法中最先进的性能。

---

### pySpatial: Generating 3D Visual Programs for Zero-Shot Spatial Reasoning

- **发布日期**: 2026-03-01
- **作者**: Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, Yaqi Xie
- **分类**: cs.CV
- **Arxiv**: [2603.00905v1](http://arxiv.org/abs/2603.00905v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.00905v1)

**Abstract (English):**

> Multi-modal Large Language Models (MLLMs) have demonstrated strong capabilities in general-purpose perception and reasoning, but they still struggle with tasks that require spatial understanding of the 3D world. To address this, we introduce pySpatial, a visual programming framework that equips MLLMs with the ability to interface with spatial tools via Python code generation. Given an image sequence and a natural-language query, the model composes function calls to spatial tools including 3D reconstruction, camera-pose recovery, novel-view rendering, etc. These operations convert raw 2D inputs into an explorable 3D scene, enabling MLLMs to reason explicitly over structured spatial representations. Notably, pySpatial requires no gradient-based fine-tuning and operates in a fully zero-shot setting. Experimental evaluations on the challenging MindCube and Omni3D-Bench benchmarks demonstrate that our framework pySpatial consistently surpasses strong MLLM baselines; for instance, it outperforms GPT-4.1-mini by 12.94% on MindCube. Furthermore, we conduct real-world indoor navigation experiments where the robot can successfully traverse complex environments using route plans generated by pySpatial, highlighting the practical effectiveness of our approach.

**摘要 (中文翻译):**

> 多模态大型语言模型 (MLLM) 在通用感知和推理方面表现出了强大的能力，但它们仍然难以完成需要对 3D 世界进行空间理解的任务。为了解决这个问题，我们引入了 pySpatial，这是一个可视化编程框架，使 MLLM 能够通过 Python 代码生成与空间工具交互。给定图像序列和自然语言查询，该模型组成对空间工具的函数调用，包括 3D 重建、相机姿势恢复、新颖视图渲染等。这些操作将原始 2D 输入转换为可探索的 3D 场景，使 MLLM 能够对结构化空间表示进行显式推理。值得注意的是，pySpatial 不需要基于梯度的微调，并且在完全零样本设置下运行。对具有挑战性的 MindCube 和 Omni3D-Bench 基准的实验评估表明，我们的框架 pySpatial 始终超越强大的 MLLM 基线；例如，它在 MindCube 上的性能比 GPT-4.1-mini 高出 12.94%。此外，我们进行了现实世界的室内导航实验，机器人可以使用 pySpatial 生成的路线计划成功穿越复杂的环境，突出了我们方法的实际有效性。

---

### Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning

- **发布日期**: 2026-02-28
- **作者**: Wentao Huang, Weimin Lyu, Peiliang Lou, Qingqiao Hu, Xiaoling Hu, Shahira Abousamra, Wenchao Han, Ruifeng Guo, Jiawei Zhou, Chao Chen et al. (共11位作者)
- **分类**: cs.CV
- **Arxiv**: [2603.00667v1](http://arxiv.org/abs/2603.00667v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.00667v1)

**Abstract (English):**

> Computational pathology has advanced rapidly in recent years, driven by domain-specific image encoders and growing interest in using vision-language models to answer natural-language questions about diseases. Yet, the core problem behind pathology question-answering remains unsolved, considering that a gigapixel slide contains far more information than necessary for a given question. Pathologists naturally navigate tissue and morphology complexity by scanning broadly, and zooming in selectively according to the clinical questions. Current models, in contrast, rely on uniform patch sampling or broad attention maps, often attending equally to irrelevant regions while overlooking key visual evidence. In this work, we try to bring models closer to how humans actually examine slides. We propose a question-guided, tissue-aware, and coarse-to-fine retrieval framework, HistoSelect, that consists of two key components: a group sampler that identifies question-relevant tissue regions, followed by a patch selector that retrieves the most informative patches within those regions. By selecting only the most informative patches, our method becomes significantly more efficient: reducing visual token usage by 70% on average, while improving accuracy across three pathology QA tasks. Evaluated on 356,000 question-answer pairs, our approach outperforms existing methods and produces answers grounded in interpretable, pathologist-consistent regions. Our results suggest that bringing human-like search and attention patterns into WSI reasoning is a promising direction for building practical and reliable pathology VLMs.

**摘要 (中文翻译):**

> 近年来，在特定领域图像编码器以及对使用视觉语言模型回答有关疾病的自然语言问题的兴趣日益浓厚的推动下，计算病理学取得了迅速发展。然而，考虑到十亿像素幻灯片包含的信息远多于给定问题所需的信息，病理学问答背后的核心问题仍未解决。病理学家通过广泛扫描并根据临床问题选择性放大来自然地驾驭组织和形态的复杂性。相比之下，当前的模型依赖于统一的斑块采样或广泛的注意力图，通常同样关注不相关的区域，同时忽略关键的视觉证据。在这项工作中，我们试图使模型更接近人类实际检查幻灯片的方式。我们提出了一个问题引导、组织感知、从粗到精的检索框架 HistoSelect，它由两个关键组件组成：一个识别与问题相关的组织区域的组采样器，然后是一个检索这些区域内信息最丰富的补丁的补丁选择器。通过仅选择信息最丰富的补丁，我们的方法变得更加高效：平均减少 70% 的视觉标记使用，同时提高三个病理 QA 任务的准确性。经过对 356,000 个问答对的评估，我们的方法优于现有方法，并生成基于可解释、病理学家一致区域的答案。我们的结果表明，将类人搜索和注意力模式引入 WSI 推理是构建实用且可靠的病理 VLM 的一个有前途的方向。

---

### TACIT Benchmark: A Programmatic Visual Reasoning Benchmark for Generative and Discriminative Models

- **发布日期**: 2026-02-27
- **作者**: Daniel Nobrega Medeiros
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2603.00206v1](http://arxiv.org/abs/2603.00206v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.00206v1)

**Abstract (English):**

> Existing visual reasoning benchmarks predominantly rely on natural language prompts, evaluate narrow reasoning modalities, or depend on subjective scoring procedures such as LLM-as-judge. We introduce the TACIT Benchmark, a programmatic visual reasoning benchmark comprising 10 tasks across 6 reasoning domains: spatial navigation, abstract pattern completion, causal simulation, logical constraint satisfaction, graph theory, and topology. The benchmark provides dual-track evaluation: a generative track in which models must produce solution images verified through deterministic computer-vision pipelines, and a discriminative track offering five-way multiple choice with structurally plausible near-miss distractors. Each distractor violates exactly one structural constraint, requiring models to reason about fine-grained visual differences rather than exploit superficial cues. Version 0.1.0 distributes 6,000 puzzles (108,000 PNG images across three resolutions) with fully deterministic seeded generation and reproducible verification. The dataset, generation code, and evaluation harness are released under the Apache 2.0 license on HuggingFace (DOI: 10.57967/hf/7904).

**摘要 (中文翻译):**

> 现有的视觉推理基准主要依赖于自然语言提示，评估狭隘的推理模式，或依赖于主观评分程序，例如法学硕士作为法官。我们引入了 TACIT Benchmark，这是一个程序化视觉推理基准，包含 6 个推理领域的 10 项任务：空间导航、抽象模式完成、因果模拟、逻辑约束满足、图论和拓扑。该基准提供双轨评估：一个生成轨道，其中模型必须生成通过确定性计算机视觉管道验证的解决方案图像，以及一个判别轨道，提供五向多项选择，并具有结构合理的近乎失误干扰因素。每个干扰因素都违反了一个结构约束，要求模型推理细粒度的视觉差异，而不是利用表面的线索。 0.1.0 版本分发了 6,000 个谜题（三种分辨率的 108,000 张 PNG 图像），具有完全确定性的种子生成和可重复的验证。数据集、生成代码和评估工具根据 Apache 2.0 许可证在 HuggingFace 上发布（DOI：10.57967/hf/7904）。

---

### Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos

- **发布日期**: 2026-02-27
- **作者**: Haoxuan Xu, Tianfu Li, Wenbo Chen, Yi Liu, Xingxing Zuo, Yaoxian Song, Haoang Li
- **分类**: cs.RO, cs.CV
- **Arxiv**: [2602.23937v1](http://arxiv.org/abs/2602.23937v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.23937v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) agents often struggle with long-horizon reasoning in unseen environments, particularly when facing ambiguous, coarse-grained instructions. While recent advances use knowledge graph to enhance reasoning, the potential of multimodal event knowledge inspired by human episodic memory remains underexplored. In this work, we propose an event-centric knowledge enhancement strategy for automated process knowledge mining and feature fusion to solve coarse-grained instruction and long-horizon reasoning in VLN task. First, we construct YE-KG, the first large-scale multimodal spatiotemporal knowledge graph, with over 86k nodes and 83k edges, derived from real-world indoor videos. By leveraging multimodal large language models (i.e., LLaVa, GPT4), we extract unstructured video streams into structured semantic-action-effect events to serve as explicit episodic memory. Second, we introduce STE-VLN, which integrates the above graph into VLN models via a Coarse-to-Fine Hierarchical Retrieval mechanism. This allows agents to retrieve causal event sequences and dynamically fuse them with egocentric visual observations. Experiments on REVERIE, R2R, and R2R-CE benchmarks demonstrate the efficiency of our event-centric strategy, outperforming state-of-the-art approaches across diverse action spaces. Our data and code are available on the project website https://sites.google.com/view/y-event-kg/.

**摘要 (中文翻译):**

> 视觉语言导航（VLN）代理经常在看不见的环境中进行长视野推理，特别是在面对模糊的、粗粒度的指令时。虽然最近的进展使用知识图来增强推理，但受人类情景记忆启发的多模态事件知识的潜力仍未得到充分探索。在这项工作中，我们提出了一种以事件为中心的知识增强策略，用于自动化流程知识挖掘和特征融合，以解决 VLN 任务中的粗粒度指令和长范围推理问题。首先，我们构建了 YE-KG，这是第一个大规模多模态时空知识图，具有超过 86k 个节点和 83k 个边，源自真实世界的室内视频。通过利用多模态大语言模型（即 LLaVa、GPT4），我们将非结构化视频流提取为结构化语义-动作-效果事件，作为显式情景记忆。其次，我们介绍STE-VLN，它通过从粗到细的层次检索机制将上述图集成到VLN模型中。这使得智能体能够检索因果事件序列，并将它们与以自我为中心的视觉观察动态融合。 REVERIE、R2R 和 R2R-CE 基准测试证明了我们以事件为中心的策略的效率，在不同的行动空间中优于最先进的方法。我们的数据和代码可在项目网站 https://sites.google.com/view/y-event-kg/ 上找到。

---

### See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent

- **发布日期**: 2026-02-27
- **作者**: Tianci Tang, Tielong Cai, Hongwei Wang, Gaoang Wang
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2602.23806v1](http://arxiv.org/abs/2602.23806v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.23806v1)

**Abstract (English):**

> Pre-trained perception models excel in generic image domains but degrade significantly in novel environments like indoor scenes. The conventional remedy is fine-tuning on downstream data which incurs catastrophic forgetting of prior knowledge and demands costly, scene-specific annotations. We propose a paradigm shift through Sea$^2$ (See, Act, Adapt): rather than adapting the perception modules themselves, we adapt how they are deployed through an intelligent pose-control agent. Sea$^2$ keeps all perception modules frozen, requiring no downstream labels during training, and uses only scalar perceptual feedback to navigate the agent toward informative viewpoints. Specially, we transform a vision-language model (VLM) into a low-level pose controller through a two-stage training pipeline: first fine-tuning it on rule-based exploration trajectories that systematically probe indoor scenes, and then refining the policy via unsupervised reinforcement learning that constructs rewards from the perception module's outputs and confidence. Unlike prior active perception methods that couple exploration with specific models or collect data for retraining them, Sea$^2$ directly leverages off-the-shelf perception models for various tasks without the need for retraining. We conducted experiments on three visual perception tasks, including visual grounding, segmentation and 3D box estimation, with performance improvements of 13.54%, 15.92% and 27.68% respectively on dataset ReplicaCAD.

**摘要 (中文翻译):**

> 预训练的感知模型在通用图像领域表现出色，但在室内场景等新环境中性能显着下降。传统的补救措施是对下游数据进行微调，这会导致先验知识的灾难性遗忘，并且需要昂贵的特定场景注释。我们提出通过 Sea$^2$（查看、行动、适应）进行范式转变：我们不是调整感知模块本身，而是通过智能姿势控制代理调整它们的部署方式。 Sea$^2$ 保持所有感知模块冻结，在训练期间不需要下游标签，并且仅使用标量感知反馈来引导代理走向信息观点。特别地，我们通过两阶段训练流程将视觉语言模型（VLM）转换为低级姿态控制器：首先在基于规则的探索轨迹上对其进行微调，系统地探测室内场景，然后通过无监督强化学习来完善策略，从感知模块的输出和置信度中构建奖励。与之前将探索与特定模型相结合或收集数据以进行再训练的主动感知方法不同，Sea$^2$ 直接利用现成的感知模型来执行各种任务，而无需进行再训练。我们对三个视觉感知任务进行了实验，包括视觉基础、分割和 3D 框估计，在数据集 ReplicaCAD 上性能分别提高了 13.54%、15.92% 和 27.68%。

---

### LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding

- **发布日期**: 2026-02-24
- **作者**: Jihao Qiu, Lingxi Xie, Xinyue Huo, Qi Tian, Qixiang Ye
- **分类**: cs.CV
- **Arxiv**: [2602.20913v1](http://arxiv.org/abs/2602.20913v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.20913v1)

**Abstract (English):**

> This paper addresses the critical and underexplored challenge of long video understanding with low computational budgets. We propose LongVideo-R1, an active, reasoning-equipped multimodal large language model (MLLM) agent designed for efficient video context navigation, avoiding the redundancy of exhaustive search. At the core of LongVideo-R1 lies a reasoning module that leverages high-level visual cues to infer the most informative video clip for subsequent processing. During inference, the agent initiates traversal from top-level visual summaries and iteratively refines its focus, immediately halting the exploration process upon acquiring sufficient knowledge to answer the query. To facilitate training, we first extract hierarchical video captions from CGBench, a video corpus with grounding annotations, and guide GPT-5 to generate 33K high-quality chain-of-thought-with-tool trajectories. The LongVideo-R1 agent is fine-tuned upon the Qwen-3-8B model through a two-stage paradigm: supervised fine-tuning (SFT) followed by reinforcement learning (RL), where RL employs a specifically designed reward function to maximize selective and efficient clip navigation. Experiments on multiple long video benchmarks validate the effectiveness of name, which enjoys superior tradeoff between QA accuracy and efficiency. All curated data and source code are provided in the supplementary material and will be made publicly available. Code and data are available at: https://github.com/qiujihao19/LongVideo-R1

**摘要 (中文翻译):**

> 本文解决了低计算预算下长视频理解的关键且尚未充分探索的挑战。我们提出了 LongVideo-R1，一种主动的、配备推理的多模态大语言模型（MLLM）代理，设计用于高效的视频上下文导航，避免详尽搜索的冗余。 LongVideo-R1 的核心是一个推理模块，它利用高级视觉线索来推断信息最丰富的视频剪辑，以供后续处理。在推理过程中，代理从顶级视觉摘要开始遍历，并迭代地细化其焦点，在获得足够的知识来回答查询后立即停止探索过程。为了便于训练，我们首先从带有基础注释的视频语料库 CGBench 中提取分层视频字幕，并引导 GPT-5 生成 33K 高质量的思想链工具轨迹。 LongVideo-R1 代理通过两阶段范式在 Qwen-3-8B 模型上进行微调：监督微调 (SFT)，然后是强化学习 (RL)，其中 RL 采用专门设计的奖励函数来最大限度地提高选择性和高效的剪辑导航。在多个长视频基准上进行的实验验证了 name 的有效性，它在 QA 准确性和效率之间享有卓越的权衡。所有精选数据和源代码均在补充材料中提供，并将公开发布。代码和数据可参见：https://github.com/qiujihao19/LongVideo-R1

---

### Contextual Safety Reasoning and Grounding for Open-World Robots

- **发布日期**: 2026-02-23
- **作者**: Zachary Ravichandran, David Snyder, Alexander Robey, Hamed Hassani, Vijay Kumar, George J. Pappas
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2602.19983v2](http://arxiv.org/abs/2602.19983v2)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.19983v2)

**Abstract (English):**

> Robots are increasingly operating in open-world environments where safe behavior depends on context: the same hallway may require different navigation strategies when crowded versus empty, or during an emergency versus normal operations. Traditional safety approaches enforce fixed constraints in user-specified contexts, limiting their ability to handle the open-ended contextual variability of real-world deployment. We address this gap via CORE, a safety framework that enables online contextual reasoning, grounding, and enforcement without prior knowledge of the environment (e.g., maps or safety specifications). CORE uses a vision-language model (VLM) to continuously reason about context-dependent safety rules directly from visual observations, grounds these rules in the physical environment, and enforces the resulting spatially-defined safe sets via control barrier functions. We provide probabilistic safety guarantees for CORE that account for perceptual uncertainty, and we demonstrate through simulation and real-world experiments that CORE enforces contextually appropriate behavior in unseen environments, significantly outperforming prior semantic safety methods that lack online contextual reasoning. Ablation studies validate our theoretical guarantees and underscore the importance of both VLM-based reasoning and spatial grounding for enforcing contextual safety in novel settings. We provide additional resources at https://zacravichandran.github.io/CORE.

**摘要 (中文翻译):**

> 机器人越来越多地在开放世界环境中运行，其中安全行为取决于上下文：同一走廊在拥挤与空旷时，或者在紧急情况与正常操作期间可能需要不同的导航策略。传统的安全方法在用户指定的上下文中强制执行固定约束，限制了它们处理现实世界部署的开放式上下文可变性的能力。我们通过 CORE 来解决这一差距，CORE 是一个安全框架，可以在无需事先了解环境（例如地图或安全规范）的情况下实现在线上下文推理、接地和执行。 CORE 使用视觉语言模型 (VLM) 直接从视觉观察中持续推理上下文相关的安全规则，将这些规则建立在物理环境中，并通过控制屏障函数强制执行由此产生的空间定义的安全集。我们为 CORE 提供了考虑感知不确定性的概率安全保证，并通过模拟和现实世界实验证明，CORE 在未见的环境中强制执行上下文适当的行为，显着优于先前缺乏在线上下文推理的语义安全方法。消融研究验证了我们的理论保证，并强调了基于 VLM 的推理和空间基础对于在新环境中加强情境安全的重要性。我们在 https://zacravichandran.github.io/CORE 提供更多资源。

---

### Global Commander and Local Operative: A Dual-Agent Framework for Scene Navigation

- **发布日期**: 2026-02-21
- **作者**: Kaiming Jin, Yuefan Wu, Shengqiong Wu, Bobo Li, Shuicheng Yan, Tat-Seng Chua
- **分类**: cs.CV
- **Arxiv**: [2602.18941v1](http://arxiv.org/abs/2602.18941v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.18941v1)

**Abstract (English):**

> Vision-and-Language Scene navigation is a fundamental capability for embodied human-AI collaboration, requiring agents to follow natural language instructions to execute coherent action sequences in complex environments. Existing approaches either rely on multiple agents, incurring high coordination and resource costs, or adopt a single-agent paradigm, which overloads the agent with both global planning and local perception, often leading to degraded reasoning and instruction drift in long-horizon settings. To address these issues, we introduce DACo, a planning-grounding decoupled architecture that disentangles global deliberation from local grounding. Concretely, it employs a Global Commander for high-level strategic planning and a Local Operative for egocentric observing and fine-grained execution. By disentangling global reasoning from local action, DACo alleviates cognitive overload and improves long-horizon stability. The framework further integrates dynamic subgoal planning and adaptive replanning to enable structured and resilient navigation. Extensive evaluations on R2R, REVERIE, and R4R demonstrate that DACo achieves 4.9%, 6.5%, 5.4% absolute improvements over the best-performing baselines in zero-shot settings, and generalizes effectively across both closed-source (e.g., GPT-4o) and open-source (e.g., Qwen-VL Series) backbones. DACo provides a principled and extensible paradigm for robust long-horizon navigation. Project page: https://github.com/ChocoWu/DACo

**摘要 (中文翻译):**

> 视觉和语言场景导航是人类与人工智能协作的一项基本功能，要求智能体遵循自然语言指令在复杂的环境中执行连贯的动作序列。现有的方法要么依赖多个代理，导致较高的协调和资源成本，要么采用单代理范式，这使代理在全局规划和局部感知方面超载，通常导致长视野环境中的推理能力下降和指令漂移。为了解决这些问题，我们引入了 DACo，这是一种规划与落地分离的架构，可以将全局审议与本地落地分开。具体来说，它聘用一名全球指挥官进行高层战略规划，聘用一名本地特工进行以自我为中心的观察和细粒度的执行。通过将全局推理与局部行动分开，DACo 减轻了认知过载并提高了长期稳定性。该框架进一步集成了动态子目标规划和自适应重新规划，以实现结构化和弹性导航。对 R2R、REVERIE 和 R4R 的广泛评估表明，DACo 比零样本设置中的最佳性能基线实现了 4.9%、6.5%、5.4% 的绝对改进，并且在闭源（例如 GPT-4o）和开源（例如 Qwen-VL 系列）骨干网中有效推广。 DACo 为稳健的长视野导航提供了原则性且可扩展的范例。项目页面：https://github.com/ChocoWu/DACo

---

### CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation

- **发布日期**: 2026-02-20
- **作者**: Xia Su, Ruiqi Chen, Benlin Liu, Jingwei Ma, Zonglin Di, Ranjay Krishna, Jon Froehlich
- **分类**: cs.CV, cs.RO
- **Arxiv**: [2602.18424v1](http://arxiv.org/abs/2602.18424v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.18424v1)

**Abstract (English):**

> Vision-Language Models (VLMs) have shown remarkable progress in Vision-Language Navigation (VLN), offering new possibilities for navigation decision-making that could benefit both robotic platforms and human users. However, real-world navigation is inherently conditioned by the agent's mobility constraints. For example, a sweeping robot cannot traverse stairs, while a quadruped can. We introduce Capability-Conditioned Navigation (CapNav), a benchmark designed to evaluate how well VLMs can navigate complex indoor spaces given an agent's specific physical and operational capabilities. CapNav defines five representative human and robot agents, each described with physical dimensions, mobility capabilities, and environmental interaction abilities. CapNav provides 45 real-world indoor scenes, 473 navigation tasks, and 2365 QA pairs to test if VLMs can traverse indoor environments based on agent capabilities. We evaluate 13 modern VLMs and find that current VLM's navigation performance drops sharply as mobility constraints tighten, and that even state-of-the-art models struggle with obstacle types that require reasoning on spatial dimensions. We conclude by discussing the implications for capability-aware navigation and the opportunities for advancing embodied spatial reasoning in future VLMs. The benchmark is available at https://github.com/makeabilitylab/CapNav

**摘要 (中文翻译):**

> 视觉语言模型 (VLM) 在视觉语言导航 (VLN) 方面取得了显着进展，为导航决策提供了新的可能性，使机器人平台和人类用户都受益。然而，现实世界的导航本质上受到代理的移动性限制的限制。例如，扫地机器人不能走楼梯，而四足机器人可以。我们引入了能力条件导航 (CapNav)，这是一个基准，旨在评估 VLM 在给定代理的特定物理和操作能力的情况下导航复杂室内空间的能力。 CapNav 定义了五个具有代表性的人类和机器人代理，每个代理都描述了物理尺寸、移动能力和环境交互能力。 CapNav 提供了 45 个真实室内场景、473 个导航任务和 2365 个 QA 对，以测试 VLM 是否可以基于代理功能遍历室内环境。我们评估了 13 个现代 VLM，发现当前 VLM 的导航性能随着移动性限制的收紧而急剧下降，而且即使是最先进的模型也难以应对需要空间维度推理的障碍类型。最后，我们讨论了能力感知导航的影响以及在未来 VLM 中推进体现空间推理的机会。该基准可在 https://github.com/makeabilitylab/CapNav 获取

---

### RoboLayout: Differentiable 3D Scene Generation for Embodied Agents

- **发布日期**: 2026-02-18
- **作者**: Ali Shamsaddinlou
- **分类**: cs.AI, cs.CV, cs.LG, cs.RO
- **Arxiv**: [2603.05522v1](http://arxiv.org/abs/2603.05522v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2603.05522v1)

**Abstract (English):**

> Recent advances in vision language models (VLMs) have shown strong potential for spatial reasoning and 3D scene layout generation from open-ended language instructions. However, generating layouts that are not only semantically coherent but also feasible for interaction by embodied agents remains challenging, particularly in physically constrained indoor environments. In this paper, RoboLayout is introduced as an extension of LayoutVLM that augments the original framework with agent-aware reasoning and improved optimization stability. RoboLayout integrates explicit reachability constraints into a differentiable layout optimization process, enabling the generation of layouts that are navigable and actionable by embodied agents. Importantly, the agent abstraction is not limited to a specific robot platform and can represent diverse entities with distinct physical capabilities, such as service robots, warehouse robots, humans of different age groups, or animals, allowing environment design to be tailored to the intended agent. In addition, a local refinement stage is proposed that selectively reoptimizes problematic object placements while keeping the remainder of the scene fixed, improving convergence efficiency without increasing global optimization iterations. Overall, RoboLayout preserves the strong semantic alignment and physical plausibility of LayoutVLM while enhancing applicability to agent-centric indoor scene generation, as demonstrated by experimental results across diverse scene configurations.

**摘要 (中文翻译):**

> 视觉语言模型 (VLM) 的最新进展显示出通过开放式语言指令进行空间推理和 3D 场景布局生成的强大潜力。然而，生成不仅语义一致而且可实现实体交互的布局仍然具有挑战性，特别是在物理受限的室内环境中。在本文中，RoboLayout 被介绍为 LayoutVLM 的扩展，它通过代理感知推理和改进的优化稳定性增强了原始框架。 RoboLayout 将显式可达性约束集成到可微布局优化过程中，从而能够生成可由具体代理导航和操作的布局。重要的是，代理抽象并不局限于特定的机器人平台，可以代表具有不同物理能力的不同实体，例如服务机器人、仓库机器人、不同年龄段的人类或动物，从而允许根据预期代理定制环境设计。此外，还提出了局部细化阶段，有选择地重新优化有问题的对象放置，同时保持场景的其余部分固定，从而在不增加全局优化迭代的情况下提高收敛效率。总体而言，RoboLayout 保留了 LayoutVLM 强大的语义对齐和物理合理性，同时增强了以代理为中心的室内场景生成的适用性，正如跨不同场景配置的实验结果所证明的那样。

---

### Learning to Retrieve Navigable Candidates for Efficient Vision-and-Language Navigation

- **发布日期**: 2026-02-17
- **作者**: Shutian Gu, Chengkai Huang, Ruoyu Wang, Lina Yao
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2602.15724v1](http://arxiv.org/abs/2602.15724v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.15724v1)

**Abstract (English):**

> Vision-and-Language Navigation (VLN) requires an agent to follow natural-language instructions and navigate through previously unseen environments. Recent approaches increasingly employ large language models (LLMs) as high-level navigators due to their flexibility and reasoning capability. However, prompt-based LLM navigation often suffers from inefficient decision-making, as the model must repeatedly interpret instructions from scratch and reason over noisy and verbose navigable candidates at each step. In this paper, we propose a retrieval-augmented framework to improve the efficiency and stability of LLM-based VLN without modifying or fine-tuning the underlying language model. Our approach introduces retrieval at two complementary levels. At the episode level, an instruction-level embedding retriever selects semantically similar successful navigation trajectories as in-context exemplars, providing task-specific priors for instruction grounding. At the step level, an imitation-learned candidate retriever prunes irrelevant navigable directions before LLM inference, reducing action ambiguity and prompt complexity. Both retrieval modules are lightweight, modular, and trained independently of the LLM. We evaluate our method on the Room-to-Room (R2R) benchmark. Experimental results demonstrate consistent improvements in Success Rate, Oracle Success Rate, and SPL on both seen and unseen environments. Ablation studies further show that instruction-level exemplar retrieval and candidate pruning contribute complementary benefits to global guidance and step-wise decision efficiency. These results indicate that retrieval-augmented decision support is an effective and scalable strategy for enhancing LLM-based vision-and-language navigation.

**摘要 (中文翻译):**

> 视觉和语言导航（VLN）要求代理遵循自然语言指令并在以前未见过的环境中导航。由于其灵活性和推理能力，最近的方法越来越多地采用大型语言模型（LLM）作为高级导航器。然而，基于提示的 LLM 导航通常会遇到决策效率低下的问题，因为模型必须从头开始重复解释指令，并在每一步对嘈杂且冗长的可导航候选人进行推理。在本文中，我们提出了一种检索增强框架，以提高基于 LLM 的 VLN 的效率和稳定性，而无需修改或微调底层语言模型。我们的方法在两个互补的层面上引入了检索。在情节级别，指令级嵌入检索器选择语义相似的成功导航轨迹作为上下文示例，为指令基础提供特定于任务的先验。在步骤级别，模仿学习的候选检索器在 LLM 推理之前修剪不相关的可导航方向，从而减少动作模糊性和提示复杂性。这两个检索模块都是轻量级、模块化的，并且独立于法学硕士进行训练。我们在 Room-to-Room (R2R) 基准上评估我们的方法。实验结果表明，在可见和不可见的环境中，成功率、Oracle 成功率和 SPL 均得到了持续改进。消融研究进一步表明，指令级样本检索和候选修剪为全局指导和逐步决策效率提供了互补的好处。这些结果表明，检索增强决策支持是增强基于 LLM 的视觉和语言导航的有效且可扩展的策略。

---

### pFedNavi: Structure-Aware Personalized Federated Vision-Language Navigation for Embodied AI

- **发布日期**: 2026-02-16
- **作者**: Qingqian Yang, Hao Wang, Sai Qian Zhang, Jian Li, Yang Hua, Miao Pan, Tao Song, Zhengwei Qi, Haibing Guan
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2602.14401v1](http://arxiv.org/abs/2602.14401v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.14401v1)

**Abstract (English):**

> Vision-Language Navigation VLN requires large-scale trajectory instruction data from private indoor environments, raising significant privacy concerns. Federated Learning FL mitigates this by keeping data on-device, but vanilla FL struggles under VLNs' extreme cross-client heterogeneity in environments and instruction styles, making a single global model suboptimal. This paper proposes pFedNavi, a structure-aware and dynamically adaptive personalized federated learning framework tailored for VLN. Our key idea is to personalize where it matters: pFedNavi adaptively identifies client-specific layers via layer-wise mixing coefficients, and performs fine-grained parameter fusion on the selected components (e.g., the encoder-decoder projection and environment-sensitive decoder layers) to balance global knowledge sharing with local specialization. We evaluate pFedNavi on two standard VLN benchmarks, R2R and RxR, using both ResNet and CLIP visual representations. Across all metrics, pFedNavi consistently outperforms the FedAvg-based VLN baseline, achieving up to 7.5% improvement in navigation success rate and up to 7.8% gain in trajectory fidelity, while converging 1.38x faster under non-IID conditions.

**摘要 (中文翻译):**

> 视觉语言导航 VLN 需要来自私人室内环境的大规模轨迹指令数据，引发了严重的隐私问题。联邦学习 FL 通过将数据保留在设备上来缓解这一问题，但普通 FL 在 VLN 环境和指令风格的极端跨客户端异质性下陷入困境，使得单一全局模型不是最优的。本文提出了 pFedNavi，一种为 VLN 量身定制的结构感知、动态自适应的个性化联邦学习框架。我们的关键思想是在重要的地方进行个性化：pFedNavi 通过逐层混合系数自适应地识别特定于客户端的层，并对所选组件（例如编码器-解码器投影和环境敏感解码器层）执行细粒度参数融合，以平衡全局知识共享与局部专业化。我们使用 ResNet 和 CLIP 视觉表示在两个标准 VLN 基准 R2R 和 RxR 上评估 pFedNavi。在所有指标中，pFedNavi 始终优于基于 FedAvg 的 VLN 基线，导航成功率提高了 7.5%，轨迹保真度提高了 7.8%，同时在非 IID 条件下收敛速度提高了 1.38 倍。

---

### AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

- **发布日期**: 2026-02-10
- **作者**: Xiaolou Sun, Wufei Si, Wenhui Ni, Yuntian Li, Dongming Wu, Fei Xie, Runwei Guan, He-Yang Xu, Henghui Ding, Yuan Wu et al. (共13位作者)
- **分类**: cs.RO
- **Arxiv**: [2602.09657v1](http://arxiv.org/abs/2602.09657v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.09657v1)

**Abstract (English):**

> Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI. Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes. However, real-world outdoor exploration typically occurs in unknown environments where detailed navigation instructions are unavailable. Instead, only coarse-grained positional or directional guidance can be provided, requiring UAVs to autonomously navigate through continuous planning and obstacle avoidance. To bridge this gap, we propose AutoFly, an end-to-end Vision-Language-Action (VLA) model for autonomous UAV navigation. AutoFly incorporates a pseudo-depth encoder that derives depth-aware features from RGB inputs to enhance spatial reasoning, coupled with a progressive two-stage training strategy that effectively aligns visual, depth, and linguistic representations with action policies. Moreover, existing VLN datasets have fundamental limitations for real-world autonomous navigation, stemming from their heavy reliance on explicit instruction-following over autonomous decision-making and insufficient real-world data. To address these issues, we construct a novel autonomous navigation dataset that shifts the paradigm from instruction-following to autonomous behavior modeling through: (1) trajectory collection emphasizing continuous obstacle avoidance, autonomous planning, and recognition workflows; (2) comprehensive real-world data integration. Experimental results demonstrate that AutoFly achieves a 3.9% higher success rate compared to state-of-the-art VLA baselines, with consistent performance across simulated and real environments.

**摘要 (中文翻译):**

> 视觉语言导航（VLN）需要智能代理通过解释语言指令和视觉观察来导航环境，这是嵌入式人工智能的基石任务。目前针对无人机 (UAV) 的 VLN 研究依赖于详细的、预先指定的指令来引导无人机沿预定路线行驶。然而，现实世界的户外探索通常发生在无法获得详细导航说明的未知环境中。相反，只能提供粗粒度的位置或方向引导，要求无人机通过连续规划和避障来自主导航。为了弥补这一差距，我们提出了 AutoFly，一种用于自主无人机导航的端到端视觉-语言-动作（VLA）模型。 AutoFly 采用了伪深度编码器，可从 RGB 输入中派生深度感知特征以增强空间推理，再加上渐进式两阶段训练策略，可有效地将视觉、深度和语言表示与动作策略保持一致。此外，现有的 VLN 数据集对于现实世界的自主导航存在根本性的限制，因为它们严重依赖于自主决策的明确指令跟踪以及现实世界数据的不足。为了解决这些问题，我们构建了一个新颖的自主导航数据集，通过以下方式将范式从遵循指令转变为自主行为建模：（1）轨迹收集，强调连续避障、自主规划和识别工作流程； (2)全面的现实世界数据集成。实验结果表明，与最先进的 VLA 基线相比，AutoFly 的成功率提高了 3.9%，并且在模拟和真实环境中具有一致的性能。

---

### Nipping the Drift in the Bud: Retrospective Rectification for Robust Vision-Language Navigation

- **发布日期**: 2026-02-06
- **作者**: Gang He, Zhenyang Liu, Kepeng Xu, Li Xu, Tong Qiao, Wenxin Yu, Chang Wu, Weiying Xie
- **分类**: cs.RO, eess.SY
- **Arxiv**: [2602.06356v1](http://arxiv.org/abs/2602.06356v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.06356v1)

**Abstract (English):**

> Vision-Language Navigation (VLN) requires embodied agents to interpret natural language instructions and navigate through complex continuous 3D environments. However, the dominant imitation learning paradigm suffers from exposure bias, where minor deviations during inference lead to compounding errors. While DAgger-style approaches attempt to mitigate this by correcting error states, we identify a critical limitation: Instruction-State Misalignment. Forcing an agent to learn recovery actions from off-track states often creates supervision signals that semantically conflict with the original instruction. In response to these challenges, we introduce BudVLN, an online framework that learns from on-policy rollouts by constructing supervision to match the current state distribution. BudVLN performs retrospective rectification via counterfactual re-anchoring and decision-conditioned supervision synthesis, using a geodesic oracle to synthesize corrective trajectories that originate from valid historical states, ensuring semantic consistency. Experiments on the standard R2R-CE and RxR-CE benchmarks demonstrate that BudVLN consistently mitigates distribution shift and achieves state-of-the-art performance in both Success Rate and SPL.

**摘要 (中文翻译):**

> 视觉语言导航 (VLN) 需要实体代理来解释自然语言指令并在复杂的连续 3D 环境中进行导航。然而，占主导地位的模仿学习范式存在暴露偏差，推理过程中的微小偏差会导致复合错误。虽然 DAgger 风格的方法试图通过纠正错误状态来缓解这一问题，但我们发现了一个关键限制：指令状态错位。强迫智能体从偏离轨道的状态中学习恢复动作通常会产生与原始指令在语义上冲突的监督信号。为了应对这些挑战，我们引入了 BudVLN，这是一个在线框架，它通过构建监督来匹配当前的状态分布，从而从策略部署中学习。 BudVLN 通过反事实重新锚定和决策条件监督合成来执行回顾性纠正，使用测地线预言机来合成源自有效历史状态的纠正轨迹，确保语义一致性。标准 R2R-CE 和 RxR-CE 基准测试的实验表明，BudVLN 始终如一地减轻分布偏移，并在成功率和 SPL 方面实现最先进的性能。

---

### VLN-Pilot: Large Vision-Language Model as an Autonomous Indoor Drone Operator

- **发布日期**: 2026-02-05
- **作者**: Bessie Dominguez-Dager, Sergio Suescun-Ferrandiz, Felix Escalona, Francisco Gomez-Donoso, Miguel Cazorla
- **分类**: cs.RO, cs.CV
- **Arxiv**: [2602.05552v1](http://arxiv.org/abs/2602.05552v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.05552v1)

**Abstract (English):**

> This paper introduces VLN-Pilot, a novel framework in which a large Vision-and-Language Model (VLLM) assumes the role of a human pilot for indoor drone navigation. By leveraging the multimodal reasoning abilities of VLLMs, VLN-Pilot interprets free-form natural language instructions and grounds them in visual observations to plan and execute drone trajectories in GPS-denied indoor environments. Unlike traditional rule-based or geometric path-planning approaches, our framework integrates language-driven semantic understanding with visual perception, enabling context-aware, high-level flight behaviors with minimal task-specific engineering. VLN-Pilot supports fully autonomous instruction-following for drones by reasoning about spatial relationships, obstacle avoidance, and dynamic reactivity to unforeseen events. We validate our framework on a custom photorealistic indoor simulation benchmark and demonstrate the ability of the VLLM-driven agent to achieve high success rates on complex instruction-following tasks, including long-horizon navigation with multiple semantic targets. Experimental results highlight the promise of replacing remote drone pilots with a language-guided autonomous agent, opening avenues for scalable, human-friendly control of indoor UAVs in tasks such as inspection, search-and-rescue, and facility monitoring. Our results suggest that VLLM-based pilots may dramatically reduce operator workload while improving safety and mission flexibility in constrained indoor environments.

**摘要 (中文翻译):**

> 本文介绍了 VLN-Pilot，这是一种新颖的框架，其中大型视觉和语言模型（VLLM）承担了室内无人机导航人类飞行员的角色。通过利用 VLLM 的多模态推理能力，VLN-Pilot 可以解释自由形式的自然语言指令，并将其基于视觉观察，以在 GPS 拒绝的室内环境中规划和执行无人机轨迹。与传统的基于规则或几何路径规划方法不同，我们的框架将语言驱动的语义理解与视觉感知相结合，以最少的特定任务工程实现上下文感知的高级飞行行为。 VLN-Pilot 通过推理空间关系、避障以及对不可预见事件的动态反应，支持无人机完全自主地执行指令。我们在定制的真实感室内模拟基准上验证了我们的框架，并展示了 VLLM 驱动的代理在复杂的指令跟踪任务（包括具有多个语义目标的长视野导航）上实现高成功率的能力。实验结果凸显了用语言引导的自主代理取代远程无人机飞行员的前景，为在检查、搜索和救援以及设施监控等任务中对室内无人机进行可扩展、人性化的控制开辟了途径。我们的结果表明，基于 VLLM 的飞行员可以显着减少操作员的工作量，同时提高受限室内环境中的安全性和任务灵活性。

---

### MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation

- **发布日期**: 2026-02-05
- **作者**: Dekang Qi, Shuang Zeng, Xinyuan Chang, Feng Xiong, Shichao Xie, Xiaolong Wu, Mu Xu
- **分类**: cs.CV, cs.CL, cs.RO
- **Arxiv**: [2602.05467v1](http://arxiv.org/abs/2602.05467v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.05467v1)

**Abstract (English):**

> Visual Language Navigation (VLN) is one of the fundamental capabilities for embodied intelligence and a critical challenge that urgently needs to be addressed. However, existing methods are still unsatisfactory in terms of both success rate (SR) and generalization: Supervised Fine-Tuning (SFT) approaches typically achieve higher SR, while Training-Free (TF) approaches often generalize better, but it is difficult to obtain both simultaneously. To this end, we propose a Memory-Execute-Review framework. It consists of three parts: a hierarchical memory module for providing information support, an execute module for routine decision-making and actions, and a review module for handling abnormal situations and correcting behavior. We validated the effectiveness of this framework on the Object Goal Navigation task. Across 4 datasets, our average SR achieved absolute improvements of 7% and 5% compared to all baseline methods under TF and Zero-Shot (ZS) settings, respectively. On the most commonly used HM3D_v0.1 and the more challenging open vocabulary dataset HM3D_OVON, the SR improved by 8% and 6%, under ZS settings. Furthermore, on the MP3D and HM3D_OVON datasets, our method not only outperformed all TF methods but also surpassed all SFT methods, achieving comprehensive leadership in both SR (5% and 2%) and generalization.

**摘要 (中文翻译):**

> 视觉语言导航（VLN）是体现智能的基本能力之一，也是迫切需要解决的关键挑战。然而，现有方法在成功率（SR）和泛化方面仍然不能令人满意：有监督微调（SFT）方法通常可以实现更高的SR，而免训练（TF）方法通常可以更好地泛化，但很难同时获得两者。为此，我们提出了一个内存执行审查框架。它由三部分组成：提供信息支持的分层记忆模块、日常决策和行动的执行模块、处理异常情况和纠正行为的回顾模块。我们验证了该框架在对象目标导航任务上的有效性。在 4 个数据集中，与 TF 和零样本 (ZS) 设置下的所有基线方法相比，我们的平均 SR 分别实现了 7% 和 5% 的绝对改进。在最常用的 HM3D_v0.1 和更具挑战性的开放词汇数据集 HM3D_OVON 上，在 ZS 设置下，SR 分别提高了 8% 和 6%。此外，在 MP3D 和 HM3D_OVON 数据集上，我们的方法不仅优于所有 TF 方法，而且超越所有 SFT 方法，在 SR（5% 和 2%）和泛化方面实现全面领先。

---

### Fly0: Decoupling Semantic Grounding from Geometric Planning for Zero-Shot Aerial Navigation

- **发布日期**: 2026-02-02
- **作者**: Zhenxing Xu, Brikit Lu, Weidong Bao, Zhengqiu Zhu, Junsong Zhang, Hui Yan, Wenhao Lu, Ji Wang
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2602.15875v1](http://arxiv.org/abs/2602.15875v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.15875v1)

**Abstract (English):**

> Current Visual-Language Navigation (VLN) methodologies face a trade-off between semantic understanding and control precision. While Multimodal Large Language Models (MLLMs) offer superior reasoning, deploying them as low-level controllers leads to high latency, trajectory oscillations, and poor generalization due to weak geometric grounding. To address these limitations, we propose Fly0, a framework that decouples semantic reasoning from geometric planning. The proposed method operates through a three-stage pipeline: (1) an MLLM-driven module for grounding natural language instructions into 2D pixel coordinates; (2) a geometric projection module that utilizes depth data to localize targets in 3D space; and (3) a geometric planner that generates collision-free trajectories. This mechanism enables robust navigation even when visual contact is lost. By eliminating the need for continuous inference, Fly0 reduces computational overhead and improves system stability. Extensive experiments in simulation and real-world environments demonstrate that Fly0 outperforms state-of-the-art baselines, improving the Success Rate by over 20\% and reducing Navigation Error (NE) by approximately 50\% in unstructured environments. Our code is available at https://github.com/xuzhenxing1/Fly0.

**摘要 (中文翻译):**

> 当前的视觉语言导航（VLN）方法面临着语义理解和控制精度之间的权衡。虽然多模态大型语言模型 (MLLM) 提供卓越的推理能力，但将它们部署为低级控制器会导致高延迟、轨迹振荡以及由于几何基础薄弱而导致泛化能力差。为了解决这些限制，我们提出了 Fly0，一个将语义推理与几何规划分离的框架。所提出的方法通过三级管道进行操作：（1）MLLM 驱动模块，用于将自然语言指令转化为 2D 像素坐标； (2)几何投影模块，利用深度数据在3D空间中定位目标； (3) 生成无碰撞轨迹的几何规划器。即使失去视觉接触，这种机制也能实现稳健的导航。通过消除连续推理的需要，Fly0 减少了计算开销并提高了系统稳定性。模拟和现实环境中的大量实验表明，Fly0 的性能优于最先进的基线，在非结构化环境中将成功率提高了 20% 以上，并将导航错误 (NE) 减少了约 50%。我们的代码可在 https://github.com/xuzhenxing1/Fly0 获取。

---

### MapDream: Task-Driven Map Learning for Vision-Language Navigation

- **发布日期**: 2026-01-30
- **作者**: Guoxin Lian, Shuo Wang, Yucheng Wang, Yongcai Wang, Maiyue Chen, Kaihui Wang, Bo Zhang, Zhizhong Su, Deying Li, Zhaoxin Fan
- **分类**: cs.RO, cs.AI, cs.CV
- **Arxiv**: [2602.00222v2](http://arxiv.org/abs/2602.00222v2)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.00222v2)

**Abstract (English):**

> Vision-Language Navigation (VLN) requires agents to follow natural language instructions in partially observed 3D environments, motivating map representations that aggregate spatial context beyond local perception. However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy. We argue that maps should instead be learned representations shaped directly by navigation objectives rather than exhaustive reconstructions. Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird's-eye-view (BEV) image synthesis. The framework jointly learns map generation and action prediction, distilling environmental context into a compact three-channel BEV map that preserves only navigation-critical affordances. Supervised pre-training bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning. Experiments on R2R-CE and RxR-CE achieve state-of-the-art monocular performance, validating task-driven generative map learning.

**摘要 (中文翻译):**

> 视觉语言导航 (VLN) 要求代理在部分观察的 3D 环境中遵循自然语言指令，激发地图表示，聚合超出局部感知的空间上下文。然而，大多数现有方法依赖于独立于导航策略构建的手工制作的地图。我们认为地图应该是由导航目标直接塑造的学习表示，而不是详尽的重建。基于这一见解，我们提出了 MapDream，这是一个地图循环框架，它将地图构建表述为自回归鸟瞰 (BEV) 图像合成。该框架共同学习地图生成和动作预测，将环境背景提炼成紧凑的三通道 BEV 地图，仅保留对导航至关重要的可供性。有监督的预训练引导了可靠的映射到控制接口，而自回归设计则通过强化微调实现端到端联合优化。 R2R-CE 和 RxR-CE 上的实验实现了最先进的单目性能，验证了任务驱动的生成图学习。

---

### Mitigating Error Accumulation in Continuous Navigation via Memory-Augmented Kalman Filtering

- **发布日期**: 2026-01-30
- **作者**: Yin Tang, Jiawei Ma, Jinrui Zhang, Alex Jinpeng Wang, Deyu Zhang
- **分类**: cs.RO, cs.CV, eess.SY
- **Arxiv**: [2602.11183v1](http://arxiv.org/abs/2602.11183v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2602.11183v1)

**Abstract (English):**

> Continuous navigation in complex environments is critical for Unmanned Aerial Vehicle (UAV). However, the existing Vision-Language Navigation (VLN) models follow the dead-reckoning, which iteratively updates its position for the next waypoint prediction, and subsequently construct the complete trajectory. Then, such stepwise manner will inevitably lead to accumulated errors of position over time, resulting in misalignment between internal belief and objective coordinates, which is known as "state drift" and ultimately compromises the full trajectory prediction. Drawing inspiration from classical control theory, we propose to correct for errors by formulating such sequential prediction as a recursive Bayesian state estimation problem. In this paper, we design NeuroKalman, a novel framework that decouples navigation into two complementary processes: a Prior Prediction, based on motion dynamics and a Likelihood Correction, from historical observation. We first mathematically associate Kernel Density Estimation of the measurement likelihood with the attention-based retrieval mechanism, which then allows the system to rectify the latent representation using retrieved historical anchors without gradient updates. Comprehensive experiments on TravelUAV benchmark demonstrate that, with only 10% of the training data fine-tuning, our method clearly outperforms strong baselines and regulates drift accumulation.

**摘要 (中文翻译):**

> 复杂环境中的连续导航对于无人机 (UAV) 至关重要。然而，现有的视觉语言导航（VLN）模型遵循航位推算，迭代更新其位置以进行下一个航路点预测，并随后构建完整的轨迹。那么，这种逐步的方式将不可避免地导致位置误差随着时间的推移而累积，导致内部信念与客观坐标之间的错位，这被称为“状态漂移”，并最终损害完整的轨迹预测。受到经典控制理论的启发，我们建议通过将这种顺序预测表述为递归贝叶斯状态估计问题来纠正错误。在本文中，我们设计了 NeuroKalman，这是一种新颖的框架，它将导航解耦为两个互补的过程：基于运动动力学的先验预测和来自历史观察的似然校正。我们首先在数学上将测量可能性的核密度估计与基于注意力的检索机制相关联，然后允许系统使用检索到的历史锚点来纠正潜在表示，而无需梯度更新。 TravelUAV 基准的综合实验表明，只需 10% 的训练数据微调，我们的方法就明显优于强基线并调节漂移累积。

---

### Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation

- **发布日期**: 2026-01-29
- **作者**: Jiankun Peng, Jianyuan Guo, Ying Xu, Yue Liu, Jiashuang Yan, Xuanwei Ye, Houhua Li, Xiaoming Wang
- **分类**: cs.CV
- **Arxiv**: [2601.21751v1](http://arxiv.org/abs/2601.21751v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.21751v1)

**Abstract (English):**

> Vision-Language Navigation in Continuous Environments (VLN-CE) presents a core challenge: grounding high-level linguistic instructions into precise, safe, and long-horizon spatial actions. Explicit topological maps have proven to be a vital solution for providing robust spatial memory in such tasks. However, existing topological planning methods suffer from a "Granularity Rigidity" problem. Specifically, these methods typically rely on fixed geometric thresholds to sample nodes, which fails to adapt to varying environmental complexities. This rigidity leads to a critical mismatch: the model tends to over-sample in simple areas, causing computational redundancy, while under-sampling in high-uncertainty regions, increasing collision risks and compromising precision. To address this, we propose DGNav, a framework for Dynamic Topological Navigation, introducing a context-aware mechanism to modulate map density and connectivity on-the-fly. Our approach comprises two core innovations: (1) A Scene-Aware Adaptive Strategy that dynamically modulates graph construction thresholds based on the dispersion of predicted waypoints, enabling "densification on demand" in challenging environments; (2) A Dynamic Graph Transformer that reconstructs graph connectivity by fusing visual, linguistic, and geometric cues into dynamic edge weights, enabling the agent to filter out topological noise and enhancing instruction adherence. Extensive experiments on the R2R-CE and RxR-CE benchmarks demonstrate DGNav exhibits superior navigation performance and strong generalization capabilities. Furthermore, ablation studies confirm that our framework achieves an optimal trade-off between navigation efficiency and safe exploration. The code is available at https://github.com/shannanshouyin/DGNav.

**摘要 (中文翻译):**

> 连续环境中的视觉语言导航（VLN-CE）提出了一个核心挑战：将高级语言指令转化为精确、安全和长视野的空间动作。事实证明，显式拓扑图是在此类任务中提供强大空间记忆的重要解决方案。然而，现有的拓扑规划方法存在“粒度刚性”问题。具体来说，这些方法通常依赖于样本节点的固定几何阈值，这无法适应不断变化的环境复杂性。这种刚性导致了严重的不匹配：模型往往在简单区域过度采样，导致计算冗余，而在高不确定性区域采样不足，增加碰撞风险并影响精度。为了解决这个问题，我们提出了 DGNav，一种动态拓扑导航框架，引入了上下文感知机制来动态调整地图密度和连接性。我们的方法包括两个核心创新：（1）场景感知自适应策略，根据预测路径点的分散度动态调整图形构建阈值，从而在具有挑战性的环境中实现“按需致密化”； (2) 动态图转换器，通过将视觉、语言和几何线索融合到动态边缘权重中来重建图连接性，使代理能够滤除拓扑噪声并增强指令依从性。在 R2R-CE 和 RxR-CE 基准上的大量实验表明，DGNav 具有卓越的导航性能和强大的泛化能力。此外，消融研究证实我们的框架实现了导航效率和安全探索之间的最佳权衡。代码可在 https://github.com/shannanshouyin/DGNav 获取。

---

### DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation

- **发布日期**: 2026-01-26
- **作者**: Zijun Li, Shijie Li, Zhenxi Zhang, Bin Li, Shoujun Zhou
- **分类**: cs.RO
- **Arxiv**: [2601.18492v1](http://arxiv.org/abs/2601.18492v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.18492v1)

**Abstract (English):**

> Vision-and-Language Navigation (VLN) requires an embodied agent to navigate in a complex 3D environment according to natural language instructions. Recent progress in large language models (LLMs) has enabled language-driven navigation with improved interpretability. However, most LLM-based agents still rely on single-shot action decisions, where the model must choose one option from noisy, textualized multi-perspective observations. Due to local mismatches and imperfect intermediate reasoning, such decisions can easily deviate from the correct path, leading to error accumulation and reduced reliability in unseen environments. In this paper, we propose DV-VLN, a new VLN framework that follows a generate-then-verify paradigm. DV-VLN first performs parameter-efficient in-domain adaptation of an open-source LLaMA-2 backbone to produce a structured navigational chain-of-thought, and then verifies candidate actions with two complementary channels: True-False Verification (TFV) and Masked-Entity Verification (MEV). DV-VLN selects actions by aggregating verification successes across multiple samples, yielding interpretable scores for reranking. Experiments on R2R, RxR (English subset), and REVERIE show that DV-VLN consistently improves over direct prediction and sampling-only baselines, achieving competitive performance among language-only VLN agents and promising results compared with several cross-modal systems.Code is available at https://github.com/PlumJun/DV-VLN.

**摘要 (中文翻译):**

> 视觉和语言导航 (VLN) 需要具体代理根据自然语言指令在复杂的 3D 环境中进行导航。大语言模型 (LLM) 的最新进展使得语言驱动的导航成为可能，并提高了可解释性。然而，大多数基于 LLM 的智能体仍然依赖于单次动作决策，其中模型必须从嘈杂的、文本化的多视角观察中选择一个选项。由于局部不匹配和不完善的中间推理，此类决策很容易偏离正确路径，导致错误累积并在未见的环境中降低可靠性。在本文中，我们提出了 DV-VLN，这是一种遵循“生成然后验证”范式的新 VLN 框架。 DV-VLN 首先对开源 LLaMA-2 主干执行参数高效的域内适应，以生成结构化的导航思想链，然后使用两个互补通道验证候选操作：真假验证 (TFV) 和屏蔽实体验证 (MEV)。 DV-VLN 通过聚合多个样本的验证成功来选择操作，生成可解释的分数以进行重新排名。 R2R、RxR（英语子集）和 REVERIE 上的实验表明，DV-VLN 始终优于直接预测和仅采样基线，在纯语言 VLN 代理中实现了有竞争力的性能，并且与几种跨模态系统相比取得了可喜的结果。代码可在 https://github.com/PlumJun/DV-VLN 上获取。

---

### \textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation

- **发布日期**: 2026-01-26
- **作者**: Weiye Zhu, Zekai Zhang, Xiangchen Wang, Hewei Pan, Teng Wang, Tiantian Geng, Rongtao Xu, Feng Zheng
- **分类**: cs.CV, cs.AI
- **Arxiv**: [2601.18188v1](http://arxiv.org/abs/2601.18188v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.18188v1)

**Abstract (English):**

> Vision-and-Language Navigation (VLN) requires agents to interpret natural language instructions and act coherently in visually rich environments. However, most existing methods rely on reactive state-action mappings without explicitly modeling how actions causally transform subsequent visual observations. Lacking such vision-action causality, agents cannot anticipate the visual changes induced by its own actions, leading to unstable behaviors, weak generalization, and cumulative error along trajectory. To address these issues, we introduce \textsc{NaVIDA} (\textbf{Nav}igation with \textbf{I}nverse \textbf{D}ynamics \textbf{A}ugmentation), a unified VLN framework that couples policy learning with action-grounded visual dynamics and adaptive execution. \textsc{NaVIDA} augments training with chunk-based inverse-dynamics supervision to learn causal relationship between visual changes and corresponding actions. To structure this supervision and extend the effective planning range, \textsc{NaVIDA} employs hierarchical probabilistic action chunking (HPAC), which organizes trajectories into multi-step chunks and provides discriminative, longer-range visual-change cues. To further curb error accumulation and stabilize behavior at inference, an entropy-guided mechanism adaptively sets the execution horizon of action chunks. Extensive experiments show that \textsc{NaVIDA} achieves superior navigation performance compared to state-of-the-art methods with fewer parameters (3B vs. 8B). Real-world robot evaluations further validate the practical feasibility and effectiveness of our approach. Code and data will be available upon acceptance.

**摘要 (中文翻译):**

> 视觉和语言导航（VLN）要求代理解释自然语言指令并在视觉丰富的环境中连贯地行动。然而，大多数现有方法依赖于反应性状态-动作映射，而没有明确建模动作如何因果地改变后续视觉观察。由于缺乏这种视觉-动作因果关系，智能体无法预测其自身动作引起的视觉变化，从而导致行为不稳定、泛化能力弱以及沿着轨迹的累积误差。为了解决这些问题，我们引入了 \textsc{NavIDA} （\textbf{Nav}igation 与 \textbf{I}nverse \textbf{D}ynamics \textbf{A}ugmentation），这是一个统一的 VLN 框架，它将策略学习与基于动作的视觉动态和自适应执行结合起来。 \textsc{NavIDA} 通过基于块的逆动态监督增强训练，以学习视觉变化和相应动作之间的因果关系。为了构建这种监督并扩展有效的规划范围，\textsc{NavIDA} 采用分层概率动作分块（HPAC），它将轨迹组织成多步骤块，并提供有区别的、较长范围的视觉变化线索。为了进一步抑制错误积累并稳定推理行为，熵引导机制自适应地设置动作块的执行范围。大量实验表明，与参数较少的最先进方法（3B 与 8B）相比，\textsc{NavIDA} 实现了卓越的导航性能。现实世界的机器人评估进一步验证了我们方法的实际可行性和有效性。代码和数据将在接受后提供。

---

### FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation

- **发布日期**: 2026-01-20
- **作者**: Jing Zuo, Lingzhou Mu, Fan Jiang, Chengcheng Ma, Mu Xu, Yonggang Qi
- **分类**: cs.CV, cs.RO
- **Arxiv**: [2601.13976v2](http://arxiv.org/abs/2601.13976v2)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.13976v2)

**Abstract (English):**

> Achieving human-level performance in Vision-and-Language Navigation (VLN) requires an embodied agent to jointly understand multimodal instructions and visual-spatial context while reasoning over long action sequences. Recent works, such as NavCoT and NavGPT-2, demonstrate the potential of Chain-of-Thought (CoT) reasoning for improving interpretability and long-horizon planning. Moreover, multimodal extensions like OctoNav-R1 and CoT-VLA further validate CoT as a promising pathway toward human-like navigation reasoning. However, existing approaches face critical drawbacks: purely textual CoTs lack spatial grounding and easily overfit to sparse annotated reasoning steps, while multimodal CoTs incur severe token inflation by generating imagined visual observations, making real-time navigation impractical. In this work, we propose FantasyVLN, a unified implicit reasoning framework that preserves the benefits of CoT reasoning without explicit token overhead. Specifically, imagined visual tokens are encoded into a compact latent space using a pretrained Visual AutoRegressor (VAR) during CoT reasoning training, and the model jointly learns from textual, visual, and multimodal CoT modes under a unified multi-CoT strategy. At inference, our model performs direct instruction-to-action mapping while still enjoying reasoning-aware representations. Extensive experiments on LH-VLN show that our approach achieves reasoning-aware yet real-time navigation, improving success rates and efficiency while reducing inference latency by an order of magnitude compared to explicit CoT methods.

**摘要 (中文翻译):**

> 要在视觉和语言导航（VLN）中实现人类水平的表现，需要一个实体代理来共同理解多模态指令和视觉空间上下文，同时对长动作序列进行推理。最近的工作，例如 NavCoT 和 NavGPT-2，展示了思想链 (CoT) 推理在提高可解释性和长期规划方面的潜力。此外，OctoNav-R1 和 CoT-VLA 等多模态扩展进一步验证了 CoT 是实现类人导航推理的一条有前途的途径。然而，现有的方法面临着严重的缺点：纯文本 CoT 缺乏空间基础，很容易过度适应稀疏的注释推理步骤，而多模态 CoT 通过生成想象的视觉观察而导致严重的标记膨胀，使得实时导航不切实际。在这项工作中，我们提出了 FantasyVLN，这是一个统一的隐式推理框架，它保留了 CoT 推理的优点，而无需显式的令牌开销。具体来说，在 CoT 推理训练期间，使用预训练的视觉自回归器 (VAR) 将想象的视觉标记编码到紧凑的潜在空间中，并且该模型在统一的多 CoT 策略下从文本、视觉和多模态 CoT 模式中联合学习。在推理时，我们的模型执行直接指令到动作的映射，同时仍然享受推理感知表示。 LH-VLN 上的大量实验表明，与显式 CoT 方法相比，我们的方法实现了推理感知且实时的导航，提高了成功率和效率，同时将推理延迟减少了一个数量级。

---

### Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration

- **发布日期**: 2026-01-19
- **作者**: Lu Yue, Yue Fan, Shiwei Lian, Yu Zhao, Jiaxin Yu, Liang Xie, Feitian Zhang
- **分类**: cs.CV, eess.SY
- **Arxiv**: [2601.12766v1](http://arxiv.org/abs/2601.12766v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.12766v1)

**Abstract (English):**

> Zero-shot Vision-and-Language Navigation (VLN) agents leveraging Large Language Models (LLMs) excel in generalization but suffer from insufficient spatial perception. Focusing on complex continuous environments, we categorize key perceptual bottlenecks into three spatial challenges: door interaction,multi-room navigation, and ambiguous instruction execution, where existing methods consistently suffer high failure rates. We present Spatial-VLN, a perception-guided exploration framework designed to overcome these challenges. The framework consists of two main modules. The Spatial Perception Enhancement (SPE) module integrates panoramic filtering with specialized door and region experts to produce spatially coherent, cross-view consistent perceptual representations. Building on this foundation, our Explored Multi-expert Reasoning (EMR) module uses parallel LLM experts to address waypoint-level semantics and region-level spatial transitions. When discrepancies arise between expert predictions, a query-and-explore mechanism is activated, prompting the agent to actively probe critical areas and resolve perceptual ambiguities. Experiments on VLN-CE demonstrate that Spatial VLN achieves state-of-the-art performance using only low-cost LLMs. Furthermore, to validate real-world applicability, we introduce a value-based waypoint sampling strategy that effectively bridges the Sim2Real gap. Extensive real-world evaluations confirm that our framework delivers superior generalization and robustness in complex environments. Our codes and videos are available at https://yueluhhxx.github.io/Spatial-VLN-web/.

**摘要 (中文翻译):**

> 利用大型语言模型（LLM）的零样本视觉和语言导航（VLN）代理在泛化方面表现出色，但空间感知不足。着眼于复杂的连续环境，我们将关键的感知瓶颈分为三个空间挑战：门交互、多房间导航和模糊的指令执行，其中现有方法始终遭受高失败率。我们提出了 Spatial-VLN，这是一个旨在克服这些挑战的感知引导探索框架。该框架由两个主要模块组成。空间感知增强 (SPE) 模块将全景过滤与专业的门和区域专家集成在一起，以生成空间连贯、跨视图一致的感知表示。在此基础上，我们的探索型多专家推理 (EMR) 模块使用并行的 LLM 专家来解决航点级语义和区域级空间转换。当专家预测之间出现差异时，查询和探索机制就会被激活，促使智能体积极探索关键领域并解决感知模糊性。 VLN-CE 上的实验表明，Spatial VLN 仅使用低成本的 LLM 即可实现最先进的性能。此外，为了验证现实世界的适用性，我们引入了一种基于价值的路点采样策略，可以有效地弥补 Sim2Real 的差距。广泛的现实世界评估证实，我们的框架在复杂环境中提供了卓越的泛化性和鲁棒性。我们的代码和视频可在 https://yueluhhxx.github.io/Spatial-VLN-web/ 获取。

---

### Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning

- **发布日期**: 2026-01-14
- **作者**: Yang Li, Aming Wu, Zihao Zhang, Yahong Han
- **分类**: cs.CV
- **Arxiv**: [2601.09111v1](http://arxiv.org/abs/2601.09111v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.09111v1)

**Abstract (English):**

> Vision-Language Navigation aims to enable agents to navigate to a target location based on language instructions. Traditional VLN often follows a close-set assumption, i.e., training and test data share the same style of the input images and instructions. However, the real world is open and filled with various unseen environments, posing enormous difficulties for close-set methods. To this end, we focus on the General Scene Adaptation (GSA-VLN) task, aiming to learn generalized navigation ability by introducing diverse environments and inconsistent intructions.Towards this task, when facing unseen environments and instructions, the challenge mainly lies in how to enable the agent to dynamically produce generalized strategies during the navigation process. Recent research indicates that by means of fast and slow cognition systems, human beings could generate stable policies, which strengthen their adaptation for open world. Inspired by this idea, we propose the slow4fast-VLN, establishing a dynamic interactive fast-slow reasoning framework. The fast-reasoning module, an end-to-end strategy network, outputs actions via real-time input. It accumulates execution records in a history repository to build memory. The slow-reasoning module analyze the memories generated by the fast-reasoning module. Through deep reflection, it extracts experiences that enhance the generalization ability of decision-making. These experiences are structurally stored and used to continuously optimize the fast-reasoning module. Unlike traditional methods that treat fast-slow reasoning as independent mechanisms, our framework enables fast-slow interaction. By leveraging the experiences from slow reasoning. This interaction allows the system to continuously adapt and efficiently execute navigation tasks when facing unseen scenarios.

**摘要 (中文翻译):**

> 视觉语言导航旨在使智能体能够根据语言指令导航到目标位置。传统的 VLN 通常遵循闭集假设，即训练和测试数据共享相同风格的输入图像和指令。然而，现实世界是开放的，充满了各种看不见的环境，给近集方法带来了巨大的困难。为此，我们专注于通用场景适应（GSA-VLN）任务，旨在通过引入多样化的环境和不一致的指令来学习广义导航能力。对于该任务，当面对未见的环境和指令时，挑战主要在于如何使智能体在导航过程中动态产生广义策略。最近的研究表明，通过快速和慢速认知系统，人类可以制定稳定的政策，从而加强他们对开放世界的适应。受这个想法的启发，我们提出了slow4fast-VLN，建立了动态​​交互的快慢推理框架。快速推理模块是一个端到端的策略网络，通过实时输入输出动作。它将执行记录累积在历史存储库中以构建内存。慢速推理模块分析快速推理模块生成的记忆。通过深度反思，提炼经验，增强决策的泛化能力。这些经验被结构化存储并用于不断优化快速推理模块。与将快慢推理视为独立机制的传统方法不同，我们的框架支持快慢交互。通过利用缓慢推理的经验。这种交互使得系统在面对未见过的场景时能够不断适应并有效地执行导航任务。

---

### GROKE: Vision-Free Navigation Instruction Evaluation via Graph Reasoning on OpenStreetMap

- **发布日期**: 2026-01-12
- **作者**: Farzad Shami, Subhrasankha Dey, Nico Van de Weghe, Henrikki Tenkanen
- **分类**: cs.CL
- **Arxiv**: [2601.07375v1](http://arxiv.org/abs/2601.07375v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.07375v1)

**Abstract (English):**

> The evaluation of navigation instructions remains a persistent challenge in Vision-and-Language Navigation (VLN) research. Traditional reference-based metrics such as BLEU and ROUGE fail to capture the functional utility of spatial directives, specifically whether an instruction successfully guides a navigator to the intended destination. Although existing VLN agents could serve as evaluators, their reliance on high-fidelity visual simulators introduces licensing constraints and computational costs, and perception errors further confound linguistic quality assessment. This paper introduces GROKE(Graph-based Reasoning over OSM Knowledge for instruction Evaluation), a vision-free training-free hierarchical LLM-based framework for evaluating navigation instructions using OpenStreetMap data. Through systematic ablation studies, we demonstrate that structured JSON and textual formats for spatial information substantially outperform grid-based and visual graph representations. Our hierarchical architecture combines sub-instruction planning with topological graph navigation, reducing navigation error by 68.5% compared to heuristic and sampling baselines on the Map2Seq dataset. The agent's execution success, trajectory fidelity, and decision patterns serve as proxy metrics for functional navigability given OSM-visible landmarks and topology, establishing a scalable and interpretable evaluation paradigm without visual dependencies. Code and data are available at https://anonymous.4open.science/r/groke.

**摘要 (中文翻译):**

> 导航指令的评估仍然是视觉和语言导航（VLN）研究中持续存在的挑战。 BLEU 和 ROUGE 等传统的基于参考的指标无法捕捉空间指令的功能效用，特别是指令是否成功引导导航器到达预期目的地。尽管现有的 VLN 代理可以充当评估器，但它们对高保真视觉模拟器的依赖引入了许可限制和计算成本，并且感知错误进一步混淆了语言质量评估。本文介绍了 GROKE（基于 OSM 知识的图形推理指令评估），这是一种无需视觉、无需训练、基于 LLM 的分层框架，用于使用 OpenStreetMap 数据评估导航指令。通过系统的消融研究，我们证明空间信息的结构化 JSON 和文本格式大大优于基于网格和可视化图形表示。我们的分层架构将子指令规划与拓扑图导航相结合，与 Map2Seq 数据集上的启发式和采样基线相比，将导航错误减少了 68.5%。代理的执行成功、轨迹保真度和决策模式作为给定 OSM 可见地标和拓扑的功能导航性的代理指标，建立了一个可扩展且可解释的评估范例，无需视觉依赖性。代码和数据可在 https://anonymous.4open.science/r/groke 获取。

---

### SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation

- **发布日期**: 2026-01-11
- **作者**: Jiwen Zhang, Zejun Li, Siyuan Wang, Xiangyu Shi, Zhongyu Wei, Qi Wu
- **分类**: cs.CV, cs.AI, cs.RO
- **Arxiv**: [2601.06806v1](http://arxiv.org/abs/2601.06806v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.06806v1)

**Abstract (English):**

> Although learning-based vision-and-language navigation (VLN) agents can learn spatial knowledge implicitly from large-scale training data, zero-shot VLN agents lack this process, relying primarily on local observations for navigation, which leads to inefficient exploration and a significant performance gap. To deal with the problem, we consider a zero-shot VLN setting that agents are allowed to fully explore the environment before task execution. Then, we construct the Spatial Scene Graph (SSG) to explicitly capture global spatial structure and semantics in the explored environment. Based on the SSG, we introduce SpatialNav, a zero-shot VLN agent that integrates an agent-centric spatial map, a compass-aligned visual representation, and a remote object localization strategy for efficient navigation. Comprehensive experiments in both discrete and continuous environments demonstrate that SpatialNav significantly outperforms existing zero-shot agents and clearly narrows the gap with state-of-the-art learning-based methods. Such results highlight the importance of global spatial representations for generalizable navigation.

**摘要 (中文翻译):**

> 虽然基于学习的视觉和语言导航（VLN）智能体可以从大规模训练数据中隐式学习空间知识，但零样本 VLN 智能体缺乏这个过程，主要依靠局部观察进行导航，这导致探索效率低下和显着的性能差距。为了解决这个问题，我们考虑零样本 VLN 设置，允许代理在任务执行之前充分探索环境。然后，我们构建空间场景图（SSG）来显式捕获所探索环境中的全局空间结构和语义。基于 SSG，我们引入了 SpatialNav，这是一种零样本 VLN 代理，它集成了以代理为中心的空间地图、罗盘对齐的视觉表示和远程对象定位策略，以实现高效导航。在离散和连续环境中进行的综合实验表明，SpatialNav 的性能显着优于现有的零样本代理，并明显缩小了与最先进的基于学习的方法的差距。这些结果凸显了全局空间表示对于通用导航的重要性。

---

### SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning

- **发布日期**: 2026-01-08
- **作者**: Zebin Han, Xudong Wang, Baichen Liu, Qi Lyu, Zhenduo Shang, Jiahua Dong, Lianqing Liu, Zhi Han
- **分类**: cs.RO, cs.AI
- **Arxiv**: [2601.04699v1](http://arxiv.org/abs/2601.04699v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.04699v1)

**Abstract (English):**

> Sequential-Horizon Vision-and-Language Navigation (SH-VLN) presents a challenging scenario where agents should sequentially execute multi-task navigation guided by complex, long-horizon language instructions. Current vision-and-language navigation models exhibit significant performance degradation with such multi-task instructions, as information overload impairs the agent's ability to attend to observationally relevant details. To address this problem, we propose SeqWalker, a navigation model built on a hierarchical planning framework. Our SeqWalker features: i) A High-Level Planner that dynamically selects global instructions into contextually relevant sub-instructions based on the agent's current visual observations, thus reducing cognitive load; ii) A Low-Level Planner incorporating an Exploration-Verification strategy that leverages the inherent logical structure of instructions for trajectory error correction. To evaluate SH-VLN performance, we also extend the IVLN dataset and establish a new benchmark. Extensive experiments are performed to demonstrate the superiority of the proposed SeqWalker.

**摘要 (中文翻译):**

> 顺序视野视觉和语言导航（SH-VLN）提出了一个具有挑战性的场景，其中代理应该在复杂的长视野语言指令的指导下顺序执行多任务导航。当前的视觉和语言导航模型在这种多任务指令下表现出显着的性能下降，因为信息过载削弱了智能体关注观察相关细节的能力。为了解决这个问题，我们提出了 SeqWalker，一种基于分层规划框架构建的导航模型。我们的 SeqWalker 具有以下特点： i) 高级规划器，可根据智能体当前的视觉观察动态地将全局指令选择为上下文相关的子指令，从而减少认知负荷； ii) 低级规划器结合了探索验证策略，利用指令的固有逻辑结构进行轨迹误差校正。为了评估 SH-VLN 性能，我们还扩展了 IVLN 数据集并建立了新的基准。进行了大量的实验来证明所提出的 SeqWalker 的优越性。

---

### AirNav: A Large-Scale Real-World UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions

- **发布日期**: 2026-01-07
- **作者**: Hengxing Cai, Yijie Rao, Ligang Huang, Zanyang Zhong, Jinhan Dong, Jingjun Tan, Wenhao Lu, Renxin Zhong
- **分类**: cs.CL
- **Arxiv**: [2601.03707v1](http://arxiv.org/abs/2601.03707v1)
- **PDF**: [下载链接](https://arxiv.org/pdf/2601.03707v1)

**Abstract (English):**

> Existing Unmanned Aerial Vehicle (UAV) Vision-Language Navigation (VLN) datasets face issues such as dependence on virtual environments, lack of naturalness in instructions, and limited scale. To address these challenges, we propose AirNav, a large-scale UAV VLN benchmark constructed from real urban aerial data, rather than synthetic environments, with natural and diverse instructions. Additionally, we introduce the AirVLN-R1, which combines Supervised Fine-Tuning and Reinforcement Fine-Tuning to enhance performance and generalization. The feasibility of the model is preliminarily evaluated through real-world tests. Our dataset and code are publicly available.

**摘要 (中文翻译):**

> 现有的无人机（UAV）视觉语言导航（VLN）数据集面临着对虚拟环境的依赖、指令缺乏自然性和规模有限等问题。为了应对这些挑战，我们提出了 AirNav，这是一种大型无人机 VLN 基准，由真实的城市航空数据而不是合成环境构建，具有自然和多样化的指令。此外，我们还推出了 AirVLN-R1，它结合了监督微调和强化微调，以增强性能和泛化能力。通过实际测试初步评估了模型的可行性。我们的数据集和代码是公开的。

---

### VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents

- **发布日期**: 2025-12-31
- **作者**: Xunyi Zhao, Gengze Zhou, Qi Wu
- **分类**: cs.CV, cs.RO
- **Arxiv**: [2512.24851v2](http://arxiv.org/abs/2512.24851v2)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.24851v2)

**Abstract (English):**

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities across a wide range of vision-language tasks. However, their performance as embodied agents, which requires multi-round dialogue spatial reasoning and sequential action prediction, needs further exploration. Our work investigates this potential in the context of Vision-and-Language Navigation (VLN) by introducing a unified and extensible evaluation framework to probe MLLMs as zero-shot agents by bridging traditional navigation datasets into a standardized benchmark, named VLN-MME. We simplify the evaluation with a highly modular and accessible design. This flexibility streamlines experiments, enabling structured comparisons and component-level ablations across diverse MLLM architectures, agent designs, and navigation tasks. Crucially, enabled by our framework, we observe that enhancing our baseline agent with Chain-of-Thought (CoT) reasoning and self-reflection leads to an unexpected performance decrease. This suggests MLLMs exhibit poor context awareness in embodied navigation tasks; although they can follow instructions and structure their output, their 3D spatial reasoning fidelity is low. VLN-MME lays the groundwork for systematic evaluation of general-purpose MLLMs in embodied navigation settings and reveals limitations in their sequential decision-making capabilities. We believe these findings offer crucial guidance for MLLM post-training as embodied agents.

**摘要 (中文翻译):**

> 多模态大语言模型 (MLLM) 在广泛的视觉语言任务中表现出了卓越的能力。然而，它们作为具体代理的性能需要多轮对话空间推理和顺序动作预测，需要进一步探索。我们的工作通过引入一个统一且可扩展​​的评估框架来探索 MLLM 作为零样本代理，通过将传统导航数据集桥接到一个名为 VLN-MME 的标准化基准，来研究视觉和语言导航 (VLN) 背景下的这种潜力。我们通过高度模块化且易于访问的设计简化了评估。这种灵活性简化了实验，实现了跨不同 MLLM 架构、代理设计和导航任务的结构化比较和组件级消融。至关重要的是，在我们的框架的支持下，我们观察到通过思想链（CoT）推理和自我反思来增强我们的基线代理会导致性能意外下降。这表明 MLLM 在具体导航任务中表现出较差的上下文感知能力；尽管它们可以遵循指令并构建输出，但它们的 3D 空间推理保真度较低。 VLN-MME 为在具体导航设置中系统评估通用 MLLM 奠定了基础，并揭示了其顺序决策能力的局限性。我们相信这些发现为 MLLM 作为具体代理的后期培训提供了重要的指导。

---

