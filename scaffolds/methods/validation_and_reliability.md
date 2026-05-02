# Validation And Reliability Scaffold

This file makes the project academically viable. It should generate
`methods/reliability_validation.md` and the validation section of
`docs/publication_plan.md`.

---

## Why This Matters

The largest methodological risk is that metaphor annotation becomes subjective
literary interpretation disguised as data. The project avoids this by building
formal validation into the workflow.

The minimum publishable standard is:

- explicit codebook
- documented corpus
- repeatable pipeline
- reliability sample
- uncertainty reporting
- disconfirmation tests
- register controls
- modest statistics

---

## Annotation Reliability

### Preferred Design

Use two annotators for a random validation sample.

Minimum sample:

- 200 sentences total
- at least 6 actors
- at least 4 registers
- at least 3 conflict phases
- include both high-priority and ordinary documents

Code independently:

1. metaphor present or absent
2. source domain
3. target domain
4. cluster
5. fantasy type
6. violence logic
7. obligatory frame
8. action orientation
9. absence flag

Metrics:

- Cohen's kappa for categorical fields
- percent agreement for rare fields
- adjudication notes for disagreements

### Solo Researcher Fallback

If only one annotator is available:

1. Sample at least 200 sentences.
2. Annotate them.
3. Wait at least 7 days.
4. Re-annotate without viewing the original labels.
5. Compute intra-annotator agreement.
6. Report drift and revise codebook.

This is less strong than inter-annotator reliability, but stronger than no
validation.

---

## Candidate Extraction Validation

If the pipeline includes candidate metaphor detection, evaluate it separately
from interpretive annotation.

Sample:

- 100 candidate sentences
- 100 non-candidate sentences

Report:

- precision: candidate sentences that contain metaphors
- recall estimate: metaphors missed in non-candidate sample
- false-positive patterns
- false-negative patterns
- cluster bias: whether the extractor overfinds body, religion, or war terms

Do not let automated extraction define the corpus of metaphors. It is a triage
tool only.

---

## Confidence Scoring

Use this base scale:

- `0.95-1.00`: explicit metaphor, clear mapping, clear entailments, strong source
- `0.85-0.94`: clear metaphor, minor boundary or entailment ambiguity
- `0.70-0.84`: plausible metaphor, conventional or context-dependent
- `0.50-0.69`: weak or contested metaphor; include only with ambiguity flag
- below `0.50`: exclude from main annotation

Adjustments:

- strong manuscript or scholarly edition: no penalty
- newspaper transcript: `-0.05`
- retrospective memoir: `-0.10` for wartime-cognition claims
- translated text: `-0.10` unless translation is central object of study
- fragment or uncertain date: `-0.05`
- contested authorship: `-0.10`

Confidence-weighted analyses should be generated alongside raw counts.

---

## Register Controls

Never compare raw counts across actors without register caveat.

Required register-control outputs:

- density per 1,000 words by register
- cluster distribution within register
- actor comparison within same register
- group comparison with register distribution table
- sensitivity analysis excluding retrospective memoirs

Example:

Sherman memoir material should not be compared directly with Lincoln's formal
addresses unless the report states that the difference may reflect register and
retrospection rather than actor psychology alone.

---

## Disconfirmation Protocol

Each person module must define:

- expected clusters
- expected magical objects
- expected violence logics
- expected action orientations
- evidence that would weaken each expectation

Reports must include a section named `Disconfirmed Or Revised Priors`.

No person profile is complete if it only confirms the priors.

---

## Statistical Minimums

At least one statistical test is required in each major comparison report.

Recommended tests:

- chi-square test for cluster distribution by group
- Fisher exact test for rare features such as purification logic
- logistic regression for obligatory frame by group/register
- Spearman correlation for phase trend
- bootstrap confidence intervals for metaphor density

Always report:

- test used
- unit of analysis
- exclusions
- whether confidence weighting was used
- whether retrospective memoirs were included
- limitations

---

## Quality Gates

The project cannot claim completion until:

- all manifests validate
- all segmented files validate
- all annotation files validate
- reliability sample exists
- reliability report exists
- codebook revision log exists
- at least one group comparison exists
- all major claims link to evidence IDs

---

## Reviewer-Facing Transparency

Create `docs/limitations.md` with:

- corpus limits
- actor representativeness limits
- genre/register limits
- source transmission limits
- interpretive limits
- limits of applying Koenigsbergian method outside genocide studies
- limits of inferring action from language
- ethical handling of racist and violent primary texts

This section should be frank. It increases credibility.

