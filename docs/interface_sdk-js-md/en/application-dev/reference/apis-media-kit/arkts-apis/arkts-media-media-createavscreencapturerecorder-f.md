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

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>--><!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md)&gt; | Promise used to return the result. If the operation is successful, an AVScreenCaptureRecorder instance is returned; otherwise, **null** is returned. The instance can be used for screen capture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by promise. |

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder | undefined>--><!--Device-media-function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md) \| undefined&gt; | Promise used to return the result. If the operation is successful, an **AVScreenCaptureRecorder** instance is returned; otherwise, **undefined** is returned. The instance can be used for screen capture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) | No memory. Return by promise. |

