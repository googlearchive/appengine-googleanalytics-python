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

"""Tests the tracking function."""


import tracking
import unittest

from google.appengine.api import apiproxy_stub
from google.appengine.api import apiproxy_stub_map


class URLFetchServiceMock(apiproxy_stub.APIProxyStub):
  """Mock for google.appengine.api.urlfetch."""
  def __init__(self, service_name='urlfetch'):
    super(URLFetchServiceMock, self).__init__(service_name)
 
  def set_return_values(self, **kwargs):
    self.return_values = kwargs
 
  def _Dynamic_Fetch(self, request, response):
    return_values = self.return_values
    response.set_content(return_values.get('content', ''))
    response.set_statuscode(return_values.get('status_code', 200))
    for header_key, header_value in return_values.get('headers', {}).iteritems():
      new_header = response.add_header()
      new_header.set_key(header_key)
      new_header.set_value(header_value)
    response.set_finalurl(return_values.get('final_url', request.url()))
    response.set_contentwastruncated(return_values.get('content_was_truncated', False))

    self.request = request
    self.response = response


class TrackingTest(unittest.TestCase):
  """Test for tracking function."""

  def test_track_event_to_ga(self):
    urlfetch_mock = URLFetchServiceMock()
    apiproxy_stub_map.apiproxy.RegisterStub('urlfetch', urlfetch_mock)
    urlfetch_mock.set_return_values(content='')
    status_code = tracking.track_event_to_ga("Error", "Payment", "Amount", "100")
    self.assertEqual(200, status_code)

if __name__ == '__main__':
  unittest.main()