# onDeviceStateChanged (System API)

## onDeviceStateChanged

```TypeScript
function onDeviceStateChanged(callback: Callback<DeviceState>): void
```

Registers a system callback for the device connection phase.The callback includes information such as error codes, connection status, radar errors, and user behavior codes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void--><!--Device-avSession-function onDeviceStateChanged(callback: Callback<DeviceState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DeviceState&gt; | Yes | Callback used to return the device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

