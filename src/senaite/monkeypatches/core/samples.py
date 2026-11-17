# -*- coding: utf-8 -*-
"""Environment configuration for the Samples listing."""
import os

from senaite.core.browser.samples.view import SamplesView


_original_init = SamplesView.__init__


def samples_init(self, context, request):
    _original_init(self, context, request)
    if os.environ.get(
        "SENAITE_SAMPLES_ACTIVE_EXCLUDE_VERIFIED", ""
    ).strip().lower() not in ("true", "1", "yes", "on"):
        return

    for review_state in self.review_states:
        if review_state["id"] == "default":
            content_filter = review_state["contentFilter"]
            content_filter["review_state"] = tuple(
                state for state in content_filter["review_state"]
                if state != "verified"
            )
            break
