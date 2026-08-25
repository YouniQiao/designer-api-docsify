# createAVTranscoder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVTranscoder

```TypeScript
function createAVTranscoder(): Promise<AVTranscoder>
```

Creates an AVTranscoder instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> A maximum of 2 AVTranscoder instances can be created.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVTranscoder](arkts-media-media-avtranscoder-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
