# createMicInAudioCapturer (System API)

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createMicInAudioCapturer

```TypeScript
function createMicInAudioCapturer(config: AudioCapturerMicInConfig): Promise<AudioCapturer | null>
```

获取一个特殊的{@link #AudioCapturer}实例。该方法使用promise返回录音实例。此捕获可用于记录Mic-In音频数据和回声参考信号，以便应用处理算法。Mic-In音频数据和回声参考信号将根据应用程序设置的配置被放入一个或多个缓冲。当应用程序处于后台时，不允许创建录音实例。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.MICROPHONE

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createMicInAudioCapturer(config: AudioCapturerMicInConfig): Promise<AudioCapturer | null>--><!--Device-audio-function createMicInAudioCapturer(config: AudioCapturerMicInConfig): Promise<AudioCapturer | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [AudioCapturerMicInConfig](arkts-audio-audio-audiocapturermicinconfig-i-sys.md) | Yes | Capturer configuration, see {@link #AudioCapturerMicInConfig} for details. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioCapturer \| null&gt; | Promise用于返回录音实例。 如果出现错误，则返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 201 | Permission denied, including background recording. |
| 202 | Caller is not a system application. |
| 6800301 | Audio system internal error, such as system process crash. |
| 6800104 | Capturer creation is not supported, may caused by following problems: &lt;br&gt; 1. Source type is unsupported for this capturer, only {@link #SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT} and {@link #SOURCE_TYPE_VOICE_RECOGNITION} are supported currently. &lt;br&gt; 2. Echo reference signal's config is unsupported, echo reference's sampling rate and format must be the same as MicIn audio data currently. |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioEcStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Encoding format.
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT, // Audio source type: microphone. The value of SourceType must be SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT.
  capturerFlags: 0 // AudioCapturer flag.
};

let audioMicInStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Encoding format.
};

let audioCapturerMicInConfig: audio.AudioCapturerMicInConfig = {
  ecStreamInfo: audioEcStreamInfo,
  capturerInfo: audioCapturerInfo,
  micInStreamInfo: audioMicInStreamInfo
};

let audioCapturer: audio.AudioCapturer | null = null;

audio.createMicInAudioCapturer(audioCapturerMicInConfig).then((data) => {
  audioCapturer = data;
  console.info('AudioCapturer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioCapturer Created : ERROR : ${err}`);
});
```

