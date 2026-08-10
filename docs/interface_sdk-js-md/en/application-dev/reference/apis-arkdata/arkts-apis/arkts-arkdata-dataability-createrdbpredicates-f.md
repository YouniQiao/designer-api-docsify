# createRdbPredicates

## Modules to Import

```TypeScript
import { dataAbility } from 'kits/@kit.ArkData';
```

## createRdbPredicates

```TypeScript
function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates
```

通过表名和DataAbility谓词对象创建Rdb谓词对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates--><!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 数据库表中的表名，不能为空字符串。 |
| dataAbilityPredicates | [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) | Yes | DataAbility谓词。 |

**Return value:**

| Type | Description |
| --- | --- |
| rdb.RdbPredicates | 返回RdbPredicates对象。 |

## Examples

```TypeScript
let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
dataAbilityPredicates.equalTo("NAME", "Rose")
// EMPLOYEE is a table created in an RDB store.
let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates)
```

