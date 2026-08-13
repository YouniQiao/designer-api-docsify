# StoreConfig

Defines the RDB store configuration.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-relationalStore-interface StoreConfig--><!--Device-relationalStore-interface StoreConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## autoCleanDeviceDirtyData

```TypeScript
autoCleanDeviceDirtyData?: boolean
```

Specifies whether to clean up dirty data that is synchronized to the local but deleted on the remote device. &lt;br&gt;Default value:true.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StoreConfig-autoCleanDeviceDirtyData?: boolean--><!--Device-StoreConfig-autoCleanDeviceDirtyData?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## haMode

```TypeScript
haMode?: HAMode
```

Enumerates the high availability modes of the RDB store.

**Type:** [HAMode](arkts-arkdata-relationalstore-hamode-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-StoreConfig-haMode?: HAMode--><!--Device-StoreConfig-haMode?: HAMode-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## isSearchable

```TypeScript
isSearchable?: boolean
```

Specifies whether data can be searched.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-StoreConfig-isSearchable?: boolean--><!--Device-StoreConfig-isSearchable?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

