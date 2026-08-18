# offDeviceLogEvent (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## offDeviceLogEvent

```TypeScript
function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void
```

UnRegister log event callback.

**Since:** 23

<!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceLogEventCode](arkts-avsession-avsession-devicelogeventcode-e-sys.md)&gt; | No | Used to handle ('deviceLogEvent') command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

