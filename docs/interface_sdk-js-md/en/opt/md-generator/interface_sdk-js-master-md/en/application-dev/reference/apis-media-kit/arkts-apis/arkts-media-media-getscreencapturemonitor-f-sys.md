# getScreenCaptureMonitor (System API)

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## getScreenCaptureMonitor

```TypeScript
function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>
```

Obtains a **ScreenCaptureMonitor** instance. This API uses a promise to return the result.

**Since:** 18

<!--Device-media-function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>--><!--Device-media-function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ScreenCaptureMonitor](arkts-media-media-screencapturemonitor-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let screenCaptureMonitor: media.ScreenCaptureMonitor;
try {
  screenCaptureMonitor = await media.getScreenCaptureMonitor();
} catch (err) {
  console.error(`getScreenCaptureMonitor failed, error message:${err.message}`);
}
```
