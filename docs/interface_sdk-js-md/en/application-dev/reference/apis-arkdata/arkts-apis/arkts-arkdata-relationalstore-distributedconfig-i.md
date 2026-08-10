# DistributedConfig

记录表的分布式配置信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface DistributedConfig--><!--Device-relationalStore-interface DistributedConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## assetConflictPolicy

```TypeScript
assetConflictPolicy?: AssetConflictPolicy
```

资产冲突策略。默认值为CONFLICT_POLICY_DEFAULT。

**Type:** [AssetConflictPolicy](arkts-arkdata-relationalstore-assetconflictpolicy-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedConfig-assetConflictPolicy?: AssetConflictPolicy--><!--Device-DistributedConfig-assetConflictPolicy?: AssetConflictPolicy-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## assetDownloadOnDemand

```TypeScript
assetDownloadOnDemand?: boolean
```

是否按需下载资产。true表示仅下行数据到本地，当需要下载资产时，调用[cloudSyncEx](arkts-arkdata-relationalstore-rdbstore-i.md#cloudsyncex)接口触发资产下载；false表示数据与资产都下行到本地。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedConfig-assetDownloadOnDemand?: boolean--><!--Device-DistributedConfig-assetDownloadOnDemand?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## assetTempPath

```TypeScript
assetTempPath?: string
```

资产临时路径。仅当assetConflictPolicy值为CONFLICT_POLICY_TEMP_PATH时生效，需指定为  
[distributedfiles](../../../file-management/app-sandbox-directory.md#应用文件目录与应用文件路径)下的临时路径，格式示例：tmp/，若未填写或路径不合规，将抛出 401 错误码。默认值为空。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedConfig-assetTempPath?: string--><!--Device-DistributedConfig-assetTempPath?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## asyncDownloadAsset

```TypeScript
asyncDownloadAsset?: boolean
```

表示当前数据库在端云同步时，同步或异步下载资产。true表示优先下载完所有数据后，使用异步任务下载资产；false表示同步下载资产；默认值为false。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-asyncDownloadAsset?: boolean--><!--Device-DistributedConfig-asyncDownloadAsset?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## autoSync

```TypeScript
autoSync: boolean
```

表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用  
[cloudSync](arkts-arkdata-relationalstore-rdbstore-i.md#cloudsync)接口触发端云同步。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-autoSync: boolean--><!--Device-DistributedConfig-autoSync: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## autoSyncSwitch

```TypeScript
autoSyncSwitch?: boolean
```

是否启用自动同步开关。true表示启用自动同步，false表示不启用。默认值为true。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedConfig-autoSyncSwitch?: boolean--><!--Device-DistributedConfig-autoSyncSwitch?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## enableCloud

```TypeScript
enableCloud?: boolean
```

表示当前数据库是否允许端云同步。true表示允许端云同步；false表示不允许端云同步。默认值为true。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-enableCloud?: boolean--><!--Device-DistributedConfig-enableCloud?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## tableType

```TypeScript
tableType?: DistributedTableType
```

分布式表类型。DEVICE_COLLABORATION表示设备协作表；SINGLE_VERSION表示单版本表。跨设备数据同步时，默认值为DEVICE_COLLABORATION；端云数据同步时，默认值为SINGLE_VERSION，不支持DEVICE_COLLABORATION。

**Type:** [DistributedTableType](arkts-arkdata-relationalstore-distributedtabletype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DistributedConfig-tableType?: DistributedTableType--><!--Device-DistributedConfig-tableType?: DistributedTableType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

