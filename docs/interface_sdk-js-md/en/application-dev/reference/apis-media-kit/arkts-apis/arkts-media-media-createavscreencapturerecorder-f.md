# createAVScreenCaptureRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVScreenCaptureRecorder

```TypeScript
function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>
```

Creates an AVScreenCaptureRecorder instance. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
