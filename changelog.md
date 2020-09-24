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

* Added the option to seed the game world with various fetishes. Fetishes associated with content disabled by game rules will not spawn.
* Fetishes are stored as a `variable_list` attached to characters and do not spawn until they are 16 years old.

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

### Miscellaneous

* Added a game rule to prevent pregnancy complications from happening.

New scripted triggers:
* `carn_should_have_no_consequences_for_extramarital_sex_trigger`
* `carn_should_have_no_consequences_for_extramarital_sex_with_partner_trigger` (requires `PARTNER`)

New character and trait flags for modders:
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
