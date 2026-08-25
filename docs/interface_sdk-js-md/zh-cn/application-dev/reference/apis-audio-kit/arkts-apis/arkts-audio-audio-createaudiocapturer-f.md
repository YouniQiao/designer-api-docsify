# createAudioCapturer

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void
```

获取音频采集器。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md)&gt; | 是 |


## createAudioCapturer

```TypeScript
function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>
```

获取音频采集器。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AudioCapturerOptions](arkts-audio-audio-audiocaptureroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioCapturer](arkts-audio-audio-audiocapturer-i.md)&gt; |
