# offDeviceAvailable (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
import { avSession } from '@kit.AVSessionKit';
```

## offDeviceAvailable

```TypeScript
function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void
```

Unregister device discovery callback

**Since:** 23

<!--Device-avSession-function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function offDeviceAvailable(callback?: Callback<OutputDeviceInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | No | Used to returns the device info |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

