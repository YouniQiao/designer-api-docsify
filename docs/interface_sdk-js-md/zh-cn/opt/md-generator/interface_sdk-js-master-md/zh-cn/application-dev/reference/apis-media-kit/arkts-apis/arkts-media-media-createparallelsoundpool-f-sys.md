# createParallelSoundPool（系统接口）

## createParallelSoundPool

```TypeScript
function createParallelSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

Creates a **SoundPool** instance. This API uses a promise to return the result. If a **SoundPool** instance created using [createSoundPool](arkts-media-media-createsoundpool-f.md#createSoundPool) is used to play the same sound again, it stops the current audio and restarts the audio. However, if the instance is created using **createParallelSoundPool**, it keeps playing the first audio and starts the new one alongside it.

**起始版本：** 23

**废弃版本：** -1

<!--Device-media-function createParallelSoundPool(maxStreams: int, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>--><!--Device-media-function createParallelSoundPool(maxStreams: int, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxStreams | number | 是 |
| audioRenderInfo | audio.AudioRendererInfo | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SoundPool & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags : 0
}

media.createParallelSoundPool(5, audioRendererInfo).then((soundpool_: media.SoundPool) => {
  if (soundpool_ != null) {
    soundPool = soundpool_;
    console.info('Succeeded in creating SoundPool');
  } else {
    console.error('Failed to create SoundPool');
  }
}, (error: BusinessError) => {
  console.error(`soundpool catchCallback, error message:${error.message}`);
});
```
