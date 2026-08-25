# createMediaSourceWithStreamData

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithStreamData

```TypeScript
function createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource
```

Creates a multi-bitrate media source for streaming media. Currently, only the HTTP-FLV multi-bitrate media source is supported.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streams | Array&lt;[MediaStream](arkts-media-media-mediastream-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) |
