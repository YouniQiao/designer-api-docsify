# ResultSet

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

ResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)、  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)、  
[remoteQuery](arkts-arkdata-relationalstore-rdbstore-i.md#remoteQuery)、[queryLockedRow](arkts-arkdata-relationalstore-rdbstore-i.md#queryLockedRow)等query类方法中任一方法获取到ResultSet实例，再通过此实例调用对应方法。

**起始版本：** 9

<!--Device-relationalStore-interface ResultSet--><!--Device-relationalStore-interface ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## getFloat32Array

```TypeScript
getFloat32Array(columnIndex: number): Float32Array
```

以浮点数组的形式获取当前行中指定列的值，仅可在向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig)中配置vector为true）下可用。

**起始版本：** 12

<!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array--><!--Device-ResultSet-getFloat32Array(columnIndex: int): Float32Array-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Float32Array |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800013-列号越界或列类型与当前调用接口不兼容) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
