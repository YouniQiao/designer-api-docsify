# createRdbPredicates

## Modules to Import

```TypeScript
import { dataAbility } from '@kit.ArkData';
```

## createRdbPredicates

```TypeScript
function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates
```

Creates an **RdbPredicates** object with a table name and **DataAbilityPredicates** object.

**Since:** 7

**Deprecated since:** -1

<!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates--><!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| dataAbilityPredicates | [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rdb.RdbPredicates |

## Examples

```TypeScript
let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
dataAbilityPredicates.equalTo("NAME", "Rose")
// EMPLOYEE is a table created in an RDB store.
let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates)
```
