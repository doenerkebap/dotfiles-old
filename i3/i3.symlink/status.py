from i3pystatus import Status

color_good = "#859900"
color_degraded = "#b58900"
color_bad = "#dc322f"

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
# status.register("clock",
#         format="%a %-d %b %H:%M:%S KW%V",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

status.register("cpu_usage")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# CPU freq
status.register("cpu_freq",
    format="{avgg} GHz",)



# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
status.register("battery",
    format="BAT {status} {consumption:.2f}W [{percentage_design:.2f}%] {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)


status.register("backlight",
        format="{percentage}%",
        base_path="/sys/class/backlight/intel_backlight/",
        on_leftclick="lighter",
        on_rightclick="darker")

# This would look like this:
# Discharging 6h:51m
# status.register("battery",
#     format="{status} {remaining:%E%hh:%Mm}",
#     alert=True,
#     alert_percentage=5,
#     status={
#         "DIS":  "Discharging",
#         "CHR":  "Charging",
#         "FULL": "Bat full",
#     },)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="enp0s25",
    format_up="{v4cidr}",
    color_up=color_good,
    color_down=color_bad)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp3s0",
    format_up="{essid} {quality:2.0f}% {v4cidr}",
    color_up=color_good,
    color_down=color_bad)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{avail} GiB",)

status.register("mem",
        color=color_good,
        warn_color=color_degraded,
        alert_color=color_bad)

status.register("alsa",
        format="VOL {volume}")
# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
# status.register("pulseaudio",
    # format="♪{volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
# status.register("mpd",
#     format="{title}{status}{album}",
#     status={
#         "pause": "▷",
#         "play": "▶",
#         "stop": "◾",
#     },)

status.run()
