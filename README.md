# Sunline

_A clean, minimal light theme where the blue sky meets the warm sun._

![banner](images/banners/banner-top.png)

## Features

- **Azure blue** as the primary color for navigation and actions
- **Warm orange** accents for highlights, warnings, and focal points
- **Tropical teal & green** for strings and comments
- Clean white backgrounds with subtle blue tints
- Carefully balanced contrast for comfortable long coding sessions
- Semantic token coloring for modern language support
- Complete UI theming including merge editor and notebooks

## Color Palette

### Syntax Colors

| Color                                                             | Hex       | Usage                                   |
| ----------------------------------------------------------------- | --------- | --------------------------------------- |
| ![black](images/colors/black.png) **Black bold**                  | `#000000` | Keywords, control flow, declarations    |
| ![blue](images/colors/blue.png) **Blue bold**                     | `#007AFF` | Functions, methods, modules, exceptions |
| ![blue-denim](images/colors/blue-denim.png) **Denim blue**        | `#5085B0` | Decorators, regex                       |
| ![blue-light](images/colors/blue-light.png) **Light blue italic** | `#5A9FD4` | Instance references, numbers, constants |
| ![orange](images/colors/orange.png) **Orange bold**               | `#E67300` | Classes, types, language constants      |
| ![orange](images/colors/orange.png) **Orange italic**             | `#E67300` | Parameters                              |
| ![teal](images/colors/teal.png) **Teal**                          | `#048A81` | Strings                                 |
| ![green-grass](images/colors/green-grass.png) **Green italic**    | `#4CB944` | Docstrings                              |
| ![teal-gray](images/colors/teal-gray.png) **Teal gray italic**    | `#5A8A85` | Comments                                |
| ![teal-blue](images/colors/teal-blue.png) **Teal blue**           | `#51A3A3` | Operators, punctuation                  |

### UI Colors

| Color                                                            | Hex       | Usage                                    |
| ---------------------------------------------------------------- | --------- | ---------------------------------------- |
| ![blue](images/colors/blue.png) **Blue**                         | `#007AFF` | Active borders, icons, links, selections |
| ![blue-inactive](images/colors/blue-inactive.png) **Light blue** | `#66B3FF` | Inactive icons, secondary elements       |
| ![blue-pale](images/colors/blue-pale.png) **Pale blue**          | `#E3ECFF` | Hover backgrounds, highlights            |
| ![orange](images/colors/orange.png) **Orange**                   | `#E67300` | Warnings, modified files, badges, cursor |
| ![red](images/colors/red.png) **Red**                            | `#D93526` | Errors                                   |
| ![green](images/colors/green.png) **Green**                      | `#32A852` | Success, Git additions                   |

### Merge Editor

| Color      | Usage                         |
| ---------- | ----------------------------- |
| **Blue**   | Current changes (your code)   |
| **Orange** | Incoming changes (their code) |
| **Gray**   | Common ancestor               |

## Screenshots

### Python

![Python](images/code-blocks/python.png)

### JavaScript

![JavaScript](images/code-blocks/javascript.png)

### HTML & CSS

![HTML](images/code-blocks/html.png)
![CSS](images/code-blocks/css.png)

## Installation

1. Open **Extensions** in VS Code (`Ctrl + Shift + X`)
2. Search for _`Sunline`_
3. Click **Install**
4. Open **Command Palette** (`Ctrl + Shift + P`)
5. Select `Preferences: Color Theme` → `Sunline`

## Recommended Settings

For the best experience, consider these VS Code settings:

```json
{
    "editor.fontFamily": "JetBrains Mono, Fira Code, monospace",
    "editor.fontLigatures": true,
    "editor.bracketPairColorization.enabled": true,
    "editor.guides.bracketPairs": true
}
```

[MIT](LICENSE)

**Sunline: Where code meets the sunrise!** 🌅

![banner-footer](images/banners/banner-footer.png)
