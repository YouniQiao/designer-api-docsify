# createAsrProcessingController (System API)

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createAsrProcessingController

```TypeScript
function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController
```

Create ASR processing controller on one audio capturer.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController--><!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| audioCapturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i-sys.md) | Yes | The audio capturer whose ASR processing will be controlled. The source type of this capturer must be {@link SourceType#SOURCE_TYPE_VOICE_RECOGNITION}. |

**Return value:**

| Type | Description |
| --- | --- |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) | ASR Processing Controller. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800104 | Operation not allowed. e.g. the source type of the input audio capturer is not {@link SourceType#SOURCE_TYPE_VOICE_RECOGNITION} or {@link SourceType#SOURCE_TYPE_WAKEUP}, or this audio capturer is already released. |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC,
  capturerFlags: 0
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
  if (err) {
    console.error(`AudioCapturer Created : Error: ${err}`);
  } else {
    console.info('AudioCapturer Created : Success : SUCCESS');
    let audioCapturer = data;
    let asrProcessingController = audio.createAsrProcessingController(audioCapturer);
    console.info('AsrProcessingController Created : Success : SUCCESS');
  }
});
```


## createAsrProcessingController

```TypeScript
function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController | null
```

Create ASR processing controller on one audio capturer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController | null--><!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController | null-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| audioCapturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i-sys.md) | Yes | The audio capturer whose ASR processing will be controlled. The source type of this capturer must be {@link SourceType#SOURCE_TYPE_VOICE_RECOGNITION}. |

**Return value:**

| Type | Description |
| --- | --- |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) | ASR Processing Controller, or null when an error happens. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800104 | Operation not allowed. e.g. the source type of the input audio capturer is not {@link SourceType#SOURCE_TYPE_VOICE_RECOGNITION} or {@link SourceType#SOURCE_TYPE_WAKEUP}, or this audio capturer is already released. |

