# Field (System API)

数据库中的字段结构。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface Field--><!--Device-cloudExtension-export interface Field-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## alias

```TypeScript
alias: string
```

该字段在服务器表中的别名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Field-alias: string--><!--Device-Field-alias: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## colName

```TypeScript
colName: string
```

列名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Field-colName: string--><!--Device-Field-colName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## nullable

```TypeScript
nullable: boolean
```

当前列是否允许为空值。true表示允许为空，false表示不允许为空。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Field-nullable: boolean--><!--Device-Field-nullable: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## primary

```TypeScript
primary: boolean
```

当前列是否为主键。true表示是主键，false表示不是主键。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Field-primary: boolean--><!--Device-Field-primary: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## type

```TypeScript
type: FieldType
```

字段类型。

**Type:** [FieldType](arkts-arkdata-cloudextension-fieldtype-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Field-type: FieldType--><!--Device-Field-type: FieldType-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

