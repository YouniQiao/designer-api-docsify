# CloudData (System API)

Represents the cloud data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cloudExtension-export interface CloudData--><!--Device-cloudExtension-export interface CloudData-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'cloudExtension';
```

## hasMore

```TypeScript
hasMore: boolean
```

Whether there is data to be queried on the server. The value true means there is data to be queried on the server; the value false means the opposite.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CloudData-hasMore: boolean--><!--Device-CloudData-hasMore: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## nextCursor

```TypeScript
nextCursor: string
```

Cursor for data query.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CloudData-nextCursor: string--><!--Device-CloudData-nextCursor: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## values

```TypeScript
values: Array<Record<string, CloudType>>
```

Array of data to be queried, which consists of the data value and ExtensionValue.

**Type:** Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CloudData-values: Array<Record<string, CloudType>>--><!--Device-CloudData-values: Array<Record<string, CloudType>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

