# createAVScreenCaptureRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVScreenCaptureRecorder

```TypeScript
function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>
```

Creates an AVScreenCaptureRecorder instance. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

<!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>--><!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avScreenCaptureRecorder: media.AVScreenCaptureRecorder;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in createAVScreenCaptureRecorder');
  } else {
    console.error('Failed to createAVScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});
```


## createAVScreenCaptureRecorder

```TypeScript
function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder | undefined>
```

Creates an **AVScreenCaptureRecorder** instance. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder | undefined>--><!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
