# DataProxyErrorCode

配置共享批量操作返回值的状态码枚举。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-enum DataProxyErrorCode--><!--Device-dataShare-enum DataProxyErrorCode-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## SUCCESS

```TypeScript
SUCCESS = 0
```

表示操作成功。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyErrorCode-SUCCESS = 0--><!--Device-DataProxyErrorCode-SUCCESS = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## URI_NOT_EXIST

```TypeScript
URI_NOT_EXIST = 1
```

URI不存在或取消订阅一个未订阅过的URI。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyErrorCode-URI_NOT_EXIST = 1--><!--Device-DataProxyErrorCode-URI_NOT_EXIST = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## NO_PERMISSION

```TypeScript
NO_PERMISSION = 2
```

没有权限在该URI上执行此操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyErrorCode-NO_PERMISSION = 2--><!--Device-DataProxyErrorCode-NO_PERMISSION = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## OVER_LIMIT

```TypeScript
OVER_LIMIT = 3
```

API版本26.0.0之前，表示当前应用发布的配置超过32个配置的上限；从API版本26.0.0开始，表示当前应用发布的配置超过64个配置的上限或获取的共享配置项的值超出  
[DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md)中maxValueLength字段配置的最大长度限制。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyErrorCode-OVER_LIMIT = 3--><!--Device-DataProxyErrorCode-OVER_LIMIT = 3-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

