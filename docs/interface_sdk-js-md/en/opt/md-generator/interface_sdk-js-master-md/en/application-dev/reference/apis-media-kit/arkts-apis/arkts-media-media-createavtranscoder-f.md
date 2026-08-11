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

> **NOTE：**
> 
> A maximum of 2 AVTranscoder instances can be created.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-media-function createAVTranscoder(): Promise<AVTranscoder>--><!--Device-media-function createAVTranscoder(): Promise<AVTranscoder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AVTranscoder&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avTranscoder: media.AVTranscoder | undefined = undefined;
media.createAVTranscoder().then((transcoder: media.AVTranscoder) => {
  if (transcoder) {
    avTranscoder = transcoder;
    console.info('Succeeded in creating AVTranscoder');
  } else {
    console.error('Failed to create AVTranscoder');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVTranscoder, error message:${error.message}`);
});
```
