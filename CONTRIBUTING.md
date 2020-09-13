# How to contribute to the Carnalitas Framework

## You want to add a new feature or bugfix

In order to keep the development branch stable, you should not commit directly to it. Here is the workflow you should follow:

### Create a new branch

If you are an official contributor to this project, **create a new branch** from the "developing" branch (you can do it from github or directly from your local git repository)
> If you are not an official contributor, you can fork this project and work on your feature there

- It is recommended to name your branch "**feature/concise-name-of-the-feature**" for a new feature or "**fix/concise-name-of-the-bugfix**" for a bugfix.

### Work on your branch

You can now start working on your feature by pushing your modification to your feature branch.

- Only add changes that are related to that feature

### Create a pull request

Once your feature is done, or at least stable and functioning (doesn't cause crashes or break existing stuff), you can **create a pull request** from your feature branch to the development branch

- Follow the template instructions
- Add a reviewer to the pull request (cherisong and potentially another contributor who already worked on the code you are modifying)
- Add the label "enhancement" and any other relevant label, like "visual" if you made some graphical modification
- If your feature or bugfix is supposed to close or fix an existing issue, please link it in the pull request (the option is also in the right-hand column)

## Adding new translations

Translations go into the `localization` folder where each language gets its own sub directory. You can use the localization helper to quickly setup a new language (requires [Python](https://www.python.org/)):

```shell
python localization_helper.py update --lang <language>
```

Where `<language>` is the name of the language you want to translate to, eg: `german`.

Make sure to mark untranslated strings with `key:0 "value"` instead of `key: "value"`. The `:0` means the string is untranslated and helps track progress. This also means you should remove the `:0` after you translated it.

If you want to see translation statistics use `python localization_helper.py stats`.
