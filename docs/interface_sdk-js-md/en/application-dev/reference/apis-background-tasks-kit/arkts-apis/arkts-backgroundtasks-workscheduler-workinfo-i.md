# WorkInfo

Represents the deferred task information, which is used to set the trigger condition.

**Since:** 23

<!--Device-workScheduler-export interface WorkInfo--><!--Device-workScheduler-export interface WorkInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## abilityName

```TypeScript
abilityName: string
```

Ability name in the bundle.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-abilityName: string--><!--Device-WorkInfo-abilityName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## batteryLevel

```TypeScript
batteryLevel?: int
```

Battery level.Value range: [0, 100]

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-batteryLevel?: int--><!--Device-WorkInfo-batteryLevel?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## batteryStatus

```TypeScript
batteryStatus?: BatteryStatus
```

Battery status.

**Type:** [BatteryStatus](arkts-backgroundtasks-workscheduler-batterystatus-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-batteryStatus?: BatteryStatus--><!--Device-WorkInfo-batteryStatus?: BatteryStatus-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application where the deferred task is located.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-bundleName: string--><!--Device-WorkInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## chargerType

```TypeScript
chargerType?: ChargingType
```

Charging type.

**Type:** [ChargingType](arkts-backgroundtasks-workscheduler-chargingtype-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-chargerType?: ChargingType--><!--Device-WorkInfo-chargerType?: ChargingType-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## earliestStartTime

```TypeScript
earliestStartTime?: int
```

Interval between the initial execution time and the request time for a task, in milliseconds. The default value is **0**, and the value must be greater than or equal to 0. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-earliestStartTime?: int--><!--Device-WorkInfo-earliestStartTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## idleWaitTime

```TypeScript
idleWaitTime?: int
```

Idle wait time, in milliseconds.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-idleWaitTime?: int--><!--Device-WorkInfo-idleWaitTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isCharging

```TypeScript
isCharging?: boolean
```

Whether the device needs to enter the charging state. The default value is **false**.  
- **true**: The device needs to enter the charging state to trigger deferred task scheduling. - **false**: The device does not need to enter the charging state to trigger deferred task scheduling.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isCharging?: boolean--><!--Device-WorkInfo-isCharging?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isDeepIdle

```TypeScript
isDeepIdle?: boolean
```

Whether the device needs to enter the idle state to trigger deferred task scheduling. The default value is **false**.  
- **true**: The device needs to enter the idle state to trigger deferred task scheduling. - **false**: The device does not need to enter the idle state to trigger deferred task scheduling.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isDeepIdle?: boolean--><!--Device-WorkInfo-isDeepIdle?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isPersisted

```TypeScript
isPersisted?: boolean
```

Whether the registered deferred task can be saved in the system. The default value is **false**.  
- **true**: The task can be saved. That is, the task can be restored after the system restarts. - **false**: The task cannot be saved.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isPersisted?: boolean--><!--Device-WorkInfo-isPersisted?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isRepeat

```TypeScript
isRepeat?: boolean
```

Whether the task is repeated. The default value is **false**.  
- **true**: The task is repeated. - **false**: The task is not repeated.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isRepeat?: boolean--><!--Device-WorkInfo-isRepeat?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## networkType

```TypeScript
networkType?: NetworkType
```

Network type.

**Type:** NetworkType

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-networkType?: NetworkType--><!--Device-WorkInfo-networkType?: NetworkType-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## parameters

```TypeScript
parameters?: Record<string, int | double | string | boolean>
```

Carried parameters.

**Type:** Record&lt;string, int \| double \| string \| boolean&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-parameters?: Record<string, int | double | string | boolean>--><!--Device-WorkInfo-parameters?: Record<string, int | double | string | boolean>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## repeatCount

```TypeScript
repeatCount?: int
```

Number of repeat times.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-repeatCount?: int--><!--Device-WorkInfo-repeatCount?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## repeatCycleTime

```TypeScript
repeatCycleTime?: int
```

Repeat interval, in milliseconds.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-repeatCycleTime?: int--><!--Device-WorkInfo-repeatCycleTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## storageRequest

```TypeScript
storageRequest?: StorageRequest
```

Storage status.

**Type:** [StorageRequest](arkts-backgroundtasks-workscheduler-storagerequest-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-storageRequest?: StorageRequest--><!--Device-WorkInfo-storageRequest?: StorageRequest-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## workId

```TypeScript
workId: int
```

ID of the deferred task.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-workId: int--><!--Device-WorkInfo-workId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

