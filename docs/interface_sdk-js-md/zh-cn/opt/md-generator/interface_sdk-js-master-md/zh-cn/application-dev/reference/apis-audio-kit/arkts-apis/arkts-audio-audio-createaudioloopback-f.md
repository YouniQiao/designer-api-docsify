# createAudioLoopback

## createAudioLoopback

```TypeScript
function createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>
```

创建音频返听器。使用Promise异步回调。

在使用createAudioLoopback接口之前，需先通过[isAudioLoopbackSupported](arkts-audio-audio-audiostreammanager-i.md#isaudioloopbacksupported)查询系统返听能力。

**起始版本：** 26.0.0

<!--Device-audio-function createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>--><!--Device-audio-function createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;AudioLoopback&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioLoopback: audio.AudioLoopback;

audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
  audioLoopback = data;
  console.info('AudioLoopback Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioLoopback Created : ERROR : ${err}`);
});
```
