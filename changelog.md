# Carnalitas v1.2

## New Features

### Prostitution System

* Added a game rule to enable or disable prostitution content.
* Added a religious doctrine about the criminality of prostitution, and a game rule to set its default setting for all religions.
* Added three new traits: Novice Prostitute (`prostitute_1`), Experienced Prostitute (`prostitute_2`), and Masterful Prostitute (`prostitute_3`).
* Add new decisions to Work as a Prostitute and Stop Working as a Prostitute. Working as a prostitute gives you a character modifier which gives you extra income in exchange for decreased prestige. As you upgrade your prostitute lifestyle trait, you get better and better modifiers.
* Added some random events that can trigger yearly when you're working as a prostitute, including the chance to upgrade your prostitution trait. Modders can add new random events to the on_action `carn_prostitution_random_events_pulse`

New triggers:
* `carn_is_prostitute_trigger`
* `carn_is_working_as_prostitute_trigger`

New effects:
* `carn_start_working_as_prostitute_effect`
* `carn_stop_working_as_prostitute_effect`
* `carn_update_working_as_prostitute_modifier_effect`
* `carn_upgrade_lifestyle_prostitute_effect`

New character and trait flags for modders:
* `carn_is_prostitute`
* `carn_cannot_be_prostitute`

### Same-Sex Concubinage

* Added some basic interactions to take same-sex concubines. These can be used as long as your faith accepts same-sex relations.

### Fetish System

* Added the option to seed the game world with various fetishes. This currently doesn't do anything, but can be used as a hook for various mods.
* Fetishes are stored as a `variable_list` attached to characters and do not spawn until they are 16 years old.
* Fetishes associated with content disabled by game rules will not spawn.

List of fetishes:
* `flag:carn_fetish_anal`
* `flag:carn_fetish_sadism`
* `flag:carn_fetish_masochism`
* `flag:carn_fetish_bestiality`
* `flag:carn_fetish_watersports`
* `flag:carn_fetish_scat`
* `flag:carn_fetish_gore`
* `flag:carn_fetish_foot_play`
* `flag:carn_fetish_bondage`
* `flag:carn_fetish_domination`
* `flag:carn_fetish_submission`

### Body Part Traits Update for Modders

New scripted effects:
* `carn_increase_dick_size_one_step_effect`
* `carn_decrease_dick_size_one_step_effect`
* `carn_increase_tits_size_one_step_effect`
* `carn_decrease_tits_size_one_step_effect`

New scripted triggers:
* `carn_has_bigger_dick_than_character_trigger` (requires `CHARACTER`)
* `carn_has_smaller_dick_than_character_trigger` (requires `CHARACTER`)
* `carn_has_bigger_tits_than_character_trigger` (requires `CHARACTER`)
* `carn_has_smaller_tits_than_character_trigger` (requires `CHARACTER`)

### Health and Transformation Library for Modders

New scripted effects:
* `carn_increase_beauty_one_step_effect`
* `carn_decrease_beauty_one_step_effect`
* `carn_increase_intellect_one_step_effect`
* `carn_decrease_intellect_one_step_effect`
* `carn_increase_physique_one_step_effect`
* `carn_decrease_physique_one_step_effect`
* `carn_remove_random_negative_congenital_trait_effect`
* `carn_remove_all_negative_congenital_traits_effect`
* `carn_heal_wounds_one_step_effect`
* `carn_remove_all_wounds_effect`
* `carn_remove_random_minor_disfigurement_effect`
* `carn_remove_all_minor_disfigurements_effect`
* `carn_remove_random_major_disfigurement_effect`
* `carn_remove_all_major_disfigurements_effect`
* `carn_recover_from_all_diseases_effect`

New scripted triggers:
* `carn_has_any_negative_congenital_trait_trigger`
* `carn_has_any_minor_disfigurement_trigger`
* `carn_has_any_major_disfigurement_trigger`

New character and trait flags:
* `immune_to_disease` (as a trait flag)
* `immune_to_std` (as a trait flag)

### Miscellaneous

* Added a game rule to prevent pregnancy complications from happening.

New scripted triggers:
* `carn_should_have_no_consequences_for_extramarital_sex_trigger`
* `carn_should_have_no_consequences_for_extramarital_sex_with_partner_trigger` (requires `PARTNER`)
* `carn_should_have_no_consequences_for_extramarital_sex_with_no_partner_trigger`

New character and trait flags:
* `carn_no_pregnancy_complications`
* `carn_no_consequences_for_extramarital_sex_with_others`
* `carn_no_consequences_for_extramarital_sex_with_me`

## Tweaks

* AI no longer asks to buy your slaves.
* Taking a slave now breaks their marriages and/or betrothal.
* You now get a notification in the Issues tab when you can Lay With Lover.
* `carn_can_have_sex_trigger` now requires that you are not wounded and you don't have any disease more serious than lover's pox.

## Bug Fixes

* Fixed not being able to Lay With Lover targeting your slaves.
* Fixed extramarital sex being illegal between slaves and slave owners.
