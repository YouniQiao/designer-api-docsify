# DistributedTableType

分布式表类型的枚举。请使用枚举名称而非枚举值。此配置项为数据库级配置，如果数据库中有多张分布式表，则所有表必须使用相同的分布式表类型，且不支持切换升级。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-relationalStore-enum DistributedTableType--><!--Device-relationalStore-enum DistributedTableType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## DEVICE_COLLABORATION

```TypeScript
DEVICE_COLLABORATION = 0
```

多设备协同表，各设备的数据将被隔离存储在独立的分布式表中，而非写入本地表，分布式表名为在原来表名前拼接对端设备的DeviceID标识符。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedTableType-DEVICE_COLLABORATION = 0--><!--Device-DistributedTableType-DEVICE_COLLABORATION = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## SINGLE_VERSION

```TypeScript
SINGLE_VERSION = 1
```

单版本表，数据通过分布式数据管理框架直接写入对端设备的本地表中。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedTableType-SINGLE_VERSION = 1--><!--Device-DistributedTableType-SINGLE_VERSION = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

