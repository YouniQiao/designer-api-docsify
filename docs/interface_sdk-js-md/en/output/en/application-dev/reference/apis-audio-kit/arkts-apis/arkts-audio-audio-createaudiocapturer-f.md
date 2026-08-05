# createAudioCapturer

## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void
```

Creates an AudioCapturer instance. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Capturer configurations. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AudioCapturer&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the AudioCapturer instance obtained; otherwise, **err** is an error object. If the operation fails, an error object with one of the following error codes is returned:\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Error code 6800301: indicates a parameter verification exception, permission verification exception, or system processing exception. For details, see system logs.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Error code 6800101: indicates that a mandatory parameter is null or the parameter type is incorrect. |

**Example**

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

Obtains an \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses an asynchronous callback to return the capturer instance. Using \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to record audio will need permission according to different \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ in options parameter, like \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ for the most microphone recording cases.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer | null>): void--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer | null>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Capturer configurations. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AudioCapturer \| null&gt; | Yes | Callback used to return the audio capturer instance, or null if any error occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio system internal error, such as system crash. |


## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>
```

Creates an AudioCapturer instance. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Capturer configurations. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioCapturer&gt; | Promise used to return the result. If the operation is successful, an |

**Example**

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

Obtains an \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses a promise to return the capturer instance. Using \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to record audio will need permission according to different \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ in options parameter, like \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ for the most microphone recording cases.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer | null>--><!--Device-audio-function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Capturer configurations. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioCapturer \| null&gt; | Promise used to return the audio capturer instance, |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-system-error) | Audio system internal error, such as system crash. |

