# Carnalitas v1.1

## Slavery System

* A new game rule to enable or disable the slavery system.
* New relation: Slave (`slave`) and Owner (`slave_owner`). Owners automatically get hooks on their Slaves, and transfer ownership to their primary heir if they die.
* Character interaction to enslave characters, incurring tyranny and opinion penalties if the enslavement is unjust.
* Character interaction to free a slave, with various demands you can make similar to releasing a prisoner.
* Character interaction to demand that a character free their illegal slaves.
* Character interaction to buy a slave from someone else.
* Character interaction to sell a slave to someone else.
* New religious doctrines regarding religions' views on slavery, as well as a game rule to change their default stance on slavery.
* New custom GUI showing a character's owned slaves in the character window.
* Encyclopedia entries for Slaves, Owners, and the Slave Market.

## Misc Features

* Added a game rule to toggle bestiality events (off by default).
* Added english fallback for all official CK3 languages.

## For Modders

### Sex Scene System

* **IMPORTANT:** `carn_sex_scene_effect` and `carn_had_sex_with_effect` have been reworked.

  * `carn_sex_scene_effect` and `carn_had_sex_with_effect` now require argument `STRESS_EFFECTS` (boolean). This is now separate from `DRAMA`.

  * `carn_sex_scene_effect` now requires argument `DRAMA` (boolean). It passes this argument to the requested event, which should check for it and apply it to `carn_had_sex_with_effect` as appropriate.

  * `carn_had_sex_with_effect`'s `PREGNANCY_CHANCE` has been broken up into `C1_PREGNANCY_CHANCE` and `C2_PREGNANCY_CHANCE`, this allows you to fine-tune the pregnancy chances in non-penetrative sex scenes for example.
* `carn_had_sex_effect` now returns `scope:carn_sex_char_1_could_be_impregnated`, `scope:carn_sex_char_2_could_be_impregnated`. These are yes if the character had a pregnancy chance greater than 0 through the sex effect, and no otherwise.
* `carn_had_sex_effect` now returns `scope:carn_sex_char_1_impregnated`, `scope:carn_sex_char_2_impregnated`. These are yes if the character was impregnated through the sex effect, and no otherwise.

* New sex scene tag: `giving_player`, `receiving_player`, `orgy`, `cum_inside`, `cum_outside`
* `carn_on_sex` now provides `scope:carn_sex_partner`.

### Arousal

* Added trait and character flags `carn_has_high_arousal` and `carn_has_low_arousal`, influencing a character's stress gain from arousal.
* Added trait and character flags `carn_can_always_have_sex` and `carn_cannot_have_sex`, influencing whether a character is available for sex interactions.

### Body Part Traits

* New scripted effects: `carn_remove_dick_trait_effect`, `carn_remove_tits_trait_effect`
* New scripted effects: `carn_add_tits_big_1_effect`, etc. for all the dick and tit traits. This effect will add the appropriate dick or tit size to a character if the game rule is on, and do nothing if the game rule is off.

### Slavery

* New scripted effect: `carn_enslave_effect`. This gives the Slave trait to a character, forces them to abdicate, and makes them the Slave (relation) of another character. Takes arguments `SLAVE`, `OWNER`, `DRAMA`
* New scripted effect: `carn_free_slave_effect`. Changes the Slave trait to Former Slave and removes their Owner (which will also remove the hook their Owner has on them).
* New scripted effect: `carn_free_illegal_slaves_effect`
* New scripted effect: `carn_free_slave_interaction_effect`
* New scripted effect: `carn_buy_slave_effect`
* New scripted trigger: `carn_slave_can_be_sold_trigger`, which checks that the slave is healthy enough to sell
* Added trait and character flags `carn_cannot_be_enslaved`.
* Added trait and character flags `carn_slave_cannot_be_sold`.
* Added trait and character flags `carn_wants_to_be_a_slave` (which makes them automatically accept offers to be enslaved).
* Added opinion `carn_wants_to_be_your_slave_opinion`, which makes the character always agree to enslavement by the opinion target.

### Misc

* Added trait and character flags `can_use_abduct_scheme`. This allows a character to use the Kidnapper perk regardless of whether they have the perk unlocked.

## Tweaks

* Removed fertility bonuses and penalties from dick and tit traits.
* Updated dick trait icons.
* Made arousal event message more visible.

## Bug Fixes

* Fixed arousal event not triggering properly.
* Fixed tooltip not displaying for `carn_can_grant_titles_trigger`.
* Fixed sex scenes being possible to display even if their tags are turned off in game rules.
* Fixed tits_big and dick_big traits being flagged as bad traits.
* Fixed breast size traits forcing all characters to use the bust_clothes blendshape.
* Fixed STDs being transmitted even when disabled by game rule.
