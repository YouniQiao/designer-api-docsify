# offTrackingStateChange

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## offTrackingStateChange

```TypeScript
function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void
```

Unsubscribes from tracking events.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
