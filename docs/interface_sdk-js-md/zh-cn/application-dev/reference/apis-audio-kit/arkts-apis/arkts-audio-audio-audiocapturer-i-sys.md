# AudioCapturer

提供音频采集的相关接口。

在使用AudioCapturer的接口之前，需先通过[createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md)获取AudioCapturer实例。

> **说明：**
> 
> - 本Interface首批接口从API version 8开始支持。

**起始版本：** 23

<!--Device-audio-interface AudioCapturer--><!--Device-audio-interface AudioCapturer-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## offReadMicInData

```TypeScript
offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void
```

取消订阅micIn音频数据回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md)&gt; | 否 | 用于读取缓冲的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Caller is not a system application. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permitted at running state. |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioMicInStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT,
  capturerFlags: 0
};

let audioCapturerMicInConfig: audio.AudioCapturerMicInConfig = {
  micInStreamInfo: audioMicInStreamInfo,
  capturerInfo: audioCapturerInfo
};

let readMicInDataCallback: Callback<audio.AudioCapturerMicInData> =
  (data: audio.AudioCapturerMicInData): void => {
    console.info(`mic-in data length: ${data.micInData.byteLength}`);
  };

async function unregisterReadMicInDataCallback(): Promise<void> {
  try {
    let audioCapturer: audio.AudioCapturer | null =
      await audio.createMicInAudioCapturer(audioCapturerMicInConfig);
    if (audioCapturer === null) {
      console.error('AudioCapturer Created : ERROR : audioCapturer is null');
      return;
    }

    audioCapturer.onReadMicInData(readMicInDataCallback);

    // 取消指定回调的监听。
    audioCapturer.offReadMicInData(readMicInDataCallback);

    // 取消该事件的所有监听。
    audioCapturer.offReadMicInData();
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to create AudioCapturer. Code: ${error.code}, message: ${error.message}`);
  }
}
```

## onReadMicInData

```TypeScript
onReadMicInData(callback: Callback<AudioCapturerMicInData>): void
```

订阅micIn音频数据回调。此回调的优先级高于“readData”回调。 如果此回调和'readData'回调都被订阅，则仅此回调将被调用。 有关更多详细信息，请参见onReadData。 当有音频缓冲可用于读取更多数据时，触发该事件。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void--><!--Device-AudioCapturer-onReadMicInData(callback: Callback<AudioCapturerMicInData>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md)&gt; | 是 | 读取缓冲的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Caller is not a system application. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permitted at running state. |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioEcStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioProcessedStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioMicInStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT,
  capturerFlags: 0
};

let audioCapturerMicInConfig: audio.AudioCapturerMicInConfig = {
  processedStreamInfo: audioProcessedStreamInfo,
  micInStreamInfo: audioMicInStreamInfo,
  ecStreamInfo: audioEcStreamInfo,
  capturerInfo: audioCapturerInfo
};

// data表示处理后的音频数据，micInData表示原始Mic-In音频数据。
// ecData表示回声参考音频数据；如果未配置ecStreamInfo，该字段可能为空。
let readMicInDataCallback: Callback<audio.AudioCapturerMicInData> =
  (data: audio.AudioCapturerMicInData): void => {
    let ecDataLength = data.ecData ? data.ecData.byteLength : 0;
    console.info(`processed data length: ${data.data.byteLength}`);
    console.info(`mic-in data length: ${data.micInData.byteLength}`);
    console.info(`echo reference data length: ${ecDataLength}`);
  };

async function registerReadMicInDataCallback(): Promise<void> {
  try {
    // 先创建Mic-In采集器实例，再注册数据读取回调。
    let audioCapturer: audio.AudioCapturer | null =
      await audio.createMicInAudioCapturer(audioCapturerMicInConfig);
    if (audioCapturer === null) {
      console.error('AudioCapturer Created : ERROR : audioCapturer is null');
      return;
    }
    // 注册成功后，当有可读取的音频缓冲区时会触发readMicInDataCallback。
    audioCapturer.onReadMicInData(readMicInDataCallback);
    console.info('Succeeded in registering onReadMicInData callback.');
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to create AudioCapturer. Code: ${error.code}, message: ${error.message}`);
  }
}
```

## setInputDeviceToAccessory

```TypeScript
setInputDeviceToAccessory(): void
```

Sets default input device of this Capturer to DEVICE_TYPE_ACCESSORY. Other capturers' devices will not be affected by this method. This method can only be used before the capture stream starts. Besides, if audio accessory is not connected, this method will report fail. After calling this function, the input device of this capturer will not be affected by other interfaces.

**起始版本：** 23

<!--Device-AudioCapturer-setInputDeviceToAccessory(): void--><!--Device-AudioCapturer-setInputDeviceToAccessory(): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Caller is not a system application. |
| [6800103](../errorcode-audio.md#6800103-状态不支持) | Operation not permit at current state. |

