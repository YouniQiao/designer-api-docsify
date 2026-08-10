# ErrorType

端云同步失败类型，为枚举类型。

- 当前阶段，同步过程中，当开启无限量使用移动数据网络，移动数据网络和WIFI均不可用时，才会返回NETWORK_UNAVAILABLE；开启无限量使用移动数据网络，若有一种类型网络可用，则能正常同步。  
- 同步过程中，非充电场景下，电量低于10%，完成当前批上行同步后停止同步，返回低电量；  
- 触发同步时，非充电场景下，若电量低于10%，则不允许同步  
- 上行时，若云端空间不足，则文件上行失败，云端无该文件记录。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-cloudSync-enum ErrorType--><!--Device-cloudSync-enum ErrorType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## NO_ERROR

```TypeScript
NO_ERROR = 0
```

没有错误。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-NO_ERROR = 0--><!--Device-ErrorType-NO_ERROR = 0-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## NETWORK_UNAVAILABLE

```TypeScript
NETWORK_UNAVAILABLE = 1
```

所有网络不可用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-NETWORK_UNAVAILABLE = 1--><!--Device-ErrorType-NETWORK_UNAVAILABLE = 1-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## WIFI_UNAVAILABLE

```TypeScript
WIFI_UNAVAILABLE = 2
```

WIFI不可用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-WIFI_UNAVAILABLE = 2--><!--Device-ErrorType-WIFI_UNAVAILABLE = 2-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## BATTERY_LEVEL_LOW

```TypeScript
BATTERY_LEVEL_LOW = 3
```

低电量（低于10%）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-BATTERY_LEVEL_LOW = 3--><!--Device-ErrorType-BATTERY_LEVEL_LOW = 3-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## BATTERY_LEVEL_WARNING

```TypeScript
BATTERY_LEVEL_WARNING = 4
```

告警电量（低于15%）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-BATTERY_LEVEL_WARNING = 4--><!--Device-ErrorType-BATTERY_LEVEL_WARNING = 4-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## CLOUD_STORAGE_FULL

```TypeScript
CLOUD_STORAGE_FULL = 5
```

云端空间不足。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-CLOUD_STORAGE_FULL = 5--><!--Device-ErrorType-CLOUD_STORAGE_FULL = 5-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## LOCAL_STORAGE_FULL

```TypeScript
LOCAL_STORAGE_FULL = 6
```

本地空间不足。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-LOCAL_STORAGE_FULL = 6--><!--Device-ErrorType-LOCAL_STORAGE_FULL = 6-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## DEVICE_TEMPERATURE_TOO_HIGH

```TypeScript
DEVICE_TEMPERATURE_TOO_HIGH = 7
```

设备温度过高。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ErrorType-DEVICE_TEMPERATURE_TOO_HIGH = 7--><!--Device-ErrorType-DEVICE_TEMPERATURE_TOO_HIGH = 7-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## REMOTE_SERVER_ABNORMAL

```TypeScript
REMOTE_SERVER_ABNORMAL = 8
```

远端服务不可用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ErrorType-REMOTE_SERVER_ABNORMAL = 8--><!--Device-ErrorType-REMOTE_SERVER_ABNORMAL = 8-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

