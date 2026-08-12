# createSoundPool

## createSoundPool

```TypeScript
function createSoundPool(
    maxStreams: number,
    audioRenderInfo: audio.AudioRendererInfo,
    callback: AsyncCallback<SoundPool>
  ): void
```

创建音频池实例。使用callback异步回调。

> **说明：**
> 
> - API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
> 
> - API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**起始版本：** 10

<!--Device-media-function createSoundPool(    maxStreams: number,    audioRenderInfo: audio.AudioRendererInfo,    callback: AsyncCallback<SoundPool>  ): void--><!--Device-media-function createSoundPool(    maxStreams: number,    audioRenderInfo: audio.AudioRendererInfo,    callback: AsyncCallback<SoundPool>  ): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxStreams | number | 是 |
| audioRenderInfo | audio.AudioRendererInfo | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SoundPool&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-内存分配失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo, (error, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
  }
});
```


## createSoundPool

```TypeScript
function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

创建音频池实例。使用Promise异步回调。

> **说明：**
> 
> - API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
> 
> - API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**起始版本：** 10

<!--Device-media-function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>--><!--Device-media-function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>-End-->

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
| [5400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-内存分配失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo).then((soundpool_: media.SoundPool) => {
  if (soundpool_) {
    soundPool = soundpool_;
    console.info('Succeeded in creating SoundPool');
  } else {
    console.error('Failed to create SoundPool');
  }
}, (error: BusinessError) => {
  console.error(`soundpool catchCallback, error message:${error.message}`);
});
```
