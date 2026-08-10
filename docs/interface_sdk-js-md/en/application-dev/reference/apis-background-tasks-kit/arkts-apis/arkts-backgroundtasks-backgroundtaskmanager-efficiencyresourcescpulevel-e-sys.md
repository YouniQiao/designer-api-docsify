# EfficiencyResourcesCpuLevel (System API)

能效资源CPU级别。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-backgroundTaskManager-export enum EfficiencyResourcesCpuLevel--><!--Device-backgroundTaskManager-export enum EfficiencyResourcesCpuLevel-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## SMALL_CPU

```TypeScript
SMALL_CPU = 0
```

表示运行在小核，用于处理轻量级后台任务，CPU频点较低。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EfficiencyResourcesCpuLevel-SMALL_CPU = 0--><!--Device-EfficiencyResourcesCpuLevel-SMALL_CPU = 0-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## MEDIUM_CPU

```TypeScript
MEDIUM_CPU = 1
```

表示最高可以运行在中核，系统基于负载决策运行在小核或中核。平衡性能与能效，用于需要处理复杂任务的场景，CPU频点高。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EfficiencyResourcesCpuLevel-MEDIUM_CPU = 1--><!--Device-EfficiencyResourcesCpuLevel-MEDIUM_CPU = 1-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

## LARGE_CPU

```TypeScript
LARGE_CPU = 2
```

表示最高可以运行在大核，系统基于负载决策运行在小核、中核或大核。 极致性能，用于应对重载任务的场景，CPU频点最高。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EfficiencyResourcesCpuLevel-LARGE_CPU = 2--><!--Device-EfficiencyResourcesCpuLevel-LARGE_CPU = 2-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**System API:** This is a system API.

