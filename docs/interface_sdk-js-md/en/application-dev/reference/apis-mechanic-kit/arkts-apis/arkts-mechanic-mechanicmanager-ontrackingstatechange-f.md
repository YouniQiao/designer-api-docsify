# onTrackingStateChange

## Modules to Import

```TypeScript
import { mechanicManager } from 'mechanicManager';
```

## onTrackingStateChange

```TypeScript
function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void
```

Subscribes to tracking events.

**Since:** 23

<!--Device-mechanicManager-function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function onTrackingStateChange(callback: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md)&gt; | Yes | Callback used to return the tracking event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

