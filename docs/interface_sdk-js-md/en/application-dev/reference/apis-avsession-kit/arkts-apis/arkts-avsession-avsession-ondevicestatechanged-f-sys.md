# onDeviceStateChanged (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## onDeviceStateChanged

```TypeScript
function onDeviceStateChanged(callback: Callback<DeviceState>): void
```

Registers a system callback for the device connection phase. The callback includes information such as error codes, connection status, radar errors, and user behavior codes.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void--><!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceState](arkts-avsession-avsession-devicestate-i-sys.md)&gt; | Yes | Callback used to return the device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

