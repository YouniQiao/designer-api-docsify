# createVideoPlayer

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createVideoPlayer

```TypeScript
function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void
```

Creates a **VideoPlayer** instance. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)(callback: AsyncCallback&lt;AVPlayer&gt;)

<!--Device-media-function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void--><!--Device-media-function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VideoPlayer](arkts-media-media-videoplayer-i.md)&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
```


## createVideoPlayer

```TypeScript
function createVideoPlayer(): Promise<VideoPlayer>
```

Creates a VideoPlayer instance. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)()

<!--Device-media-function createVideoPlayer(): Promise<VideoPlayer>--><!--Device-media-function createVideoPlayer(): Promise<VideoPlayer>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VideoPlayer](arkts-media-media-videoplayer-i.md)&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer().then((video: media.VideoPlayer) => {
  if (video) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error('Failed to create VideoPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create VideoPlayer, error:${error}`);
});
```
