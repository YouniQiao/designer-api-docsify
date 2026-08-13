# MediaAssetProgressHandler

**MediaAssetProgressHandler** is used to obtain the media asset processing progress from **onProgress()**.

**Since:** 23

**Deprecated since:** -1

<!--Device-photoAccessHelper-interface MediaAssetProgressHandler--><!--Device-photoAccessHelper-interface MediaAssetProgressHandler-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onProgress

```TypeScript
onProgress(progress: number): void
```

Called when the progress of the requested video is returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaAssetProgressHandler-onProgress(progress: int): void--><!--Device-MediaAssetProgressHandler-onProgress(progress: int): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | number | Yes |
