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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function offTrackingStateChange(callback?: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TrackingEventInfo](arkts-mechanic-mechanicmanager-trackingeventinfo-i.md)&gt; | No | Callback used to return the tracking event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) | Service exception. |

