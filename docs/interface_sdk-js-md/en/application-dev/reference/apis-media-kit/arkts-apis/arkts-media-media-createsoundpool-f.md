# createSoundPool

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createSoundPool

```TypeScript
function createSoundPool(
    maxStreams: number,
    audioRenderInfo: audio.AudioRendererInfo,
    callback: AsyncCallback<SoundPool>
  ): void
```

Creates a SoundPool instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode.
> Therefore, an application process can create only one SoundPool instance.&gt;
> - In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore,
> an application process can create a maximum of 128 SoundPool instances.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxStreams | number | Yes |
| audioRenderInfo | audio.AudioRendererInfo | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SoundPool&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

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


## createSoundPool

```TypeScript
function createSoundPool(
    maxStreams: int,
    audioRenderInfo: audio.AudioRendererInfo,
    callback: AsyncCallback<SoundPool | undefined>
  ): void
```

Creates a **SoundPool** instance. This API uses an asynchronous callback to return the result.  
**NOTE：**
- In versions earlier than API version 18, the bottom layer of the created **SoundPool** object is in singleton mode. Therefore, an application process can create only one **SoundPool** instance. - In API version 18 and later versions, the bottom layer of the created **SoundPool** object is in multiton mode. Therefore, an application process can create a maximum of 128 **SoundPool** instances.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxStreams | int | Yes |
| audioRenderInfo | audio.AudioRendererInfo | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SoundPool \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

See [createSoundPool](#createsoundpool)


## createSoundPool

```TypeScript
function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

Creates a SoundPool instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> - In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode.
> Therefore, an application process can create only one SoundPool instance.&gt;
> - In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore,
> an application process can create a maximum of 128 SoundPool instances.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxStreams | number | Yes |
| audioRenderInfo | audio.AudioRendererInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SoundPool & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

See [createSoundPool](#createsoundpool)


## createSoundPool

```TypeScript
function createSoundPool(maxStreams: int, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool | undefined>
```

Creates a **SoundPool** instance. This API uses a promise to return the result.  
**NOTE：**
- In versions earlier than API version 18, the bottom layer of the created **SoundPool** object is in singleton mode. Therefore, an application process can create only one **SoundPool** instance. - In API version 18 and later versions, the bottom layer of the created **SoundPool** object is in multiton mode. Therefore, an application process can create a maximum of 128 **SoundPool** instances.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxStreams | int | Yes |
| audioRenderInfo | audio.AudioRendererInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SoundPool \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

**Examples**

See [createSoundPool](#createsoundpool)
