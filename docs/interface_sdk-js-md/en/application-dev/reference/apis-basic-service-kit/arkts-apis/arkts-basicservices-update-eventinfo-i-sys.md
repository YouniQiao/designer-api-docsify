# EventInfo (System API)

Defines an **EventInfo** object, which is used to receive the event details transferred by upgrade event notification. The object contains the **eventId** and **taskBody** fields. **eventId** indicates the event ID,which identifies the event type; **taskBody** indicates the task data, which contains the task status and progress.

Use scenarios: After an event listener is registered by calling **on**, the callback function receives an  
**EventInfo** object when an event occurs. The real-time status and progress of the upgrade task can be obtained by parsing **eventId** and **taskBody**, which can be used to monitor the upgrade process in real time.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface EventInfo--><!--Device-update-export interface EventInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## eventId

```TypeScript
eventId: EventId
```

Event ID, which identifies the upgrade event type. You can determine the specific event based on **eventId** and take corresponding actions. For example, **EVENT\_DOWNLOAD\_START** indicates that the download starts, and  
**EVENT\_UPGRADE\_SUCCESS** indicates that the upgrade is successful.

Common event types include download events (such as **EVENT\_DOWNLOAD\_START**), upgrade events (such as  
**EVENT\_UPGRADE\_START**), and completion events (such as **EVENT\_UPGRADE\_SUCCESS** and **EVENT\_UPGRADE\_FAIL**).You are advised to execute different service logic based on **eventId** in the event callback.

**Type:** EventId

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-EventInfo-eventId: EventId--><!--Device-EventInfo-eventId: EventId-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## taskBody

```TypeScript
taskBody: TaskBody
```

Represents task data.

**Type:** TaskBody

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-EventInfo-taskBody: TaskBody--><!--Device-EventInfo-taskBody: TaskBody-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

