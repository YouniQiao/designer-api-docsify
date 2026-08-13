# MediaSourceLoader

Defines a media data loader, which needs to be implemented by applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoader-read: SourceReadCallback--><!--Device-MediaSourceLoader-read: SourceReadCallback-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

