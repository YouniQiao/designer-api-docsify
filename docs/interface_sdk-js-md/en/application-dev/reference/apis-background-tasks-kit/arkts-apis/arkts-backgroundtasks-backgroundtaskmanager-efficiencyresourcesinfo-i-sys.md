# EfficiencyResourcesInfo (System API)

能效资源信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface EfficiencyResourcesInfo--><!--Device-backgroundTaskManager-interface EfficiencyResourcesInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## cpuLevel

```TypeScript
cpuLevel?: EfficiencyResourcesCpuLevel
```

指定CPU级别，能效资源类型resourceTypes为CPU时该参数用于指定CPU资源大小，系统会在负载空闲时间（例如灭屏场景）分配指定的CPU资源给应用。

**Type:** [EfficiencyResourcesCpuLevel](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcescpulevel-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EfficiencyResourcesInfo-cpuLevel?: EfficiencyResourcesCpuLevel--><!--Device-EfficiencyResourcesInfo-cpuLevel?: EfficiencyResourcesCpuLevel-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## isForProcess

```TypeScript
isForProcess: boolean
```

进程或应用申请，取值为true表示进程申请。取值为false表示应用申请。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-isForProcess: boolean--><!--Device-EfficiencyResourcesInfo-isForProcess: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## isPersistent

```TypeScript
isPersistent: boolean
```

是否永久持有资源，默认为false。取值为true表示永久持有。取值为false表示有限时间内持有。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-isPersistent: boolean--><!--Device-EfficiencyResourcesInfo-isPersistent: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## pid

```TypeScript
pid: int
```

应用进程的PID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-pid: int--><!--Device-EfficiencyResourcesInfo-pid: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## reason

```TypeScript
reason: string
```

申请资源原因。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-reason: string--><!--Device-EfficiencyResourcesInfo-reason: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## resourceTypes

```TypeScript
resourceTypes: int
```

能效资源类型。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-resourceTypes: int--><!--Device-EfficiencyResourcesInfo-resourceTypes: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## timeout

```TypeScript
timeout: int
```

超时时间，单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-timeout: int--><!--Device-EfficiencyResourcesInfo-timeout: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

应用的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-EfficiencyResourcesInfo-uid: int--><!--Device-EfficiencyResourcesInfo-uid: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

