# createMediaSourceWithDataSource

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithDataSource

```TypeScript
function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined
```

Creates a media source from a custom data source.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataSrc | [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) \| undefined |
