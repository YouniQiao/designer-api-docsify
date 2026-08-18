# createAsrProcessingController（系统接口）

## 导入模块

```TypeScript
```

## createAsrProcessingController

```TypeScript
function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController
```

Create ASR processing controller on one audio capturer.

**起始版本：** 12

<!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController--><!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| audioCapturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

**示例**

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

**起始版本：** 23

<!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController | null--><!--Device-audio-function createAsrProcessingController(audioCapturer: AudioCapturer): AsrProcessingController | null-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| audioCapturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AsrProcessingController](arkts-audio-audio-asrprocessingcontroller-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
