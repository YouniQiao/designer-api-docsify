# Reference (System API)

记录表之间通过表字段指定的关联关系。其中表a关联到表b，称a为b关联的子表，b为a关联的父表。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface Reference--><!--Device-relationalStore-interface Reference-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## refFields

```TypeScript
refFields: Record<string, string>
```

表示关联表的关联字段。键值数据中键为子表字段，值为父表字段。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Reference-refFields: Record<string, string>--><!--Device-Reference-refFields: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## sourceTable

```TypeScript
sourceTable: string
```

关联的子表名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Reference-sourceTable: string--><!--Device-Reference-sourceTable: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## targetTable

```TypeScript
targetTable: string
```

关联的父表名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Reference-targetTable: string--><!--Device-Reference-targetTable: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

