# POWERLINE DICE

A toy [Powerline](https://powerline.readthedocs.io/en/master/) segment. This segment shows a result of dice combination.

By [Miguel de Dios Matias](https://github.com/mdtrooper).

## Installation

### Using pip

```
pip install powerline-dice
```

## Configuration

You can activate the Powerline Slotmachine segment by adding it to your segment configuration,
for example in `.config/powerline/themes/shell/default.json`:

```json
{
    "function": "powerline_dice.roll",
    "priority": 90
}
```

By default shows a roll of d6 (dice of six faces).

![screenshot roll six faces](https://raw.githubusercontent.com/mdtrooper/powerline_dice/master/powerline_dice_six.jpg "screenshot roll six faces")

### Arguments

* **diceCombination (string)**: The combination of dices in [dice notation format](https://github.com/borntyping/python-dice#notation) or [wikipedia: Dice notation](https://en.wikipedia.org/wiki/Dice_notation).
  * Default: "d6"
* **preContent (string)**: The string to show before the result.
  * Default: ""
* **postContent (string)**: The string to show after the result.
  * Default: "🎲"
* **facesDice list(string) or None**: The faces of dice as list of string (can be emojis).
  * Default: None
* **critical int or list(int) or None**: The minimum or exact values to critical hit, the background change to critical success.
  * Default: None
* **fumble int or list(int) or None**: The maximum or exact values to critical fumble, the background change to critical failture. 
  * Default: None

### Examples

Rolls two dices of twenty faces and get critical hit with 40 and critical fumble with 1.

```json
{
    "function": "powerline_dice.roll",
    "priority": 30,
    "args": {
        "diceCombination": "2d20",
        "critical": 30,
        "fumble": 15
    }
},
```


![screenshot roll d20 critical and fumble](https://raw.githubusercontent.com/mdtrooper/powerline_dice/master/powerline_dice_critical.jpg "screenshot roll d20 critical and fumble")

Flip a coin with the tail 🙂 and head ️☹️.

```json
{
    "function": "powerline_dice.roll",
    "priority": 30,
    "args": {
        "diceCombination": "d2",
        "facesDice": ["🙂", "☹️"],
        "postContent": ""
    }
},
```

![screenshot flip a coin](https://raw.githubusercontent.com/mdtrooper/powerline_dice/master/powerline_flip_coin.jpg "screenshot flip a coin")


## Thanks

* [Python Dice](https://github.com/borntyping/python-dice): for great library to parse dice combination.

## License

Licensed under [the GPL3 License](https://github.com/mdtrooper/powerline_slotmachine/blob/master/LICENSE).