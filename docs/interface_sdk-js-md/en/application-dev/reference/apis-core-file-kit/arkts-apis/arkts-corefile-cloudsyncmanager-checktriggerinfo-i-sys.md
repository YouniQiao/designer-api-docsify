# CheckTriggerInfo (System API)

```TypeScript
interface CheckTriggerInfo
```

表示已完成的云盘校验的触发者及触发原因。

**Since:** 26.1.0

<!--Device-cloudSyncManager-interface CheckTriggerInfo--><!--Device-cloudSyncManager-interface CheckTriggerInfo-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## bundleName

```TypeScript
bundleName: string
```

被校验云文件的应用包名。

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckTriggerInfo-bundleName: string--><!--Device-CheckTriggerInfo-bundleName: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## reason

```TypeScript
reason: CheckTriggerReason
```

触发云盘校验的原因。

**Type:** [CheckTriggerReason](arkts-corefile-cloudsyncmanager-checktriggerreason-e-sys.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckTriggerInfo-reason: CheckTriggerReason--><!--Device-CheckTriggerInfo-reason: CheckTriggerReason-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## triggerBundleName

```TypeScript
triggerBundleName: string
```

触发云盘校验的应用包名。

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckTriggerInfo-triggerBundleName: string--><!--Device-CheckTriggerInfo-triggerBundleName: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.
