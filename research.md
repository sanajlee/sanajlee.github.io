---
layout: page
title: Research
permalink: /research
published: true
---

<div class="research-page" markdown="1">

<p class="research-lead">
I study <strong>language model behavior</strong>: what language models know about language,
how that knowledge is represented internally, and how it shapes what they eventually do.
My current work approaches these questions from three closely connected directions.
</p>


## 01. Representations & Interpretability

What happens inside a language model before an answer appears?

I am interested in how linguistic information is represented across layers and components of language models, and in connecting those internal representations to observable behavior. My work uses representation-level analyses to ask where linguistic knowledge emerges, how it changes during processing, and whether internal states can help explain, or causally alter, model behavior.

Current directions include layer-wise analysis, probing and causal interventions, as well as mechanistic approaches such as representation steering and sparse feature analysis.

### Related work

- **Do Korean-Adapted LLMs Think in Korean? Analyzing Latent Language and the Preservation of Korean-Specific Knowledge**  
  *Sangah Lee*. Language and Information, 2025.  
  [[paper]]({{ '/papers/latentlang.pdf' | relative_url }})

- **A Short Note on the Structural Priming in LLM: Focusing on Dative Constructions in Korean**  
  Semoon Hoe and *Sangah Lee*. Language and Information, 2024.  
  [[paper]]({{ '/papers/priming.pdf' | relative_url }})


## 02. Multilinguality & Latent Language

What does multilingual processing look like *inside* a language model?

Rather than treating multilinguality only as a difference in task performance across languages, I am interested in internal linguistic asymmetries: whether models rely on English or other dominant languages as intermediate representations, when target-language representations emerge, and how these internal dynamics relate to the final output.

More broadly, I study how language-specific linguistic and cultural knowledge survives — or fails to survive — multilingual model adaptation.

### Related work

- **Do Korean-Adapted LLMs Think in Korean? Analyzing Latent Language and the Preservation of Korean-Specific Knowledge**  
  *Sangah Lee*. Language and Information, 2025.  
  [[paper]]({{ '/papers/latentlang.pdf' | relative_url }})

- **Nunchi-Bench: Benchmarking Language Models on Cultural Reasoning with a Focus on Korean Superstition**  
  Kyuhee Kim and *Sangah Lee*. Findings of ACL 2025.  
  [[paper]](https://aclanthology.org/2025.findings-acl.794.pdf)


## 03. Linguistic Knowledge & Reasoning

When a language model gives the right answer, what kind of competence produced it?

I study how language models use linguistic and culturally situated knowledge during reasoning, and how we can distinguish genuine inference from memorization, heuristics, or other shortcuts. I am especially interested in cases where models appear behaviorally successful while relying on very different internal processes.

This connects linguistic evaluation with broader questions about reasoning, memorization, and the interpretation of model-generated rationales.

### Related work

- **Nunchi-Bench: Benchmarking Language Models on Cultural Reasoning with a Focus on Korean Superstition**  
  Kyuhee Kim and *Sangah Lee*. Findings of ACL 2025.  
  [[paper]](https://aclanthology.org/2025.findings-acl.794.pdf)

- **Large Language Models Show Human-Like Abstract Thinking Patterns: A Construal-Level Perspective**  
  Seung Joo Yoo and *Sangah Lee*. CogSci 2024.  
  [[paper]](https://escholarship.org/content/qt3f28f61v/qt3f28f61v_noSplash_fec2deeee2a04a7f7c0683aedd2fb478.pdf?t=sev1vq)


## Earlier Work

My earlier work focused on multilingual and low-resource NLP, particularly Korean and Manchu, as well as argument mining and discourse analysis. These projects continue to shape how I think about linguistic structure, language-specific variation, and evaluation in my current work on language models.

### Low-resource & multilingual NLP

- **ManWav: The First Manchu ASR Model**  
  Jean Seo, Minha Kang, SungJoo Byun, and *Sangah Lee*. Field Matters 2024.

- **ManNER & ManPOS: Pioneering NLP for Endangered Manchu Language**  
  *Sangah Lee*, Sungjoo Byun, Jean Seo, and Minha Kang. LREC-COLING 2024.

- **Mergen: The First Manchu-Korean Machine Translation Model Trained on Augmented Data**  
  Jean Seo, Sungjoo Byun, Minha Kang, and *Sangah Lee*. MRL 2023.

- **The Korean Morphologically Tight-Fitting Tokenizer for Noisy User-Generated Texts**  
  *Sangah Lee* and Hyopil Shin. W-NUT 2021.

### Argument mining & discourse

- **Argument Facet Detection in Online Debates Based on Attention Weights and Clustering with Combined Similarity Matrices**  
  *Sangah Lee* and Hyopil Shin. Korean Journal of Linguistics, 2021.

- **An Analysis of Linear Argumentation Structure of Korean Debate Texts Using Sequential Modeling and Linguistic Features**  
  *Sangah Lee* and Hyopil Shin. Journal of KIISE, 2018.

- **Stance Classification of Online Debate Texts based on Discourse Relations**  
  *Sangah Lee* and Hyopil Shin. Language Research, 2016.

</div>