#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for batch
processing.
Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

# [START import_libraries]
import argparse
import io
import record
# [END import_libraries]


# [START def_transcribe_file]
def transcribe_file():
    """Transcribe the given audio file."""
    record.fun()
    speech_file = "output.flac"
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code='en-IN')
    # [END migration_audio_config_file]

    # [START migration_sync_response]
    response = client.recognize(config, audio)
    #print(response)
    # [END migration_sync_request]
    # Print the first alternative of all the consecutive results.
    try:
        for result in response.results:
            print(format(result.alternatives[0].transcript))
        return (format(result.alternatives[0].transcript))
    except:
        return("I could not get that")
    # [END migration_sync_response]
# [END def_transcribe_file]


if __name__ == '__main__':
    transcribe_file()