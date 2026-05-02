# SCAFFOLD.md - acw-symbolic-psychology

This scaffold defines a new monorepo named `acw-symbolic-psychology/`.
It is not part of the earlier Lincoln project. The earlier project should be
treated as a methodological pilot and cited by URL:

https://github.com/ashitaka-emishi/lincoln-metaphor-analysis

Do not refer to the pilot by local filesystem path in project documents.

---

## Overarching Working Thesis

Civil War actors did not merely disagree over policy. They inhabited competing
symbolic worlds in which nation, slavery, violence, sacrifice, and obligation
had different psychic structures. These structures shaped what each actor
experienced as necessary action.

Treat this as the project's governing thesis, not as a single statistical
hypothesis. It frames the research problem and the interpretive stakes. The
testable claims appear below as predeclared actor and group hypotheses: which
metaphor clusters should dominate, which magical objects should organize each
symbolic world, which violence logics should appear, which absences should
recur, and where the evidence would force revision.

In practical terms:

- the thesis organizes the project
- the hypotheses operationalize the thesis
- the corpus can confirm, qualify, or disconfirm the hypotheses
- the final thesis must be revised in light of the evidence

---

## What This Project Builds

Build a structured, reproducible research monorepo for comparing the symbolic
psychology of major American Civil War voices. The primary context is the ACW,
but the framework must be repeatable and adaptable to other conflicts.

The project combines:

1. Conceptual Metaphor Theory (CMT): identifies metaphor mappings, source
   domains, target domains, and entailments.
2. Koenigsbergian historical psychology: interprets ideological fantasy,
   magical objects, sacrificial economies, guilt distribution, and violence
   logics.
3. Corpus-based digital humanities: enforces repeatable collection,
   segmentation, annotation, validation, analysis, and publication workflows.
4. Comparative group analysis: compares symbolic worlds across factions, roles,
   registers, and phases of the conflict.

The Lincoln pilot showed how to analyze one actor's metaphor system. This
monorepo generalizes that workflow to a group of actors and tests whether the
method can scale without becoming impressionistic.

---

## Big Bang For Buck Requirement

The most important upgrade from an interesting interpretive project to an
academically defensible project is not more interpretation. It is validation.

Therefore the scaffold must build in, from the start:

1. A formal codebook with operational definitions.
2. A transparent corpus registry with source provenance, register, authorship,
   transmission risk, and inclusion rationale.
3. A repeatable pipeline that can rebuild corpus, segmentation, annotations,
   tables, and reports.
4. A comparison design, not isolated single-author essays.
5. A reliability plan: inter-annotator agreement where possible; intra-annotator
   checks if working alone.
6. Uncertainty fields and disconfirmation tests.
7. At least one modest quantitative comparison per analysis layer.
8. Clear limits on causal claims: symbolic structures shape perceived
   necessity; they do not mechanically cause action.

This is the publication-grade upgrade path. Every scaffold file should protect
these requirements.

---

## Actor Set

Create a person module for each actor:

1. Abraham Lincoln
2. Frederick Douglass
3. Jefferson Davis
4. Alexander H. Stephens
5. John Brown
6. Robert E. Lee
7. Thomas J. "Stonewall" Jackson
8. James Longstreet
9. Ulysses S. Grant
10. George B. McClellan
11. William Tecumseh Sherman
12. Walt Whitman

Each person receives:

- a corpus manifest
- source acquisition notes
- person-specific metaphor cluster priors
- disconfirmation tests
- register controls
- absence-analysis targets
- action-orientation hypotheses
- individual report scaffold
- comparison hooks into group-level analysis

---

## Comparison Groups

Use overlapping group membership rather than forcing each actor into only one
category.

Primary groups:

- `union_political`: Lincoln
- `union_military`: Grant, Sherman, McClellan
- `abolitionist_prophetic`: Douglass, Brown
- `confederate_political`: Davis, Stephens
- `confederate_military`: Lee, Jackson, Longstreet
- `literary_cultural_witness`: Whitman

Secondary analytical groupings:

- `official_state_voice`
- `military_command_voice`
- `prophetic_moral_voice`
- `retrospective_memoir_voice`
- `wartime_public_voice`
- `private_or_semi_private_voice`
- `postwar_justification_voice`

Group membership is metadata. It is not interpretation by itself.

---

## Research Questions

### RQ1 - Symbolic Worlds

What symbolic world does each actor inhabit? What objects, bodies, structures,
covenants, diseases, wounds, instruments, inheritances, or divine agencies make
the war intelligible to them?

### RQ2 - Magical Object

What is treated as the sacred or magical object requiring defense, sacrifice,
obedience, proof, purification, or redemption?

Possible values include:

- `union_body`
- `confederate_nation`
- `state_sovereignty`
- `racial_order`
- `enslaved_humanity`
- `founding_proposition`
- `constitutional_covenant`
- `army_body`
- `home_or_virginia`
- `divine_will`
- `democratic_people`
- `wounded_soldier_body`

### RQ3 - Violence Logic

What does violence do within the symbolic system?

- restore a wounded body
- prove a proposition
- punish guilt
- purify contamination
- redeem sin
- defend honor
- protect home
- obey Providence
- exhaust resistance
- solve a practical military problem
- create a new political order

### RQ4 - Necessity and Action

How does metaphor convert contingency into necessity? What actions become
experienced as obligatory rather than chosen?

### RQ5 - Guilt and Agency

Where does guilt reside? Who is allowed agency? Who becomes passive, abstract,
or erased?

### RQ6 - Exit Conditions

Does the symbolic structure contain an endpoint? Wounds can heal; debts can be
paid; propositions can be proven; punishments can be completed. Purification
logic often lacks an endpoint.

### RQ7 - Group Comparison

Which symbolic structures distinguish Union political, Union military,
abolitionist prophetic, Confederate political, Confederate military, and
literary/cultural voices?

### RQ8 - Portability

Which parts of the framework are ACW-specific, and which can be reused for
other conflicts?

---

## Predeclared Hypotheses

These hypotheses guide early annotation. They are not conclusions.

### H1 - Lincoln

Lincoln's symbolic system centers on Union as body, covenant, experiment,
inheritance, and providential judgment. Its dominant violence logics are
restorative, evidentiary, obligatory, sacrificial, and theodical. The pilot
claims that disease-and-purification logic is absent or structurally refused.

### H2 - Douglass

Douglass's symbolic system centers on slavery as darkness, prison, theft,
violence, and desecration; freedom as light, speech, manhood, and deliverance.
His action orientation should intensify from moral exposure toward Black agency,
citizenship, and armed participation.

### H3 - Davis

Davis likely frames the Confederacy as rightful political selfhood under
assault. Union action appears as tyranny, invasion, coercion, or violation.
Violence becomes defensive obligation.

### H4 - Stephens

Stephens likely uses architecture, foundation, cornerstone, hierarchy, and
natural order to make racial domination appear structural, rational, and
necessary.

### H5 - Brown

Brown likely uses sin, blood, martyrdom, captivity, and divine law to make
violent action against slavery appear sacred obligation.

### H6 - Lee

Lee likely organizes action around duty, home, Virginia, honor, and Providence.
Violence appears as reluctant obligation rather than ideological aggression.

### H7 - Jackson

Jackson likely intensifies providence, obedience, instrumentality, discipline,
and death-as-passage. Agency may shift from self to God-as-commander.

### H8 - Longstreet

Longstreet likely organizes war through calculation, cost, position, defensive
logic, and professional judgment. His symbolic system may demystify sacrifice
relative to Lee and Jackson.

### H9 - Grant

Grant likely uses practical, material, pressure, work, and problem-solving
frames. Violence appears as sustained labor toward surrender and settlement.

### H10 - McClellan

McClellan likely frames the army as a beloved body and himself as guardian or
savior, while politics appears as interference, corruption, or danger.

### H11 - Sherman

Sherman likely frames war as fire, machine, storm, medicine, and social
pressure. Violence becomes a harsh cure aimed at breaking the South's will and
war-making capacity.

### H12 - Whitman

Whitman likely frames the nation as a democratic body and soldiers as sacred
or wounded bodies. His action orientation is witnessing, nursing, mourning,
absorbing, and healing rather than command.

---

## Disconfirmation Rules

Every hypothesis must have a way to fail.

Examples:

- If Stephens does not use architectural/foundation language at high salience,
  `cluster_architecture_order` must be downgraded.
- If Brown's divine-law language is less central than constitutional or
  humanitarian language, the `prophetic_martyrdom` prior must be revised.
- If Grant contains high rates of providential or sacrificial metaphor, the
  "plain practical pressure" hypothesis must be qualified.
- If disease/purification appears in Lincoln directed at a social group rather
  than an institution, the pilot's central structural claim must be reopened.
- If Sherman uses cure/destruction metaphors without purifying social-group
  logic, the distinction between `hard_war_as_medicine` and
  `disease_and_purification` must be maintained.

Disconfirmation is a success condition, not a failure of the project.

---

## Repository Layout To Generate

Create this structure in the new monorepo:

```text
acw-symbolic-psychology/
  README.md
  SCAFFOLD.md
  CITATION.cff
  LICENSE
  package.json
  pyproject.toml

  docs/
    index.md
    thesis.md
    how_to_read.md
    limitations.md
    publication_plan.md

  methods/
    theoretical_framework.md
    cmt_protocol.md
    koenigsberg_protocol.md
    metaphor_identification_protocol.md
    annotation_codebook.md
    absence_analysis.md
    reliability_validation.md
    adaptation_guide.md

  schemas/
    corpus_manifest.schema.json
    segmented_document.schema.json
    annotation.schema.json
    document_summary.schema.json
    person_profile.schema.json
    group_comparison.schema.json

  config/
    shared_taxonomy.yaml
    actors.yaml
    groups.yaml
    phases.yaml
    registers.yaml
    source_repositories.yaml

  scripts/
    acquire_sources.py
    normalize_text.py
    segment_documents.py
    extract_candidates.py
    validate_manifest.py
    validate_segments.py
    validate_annotations.py
    build_document_summaries.py
    build_person_profiles.py
    build_group_comparisons.py
    reliability_report.py
    export_tables.py
    run_pipeline.py

  data/
    raw/
    normalized/
    segmented/
    annotated/
    derived/
    reliability_samples/

  persons/
    lincoln/
    douglass/
    davis/
    stephens/
    brown/
    lee/
    jackson/
    longstreet/
    grant/
    mcclellan/
    sherman/
    whitman/

  groups/
    union_political/
    union_military/
    abolitionist_prophetic/
    confederate_political/
    confederate_military/
    literary_cultural_witness/

  analyses/
    individual/
    group/
    comparative/
    validation/
    figures/
    tables/

  scaffolds/
    methods/
    persons/
    groups/
```

The files in `scaffolds/` are the build prompts and design documents. The files
in `methods/`, `schemas/`, `config/`, `scripts/`, `data/`, `persons/`, and
`groups/` are the actual generated research project.

---

## Pipeline Stages

### Stage 0 - Method Setup

Read:

- `scaffolds/methods/theoretical_framework.md`
- `scaffolds/methods/schema_and_pipeline.md`
- `scaffolds/methods/validation_and_reliability.md`
- `scaffolds/methods/adaptation_guide.md`

Then generate shared methods, schemas, config, and validation scripts.

### Stage 1 - Corpus Manifest

For each actor, create `persons/{actor}/corpus_manifest.json`.

Each manifest item must include:

- `document_id`
- `actor_id`
- `title`
- `short_title`
- `date`
- `date_precision`
- `phase`
- `register`
- `genre`
- `authorship`
- `authorship_confidence`
- `source_repository`
- `source_url`
- `source_citation`
- `transcription_status`
- `risk_flags`
- `inclusion_rationale`
- `analytical_priority`
- `expected_cluster_priors`
- `notes`

### Stage 2 - Source Acquisition

Acquire texts into `data/raw/{actor}/`.

Rules:

- Prefer primary sources and scholarly editions.
- Keep raw text immutable.
- Record source URL and retrieval date.
- Preserve page, volume, and editorial notes where possible.
- For retrospective memoirs, set `register: retrospective_memoir` and add
  `risk_flags: ["postwar_retrospection"]`.

### Stage 3 - Normalization

Create `data/normalized/{actor}/{document_id}.md` with YAML frontmatter.

Normalize:

- OCR artifacts
- page headers
- navigation text
- footnote markers
- line breaks
- obvious transcription noise

Do not modernize spelling unless explicitly marked.

### Stage 4 - Segmentation

Create `data/segmented/{actor}/{document_id}.json`.

IDs are permanent after segmentation:

```text
{actor_id}_{doc_id}_s{NN}_p{NN}_sent{NN}
```

Never renumber after annotation begins.

### Stage 5 - Candidate Metaphor Detection

Use a hybrid process:

- MIP/MIPVU-inspired lexical candidate identification.
- Rule-based source-domain lexicons.
- Person-specific cluster priors.
- Human review before annotation.

Candidate extraction is not the final annotation. It is a triage layer.

### Stage 6 - Annotation

Annotate metaphor instances using the shared schema. Each instance must include:

- CMT fields
- Koenigsbergian fields
- historical context fields
- action-orientation fields
- absence flags
- confidence score
- uncertainty notes

### Stage 7 - Reliability And Validation

Minimum required validation:

- Random sample of at least 200 sentences across actors and registers.
- Double-code metaphor presence/absence and cluster classification.
- Compute Cohen's kappa where two coders exist.
- If working alone, do intra-annotator recoding after a time gap and report
  stability.
- Report false positives and false negatives from candidate extraction.
- Maintain a validation report in `analyses/validation/`.

### Stage 8 - Person Profiles

Generate `persons/{actor}/profile.md` and `analyses/individual/{actor}.md`.

Each profile must include:

- dominant clusters
- source-domain distribution
- target-domain distribution
- magical object profile
- violence logic profile
- guilt distribution
- sacrificial economy
- agency and absence analysis
- action-orientation analysis
- diachronic shifts
- register differences
- comparison hooks
- disconfirmed priors

### Stage 9 - Group Comparison

Generate `groups/{group}/group_profile.md` and comparison tables.

Required group comparisons:

- cluster distribution by group
- violence logic by group
- magical object by group
- guilt distribution by group
- action orientation by group
- absence flags by group
- exit-condition analysis by group
- register-controlled versions of all major claims

### Stage 10 - Publication Outputs

Generate:

- `docs/thesis.md`
- `docs/methods.md`
- `docs/findings.md`
- `docs/limitations.md`
- `analyses/tables/*.csv`
- `analyses/figures/*.png`
- `analyses/comparative/symbolic_worlds.md`
- `analyses/comparative/violence_logics.md`
- `analyses/comparative/necessary_action.md`
- `analyses/comparative/portability_to_other_conflicts.md`

---

## Shared Taxonomy

The taxonomy must distinguish universal analytic categories from ACW-specific
instantiations.

### Universal Source Domains

- body
- wound
- disease
- healing
- birth
- death
- blood
- family
- home
- architecture
- foundation
- machine
- instrument
- journey
- law
- contract
- covenant
- trial
- experiment
- light_dark
- fire
- storm
- agriculture
- property
- captivity
- religion
- providence
- sacrifice
- debt
- honor
- voice
- vision

### Universal Fantasy Types

- `wound_and_healing`
- `disease_and_purification`
- `birth_and_creation`
- `sacrifice_and_redemption`
- `oath_and_obligation`
- `punishment_and_theodicy`
- `ancestral_debt`
- `experiment_and_proof`
- `honor_and_vindication`
- `captivity_and_deliverance`
- `home_defense`
- `machine_pressure`
- `apocalypse_and_judgment`
- `witness_and_mourning`

### Violence Logics

- `restorative`
- `generative`
- `punitive`
- `purifying`
- `evidentiary`
- `obligatory`
- `defensive`
- `redemptive`
- `instrumental`
- `exhaustive`
- `protective`
- `vindicating`
- `apocalyptic`

### Action Orientations

- `preserve_union`
- `destroy_slavery`
- `defend_sovereignty`
- `defend_home`
- `vindicate_honor`
- `obey_providence`
- `redeem_sin`
- `prove_democracy`
- `punish_enemy`
- `purify_body_politic`
- `exhaust_resistance`
- `break_war_capacity`
- `protect_army`
- `bear_witness`
- `heal_after_violence`
- `reconcile_after_violence`

---

## Register Controls

Required register enum:

- `formal_public_address`
- `campaign_speech`
- `congressional_message`
- `legal_document`
- `military_order`
- `battle_report`
- `official_correspondence`
- `private_letter`
- `semi_public_letter`
- `diary_or_journal`
- `sermon_or_prophetic_address`
- `poetry`
- `literary_prose`
- `newspaper_article`
- `retrospective_memoir`
- `postwar_apologia`
- `fragment_private`

No raw frequency comparison is valid unless register is controlled or
acknowledged.

---

## Historical Phases

Use common ACW phases across all actor modules:

- `antebellum_baseline`: before 1854
- `sectional_crisis`: 1854-1860
- `secession_crisis`: November 1860-April 1861
- `early_war`: April 1861-December 1862
- `emancipation_war`: January 1863-November 1863
- `hard_war_and_reelection`: December 1863-November 1864
- `collapse_and_reconstruction_threshold`: December 1864-April 1865
- `postwar_memory`: after April 1865

Actors with no documents in a phase should record absence rather than invent
coverage.

---

## Source Hierarchy

Use this hierarchy for corpus acquisition:

1. Author manuscript, if available.
2. Contemporary printed version authorized or corrected by author.
3. Scholarly documentary edition.
4. Digitized archival collection with reliable metadata.
5. Contemporary newspaper report.
6. Later collected edition.
7. Retrospective memoir.
8. Quoted fragments in secondary sources.

Every document must carry source tier and risk flags. Retrospective memoirs are
valid data, but they answer questions about memory, justification, and symbolic
reconstruction as much as wartime cognition.

---

## Minimum Quantitative Tests

At least one test must appear in each major report:

- chi-square or Fisher exact test for cluster distribution by group
- trend analysis by phase
- register-controlled metaphor density comparison
- correlation between cluster activation and action orientation
- comparison of obligatory-frame rate across groups
- comparison of purification logic across actors
- confidence-weighted sensitivity analysis

Quantitative tests support interpretation. They do not replace close reading.

---

## Minimum Close Reading Requirements

Each actor report must include:

- one canonical metaphor passage
- one ambiguous or low-confidence passage
- one absence or suppression case
- one passage that complicates the initial hypothesis
- one passage linked to action orientation

Each group report must include:

- one representative passage per actor
- one cross-group contrast
- one register caveat
- one disconfirmation or uncertainty note

---

## Claims Discipline

Allowed claims:

- "This metaphor structure made X action intelligible as necessary."
- "This passage frames violence as restorative rather than punitive."
- "This actor's corpus shows higher rates of divine-instrument language than
  the comparison group, subject to register controls."
- "The symbolic structure helps explain why certain actions could be
  experienced as obligatory."

Forbidden or high-risk claims unless independently supported:

- "This metaphor caused the actor to do X."
- "This text proves unconscious motive."
- "This actor believed X in a simple literal sense."
- "This group thought uniformly."
- "This person represents the entire faction."

Use "symbolic structure," "action orientation," "perceived necessity," and
"interpretive hypothesis" rather than deterministic causal language.

---

## Build Order For Code Agents

1. Create all directories in the repository layout.
2. Create shared schemas and config files.
3. Create method documents from `scaffolds/methods/`.
4. Create person directories from `scaffolds/persons/`.
5. Create group directories from `scaffolds/groups/`.
6. Implement validation scripts before doing large-scale annotation.
7. Populate source manifests with starter corpus items.
8. Run validation on manifests.
9. Only then begin source acquisition and segmentation.

---

## Scaffold File Index

Method scaffolds:

- `scaffolds/methods/theoretical_framework.md`
- `scaffolds/methods/schema_and_pipeline.md`
- `scaffolds/methods/validation_and_reliability.md`
- `scaffolds/methods/adaptation_guide.md`

Group scaffold:

- `scaffolds/groups/group_analysis.md`

Person scaffolds:

- `scaffolds/persons/lincoln.md`
- `scaffolds/persons/douglass.md`
- `scaffolds/persons/jefferson_davis.md`
- `scaffolds/persons/alexander_stephens.md`
- `scaffolds/persons/john_brown.md`
- `scaffolds/persons/robert_e_lee.md`
- `scaffolds/persons/stonewall_jackson.md`
- `scaffolds/persons/james_longstreet.md`
- `scaffolds/persons/ulysses_s_grant.md`
- `scaffolds/persons/george_mcclellan.md`
- `scaffolds/persons/william_tecumseh_sherman.md`
- `scaffolds/persons/walt_whitman.md`

---

## External Anchors

Use these as starting source anchors, but verify all document-level URLs during
corpus acquisition:

- Lincoln pilot: https://github.com/ashitaka-emishi/lincoln-metaphor-analysis
- Collected Works of Abraham Lincoln: https://quod.lib.umich.edu/l/lincoln/
- Abraham Lincoln Papers, Library of Congress:
  https://www.loc.gov/collections/abraham-lincoln-papers/
- Frederick Douglass Papers, Library of Congress:
  https://www.loc.gov/collections/frederick-douglass-papers/
- Papers of Jefferson Davis, Rice University:
  https://jeffersondavis.rice.edu/
- Papers of Ulysses S. Grant, Mississippi State:
  https://scholarsjunction.msstate.edu/papers-of-ulysses-s-grant/
- Walt Whitman Archive: https://whitmanarchive.org/
- Project Gutenberg: https://www.gutenberg.org/
- Library of Congress: https://www.loc.gov/
- Open Library / Internet Archive: https://openlibrary.org/

---

## Success Criteria

The project is successful when it can:

1. Rebuild the corpus and annotations from documented sources.
2. Explain the annotation rules clearly enough for another researcher to apply.
3. Report reliability and uncertainty.
4. Compare actors without flattening register, role, faction, or date.
5. Produce individual symbolic profiles and group-level symbolic-world maps.
6. Identify where symbolic structures make violence, sacrifice, obedience, or
   reconciliation appear necessary.
7. Adapt the method to a different conflict by swapping corpus, actors, phases,
   and conflict-specific magical objects while preserving the shared schema.
