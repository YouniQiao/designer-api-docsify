# offDeviceStateChanged (System API)

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## offDeviceStateChanged

```TypeScript
function offDeviceStateChanged(callback?: Callback<DeviceState>): void
```

Unregisters a system callback for the device connection phase.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function offDeviceStateChanged(callback?: Callback<DeviceState>): void--><!--Device-avSession-function offDeviceStateChanged(callback?: Callback<DeviceState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceState](arkts-avsession-avsession-devicestate-i-sys.md)&gt; | No | Callback used to return the device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

