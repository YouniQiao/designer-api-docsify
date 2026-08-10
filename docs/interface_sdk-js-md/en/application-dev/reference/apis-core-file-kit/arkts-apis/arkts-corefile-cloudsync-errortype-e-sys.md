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

## RESPONSE_TIME_OUT

```TypeScript
RESPONSE_TIME_OUT = 9
```

云服务超时。

26.0.0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ErrorType-RESPONSE_TIME_OUT = 9--><!--Device-ErrorType-RESPONSE_TIME_OUT = 9-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## UNKNOWN_ERROR

```TypeScript
UNKNOWN_ERROR = 10
```

未知错误。

26.0.0

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ErrorType-UNKNOWN_ERROR = 10--><!--Device-ErrorType-UNKNOWN_ERROR = 10-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

