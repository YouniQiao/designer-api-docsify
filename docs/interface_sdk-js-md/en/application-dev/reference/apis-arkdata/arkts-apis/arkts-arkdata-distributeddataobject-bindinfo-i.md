# BindInfo

数据库的绑定信息。当前版本只支持关系型数据库的绑定。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-interface BindInfo--><!--Device-distributedDataObject-interface BindInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## assetName

```TypeScript
assetName: string
```

待绑定资产在所属的数据库中的资产名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BindInfo-assetName: string--><!--Device-BindInfo-assetName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## field

```TypeScript
field: string
```

待绑定资产在所属的数据库中的列名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BindInfo-field: string--><!--Device-BindInfo-field: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## primaryKey

```TypeScript
primaryKey: commonType.ValuesBucket
```

待绑定资产在所属的数据库中的主键。

**Type:** commonType.ValuesBucket

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BindInfo-primaryKey: commonType.ValuesBucket--><!--Device-BindInfo-primaryKey: commonType.ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## storeName

```TypeScript
storeName: string
```

待绑定资产在所属的数据库中的库名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BindInfo-storeName: string--><!--Device-BindInfo-storeName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## tableName

```TypeScript
tableName: string
```

待绑定资产在所属的数据库中的表名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BindInfo-tableName: string--><!--Device-BindInfo-tableName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

