# WorkInfo

延迟任务的具体信息, 用于设置延迟任务的触发条件等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-workScheduler-export interface WorkInfo--><!--Device-workScheduler-export interface WorkInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## abilityName

```TypeScript
abilityName: string
```

包内ability名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-abilityName: string--><!--Device-WorkInfo-abilityName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## batteryLevel

```TypeScript
batteryLevel?: int
```

电量。

取值范围：[0, 100]

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-batteryLevel?: int--><!--Device-WorkInfo-batteryLevel?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## batteryStatus

```TypeScript
batteryStatus?: BatteryStatus
```

电池状态。

**Type:** [BatteryStatus](arkts-backgroundtasks-workscheduler-batterystatus-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-batteryStatus?: BatteryStatus--><!--Device-WorkInfo-batteryStatus?: BatteryStatus-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## bundleName

```TypeScript
bundleName: string
```

延迟任务所在应用的包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-bundleName: string--><!--Device-WorkInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## chargerType

```TypeScript
chargerType?: ChargingType
```

充电类型。

**Type:** [ChargingType](arkts-backgroundtasks-workscheduler-chargingtype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-chargerType?: ChargingType--><!--Device-WorkInfo-chargerType?: ChargingType-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## earliestStartTime

```TypeScript
earliestStartTime?: int
```

任务首次执行时间距离任务申请时间的间隔，单位：ms，默认为0，范围大于等于0。取值范围为全体整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-earliestStartTime?: int--><!--Device-WorkInfo-earliestStartTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## idleWaitTime

```TypeScript
idleWaitTime?: int
```

空闲等待时间，单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-idleWaitTime?: int--><!--Device-WorkInfo-idleWaitTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isCharging

```TypeScript
isCharging?: boolean
```

是否充电，默认为false。

- true表示充电触发延迟任务回调。  
- false表示不充电触发延迟任务回调。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isCharging?: boolean--><!--Device-WorkInfo-isCharging?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isDeepIdle

```TypeScript
isDeepIdle?: boolean
```

是否要求设备进入空闲状态，默认为false。

- true表示需要。  
- false表示不需要。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isDeepIdle?: boolean--><!--Device-WorkInfo-isDeepIdle?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isPersisted

```TypeScript
isPersisted?: boolean
```

注册的延迟任务是否可保存在系统中，默认为false。

- true表示可保存，即系统重启后，任务可恢复。  
- false表示不可保存。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isPersisted?: boolean--><!--Device-WorkInfo-isPersisted?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## isRepeat

```TypeScript
isRepeat?: boolean
```

是否循环任务，默认为false。

- true表示循环任务。  
- false表示非循环任务。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-isRepeat?: boolean--><!--Device-WorkInfo-isRepeat?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## networkType

```TypeScript
networkType?: NetworkType
```

网络类型。

**Type:** [NetworkType](arkts-backgroundtasks-workscheduler-networktype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-networkType?: NetworkType--><!--Device-WorkInfo-networkType?: NetworkType-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## parameters

```TypeScript
parameters?: Record<string, int | double | string | boolean>
```

携带参数信息。

**Type:** ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| number \| string \| boolean&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, int \| double \| string \| boolean&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-parameters?: Record<string, int | double | string | boolean>--><!--Device-WorkInfo-parameters?: Record<string, int | double | string | boolean>-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## repeatCount

```TypeScript
repeatCount?: int
```

循环次数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-repeatCount?: int--><!--Device-WorkInfo-repeatCount?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## repeatCycleTime

```TypeScript
repeatCycleTime?: int
```

循环间隔，单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-repeatCycleTime?: int--><!--Device-WorkInfo-repeatCycleTime?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## storageRequest

```TypeScript
storageRequest?: StorageRequest
```

存储状态。

**Type:** [StorageRequest](arkts-backgroundtasks-workscheduler-storagerequest-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-storageRequest?: StorageRequest--><!--Device-WorkInfo-storageRequest?: StorageRequest-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## workId

```TypeScript
workId: int
```

延迟任务ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WorkInfo-workId: int--><!--Device-WorkInfo-workId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

