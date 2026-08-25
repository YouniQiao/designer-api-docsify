# createRdbPredicates

## Modules to Import

```TypeScript
import { dataAbility } from 'kits/@kit.ArkData';
```

## createRdbPredicates

```TypeScript
function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates
```

Creates an **RdbPredicates** object with a table name and **DataAbilityPredicates** object.

**Since:** 7

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
