# ChangeData

定义变更数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cloudSync-interface ChangeData--><!--Device-cloudSync-interface ChangeData-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## isDirectory

```TypeScript
isDirectory: Array<boolean>
```

指示更改的URI是否为目录。true：是目录。false：非目录。

**Type:** Array&lt;boolean&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ChangeData-isDirectory: Array<boolean>--><!--Device-ChangeData-isDirectory: Array<boolean>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## type

```TypeScript
type: NotifyType
```

更改的通知类型。

**Type:** [NotifyType](arkts-corefile-cloudsync-notifytype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ChangeData-type: NotifyType--><!--Device-ChangeData-type: NotifyType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## uris

```TypeScript
uris: Array<string>
```

需要更改的URI列表。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ChangeData-uris: Array<string>--><!--Device-ChangeData-uris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

