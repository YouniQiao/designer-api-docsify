# ChangeInfo

记录端云同步过程详情。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface ChangeInfo--><!--Device-relationalStore-interface ChangeInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## deleted

```TypeScript
deleted: Array<string> | Array<long>
```

记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。

**Type:** ArkTS-Dyn: Array&lt;string&gt; \| Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;string&gt; \| Array&lt;long&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ChangeInfo-deleted: Array<string> | Array<long>--><!--Device-ChangeInfo-deleted: Array<string> | Array<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## inserted

```TypeScript
inserted: Array<string> | Array<long>
```

记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。

**Type:** ArkTS-Dyn: Array&lt;string&gt; \| Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;string&gt; \| Array&lt;long&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ChangeInfo-inserted: Array<string> | Array<long>--><!--Device-ChangeInfo-inserted: Array<string> | Array<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## table

```TypeScript
table: string
```

表示发生变化的表的名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ChangeInfo-table: string--><!--Device-ChangeInfo-table: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## type

```TypeScript
type: ChangeType
```

表示发生变化的数据的类型，数据或者资产附件发生变化。

**Type:** [ChangeType](arkts-arkdata-relationalstore-changetype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ChangeInfo-type: ChangeType--><!--Device-ChangeInfo-type: ChangeType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## updated

```TypeScript
updated: Array<string> | Array<long>
```

记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。

**Type:** ArkTS-Dyn: Array&lt;string&gt; \| Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;string&gt; \| Array&lt;long&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ChangeInfo-updated: Array<string> | Array<long>--><!--Device-ChangeInfo-updated: Array<string> | Array<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

