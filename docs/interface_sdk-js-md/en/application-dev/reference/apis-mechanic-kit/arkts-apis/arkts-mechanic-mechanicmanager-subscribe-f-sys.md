# subscribe (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## subscribe

```TypeScript
function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void
```

Subscribe to the specified events.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void--><!--Device-mechanicManager-function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| events | [MechEventType](arkts-mechanic-mechanicmanager-mecheventtype-e-sys.md)[] | Yes | Events to subscribe to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MechEvent](arkts-mechanic-mechanicmanager-mechevent-i-sys.md)&gt; | Yes | Callback of event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |
| [33300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-device-not-connected) | Device not connected. |
| [33300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300003-function-not-supported) | Feature not supported. |

