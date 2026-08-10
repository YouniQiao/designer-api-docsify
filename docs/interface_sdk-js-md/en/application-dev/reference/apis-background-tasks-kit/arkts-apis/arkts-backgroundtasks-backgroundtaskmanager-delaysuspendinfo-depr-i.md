# DelaySuspendInfo

延迟挂起信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-depr-i.md)

<!--Device-backgroundTaskManager-interface DelaySuspendInfo--><!--Device-backgroundTaskManager-interface DelaySuspendInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## actualDelayTime

```TypeScript
actualDelayTime: number
```

应用的实际挂起延迟时间，单位：ms。

一般情况下默认值为180000，低电量（依据系统低电量广播）时默认值为60000。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.resourceschedule.backgroundTaskManager.DelaySuspendInfo

<!--Device-DelaySuspendInfo-actualDelayTime: number--><!--Device-DelaySuspendInfo-actualDelayTime: number-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## requestId

```TypeScript
requestId: number
```

延迟挂起的请求ID。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.resourceschedule.backgroundTaskManager.DelaySuspendInfo

<!--Device-DelaySuspendInfo-requestId: number--><!--Device-DelaySuspendInfo-requestId: number-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

