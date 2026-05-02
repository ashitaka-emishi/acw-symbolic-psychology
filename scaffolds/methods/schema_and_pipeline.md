# Schema And Pipeline Scaffold

This scaffold generates the reusable data model and workflow for
`acw-symbolic-psychology`.

---

## Design Principles

1. Raw source text is immutable.
2. Segmentation happens before annotation.
3. Sentence IDs are permanent.
4. All interpretive claims must be traceable to text spans.
5. Every document carries source, register, date, authorship, and risk metadata.
6. Every annotation carries confidence and uncertainty.
7. Every aggregate claim must be reproducible from JSON.

---

## Stage 1 Corpus Manifest Schema

Create `schemas/corpus_manifest.schema.json` and require this shape:

```json
{
  "actor_id": "lincoln",
  "actor_name": "Abraham Lincoln",
  "module_status": "pilot_reference",
  "documents": [
    {
      "document_id": "lincoln_doc_001",
      "title": "Second Inaugural Address",
      "short_title": "Second Inaugural",
      "date": "1865-03-04",
      "date_precision": "exact",
      "phase": "collapse_and_reconstruction_threshold",
      "register": "formal_public_address",
      "genre": "inaugural_address",
      "authorship": "sole_or_primary",
      "authorship_confidence": 0.99,
      "source_tier": 3,
      "source_repository": "Collected Works of Abraham Lincoln",
      "source_url": "https://quod.lib.umich.edu/l/lincoln/",
      "source_citation": "Fill in exact volume/page/item during acquisition.",
      "transcription_status": "verified",
      "risk_flags": [],
      "inclusion_rationale": "Canonical endpoint for providence, judgment, and healing clusters.",
      "analytical_priority": "critical",
      "expected_cluster_priors": ["body_wound_healing", "providence_theodicy"],
      "notes": null
    }
  ]
}
```

---

## Stage 2 Normalized Text Frontmatter

Each normalized markdown file must include:

```yaml
---
document_id: "grant_doc_004"
actor_id: "grant"
actor_name: "Ulysses S. Grant"
title: "Report on Vicksburg Campaign"
short_title: "Vicksburg Report"
date: "1863-07-06"
date_precision: "exact"
phase: "emancipation_war"
register: "battle_report"
genre: "official_report"
authorship: "sole_or_primary"
authorship_confidence: 0.95
source_tier: 3
source_repository: "Papers of Ulysses S. Grant"
source_url: "TBD exact document URL"
source_citation: "TBD"
transcription_status: "normalized"
risk_flags: []
pipeline_log:
  - stage: 2
    date: "YYYY-MM-DD"
    agent: "source_normalizer"
---
```

---

## Stage 3 Segmented Document Schema

Create `schemas/segmented_document.schema.json`.

Required shape:

```json
{
  "document_id": "actor_doc_001",
  "actor_id": "actor",
  "meta": {},
  "sections": [
    {
      "section_id": "actor_doc_001_s01",
      "section_label": "opening",
      "section_ordinal": 1,
      "paragraphs": [
        {
          "paragraph_id": "actor_doc_001_s01_p01",
          "paragraph_ordinal": 1,
          "sentences": [
            {
              "sentence_id": "actor_doc_001_s01_p01_sent01",
              "sentence_ordinal": 1,
              "text": "Sentence text.",
              "word_offset_start": 0,
              "word_offset_end": 12,
              "char_offset_start": 0,
              "char_offset_end": 70,
              "speaker": "actor",
              "authorship_note": null,
              "metaphor_candidates": [],
              "metaphor_instances": []
            }
          ]
        }
      ]
    }
  ],
  "pipeline_log": []
}
```

---

## Stage 4 Annotation Schema

Create `schemas/annotation.schema.json`.

Every metaphor instance must include:

```json
{
  "instance_id": "inst_000001",
  "actor_id": "lincoln",
  "document_id": "lincoln_doc_001",
  "sentence_id": "lincoln_doc_001_s01_p01_sent01",
  "span_text": "binding up the nation's wounds",
  "span_char_start": 14,
  "span_char_end": 44,
  "cmt": {
    "cluster_id": "body_wound_healing",
    "source_domain": "wound_healing",
    "target_domain": "national_reunification",
    "mapping": [
      {"source": "body", "target": "nation"},
      {"source": "wound", "target": "civil_war_damage"},
      {"source": "healing", "target": "reconstruction"}
    ],
    "entailments": [
      "the_nation_is_a_body",
      "division_is_physical_injury",
      "restoration_is_medical_care"
    ],
    "linguistic_form": "verbal_phrase",
    "metaphoricity": "conventional_active",
    "is_extended_metaphor": true,
    "extension_group_id": "ext_0001",
    "co_activated_clusters": []
  },
  "koenigsberg": {
    "fantasy_type": ["wound_and_healing"],
    "magical_object": ["union_body"],
    "violence_logic": ["restorative"],
    "obligatory_frame": true,
    "obligatory_frame_notes": "Healing a wound is framed as necessary care.",
    "guilt_distribution": "distributed",
    "sacrificial_economy": false,
    "sacrificial_yield": null,
    "psychic_defense": ["reparation"],
    "exit_condition_present": true,
    "exit_condition_type": "wound_healed"
  },
  "agency": {
    "agent_of_action": "healer_or_state",
    "agent_is_abstract": true,
    "object_of_action": "national_body",
    "beneficiary": "nation",
    "passive_entities": [],
    "erased_agents": ["formerly_enslaved_people_if_contextually_required"]
  },
  "action_orientation": {
    "values": ["heal_after_violence", "reconcile_after_violence"],
    "notes": "The metaphor points toward reconstruction as care."
  },
  "absence": {
    "absence_flags": [],
    "absence_notes": null
  },
  "meta": {
    "annotator": "annotator_id",
    "reviewer": null,
    "confidence": 0.92,
    "ambiguity_flag": false,
    "ambiguity_notes": null,
    "suppression_flag": false,
    "suppression_notes": null,
    "created_at": "YYYY-MM-DD"
  }
}
```

---

## Document Summary Schema

Create `schemas/document_summary.schema.json`.

Required fields:

- `total_sentences`
- `candidate_sentences`
- `annotated_sentences`
- `total_instances`
- `cluster_distribution`
- `fantasy_type_distribution`
- `violence_logic_distribution`
- `magical_object_distribution`
- `action_orientation_distribution`
- `obligatory_frame_rate`
- `sacrificial_economy_rate`
- `absence_flag_counts`
- `mean_confidence`
- `register_adjusted_density`
- `primary_finding`
- `disconfirmed_priors`
- `quality_notes`

---

## Person Profile Schema

Create `schemas/person_profile.schema.json`.

Required fields:

- `actor_id`
- `corpus_size`
- `date_range`
- `register_distribution`
- `dominant_clusters`
- `dominant_fantasy_types`
- `dominant_magical_objects`
- `dominant_violence_logics`
- `dominant_action_orientations`
- `guilt_distribution_arc`
- `sacrificial_economy_profile`
- `absence_profile`
- `diachronic_pattern`
- `register_effects`
- `comparison_hooks`
- `limitations`

---

## Group Comparison Schema

Create `schemas/group_comparison.schema.json`.

Required fields:

- `group_id`
- `actors`
- `corpus_size`
- `register_distribution`
- `cluster_distribution`
- `fantasy_type_distribution`
- `violence_logic_distribution`
- `magical_object_distribution`
- `action_orientation_distribution`
- `exit_condition_distribution`
- `group_distinctive_features`
- `within_group_variance`
- `contrast_groups`
- `statistical_tests`
- `close_reading_evidence`
- `limitations`

---

## Validation Scripts

Create scripts:

- `validate_manifest.py`
- `validate_segments.py`
- `validate_annotations.py`
- `build_document_summaries.py`
- `build_person_profiles.py`
- `build_group_comparisons.py`
- `reliability_report.py`

Validation must fail when:

- required fields are missing
- confidence is outside `[0, 1]`
- `sacrificial_economy` is false but `sacrificial_yield` is non-null
- `is_extended_metaphor` is true but `extension_group_id` is null
- sentence IDs in annotations do not exist in segmented JSON
- actor ID or document ID mismatch occurs
- source URL or citation is missing from manifest
- register is outside enum
- unapproved taxonomy value appears

---

## Pipeline Command

Create a single runner:

```bash
python scripts/run_pipeline.py --stage all
```

Stage flags:

- `manifest`
- `acquire`
- `normalize`
- `segment`
- `candidates`
- `validate`
- `summaries`
- `profiles`
- `groups`
- `export`

All generated outputs go in `data/derived/`, `analyses/tables/`, and
`analyses/figures/`.

