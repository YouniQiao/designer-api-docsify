# TransferProgress (System API)

搬迁任务的进度信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cloudSyncManager-interface TransferProgress--><!--Device-cloudSyncManager-interface TransferProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSyncManager } from 'kits/@kit.CoreFileKit';
```

## failedCount

```TypeScript
failedCount: int
```

搬迁失败的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-failedCount: int--><!--Device-TransferProgress-failedCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## state

```TypeScript
state: TransferState
```

搬迁任务的状态。

**Type:** [TransferState](arkts-corefile-cloudsyncmanager-transferstate-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-state: TransferState--><!--Device-TransferProgress-state: TransferState-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## stopReason

```TypeScript
stopReason: TransferStopReason
```

搬迁停止的原因。

**Type:** [TransferStopReason](arkts-corefile-cloudsyncmanager-transferstopreason-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-stopReason: TransferStopReason--><!--Device-TransferProgress-stopReason: TransferStopReason-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## successfulCount

```TypeScript
successfulCount: int
```

已搬迁的文件个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-successfulCount: int--><!--Device-TransferProgress-successfulCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## totalCount

```TypeScript
totalCount: int
```

待搬迁文件总个数，取值范围[0, INT32_MAX]，单位：个。进度异常时返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-totalCount: int--><!--Device-TransferProgress-totalCount: int-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## totalSize

```TypeScript
totalSize: long
```

需要搬迁的文件总大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-totalSize: long--><!--Device-TransferProgress-totalSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## transferredSize

```TypeScript
transferredSize: long
```

已搬迁的数据大小，取值范围[0, INT64_MAX)，单位：Byte。进度异常时返回INT64_MAX。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransferProgress-transferredSize: long--><!--Device-TransferProgress-transferredSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

