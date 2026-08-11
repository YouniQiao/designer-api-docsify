# createMediaSourceWithFd

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithFd

```TypeScript
function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined
```

Creates a media source from file descriptor.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-media-function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined--><!--Device-media-function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fdSrc | [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md) | Yes | file descriptor handler. &lt;br&gt;file descriptor handler. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaSource](arkts-media-media-mediasource-i.md) | MediaSource instance if the operation is successful; returns undefined otherwise. |

