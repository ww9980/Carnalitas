# Carnalitas v1.1

## Slavery System (WIP)

* New relation: Slave (`slave`) and Owner (`slave_owner`). Owners automatically get hooks on their Slaves, and transfer ownership to their primary heir if they die.
* New scripted effect: `carn_enslave_effect`. This gives the Slave trait to a character, forces them to abdicate, and makes them the Slave (relation) of another character. Takes arguments `SLAVE`, `OWNER`, `DRAMA`
* New scripted effect: `carn_free_slave_effect`. Changes the Slave trait to Former Slave and removes their Owner (which will also remove the hook their Owner has on them).
* Character interaction to enslave prisoners, incurring tyranny and opinion penalties if the enslavement is unjust.
* Encyclopedia entries for Slaves, Owners, and the Slave Market.

## Misc Features

* Added a game rule to toggle bestiality events (off by default)

## Bug Fixes

* Fixed arousal event not triggering properly
* Fixed tooltip not displaying for carn_can_grant_titles_trigger
* Fixed sex scenes being possible to display even if their tags are turned off in game rules
* Fixed tits_big and dick_big traits not being flagged as good trait
