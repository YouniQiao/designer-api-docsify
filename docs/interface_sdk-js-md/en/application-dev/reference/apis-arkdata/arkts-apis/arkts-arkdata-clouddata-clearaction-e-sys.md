# ClearAction (System API)

清除本地下载的云端数据的行为枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cloudData-enum ClearAction--><!--Device-cloudData-enum ClearAction-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## CLEAR_CLOUD_INFO

```TypeScript
CLEAR_CLOUD_INFO = 0
```

清除从云端下载的数据的云标识（即数据来源于云端的标记信息），相关数据作为本地数据保存。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ClearAction-CLEAR_CLOUD_INFO = 0--><!--Device-ClearAction-CLEAR_CLOUD_INFO = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## CLEAR_CLOUD_DATA_AND_INFO

```TypeScript
CLEAR_CLOUD_DATA_AND_INFO = 1
```

清除从云端下载的数据，不包括本地已修改的云端数据。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ClearAction-CLEAR_CLOUD_DATA_AND_INFO = 1--><!--Device-ClearAction-CLEAR_CLOUD_DATA_AND_INFO = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## CLEAR_CLOUD_NONE

```TypeScript
CLEAR_CLOUD_NONE = 2
```

不执行任何清除操作。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ClearAction-CLEAR_CLOUD_NONE = 2--><!--Device-ClearAction-CLEAR_CLOUD_NONE = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

