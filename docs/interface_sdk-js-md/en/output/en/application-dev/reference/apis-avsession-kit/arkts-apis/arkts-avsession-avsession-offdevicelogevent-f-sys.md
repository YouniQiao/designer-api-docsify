# offDeviceLogEvent (System API)

## offDeviceLogEvent

```TypeScript
function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void
```

UnRegister log event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DeviceLogEventCode&gt; | No | Used to handle ('deviceLogEvent') command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |

