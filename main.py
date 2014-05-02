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
"""A sample app that uses the Google Analytics event tracking function."""

import tracking
import webapp2

class MainPage(webapp2.RequestHandler):
  """Main page for tracking demo application."""

  def get(self):
     tracking.track_event_to_ga('Error', "Payment", 'Amount', '100')
     self.response.write('Posted a tracking event to Google Analytics.')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
