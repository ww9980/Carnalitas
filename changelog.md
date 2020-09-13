# Carnalitas v1.1

## Slavery System (WIP)

* New relation: Slave (`slave`) and Owner (`slave_owner`). Owners automatically get hooks on their Slaves, and transfer ownership to their primary heir if they die.
* Character interaction to enslave prisoners, incurring tyranny and opinion penalties if the enslavement is unjust.
* Encyclopedia entries for Slaves, Owners, and the Slave Market.

## Misc Features

* Added a game rule to toggle bestiality events (off by default)

# For Modders
* **IMPORTANT:** `carn_sex_scene_effect` now also requires argument `DRAMA` (boolean). It passes this argument to the requested event, which should check for it and apply it to `carn_had_sex_with_effect` as appropriate.
* `carn_had_sex_effect` now returns `scope:carn_sex_char_1_impregnated`, `scope:carn_sex_char_2_impregnated`. These are yes if the character was impregnated through the sex effect, and no otherwise.
` New sex scene tag: `orgy`
* `carn_on_sex` now provides `scope:carn_sex_partner`.
* New scripted effect: `carn_enslave_effect`. This gives the Slave trait to a character, forces them to abdicate, and makes them the Slave (relation) of another character. Takes arguments `SLAVE`, `OWNER`, `DRAMA`
* New scripted effect: `carn_free_slave_effect`. Changes the Slave trait to Former Slave and removes their Owner (which will also remove the hook their Owner has on them).
* Added trait and character flags `carn_has_high_arousal` and `carn_has_low_arousal`, influencing a character's stress gain from arousal.
* Added trait and character flags `carn_can_always_have_sex` and `carn_cannot_have_sex`, influencing whether a character is available for sex interactions.

## Tweaks

* Removed fertility bonuses and penalties from dick and tit traits.
* Updated dick trait icons.
* Made arousal event message more visible.

## Bug Fixes

* Fixed arousal event not triggering properly.
* Fixed tooltip not displaying for `carn_can_grant_titles_trigger`.
* Fixed sex scenes being possible to display even if their tags are turned off in game rules.
* Fixed tits_big and dick_big traits being flagged as bad traits.
