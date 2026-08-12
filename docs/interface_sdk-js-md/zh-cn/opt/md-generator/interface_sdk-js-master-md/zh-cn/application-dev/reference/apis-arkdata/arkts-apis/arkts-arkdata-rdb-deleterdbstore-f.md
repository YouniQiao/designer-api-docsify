# deleteRdbStore

## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void
```

删除数据库，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore)

<!--Device-rdb-function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void--><!--Device-rdb-function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, name: string): Promise<void>
```

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore)

<!--Device-rdb-function deleteRdbStore(context: Context, name: string): Promise<void>--><!--Device-rdb-function deleteRdbStore(context: Context, name: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
