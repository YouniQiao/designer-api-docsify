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

**Deprecated since:** -1

<!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function offDeviceLogEvent(callback?: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceLogEventCode](arkts-avsession-avsession-devicelogeventcode-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
