# createSoundPool

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createSoundPool

```TypeScript
function createSoundPool(
    maxStreams: number,
    audioRenderInfo: audio.AudioRendererInfo,
    callback: AsyncCallback<SoundPool>
  ): void
```

创建音频池实例。使用callback异步回调。

> **说明：**&gt;
> - API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。&gt;
> - API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxStreams | number | 是 |
| audioRenderInfo | audio.AudioRendererInfo | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SoundPool&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |


## createSoundPool

```TypeScript
function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

创建音频池实例。使用Promise异步回调。

> **说明：**&gt;
> - API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。&gt;
> - API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

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
