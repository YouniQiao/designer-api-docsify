# BroadcastEvent

Defines a custom system event. You can use a common event API to obtain the event.

The upload and download SA has the **ohos.permission.SEND\_TASK\_COMPLETE\_EVENT** permission. You can configure the level-2 configuration file to which the metadata of an event points to intercept other event senders.

Use the **CommonEventData** type to transmit data related to common events. The members in **CommonEventData**  
are different from those described in [CommonEventData]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.Specifically, **CommonEventData.code** indicates the task status, which is **0x40 COMPLETE** or **0x41 FAILED**,and **CommonEventData.data** indicates the task ID.

\_\_\_MD\_COMMENT\_DESC\_USD\_2\_\_\_

For details about how to obtain the event configuration and configure the level-2 configuration file, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.\_\_\_MD\_COMMENT\_DESC\_USD\_3\_\_\_

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-agent-enum BroadcastEvent--><!--Device-agent-enum BroadcastEvent-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## COMPLETE

```TypeScript
COMPLETE = 'ohos.request.event.COMPLETE'
```

Task completion event. The returned event code can be **0x40** or **0x41**, depending on whether the task is successful or fails.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BroadcastEvent-COMPLETE = 'ohos.request.event.COMPLETE'--><!--Device-BroadcastEvent-COMPLETE = 'ohos.request.event.COMPLETE'-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

