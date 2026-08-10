# ResultSet

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

ResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)、  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)、  
[remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remotequery)、[queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#querylockedrow)等query类方法中任一方法获取到ResultSet实例，再通过此实例调用对应方法。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getFloat32Array

ArkTS-Dyn:
```TypeScript
getFloat32Array(columnIndex: number): Float32Array
```

ArkTS-Sta:
```TypeScript
getFloat32Array(columnIndex: int): Float32Array
```

以浮点数组的形式获取当前行中指定列的值，仅可在向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）下可用。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array--><!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 指定的列索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Float32Array | 以浮点数组的形式返回指定列的值。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 801 | The capability is not supported because the database is not a vector DB. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800013 | Column index is out of bounds. |
| 14800014 | The target instance is already closed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800030 | SQLite: Unable to open the database file. |

