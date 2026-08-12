# getDeleteSqlInfo

## getDeleteSqlInfo

```TypeScript
function getDeleteSqlInfo(predicates: RdbPredicates):SqlInfo
```

获取用于删除数据的SQL语句，此为同步接口。

**起始版本：** 20

<!--Device-relationalStore-function getDeleteSqlInfo(predicates: RdbPredicates):SqlInfo--><!--Device-relationalStore-function getDeleteSqlInfo(predicates: RdbPredicates):SqlInfo-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SqlInfo](arkts-arkdata-relationalstore-sqlinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |

## 示例

```TypeScript
const predicates = new relationalStore.RdbPredicates("users");
predicates.equalTo("tableName", "a");
predicates.notEqualTo("age", 18);
const sqlInfo: relationalStore.SqlInfo = relationalStore.getDeleteSqlInfo(predicates);
```
