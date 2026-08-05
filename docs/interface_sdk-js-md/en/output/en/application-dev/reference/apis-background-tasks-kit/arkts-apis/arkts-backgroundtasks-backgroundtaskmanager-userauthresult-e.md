# UserAuthResult

Represents the user authorization result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-backgroundTaskManager-export enum UserAuthResult--><!--Device-backgroundTaskManager-export enum UserAuthResult-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## NOT_SUPPORTED

```TypeScript
NOT_SUPPORTED = 0
```

The authorization is not supported. For example, if the main type of the requested continuous task is not **MODE\_SPECIAL\_SCENARIO\_PROCESSING**, continuous task running in the background is not supported.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-UserAuthResult-NOT_SUPPORTED = 0--><!--Device-UserAuthResult-NOT_SUPPORTED = 0-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## NOT_DETERMINED

```TypeScript
NOT_DETERMINED = 1
```

No user operation.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-UserAuthResult-NOT_DETERMINED = 1--><!--Device-UserAuthResult-NOT_DETERMINED = 1-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## DENIED

```TypeScript
DENIED = 2
```

The authorization is denied.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-UserAuthResult-DENIED = 2--><!--Device-UserAuthResult-DENIED = 2-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## GRANTED_ONCE

```TypeScript
GRANTED_ONCE = 3
```

The authorization is granted this time. Note: The authorization record will be cleared when the application exits.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-UserAuthResult-GRANTED_ONCE = 3--><!--Device-UserAuthResult-GRANTED_ONCE = 3-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## GRANTED_ALWAYS

```TypeScript
GRANTED_ALWAYS = 4
```

The authorization is granted always. **NOTE** When the following common events are received, the related authorization records will be cleared: \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ , \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ , \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ , \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ , \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ .

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-UserAuthResult-GRANTED_ALWAYS = 4--><!--Device-UserAuthResult-GRANTED_ALWAYS = 4-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

