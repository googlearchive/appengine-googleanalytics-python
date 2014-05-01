# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START tracking_function]
"""A function that posts a tracking event to Google Analytics."""

import urllib
from google.appengine.api import urlfetch

# Set this to the specific Google Analytics Tracking Id for your application.
GA_TRACKING_ID = "UA-XXXX-Y"

def track_event_to_ga(category, action, label=None, value=None):
  """ Posts an Event Tracking message to Google Analytics. """
  form_fields = {
    "v": "1",               # Version.
    "tid": GA_TRACKING_ID,  # Tracking ID / Web property / Property ID.
    "cid": "555",           # Anonymous Client ID.
    "t": "event",           # Event hit type.
    "ec": category,         # Event Category. Required.
    "ea": action,           # Event Action. Required.
    "el": label,            # Event label.
    "ev": value,            # Event value.
  }
  form_data = urllib.urlencode(form_fields)
  result = urlfetch.fetch(url="http://www.google-analytics.com/collect",
      payload=form_data,
      method=urlfetch.POST,
      headers={"Content-Type": "application/x-www-form-urlencoded"})
  # Should return 200 if the call was successful.
  return result.status_code == 200

  # [END tracking_function]
