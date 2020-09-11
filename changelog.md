# Carnalitas v1.1

## Slavery System (WIP)

* New relation: Slave (`slave`) and Owner (`slave_owner`). Owners automatically get hooks on their Slaves, and transfer ownership to their primary heir if they die.
* New effect: `carn_enslave_effect`. Takes arguments `SLAVE`, `OWNER`, `DRAMA`
* New effect: `carn_free_slave_effect`
* Character interaction to enslave prisoners, incurring tyranny and opinion penalties if the enslavement is unjust
* Encyclopedia entries for Slaves, Owners, and the Slave Market

## Misc Features

* Added a game rule to toggle bestiality events (off by default)

## Bug Fixes

* Fixed arousal event not triggering properly
* Fixed tooltip not displaying for carn_can_grant_titles_trigger
* Fixed sex scenes being possible to display even if their tags are turned off in game rules
