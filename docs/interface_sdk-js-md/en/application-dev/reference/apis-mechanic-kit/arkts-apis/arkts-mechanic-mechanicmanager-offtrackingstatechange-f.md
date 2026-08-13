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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md)&gt; | No | Callback used to return the tracking event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) | Service exception. |

