# createRdbPredicates

## 导入模块

```TypeScript
import { dataAbility } from '@kit.ArkData';
```

## createRdbPredicates

```TypeScript
function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates
```

通过表名和DataAbility谓词对象创建Rdb谓词对象。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| dataAbilityPredicates | [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| rdb.RdbPredicates |

**示例**

```TypeScript
let dataAbilityPredicates = new dataAbility.DataAbilityPredicates();
dataAbilityPredicates.equalTo("NAME", "Rose");
// EMPLOYEE是使用关系型数据库创建的表。
let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates);
```
