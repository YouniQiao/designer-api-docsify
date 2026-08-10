# onDeviceLogEvent (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## onDeviceLogEvent

```TypeScript
function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void
```

Register log event callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function onDeviceLogEvent(callback: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceLogEventCode&gt; | Yes | Used to handle ('deviceLogEvent') command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 202 | Not System App. |

