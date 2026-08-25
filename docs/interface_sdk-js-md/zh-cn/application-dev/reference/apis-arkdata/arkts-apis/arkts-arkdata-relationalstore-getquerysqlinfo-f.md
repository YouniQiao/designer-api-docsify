# getQuerySqlInfo

## 导入模块

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getQuerySqlInfo

```TypeScript
function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>):SqlInfo
```

获取用于查询数据的SQL语句，此为同步接口。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [SqlInfo](arkts-arkdata-relationalstore-sqlinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
