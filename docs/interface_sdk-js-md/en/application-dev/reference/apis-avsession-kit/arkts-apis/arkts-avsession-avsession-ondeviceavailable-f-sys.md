# onDeviceAvailable (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## onDeviceAvailable

```TypeScript
function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void
```

Register device discovery callback

**Since:** 23

<!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | Yes | Used to returns the device info |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

