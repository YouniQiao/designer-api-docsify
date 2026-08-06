# DistributedConfig

Defines a struct for distributed configuration of a table.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface DistributedConfig--><!--Device-relationalStore-interface DistributedConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## assetConflictPolicy

```TypeScript
assetConflictPolicy?: AssetConflictPolicy
```

Specifies the asset conflict policy.

**Type:** AssetConflictPolicy

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedConfig-assetConflictPolicy?: AssetConflictPolicy--><!--Device-DistributedConfig-assetConflictPolicy?: AssetConflictPolicy-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## assetDownloadOnDemand

```TypeScript
assetDownloadOnDemand?: boolean
```

Specifies whether to download assets on demand.

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

Specifies the asset temp path.

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

Whether to download assets synchronously or asynchronously when device-cloud sync is being performed for the current RDB store. The value **true** means to use an asynchronous task to download assets after all data is downloaded; **false** means to download assets synchronously.

Default value: **false**.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-asyncDownloadAsset?: boolean--><!--Device-DistributedConfig-asyncDownloadAsset?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## autoSync

```TypeScript
autoSync: boolean
```

Whether the table supports automatic device-cloud synchronization. If the value is **true**, the system can automatically trigger device-cloud sync. If the value is **false**, the system cannot automatically trigger device-cloud sync, and the [cloudSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_API needs to be called to trigger device-cloud sync.

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-autoSync: boolean--><!--Device-DistributedConfig-autoSync: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## autoSyncSwitch

```TypeScript
autoSyncSwitch?: boolean
```

Specifies the auto synchronization switch.

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

Whether to enable device-cloud sync for this RDB store. The value **true** means to enable device-cloud sync;  
**false** means the opposite. The default value is **true**.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DistributedConfig-enableCloud?: boolean--><!--Device-DistributedConfig-enableCloud?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## tableType

```TypeScript
tableType?: DistributedTableType
```

Distributed table type. **DEVICE\_COLLABORATION** indicates the device collaboration table, and **SINGLE\_VERSION**  
indicates the single version table. For cross-device data sync, the default value is **DEVICE\_COLLABORATION**.For device-cloud data sync, the default value is **SINGLE\_VERSION**, and **DEVICE\_COLLABORATION** is not supported.

**Type:** DistributedTableType

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DistributedConfig-tableType?: DistributedTableType--><!--Device-DistributedConfig-tableType?: DistributedTableType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

