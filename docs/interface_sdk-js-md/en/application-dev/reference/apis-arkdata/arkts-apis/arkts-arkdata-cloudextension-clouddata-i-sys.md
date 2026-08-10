# CloudData (System API)

云数据。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface CloudData--><!--Device-cloudExtension-export interface CloudData-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## hasMore

```TypeScript
hasMore: boolean
```

服务器是否存在更多数据可供查询。true表示服务器上还有数据等待查询，false表示服务器上不存在可查询的数据。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudData-hasMore: boolean--><!--Device-CloudData-hasMore: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## nextCursor

```TypeScript
nextCursor: string
```

查询游标。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudData-nextCursor: string--><!--Device-CloudData-nextCursor: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## values

```TypeScript
values: Array<Record<string, CloudType>>
```

需要查询数据的数组，包括数据记录的实际值和ExtensionValue（扩展值）。

**Type:** Array&lt;Record&lt;string, CloudType&gt;&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudData-values: Array<Record<string, CloudType>>--><!--Device-CloudData-values: Array<Record<string, CloudType>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

