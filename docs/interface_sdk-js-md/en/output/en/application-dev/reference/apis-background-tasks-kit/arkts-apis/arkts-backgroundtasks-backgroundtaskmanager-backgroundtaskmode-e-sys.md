# BackgroundTaskMode

Main type of a continuous task. It is usually used together with the subtype [BackgroundTaskSubmode]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. For details, see the mapping table. The two types are newly added in API version 21 for [requesting]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and [updating]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ continuous tasks. When the main type of the continuous task is **MODE\_SPECIAL\_SCENARIO\_PROCESSING**, or that of a non-PC/2-in-1 device is **MODE\_TASK\_KEEPING**, you need to request the ACL permission \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ before calling APIs related to continuous tasks. In other scenarios, this permission is not required.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-backgroundTaskManager-export enum BackgroundTaskMode--><!--Device-backgroundTaskManager-export enum BackgroundTaskMode-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## MODE_ALLOW_WIFI_AWARE

```TypeScript
MODE_ALLOW_WIFI_AWARE = 7
```

WLAN-related services.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-BackgroundTaskMode-MODE_ALLOW_WIFI_AWARE = 7--><!--Device-BackgroundTaskMode-MODE_ALLOW_WIFI_AWARE = 7-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

