# HistoryVersion

端云文件历史版本信息，调用端云文件版本管理类[FileVersion](arkts-corefile-cloudsync-fileversion-c.md)的  
[gethistoryversionlist](arkts-corefile-cloudsync-fileversion-c.md#gethistoryversionlist)方法时，历史版本列表中的属性。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cloudSync-interface HistoryVersion--><!--Device-cloudSync-interface HistoryVersion-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## autoResolved

```TypeScript
autoResolved: boolean
```

当前版本是否为自动解决冲突的版本。

应用设置手动解冲突时，默认返回false，无意义。

应用设置自动解冲突时，端侧会自动解冲突，true表示当前版本存在冲突，端云服务已自动解决冲突，false表示无冲突，未自动解冲突。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-autoResolved: boolean--><!--Device-HistoryVersion-autoResolved: boolean-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## editedTime

```TypeScript
editedTime: long
```

文件内容修改的时间戳，单位：ms。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-editedTime: long--><!--Device-HistoryVersion-editedTime: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## fileSize

```TypeScript
fileSize: long
```

文件大小，单位：Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-fileSize: long--><!--Device-HistoryVersion-fileSize: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## originalFileName

```TypeScript
originalFileName: string
```

当前版本对应的文件名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-originalFileName: string--><!--Device-HistoryVersion-originalFileName: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## sha256

```TypeScript
sha256: string
```

当前版本对应文件内容的哈希值。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-sha256: string--><!--Device-HistoryVersion-sha256: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## versionId

```TypeScript
versionId: string
```

文件版本号。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HistoryVersion-versionId: string--><!--Device-HistoryVersion-versionId: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

