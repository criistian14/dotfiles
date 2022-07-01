# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
from helpers import rofi_script

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"      
myBrowser = "google-chrome-stable" 
myFileManager = "nautilus"

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm+" -e fish"),
             desc='Launches My Terminal'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Qutebrowser'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "r",
             lazy.spawn("rofi -show run"),
             desc='Launches Rofi'
             ),

         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),

         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),

         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),

         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),


         ### Apllication keybindings
         Key([mod, "shift"], "d",
             lazy.spawn(myFileManager),
             desc='Launch Thunar'
             ),
          Key([], "Print",
             lazy.spawn("flameshot gui"),
             desc='Screenshot'
             ),
          Key([mod], "o",
             lazy.spawn(rofi_script("open_intellij_idea.sh")),
             desc='Open project with Intellij Idea'
             ),



         ### Media keybindings
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +6%"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -6%"),
    ),
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),

]

groups = [
        Group("", {'layout': 'monadtall'}),
        Group("", {'layout': 'monadtall'}),
        Group("", {'layout': 'monadtall'}),
        Group("", {'layout': 'monadtall'}),
        Group("", {'layout': 'monadtall'}),
        Group("", {'layout': 'monadtall'}),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {
        "border_width": 2,
        "margin": 8,
        "border_focus": "#e8dfD6",
        "border_normal": "#021b21"
}

layouts = [
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
#    layout.Max(**layout_theme),
#    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
#    layout.TreeTab(
#         font = "Ubuntu",
#         fontsize = 10,
#         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
#         section_fontsize = 10,
#         border_width = 2,
#         bg_color = "1c1f24",
#         active_bg = "c678dd",
#         active_fg = "000000",
#         inactive_bg = "a9a1e1",
#         inactive_fg = "1c1f24",
#         padding_left = 0,
#         padding_x = 0,
#         padding_y = 5,
#         section_top = 10,
#         section_bottom = 20,
#         level_shift = 8,
#         vspace = 3,
#         panel_width = 200
#         ),
#    layout.Floating(**layout_theme)
]

#==== Colors ====#

colors = [
    ["#021b21", "#021b21"],  # 0
    ["#032c36", "#065f73"],  # 1
    # ["#032c36", "#61778d"],# 1 this one is bit lighter, it is for inactive workspace icons.
    ["#e8dfd6", "#e8dfd6"],  # 2
    ["#c2454e", "#c2454e"],  # 3
    ["#44b5b1", "#44b5b1"],  # 4
    ["#9ed9d8", "#9ed9d8"],  # 5
    ["#f6f6c9", "#f6f6c9"],  # 6
    ["#61778d", "#61778d"],  # 7
    ["#e2c5dc", "#e2c5dc"],  # 8
    ["#5e8d87", "#5e8d87"],  # 9
    ["#032c36", "#032c36"],  # 10
    ["#2e3340", "#2e3340"],  # 11
    ["#065f73", "#065f73"],  # 12
    ["#8a7a63", "#8a7a63"],  # 13
    ["#A4947D", "#A4947D"],  # 14
    ["#BDAD96", "#BDAD96"],  # 15
    ["#a2d9b1", "#a2d9b1"],  # 16
]


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Inconsolata for powerline",
    fontsize = 10,
    padding = 3,
    # background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            # text="  ",
            text="  ",
            font="Iosevka Nerd Font",
            fontsize="18",
            background=colors[6],
            foreground=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
            },
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[6],
            foreground=colors[0],
        ),
        widget.GroupBox(
            font="Ubuntu Nerd Font",
            fontsize=20,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            background=colors[0],
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[6],
            block_highlight_text_color=colors[0],
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize=33,
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.WindowName(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[2],
            foreground=colors[0],
        ),

        widget.Chord(
            chords_colors={
                "launch": (colors[3], colors[0]),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize=33,
            padding=0,
            background=colors[2],
            foreground=colors[0],
        ),



#        widget.TextBox(
#            text="\ue0be",
#            font="Inconsolata for powerline",
#            fontsize="33",
#            padding=0,
#            background=colors[2],
#            foreground=colors[0],
#        ),

        widget.Spacer(
            length=200, 
            background=colors[0],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[0],
            foreground=colors[10],
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.45,
            padding=0,
            background=colors[10],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=14,
        ),
        widget.CurrentLayout(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[10],
            foreground=colors[2],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[10],
            foreground=colors[11],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=18,
            padding=0,
            background=colors[11],
            foreground=colors[2],
        ),
        widget.DF(
            fmt=" {}",
            font="Iosevka Nerd Font",
            fontsize=15,
            partition="/home",
            format="{uf}{m} ({r:.0f}%)",
            visible_on_warn=False,
            background=colors[11],
            foreground=colors[2],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[11],
            foreground=colors[12],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=16,
            foreground=colors[2],
            background=colors[12],
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Memory(
            background=colors[12],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=15,
            format="{MemUsed: .0f} MB",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Sep(
            padding=8,
            linewidth=0,
            background=colors[12],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[12],
            foreground=colors[7],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[7],
        ),
        widget.Systray(
            background=colors[7],
            foreground=colors[2],
            icons_size=18,
            padding=4,
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[7],
            foreground=colors[13],
        ),
        widget.TextBox(
            text="墳 ",
            font="Iosevka Nerd Font",
            fontsize=18,
            background=colors[13],
            foreground=colors[0],
        ),
        widget.PulseVolume(
            background=colors[13],
            foreground=colors[0],
            font="Iosevka Nerd Font",
            fontsize=15,
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("kitty -e pulsemixer")},
        ),
        # Doesn't work with Spotify so its disabled!
        # widget.TextBox(
        #    text="\u2572",
        #    font="Inconsolata for powerline",
        #    fontsize="33",
        #    padding=0,
        #    background=colors[13],
        #    foreground=colors[0],
        # ),
        # widget.Mpd2(
        #   background=colors[13],
        #   foreground=colors[0],
        #   idle_message=" ",
        #   idle_format="{idle_message} Not Playing",
        #   status_format="  {artist}/{title} [{updating_db}]",
        #   font="Iosevka Nerd Font",
        #   fontsize=15,
        # ),
        # This one works with Spotify, enable if you want!
        # widget.Mpris2(
        #    background=colors[13],
        #    foreground=colors[0],
        #    name="spotify",
        #    objname="org.mpris.MediaPlayer2.spotify",
        #    fmt="\u2572   {}",
        #    display_metadata=["xesam:title", "xesam:artist"],
        #    scroll_chars=20,
        #    font="Iosevka Nerd Font",
        #    fontsize=15,
        # ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[13],
            foreground=colors[13],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[13],
            foreground=colors[15],
        ),
        widget.TextBox(
            text="   ",
            font="Iosevka Nerd Font",
            fontsize="14",
            padding=0,
            background=colors[15],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[15],
            fontsize=15,
            format="%d %b, %A",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("gnome-calendar")
            },
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[15],
            ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[15],
            foreground=colors[16],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize="18",
            padding=0,
            background=colors[16],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[16],
            fontsize=15,
            format="%I:%M %p",
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[16],
            foreground=colors[6],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),

    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
