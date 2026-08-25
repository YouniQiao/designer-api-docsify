# createParallelSoundPool（系统接口）

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createParallelSoundPool

```TypeScript
function createParallelSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

创建音频池实例。使用Promise异步回调。使用[createSoundPool](arkts-media-media-createsoundpool-f.md)创建的音频池实例，在重复播放相同音频时，会停止之前的播放并重新开始；而使用 createParallelSoundPool创建的实例，在重复播放相同音频时，不会停止之前的音频，而是并行播放。

**起始版本：** 20

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
