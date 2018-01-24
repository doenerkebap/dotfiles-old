# -*- coding: utf-8 -*-

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

mod = "mod1"


keys = [
    # Layout
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.swap_left(), lazy.layout.client_to_next()),
    Key([mod, "control"], "l", lazy.layout.swap_right(), lazy.layout.client_to_previous()),
    Key([mod], "l", lazy.layout.next(), lazy.layout.grow_main()),
    Key([mod], "h", lazy.layout.previous(), lazy.layout.shrink_main()),
    Key([mod], "m", lazy.layout.grow()),
    Key([mod], "n", lazy.layout.shrink()),
    Key([mod], "r", lazy.layout.reset()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "Tab", lazy.next_layout()),

    # qtile
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),

    # Lauch apps
    Key([mod], "Return", lazy.spawn("urxvt")),
    Key([mod], "space", lazy.spawncmd()),
    Key([mod], "s", lazy.spawn("urxvt -g 70x30 -e alsamixer")),
    Key([mod], "c", lazy.spawn("urxvt -g 70x30 -e nmtui")),
    Key([], "XF86Display", lazy.spawn("arandr")),
    Key([mod], "d", lazy.spawn("arandr")),

    # Screenshot
    Key([], "Print", lazy.spawn("scrot")),
    Key(["mod1"], "Print", lazy.spawn("scrot -s")),
    ]

group_labels = ["Z", "U", "I", "O", "P", "Ü", "+"]
group_keys = ["z", "u", "i", "o", "p", "udiaeresis", "plus"]
groups = [Group(name, label=label) for name, label in zip(group_keys, group_labels)]

for key in group_keys:
    keys.append(Key([mod], key, lazy.group[key].toscreen()))
    keys.append(Key([mod, "control"], key, lazy.window.togroup(key)))

layouts = [
    layout.Max(),
    layout.Stack(),
    layout.xmonad.MonadTall(border_width=1),
]
floating_layout = layout.Floating()


widget_defaults = dict(
    font='Liberation Mono',
    fontsize=13,
    padding=1,
)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(borderwidth=2, center_aligned=True),
                widget.WindowName(),
                widget.TextBox("eth: "),
                widget.Net(interface="enp0s25"),
                widget.TextBox("  wlan: "),
                widget.wlan.Wlan(interface="wlp3s0", format="{essid} {percent:2.0%} "),
                widget.Net(interface="wlp3s0"),
                widget.Prompt(),
                widget.BatteryIcon(update_delay=5),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


@hook.subscribe.client_new
def default_floats(window):
    names = ["alsamixer", "nmtui"]
    classes = ["arandr"]
    wm_class = window.window.get_wm_class()[0]
    wm_name = window.name
    if wm_name in names or wm_class in classes:
        window.floating = True


dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
extentions = []



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
