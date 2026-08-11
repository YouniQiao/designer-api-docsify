# createRdbPredicates

## createRdbPredicates

```TypeScript
function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates
```

通过表名和DataAbility谓词对象创建Rdb谓词对象。

**起始版本：** 7

<!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates--><!--Device-dataAbility-function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates-End-->

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

## 示例

```TypeScript
let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
dataAbilityPredicates.equalTo("NAME", "Rose")
// EMPLOYEE是使用关系型数据库创建的表。
let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates)
```
