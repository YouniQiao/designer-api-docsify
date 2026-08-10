# CloudAsset (System API)

云资产的信息。

**Inheritance/Implementation:** CloudAsset extends [relationalStore.Asset](arkts-arkdata-relationalstore-asset-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface CloudAsset extends relationalStore.Asset--><!--Device-cloudExtension-export interface CloudAsset extends relationalStore.Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## assetId

```TypeScript
assetId: string
```

资产ID。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudAsset-assetId: string--><!--Device-CloudAsset-assetId: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## hash

```TypeScript
hash: string
```

资产的修改时间和大小转换成的哈希值。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudAsset-hash: string--><!--Device-CloudAsset-hash: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

