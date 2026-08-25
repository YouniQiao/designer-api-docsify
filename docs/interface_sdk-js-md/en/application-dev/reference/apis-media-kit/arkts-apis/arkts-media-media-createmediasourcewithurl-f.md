# createMediaSourceWithUrl

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithUrl

```TypeScript
function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource
```

Creates a media source for streaming media to be pre-downloaded.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| headers | Record & lt;string, string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaSource](arkts-media-media-mediasource-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
