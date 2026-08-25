# createVideoPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createVideoPlayer

```TypeScript
function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void
```

Creates a **VideoPlayer** instance. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAVPlayer](arkts-media-media-createavplayer-f.md)(callback: AsyncCallback&lt;AVPlayer&gt;)

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VideoPlayer](arkts-media-media-videoplayer-i.md)&gt; | Yes |


## createVideoPlayer

```TypeScript
function createVideoPlayer(): Promise<VideoPlayer>
```

Creates a VideoPlayer instance. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAVPlayer](arkts-media-media-createavplayer-f.md)()

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VideoPlayer](arkts-media-media-videoplayer-i.md)&gt; |
