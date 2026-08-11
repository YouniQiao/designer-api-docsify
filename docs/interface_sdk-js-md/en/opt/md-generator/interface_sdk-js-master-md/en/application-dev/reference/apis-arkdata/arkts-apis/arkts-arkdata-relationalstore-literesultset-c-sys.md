# LiteResultSet

Defines APIs to access the result set obtained by querying the RDB store. This result set is the collection of results returned with the **query()** method called.

The **LiteResultSet** instance is not refreshed in real time. After using the result set, if the data in the database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest data.

In the following API examples, you need to obtain an **LiteResultSet** instance by using a query method, such as   
[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querywithoutrowcount) or   
[querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount), and then call the corresponding method through this instance.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 23.

**Since:** 23

<!--Device-relationalStore-class LiteResultSet--><!--Device-relationalStore-class LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getFloat32Array

```TypeScript
getFloat32Array(columnIndex: number): Float32Array
```

Obtains the value of the specified column in the current row as a float array.The implementation class determines whether to throw an exception if the value of the specified column in the current row is null or the specified column is not of the float array type.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiteResultSet-getFloat32Array(columnIndex: int): Float32Array--><!--Device-LiteResultSet-getFloat32Array(columnIndex: int): Float32Array-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| columnIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

**Error codes:**

| Error Code ID |
| --- |
| [14800041](../errorcode-data-rdb.md#14800041-type-conversion-failure) |
| [14800013](../errorcode-data-rdb.md#14800013-null-column-value-or-column-data-type-incompatible-with-the-api-called) |
| [14800012](../errorcode-data-rdb.md#14800012-empty-result-set-or-invalid-position) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
