# CheckTriggerReason (System API)

```TypeScript
enum CheckTriggerReason
```

云盘校验触发原因的枚举值。

**Since:** 26.1.0

<!--Device-cloudSyncManager-enum CheckTriggerReason--><!--Device-cloudSyncManager-enum CheckTriggerReason-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## MANUAL

```TypeScript
MANUAL = 1
```

由云盘应用手动触发云盘校验。

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckTriggerReason-MANUAL = 1--><!--Device-CheckTriggerReason-MANUAL = 1-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## PERIODIC

```TypeScript
PERIODIC = 0
```

由周期性校验任务触发云盘校验。

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckTriggerReason-PERIODIC = 0--><!--Device-CheckTriggerReason-PERIODIC = 0-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.
