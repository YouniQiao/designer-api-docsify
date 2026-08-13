# MediaAssetProgressHandler

**MediaAssetProgressHandler** is used to obtain the media asset processing progress from **onProgress()**.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-photoAccessHelper-interface MediaAssetProgressHandler--><!--Device-photoAccessHelper-interface MediaAssetProgressHandler-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onProgress

```TypeScript
onProgress(progress: int): void
```

Called when the progress of the requested video is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MediaAssetProgressHandler-onProgress(progress: int): void--><!--Device-MediaAssetProgressHandler-onProgress(progress: int): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | int | Yes | Progress in percentage. &lt;br&gt;Value range: [0, 100] |

