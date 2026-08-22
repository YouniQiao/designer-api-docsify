# MediaSourceLoader

Defines a media data loader, which needs to be implemented by applications.

**起始版本：** 23

<!--Device-unnamed-interface MediaSourceLoader--><!--Device-unnamed-interface MediaSourceLoader-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## close

```TypeScript
close: SourceCloseCallback
```

Callback function is implemented by application, which is used to handle resource close request.

**类型：** [SourceCloseCallback](arkts-media-sourceclosecallback-t.md)

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoader-close: SourceCloseCallback--><!--Device-MediaSourceLoader-close: SourceCloseCallback-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## open

```TypeScript
open: SourceOpenCallback
```

Callback function is implemented by application, which is used to handle resource opening requests.

**类型：** [SourceOpenCallback](arkts-media-sourceopencallback-t.md)

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoader-open: SourceOpenCallback--><!--Device-MediaSourceLoader-open: SourceOpenCallback-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## read

```TypeScript
read: SourceReadCallback
```

Callback function is implemented by application, which is used to handle resource read requests.

**类型：** [SourceReadCallback](arkts-media-sourcereadcallback-t.md)

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoader-read: SourceReadCallback--><!--Device-MediaSourceLoader-read: SourceReadCallback-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**示例**

```TypeScript
import { HashMap } from '@kit.ArkTS';
import { media } from '@kit.MediaKit';

let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
let uuid: number = 1;
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let mediaSourceLoader: media.MediaSourceLoader = {
  open: (request: media.MediaSourceLoadingRequest) => {
    console.info(`Opening resource: ${request.url}`);
    // 成功打开资源，返回唯一的句柄, 保证uuid和request对应。
    uuid += 1;
    requests.set(uuid, request);
    return uuid;
  },
  read: (uuid: number, requestedOffset: number, requestedLength: number) => {
    console.info(`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}`);
    // 判断uuid是否合法、存储read请求，不要在read请求阻塞去推送数据和头信息。
  },
  close: (uuid: number) => {
    console.info(`Closing resource with handle ${uuid}`);
    // 清除当前uuid相关资源。
    requests.remove(uuid);
  }
};

mediaSource.setMediaResourceLoaderDelegate(mediaSourceLoader);
let playStrategy : media.PlaybackStrategy = {
  preferredBufferDuration: 20,
};

async function setupPlayer() {
  let player = await media.createAVPlayer();
  player.setMediaSource(mediaSource, playStrategy);
}
```

