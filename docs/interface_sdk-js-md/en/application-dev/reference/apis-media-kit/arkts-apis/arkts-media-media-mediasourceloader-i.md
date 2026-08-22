# MediaSourceLoader

Defines a media data loader, which needs to be implemented by applications.

**Since:** 23

<!--Device-media-interface MediaSourceLoader--><!--Device-media-interface MediaSourceLoader-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## close

```TypeScript
close: SourceCloseCallback
```

Callback function is implemented by application, which is used to handle resource close request.

**Type:** [SourceCloseCallback](arkts-media-media-sourceclosecallback-t.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoader-close: SourceCloseCallback--><!--Device-MediaSourceLoader-close: SourceCloseCallback-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## open

```TypeScript
open: SourceOpenCallback
```

Callback function is implemented by application, which is used to handle resource opening requests.

**Type:** [SourceOpenCallback](arkts-media-media-sourceopencallback-t.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoader-open: SourceOpenCallback--><!--Device-MediaSourceLoader-open: SourceOpenCallback-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## read

```TypeScript
read: SourceReadCallback
```

Callback function is implemented by application, which is used to handle resource read requests.

**Type:** [SourceReadCallback](arkts-media-media-sourcereadcallback-t.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoader-read: SourceReadCallback--><!--Device-MediaSourceLoader-read: SourceReadCallback-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Examples**

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
    // Open the resource and return a unique handle, ensuring the mapping between the UUID and request.
    uuid += 1;
    requests.set(uuid, request);
    return uuid;
  },
  read: (uuid: number, requestedOffset: number, requestedLength: number) => {
    console.info(`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}`);
    // Check whether the UUID is valid and store the read request. Avoid blocking the request while pushing data and header information.
  },
  close: (uuid: number) => {
    console.info(`Closing resource with handle ${uuid}`);
    // Clear resources related to the current UUID.
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

