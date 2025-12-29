# Sunline

_A clean, minimal light theme where the blue sky meets the warm sun._

![banner](images/banners/banner-top.png)

## Features

- **Azure blue** as the primary color for navigation and actions
- **Warm orange** accents for highlights, warnings, and focal points
- **Tropical teal & green** for strings and comments
- **Golden sand** tones for bracket pairs and search highlights
- Clean white backgrounds with subtle blue tints
- Carefully balanced contrast for comfortable long coding sessions
- Semantic token coloring for modern language support
- Complete UI theming including merge editor and notebooks

## Color Palette

### Syntax Colors

| Color                                                          | Hex       | Usage                                         |
| -------------------------------------------------------------- | --------- | --------------------------------------------- |
| ![black](images/colors/black.png) **Black bold**               | `#000000` | Keywords, control flow, declarations          |
| ![blue](images/colors/blue.png) **Blue bold**                  | `#007AFF` | Functions, methods, exceptions                |
| ![blue](images/colors/blue.png) **Blue italic**                | `#007AFF` | Built-in functions (`print`, `range`)         |
| ![blue-light](images/colors/blue-light.png) **Light blue**     | `#5A9FD4` | Numbers, constants, `True`/`False`/`None`     |
| ![orange](images/colors/orange.png) **Orange bold**            | `#E67300` | Classes, types, CSS variables                 |
| ![orange](images/colors/orange.png) **Orange italic**          | `#E67300` | Parameters                                    |
| ![teal](images/colors/teal.png) **Teal**                       | `#048A81` | Strings, `self`/`this`, object keys           |
| ![teal](images/colors/teal.png) **Teal italic**                | `#048A81` | Built-in variables (`__name__`, `console`)    |
| ![teal-blue](images/colors/teal-blue.png) **Teal blue**        | `#51A3A3` | Operators, punctuation, decorators, CSS units |
| ![teal-gray](images/colors/teal-gray.png) **Teal gray italic** | `#5A8A85` | Comments                                      |
| ![green-grass](images/colors/green-grass.png) **Green italic** | `#4CB944` | Docstrings                                    |

### UI Colors

| Color                                                            | Hex       | Usage                                    |
| ---------------------------------------------------------------- | --------- | ---------------------------------------- |
| ![blue](images/colors/blue.png) **Blue**                         | `#007AFF` | Active borders, icons, links, selections |
| ![blue-inactive](images/colors/blue-inactive.png) **Light blue** | `#66B3FF` | Inactive icons, secondary elements       |
| ![blue-pale](images/colors/blue-pale.png) **Pale blue**          | `#E3ECFF` | Hover backgrounds, highlights            |
| ![orange](images/colors/orange.png) **Orange**                   | `#E67300` | Warnings, modified files, badges, cursor |
| ![red](images/colors/red.png) **Red**                            | `#D93526` | Errors                                   |
| ![green](images/colors/green.png) **Green**                      | `#32A852` | Success, Git additions                   |

### Tropical Accent Colors

| Color                                                                        | Hex       | Usage                  |
| ---------------------------------------------------------------------------- | --------- | ---------------------- |
| ![teal-green](images/colors/teal-green.png) **Teal green**                   | `#0A8A6E` | Bracket pair 1         |
| ![yellow-gold](images/colors/yellow-gold.png) **Golden**                     | `#D9B835` | Bracket pair 2         |
| ![teal-green-light](images/colors/teal-green-light.png) **Teal green light** | `#4A9E7E` | Bracket pair 3         |
| ![yellow-mustard](images/colors/yellow-mustard.png) **Mustard**              | `#CCAD42` | Bracket pair 4         |
| ![teal-green-gray](images/colors/teal-green-gray.png) **Teal green gray**    | `#5A8A70` | Bracket pair 5         |
| ![yellow-sand](images/colors/yellow-sand.png) **Sand**                       | `#B5A044` | Bracket pair 6         |
| ![yellow-honey](images/colors/yellow-honey.png) **Honey**                    | `#E6BE38` | Find match background  |
| ![sand-cream](images/colors/sand-cream.png) **Cream**                        | `#EBEBD3` | Inline code background |

### Merge Editor

| Color      | Usage                         |
| ---------- | ----------------------------- |
| **Blue**   | Current changes (your code)   |
| **Orange** | Incoming changes (their code) |
| **Gray**   | Common ancestor               |

## Screenshots

### Python

![Python](images/code/python.png)

### JavaScript

![JavaScript](images/code/javascript.png)

### HTML & CSS

![HTML](images/code/html.png)
![CSS](images/code/css.png)

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
    "editor.bracketPairColorization.enabled": true,
    "editor.fontFamily": "JetBrains Mono, Fira Code, monospace",
    "editor.fontLigatures": true,
    "editor.guides.bracketPairs": true,
    "editor.letterSpacing": 0.20,
    "editor.lineHeight": 20
}
```

![banner-footer](images/banners/banner-footer.png)

<small>_Sunline: where code meets the sunrise_ 🌅</small>

<small>[Sunline theme][marketplace-web] · [MIT License](LICENSE)  
Made by [**andrecat**](https://github.com/andre-cat) <sub><img src="cat.png" width="16" height="14"></sub></small>

[marketplace-web]: https://marketplace.visualstudio.com/items?itemName=andrecat.sunline-theme
