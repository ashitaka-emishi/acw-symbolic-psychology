# Theoretical Framework Scaffold

This file is the reusable theoretical core for `acw-symbolic-psychology`.
It must generate `methods/theoretical_framework.md`,
`methods/cmt_protocol.md`, `methods/koenigsberg_protocol.md`, and
`methods/annotation_codebook.md`.

---

## Project Claim

The project studies symbolic worlds. It does not merely count metaphors and it
does not claim to read minds directly. It asks how metaphor, ideology, and
historical psychology structure what actors perceive as real, valuable,
threatened, guilty, sacred, and necessary.

The central ACW working thesis is:

Civil War actors did not merely disagree over policy. They inhabited competing
symbolic worlds in which nation, slavery, violence, sacrifice, and obligation
had different psychic structures. These structures shaped what each actor
experienced as necessary action.

This is a thesis-level claim rather than one hypothesis. It becomes testable
through subordinate hypotheses about clusters, magical objects, violence
logics, absences, action orientations, phase shifts, and group differences.
The method must allow those subordinate hypotheses to fail and must revise the
thesis when the evidence requires it.

---

## Layer 1 - Conceptual Metaphor Theory

CMT supplies the structural description.

For every metaphor instance, record:

- source domain: the concrete or familiar domain
- target domain: the abstract historical or political domain
- mapping: the correspondences between source and target
- entailments: the inferences licensed by the mapping
- linguistic form: noun phrase, verb phrase, clause, extended image, etc.
- novelty: conventional, novel, dead-but-active, or ambiguous
- extension: whether the mapping continues across sentences or documents
- co-activation: whether multiple clusters operate simultaneously

Core CMT rule:

Do not annotate a metaphor unless you can state source domain, target domain,
and at least one concrete entailment.

---

## Layer 2 - Koenigsbergian Historical Psychology

Koenigsbergian analysis supplies the psychological and political function of
the metaphor. It asks what fantasy structure the metaphor activates and how
that fantasy makes action feel necessary.

Core constructs:

- fantasy type
- magical object
- violence logic
- obligatory frame
- guilt distribution
- sacrificial economy
- psychic defense
- agency distribution
- absence and erasure
- exit condition

Key premise:

Political violence is often sustained by ideological fantasy: a collective
object such as nation, race, army, covenant, state, people, or cause is treated
as an extension of the self. The object can become sacred, wounded, diseased,
humiliated, imprisoned, betrayed, or endangered. Action then appears not merely
chosen but required.

---

## Layer 3 - Historical Context

The project must remain historically grounded.

Every instance must be interpreted with:

- date and phase
- audience
- occasion
- genre/register
- factional position
- source transmission status
- known historical pressure
- relation to action, decision, or public justification

Historical context prevents free-floating psychoanalysis.

---

## Layer 4 - Action Orientation

Add `action_orientation` to connect symbolic structure to action without
claiming mechanical causality.

Action orientation asks:

What kind of action becomes intelligible, obligatory, honorable, redemptive,
or unavoidable within this symbolic world?

Allowed values:

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

Multiple values may apply. Always explain the entailment chain.

---

## Universal Fantasy Types

### wound_and_healing

A collective object is injured. Action repairs, binds, restores, or protects
the damaged object.

Common entailments:

- the object was once whole
- something caused damage
- delay worsens injury
- healing is obligatory
- an endpoint is possible

### disease_and_purification

A body or collective object contains contamination, infection, pathogen,
parasite, or corruption. Action removes or destroys the contaminating element.

Common entailments:

- the dangerous element is inside the body
- coexistence is impossible
- removal is necessary
- violence becomes hygienic
- the endpoint may recede indefinitely

Critical distinction:

Disease language applied to an institution is not automatically purification
logic. Purification logic requires a contaminating entity whose destruction or
expulsion is constructed as necessary to save the body.

### birth_and_creation

Violence or crisis produces a new order, people, nation, freedom, identity, or
historical stage.

Common entailments:

- pain is labor
- death can be generative
- the old order gives way to the new
- sacrifice may become productive

### sacrifice_and_redemption

Death, suffering, or loss produces value: national identity, proof, atonement,
freedom, honor, or sacred memory.

Common entailments:

- death must not be wasted
- the living owe completion to the dead
- loss can generate collective meaning
- grief is converted into obligation

### oath_and_obligation

A prior vow, law, covenant, constitution, commission, or duty binds action in
the present.

Common entailments:

- agency is constrained by promise
- action is enforcement, not preference
- breaking the bond is moral failure

### punishment_and_theodicy

Violence appears as divine, historical, or moral punishment.

Common entailments:

- suffering has meaning
- guilt precedes punishment
- actors may become instruments
- causation may shift from human agency to Providence or history

### ancestral_debt

The present generation inherits obligation from founders, ancestors, martyrs,
or the dead.

Common entailments:

- the living are debtors
- inheritance requires fidelity
- betrayal dishonors the dead
- sacrifice can pay or renew the debt

### experiment_and_proof

A political principle is an experiment, proposition, test, or proof. Action
generates evidence.

Common entailments:

- failure is possible
- events have evidentiary force
- sacrifice can prove a proposition
- victory or survival confirms the claim

### honor_and_vindication

The self, state, army, people, or cause has been insulted, shamed, invaded, or
misrecognized. Action restores honor.

Common entailments:

- injury is moral and symbolic
- response is required to preserve selfhood
- compromise may appear dishonorable

### captivity_and_deliverance

A person, people, or principle is bound, imprisoned, enslaved, or in darkness.
Action liberates, awakens, or delivers.

Common entailments:

- the captive cannot be left captive
- freedom is movement, light, speech, or resurrection
- liberation may justify risk or violence

### home_defense

Home, land, state, family, or locality is threatened. Action protects the sacred
domestic object.

Common entailments:

- invasion violates intimate space
- defense is duty
- locality may supersede abstract nation

### machine_pressure

War is machinery, pressure, work, logistics, or force. Action applies material
pressure until resistance breaks.

Common entailments:

- moral drama gives way to process
- persistence matters more than inspiration
- enemy capacity can be exhausted

### apocalypse_and_judgment

Events are final, world-historical, catastrophic, or eschatological. Action
occurs under judgment.

Common entailments:

- the moment is ultimate
- delay is betrayal
- violence can be cosmic or revelatory

### witness_and_mourning

The actor's role is not command but witness, care, naming, memory, or mourning.

Common entailments:

- suffering must be seen
- the dead require remembrance
- healing may begin through recognition

---

## Magical Object Codebook

The magical object is the collective object treated as sacred, wounded,
endangered, or requiring sacrifice.

Allowed starting values:

- `union_body`
- `confederate_nation`
- `state_sovereignty`
- `racial_order`
- `enslaved_humanity`
- `black_citizenship`
- `founding_proposition`
- `constitutional_covenant`
- `army_body`
- `home_or_virginia`
- `divine_will`
- `democratic_people`
- `wounded_soldier_body`
- `southern_society`
- `liberty`
- `honor`
- `the_dead`

Add new values only in `config/shared_taxonomy.yaml`, with definition and
example.

---

## Guilt Distribution

Allowed values:

- `external`: guilt belongs to the opponent
- `internal`: guilt belongs to the actor's own side or self
- `distributed`: guilt spreads across multiple parties
- `cosmic`: guilt or causation is assigned to God, history, fate, or providence
- `institutional`: guilt belongs to an institution such as slavery or monarchy
- `racialized`: guilt attaches to a racialized group
- `absent`: the passage avoids moral assignment
- `ambiguous`: multiple readings remain plausible

Always explain the evidence.

---

## Agency Distribution

Record who acts and who is acted upon.

Fields:

- `agent_of_action`
- `agent_is_abstract`
- `object_of_action`
- `beneficiary`
- `erased_agent`
- `passive_entity`

Agency is central to the project. The same metaphor can justify different
action depending on who is allowed to act.

---

## Absence Analysis

Absence is not "not mentioned." Absence is a structured silence created when a
metaphor's entailments require an entity or role, but the text withholds it.

Example:

If war is a birth, who labors? If soldier death proves democracy, who is
allowed to be a prover? If slavery is captivity, who is allowed to deliver?

General absence flags:

- `enslaved_people_non_agent`
- `black_soldiers_erased`
- `women_absent`
- `soldiers_depersonalized`
- `enemy_depersonalized`
- `civilian_suffering_absent`
- `self_non_agent`
- `god_overhumanizes_action`
- `slavery_abstracted`
- `race_hierarchy_naturalized`
- `death_abstracted`
- `class_erased`
- `indigenous_people_absent`

Actor-specific absence flags may be added in person scaffolds.

---

## Exit Conditions

Every metaphor system should be evaluated for whether it contains an endpoint.

Examples:

- wound logic: exit when healed
- oath logic: exit when obligation fulfilled
- experiment logic: exit when proof completed
- punishment logic: exit when penalty paid
- home defense: exit when invader leaves
- machine pressure: exit when resistance breaks
- purification logic: often no stable exit until contamination is fully gone

Fields:

- `exit_condition_present`
- `exit_condition_type`
- `exit_condition_notes`

---

## Coding Discipline

Use precise language:

- "This metaphor licenses..."
- "The entailment structure suggests..."
- "The passage frames..."
- "The symbolic world makes X action intelligible as..."

Avoid overclaiming:

- Do not claim direct causation from metaphor to action.
- Do not claim to prove unconscious motive.
- Do not reduce a person to one cluster.
- Do not ignore genre or audience.

---

## Bibliographic Anchors

Use these as method anchors in `docs/methods.md`:

- Lakoff and Johnson, `Metaphors We Live By`, 1980.
- Pragglejaz Group, "MIP: A Method for Identifying Metaphorically Used Words
  in Discourse," 2007.
- Steen et al., `A Method for Linguistic Metaphor Identification: From MIP to
  MIPVU`, 2010.
- Richard A. Koenigsberg, `Hitler's Ideology: A Study in Psychoanalytic
  Sociology`, 1975.
- Richard A. Koenigsberg, `Nations Have the Right to Kill`, 2009.
- Koenigsberg essays on nations as bodies and disease/purification logic,
  Library of Social Science.
