# createKVManager

## 导入模块

```TypeScript
```

## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void
```

创建一个KVManager对象实例，用于管理数据库对象，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** createKVManager

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;KVManager&gt; | 是 |


## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig): Promise<KVManager>
```

创建一个KVManager对象实例，用于管理数据库对象，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** createKVManager

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;KVManager & gt; |
