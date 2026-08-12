# createMediaSourceWithDataSource

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createMediaSourceWithDataSource

```TypeScript
function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined
```

Creates a media source from a custom data source.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-media-function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined--><!--Device-media-function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSrc | [AVDataSrcDescriptor](arkts-media-media-avdatasrcdescriptor-i.md) | Yes | Interface definition for obtaining media data. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaSource](arkts-media-media-mediasource-i.md) | MediaSource instance if the operation is successful; returns undefined otherwise. |

