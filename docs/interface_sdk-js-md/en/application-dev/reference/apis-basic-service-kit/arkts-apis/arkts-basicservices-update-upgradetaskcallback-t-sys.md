# UpgradeTaskCallback (System API)

```TypeScript
export type UpgradeTaskCallback = (eventInfo: EventInfo) => void
```

Represents an event callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export type UpgradeTaskCallback = (eventInfo: EventInfo) => void--><!--Device-update-export type UpgradeTaskCallback = (eventInfo: EventInfo) => void-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventInfo | [EventInfo](arkts-basicservices-update-eventinfo-i-sys.md) | Yes | Event information, including the eventId(eventID) and taskBody(task data) fields. |

