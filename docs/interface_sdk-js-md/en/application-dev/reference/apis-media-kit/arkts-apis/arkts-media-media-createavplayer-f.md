# createAVPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVPlayer

```TypeScript
function createAVPlayer(callback: AsyncCallback<AVPlayer>): void
```

Creates an AVPlayer instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video
> playback scenarios.<!--Del-->>
> - The actual number of instances that can be created may be different. It depends on the specifications of the
> device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer
> instances for an application in audio and video playback scenarios.<!--DelEnd-->>
> - Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing
> them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the
> system might terminate applications to free up resources.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVPlayer](arkts-media-media-avplayer-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |


## createAVPlayer

```TypeScript
function createAVPlayer(): Promise<AVPlayer>
```

Creates an AVPlayer instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video
> playback scenarios.<!--Del-->>
> - The actual number of instances that can be created may be different. It depends on the specifications of the
> device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer
> instances for an application in audio and video playback scenarios.<!--DelEnd-->>
> - Applications should reasonably use AVPlayer objects in accordance with actual service requirements, create them
> on demand, and release them in a timely manner. This avoids excessive memory consumption caused by holding too
> many AVPlayer instances, which may result in the system terminating the application.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVPlayer](arkts-media-media-avplayer-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
