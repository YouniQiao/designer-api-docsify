# onTrackingStateChange

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## onTrackingStateChange

```TypeScript
function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void
```

Subscribes to tracking events.

**Since:** 23

**Deprecated since:** -1

<!--Device-mechanicManager-function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |
