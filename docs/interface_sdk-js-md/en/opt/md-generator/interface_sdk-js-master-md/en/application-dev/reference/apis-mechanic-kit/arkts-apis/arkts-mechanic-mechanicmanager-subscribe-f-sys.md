# subscribe (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## subscribe

```TypeScript
function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void
```

Subscribe to the specified events.

**Since:** 26.0.0

<!--Device-mechanicManager-function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void--><!--Device-mechanicManager-function subscribe(events: MechEventType[], callback: Callback<MechEvent>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| events | [MechEventType](arkts-mechanic-mechanicmanager-mecheventtype-e-sys.md)[] | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MechEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
| [33300002](../errorcode-mechanic.md#33300002-device-not-connected) |
| [33300003](../errorcode-mechanic.md#33300003-function-not-supported) |
