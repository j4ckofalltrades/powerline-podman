![powerline-podman-social-preview](https://res.cloudinary.com/j4ckofalltrades/image/upload/v1697278938/foss/gh-social-icons/powerline-podman_ubesku.png)

[![PyPI](https://img.shields.io/pypi/v/powerline-podman)](https://pypi.org/project/powerline-podman/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/powerline-podman)

A custom [Powerline](https://github.com/powerline/powerline) segment for displaying the current state of Podman containers. Inspired by [powerline-docker](https://github.com/adrianmo/powerline-docker).

![powerline-podman](https://res.cloudinary.com/j4ckofalltrades/image/upload/v1680430170/foss/powerline-podman_v4mbms.png)

This segment also requires the Podman REST API service to be running:

`podman system service -t 0 &`

See [Podman docs](https://docs.podman.io/en/latest/_static/api.html) for more details.

## Installation

### Using pip

`$ pip install powerline-podman`

## Configuration

### Colorscheme

Add the following config items to your Powerline colorscheme config file (usually located at `~/.config/powerline/colorschemes/`),
see [Powerline Colorschemes](https://powerline.readthedocs.io/en/master/configuration/reference.html#colorschemes) for more info.

```json
{
  "podman":         { "fg": "gray8",           "bg": "darkestpurple", "attrs": [] },
  "podman_created": { "fg": "yellow",          "bg": "darkestpurple", "attrs": [] },
  "podman_exited":  { "fg": "brightred",       "bg": "darkestpurple", "attrs": [] },
  "podman_paused":  { "fg": "brightestorange", "bg": "darkestpurple", "attrs": [] },
  "podman_running": { "fg": "green",           "bg": "darkestpurple", "attrs": [] },
  "podman_unknown": { "fg": "gray10",          "bg": "darkestpurple", "attrs": [] },
  "podman:divider": { "fg": "gray4",           "bg": "darkestpurple", "attrs": [] } 
}
```

### Segment

Add the following config item to your Powerline segments config file,
see [Powerline Segment reference](https://powerline.readthedocs.io/en/master/configuration/segments.html#segment-reference) for more info.

The segment tries to connect to the libpod service at `unix:///run/user/1000/podman.sock`, which is where it lives on most Unix systems. You can change the URI with the `uri` argument.

Additionally, you can hide containers with specific states e.g. don't show `exited` containers by adding it to the `ignore_states` argument list.
The valid states are `created`, `exited`, `paused`, `running`, and `unknown`.

```json
{
  "function": "powerline_podman.podman",
  "priority": 30,
  "args": {
    "uri": "unix:///run/user/1000/podman.sock",
    "ignore_states": ["exited", "paused"]
  }
}
```

- If adding the segment to the shell, edit `~/.config/powerline/themes/shell/default.json`.
- If adding the segment to the tmux status line, edit `~/.config/powerline/themes/tmux/default.json`.
