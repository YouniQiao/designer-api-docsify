# Action (System API)

清理本地云相关数据时的Action，为枚举类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cloudSyncManager-enum Action--><!--Device-cloudSyncManager-enum Action-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## RETAIN_DATA

```TypeScript
RETAIN_DATA = 0
```

仅清除云端标识，保留本地缓存文件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Action-RETAIN_DATA = 0--><!--Device-Action-RETAIN_DATA = 0-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

## CLEAR_DATA

```TypeScript
CLEAR_DATA = 1
```

清除云端标识信息，若存在本地缓存文件，一并删除。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Action-CLEAR_DATA = 1--><!--Device-Action-CLEAR_DATA = 1-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

