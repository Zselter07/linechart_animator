# linechart_animator

![python_version](https://img.shields.io/static/v1?label=Python&message=3.5%20|%203.6%20|%203.7&color=blue)
[![Github All Releases](https://img.shields.io/github/downloads/Zselter07/linechart_animator/total.svg)]()

<img src="https://j.gifs.com/914qNZ.gif" width="550" height="400"/>

## Installation

`pip3` or `pip` `install linechart_animator`

## Usage

```
from linechart_animator import Animator

animator = Animator(
    x_label_text='x label',
    y_label_text='y label',
    title_text='Animated linechart'
)

animator.create_animated_chart(
    x_values = [1,10,16,43,52], # SORTED ARRAY
    y_values = [35,42,53,2,90],
    output_path='/Users/macbook/Desktop/animated_chart.mp4'
)
```

Note that x axis values must be a sorted array.

### Optional parameters with their default values

```
line_color: str='#fca311'
line_width: float=5
outer_bg_color: str='#14213d'
inner_bg_color: str='#14213d'
remove_chart_frames: bool=True
chart_frame_color: str='#000000'
tick_params_length: float=0
tick_params_color: str='#e5e5e5'
label_font_size: str=15
title_font_size: str=20
animation_interval: float=25
```
