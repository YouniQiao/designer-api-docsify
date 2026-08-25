# getScreenCaptureMonitor (System API)

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getScreenCaptureMonitor

```TypeScript
function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>
```

Obtains a **ScreenCaptureMonitor** instance. This API uses a promise to return the result.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ScreenCaptureMonitor](arkts-media-media-screencapturemonitor-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
