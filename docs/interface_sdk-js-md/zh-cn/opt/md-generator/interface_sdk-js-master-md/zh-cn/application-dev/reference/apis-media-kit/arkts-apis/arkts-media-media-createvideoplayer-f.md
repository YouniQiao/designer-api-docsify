# createVideoPlayer

## createVideoPlayer

```TypeScript
function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void
```

异步方式创建视频播放实例，使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)(callback: AsyncCallback&lt;AVPlayer&gt;)

<!--Device-media-function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void--><!--Device-media-function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VideoPlayer](arkts-media-multimedia-media-videoplayer-i.md)&gt; | 是 |

## 示例

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

异步方式创建视频播放实例，通过Promise获取返回值。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createAVPlayer](arkts-media-media-createavplayer-f.md#createAVPlayer)()

<!--Device-media-function createVideoPlayer(): Promise<VideoPlayer>--><!--Device-media-function createVideoPlayer(): Promise<VideoPlayer>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[VideoPlayer](arkts-media-multimedia-media-videoplayer-i.md)&gt; |

## 示例

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
