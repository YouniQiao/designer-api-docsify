# createSoundPool

## Modules to Import

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

Creates a SoundPool instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode.
> Therefore, an application process can create only one SoundPool instance.&gt;
> - In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore,
> an application process can create a maximum of 128 SoundPool instances.

**Since:** 10

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
