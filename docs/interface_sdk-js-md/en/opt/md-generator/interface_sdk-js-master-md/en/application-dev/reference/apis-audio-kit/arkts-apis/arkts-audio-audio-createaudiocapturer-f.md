# createAudioCapturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void
```

Creates an AudioCapturer instance. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** -1

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md)&gt; | Yes |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Encoding format.
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
  if (err) {
    console.error(`AudioCapturer Created : Error: ${err}`);
  } else {
    console.info('AudioCapturer Created : SUCCESS');
    audioCapturer = data;
  }
});
```


## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer | null>): void
```

Obtains an [AudioCapturer](arkts-audio-audio-audiocapturer-i.md#AudioCapturer) instance. This method uses an asynchronous callback to return the capturer instance. Using [AudioCapturer](arkts-audio-audio-audiocapturer-i.md#AudioCapturer) to record audio will need permission according to different Sourcetype in options parameter, like MICROPHONE for the most microphone recording cases.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer | null>): void--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer | null>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md) \| null & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |


## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>
```

Creates an AudioCapturer instance. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** -1

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md)&gt; |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Encoding format.
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

let audioCapturerOptions:audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions).then((data) => {
  audioCapturer = data;
  console.info('AudioCapturer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioCapturer Created : ERROR : ${err}`);
});
```


## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer | null>
```

Obtains an [AudioCapturer](arkts-audio-audio-audiocapturer-i.md#AudioCapturer) instance. This method uses a promise to return the capturer instance. Using [AudioCapturer](arkts-audio-audio-audiocapturer-i.md#AudioCapturer) to record audio will need permission according to different Sourcetype in options parameter, like MICROPHONE for the most microphone recording cases.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer | null>--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
