# Group Analysis Scaffold

This scaffold generates the group-level comparison layer for
`acw-symbolic-psychology`.

---

## Purpose

The individual modules identify each actor's symbolic world. The group layer
asks how those worlds cluster, conflict, overlap, and diverge across the ACW.

The group layer is the main difference between this monorepo and the Lincoln
pilot. The pilot demonstrated an individual pipeline. This project studies a
field of competing symbolic worlds.

---

## Primary Groups

### union_political

Actors:

- Abraham Lincoln

Analytical focus:

- Union as body, covenant, proposition, inheritance, and divine instrument
- violence as preservation, proof, sacrifice, and judgment
- emancipation as both moral shift and strategic act
- reconciliation and exit conditions

### union_military

Actors:

- Ulysses S. Grant
- William Tecumseh Sherman
- George B. McClellan

Analytical focus:

- war as work, pressure, machine, logistics, protection, or cure
- army as instrument, body, or beloved object
- violence as practical compulsion versus moral drama
- differences among command temperaments

### abolitionist_prophetic

Actors:

- Frederick Douglass
- John Brown

Analytical focus:

- slavery as captivity, sin, blood guilt, darkness, theft, or desecration
- freedom as light, deliverance, manhood, testimony, or divine law
- Black agency and armed action
- martyrdom and prophetic violence

### confederate_political

Actors:

- Jefferson Davis
- Alexander H. Stephens

Analytical focus:

- sovereignty, honor, racial hierarchy, constitutional compact
- Confederacy as rightful nation or corrected foundation
- Union as tyranny, coercion, invasion, or violation
- slavery as order, property, foundation, or natural hierarchy

### confederate_military

Actors:

- Robert E. Lee
- Thomas J. "Stonewall" Jackson
- James Longstreet

Analytical focus:

- duty, home, Virginia, Providence, obedience, cost, position
- military action as reluctant obligation, divine instrumentality, or
  professional calculation
- sacrifice and defeat
- postwar memory and apologia

### literary_cultural_witness

Actors:

- Walt Whitman

Analytical focus:

- nation as democratic body
- soldier bodies, wounds, nursing, witnessing, mourning
- death as absorption, renewal, and memory
- cultural healing rather than command decision

---

## Required Comparative Axes

Every group report must compare these axes:

1. `magical_object`
2. `dominant_source_domains`
3. `dominant_target_domains`
4. `fantasy_type`
5. `violence_logic`
6. `obligatory_frame_rate`
7. `sacrificial_economy_rate`
8. `guilt_distribution`
9. `agency_distribution`
10. `absence_flags`
11. `action_orientation`
12. `exit_condition`
13. `register_effects`
14. `diachronic_phase_effects`

---

## Core Group Questions

### Q1 - What Is Being Saved?

Compare the object of defense:

- Union
- Confederacy
- state sovereignty
- racial order
- enslaved humanity
- army
- home
- democracy
- divine purpose
- wounded soldiers

### Q2 - What Is The Threat?

Compare threat construction:

- wound
- tyranny
- contamination
- captivity
- dishonor
- chaos
- invasion
- sin
- death
- failed experiment
- military resistance

### Q3 - What Does Violence Do?

Compare violence logic:

- restore
- prove
- punish
- purify
- redeem
- defend
- exhaust
- cure
- obey
- witness

### Q4 - Who Acts?

Compare agency:

- president
- army
- God
- states
- race
- enslaved people
- soldiers
- people
- history
- machinery/logistics
- no one, because events act

### Q5 - Who Disappears?

Compare absences:

- enslaved people as agents
- Black soldiers
- women
- civilians
- enemy persons
- ordinary soldiers
- slaves as subjects rather than objects
- Northern dissenters
- Southern Unionists
- indigenous people

### Q6 - Is There An Exit?

Compare exit conditions:

- healing completed
- oath fulfilled
- surrender obtained
- enemy exhausted
- sin redeemed
- honor vindicated
- home defended
- divine judgment accepted
- contamination removed
- no exit condition

---

## Required Outputs

Generate:

```text
groups/{group_id}/group_profile.md
groups/{group_id}/group_summary.json
analyses/group/{group_id}.md
analyses/comparative/symbolic_worlds.md
analyses/comparative/magical_objects.md
analyses/comparative/violence_logics.md
analyses/comparative/guilt_and_agency.md
analyses/comparative/action_orientation.md
analyses/comparative/exit_conditions.md
analyses/tables/group_cluster_distribution.csv
analyses/tables/group_violence_logic_distribution.csv
analyses/tables/group_action_orientation_distribution.csv
analyses/tables/register_controlled_group_density.csv
```

---

## Required Tables

### Symbolic World Matrix

Rows: actors.

Columns:

- dominant magical object
- top 3 clusters
- top 3 source domains
- dominant violence logic
- dominant action orientation
- exit condition

### Group Contrast Matrix

Rows: groups.

Columns:

- distinct clusters
- shared clusters
- distinctive absence flags
- distinctive action orientations
- register caveats

### Phase Shift Matrix

Rows: phases.

Columns:

- actors represented
- dominant clusters
- dominant violence logics
- key symbolic shifts
- missing data warnings

---

## Quantitative Minimums

Each group report must include at least one of:

- chi-square comparison of cluster distribution by group
- Fisher exact test for rare fantasy types
- register-controlled metaphor density table
- confidence-weighted sensitivity analysis
- bootstrapped confidence intervals for density estimates

Reports must not pretend statistical significance is historical significance.
Use quantitative results to target close reading.

---

## Close Reading Minimums

Each group report must include:

- one canonical passage for each actor in the group
- one passage that complicates the group label
- one passage showing an absence
- one passage connecting metaphor to action orientation
- one register caveat

---

## Group-Level Thesis Template

Use this template for each group:

```text
In {group_id}, the dominant symbolic object is {magical_object}. The group
most often frames threat as {threat_type} and violence as {violence_logic}.
This makes {action_orientation} appear {necessary/honorable/redemptive/
defensive/practical}. However, the group is internally divided: {actor_a}
emphasizes {cluster_a}, while {actor_b} emphasizes {cluster_b}. The major
structured absence is {absence}. The symbolic system's exit condition is
{exit_condition}, with the following caveats: {caveats}.
```

---

## Cross-Group Master Questions

The final comparative report should answer:

1. Which groups see the war as a constitutional crisis?
2. Which see it as divine judgment?
3. Which see it as family/home defense?
4. Which see it as racial order under threat?
5. Which see it as captivity and deliverance?
6. Which see it as a practical military problem?
7. Which see it as sacrifice and rebirth?
8. Which symbolic structures contain reconciliation logic?
9. Which symbolic structures lack exit conditions?
10. Which groups erase the agency of enslaved people or soldiers?

