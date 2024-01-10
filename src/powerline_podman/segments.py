# -*- coding: utf-8 -*-

from podman import PodmanClient
from powerline.segments import Segment, with_docstring

PODMAN_CONTAINER_STATES = ('created', 'exited', 'paused', 'running', 'unknown')

SEGMENT_INFO = {
    'created': {
        'icon': '^',
        'highlight_group': 'podman_running'
    },
    'exited': {
        'icon': '✖',
        'highlight_group': 'podman_exited'
    },
    'paused': {
        'icon': '~',
        'highlight_group': 'podman_paused'
    },
    'running': {
        'icon': '●',
        'highlight_group': 'podman_running'
    },
    'unknown': {
        'icon': '?',
        'highlight_group': 'podman_unknown'
    }
}


class PodmanSegment(Segment):
    """Return the states of Podman containers."""

    def __call__(self, pl, uri="unix:///run/user/1000/podman/podman.sock", ignore_states=None):
        pl.debug('Running powerline-podman...')

        if ignore_states is None:
            ignore_states = []

        self.cli = PodmanClient(base_url=uri)
        self.ignore_states = ignore_states

        states_count = []
        try:
            for state in PODMAN_CONTAINER_STATES:
                if state in self.ignore_states:
                    continue
                containers = self.cli.containers.list(all=True)
                if not containers:
                    continue
                matching_containers = [c for c in containers if c.attrs["State"] == state]
                states_count.append({'state': state, 'quantity': len(matching_containers)})
        except ConnectionError:
            pl.error('Cannot connect to Podman server on \'%s\'' % (uri,))
            return
        except Exception as e:
            pl.error(e)
            return

        segments = [
            {
                'contents': u'\U0001F9AD',
                'highlight_groups': ['podman'],
                'divider_highlight_group': 'podman:divider'
            }
        ]

        for count in states_count:
            if count['quantity'] > 0:
                segments.append({
                    'contents': ' %s %d' % (SEGMENT_INFO[count['state']]['icon'], count['quantity']),
                    'highlight_groups': [SEGMENT_INFO[count['state']]['highlight_group'], 'podman'],
                    'divider_highlight_group': 'podman:divider'
                })

        return segments


podman = with_docstring(PodmanSegment(), '''Return the states of Podman containers.

It will show the number of Podman containers running and exited.
It requires Podman, podman-py to be installed.
It also requires the Podman REST API service to be running.

:param str uri:
    URI path where the libpod service is running.
    Defaults to ``unix:///run/user/1000/podman/podman.sock``, which is where it lives on most Unix systems.

:param list ignore_states:
    list of states which will be ignored and not printed out (e.g. ``["exited", "paused"]``).

Divider highlight group used: ``podman:divider``.

Highlight groups used: ``podman_running``, ``podman_paused``, ``podman_exited``, ``podman_created``, ``podman_unknown``,
``podman``.
''')
