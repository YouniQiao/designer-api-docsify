# SingleKVStore

SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据端端同步完成的方法。 在调用SingleKVStore的方法前，需要先通过 getKVStore 构建一个SingleKVStore实例。

**起始版本：** 23

<!--Device-distributedKVStore-interface SingleKVStore--><!--Device-distributedKVStore-interface SingleKVStore-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
```

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void
```

从数据库中删除符合predicates条件的键值对，使用callback异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>
```

从数据库中删除符合predicates条件的键值对，使用Promise异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与指定Predicates对象匹配的KVStoreResultSet对象，使用callback异步回调。获取结果集后，需要及时调用closeResultSet方法关闭结果集以释放资源。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

获取与指定Predicates对象匹配的KVStoreResultSet对象，使用Promise异步回调。获取结果集后，需要及时调用closeResultSet方法关闭结果集以释放资源。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Provider

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

批量写入键值对数据，每个ValuesBucket对象包含key和value字段，使用callback异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>): Promise<void>
```

批量写入键值对数据，每个ValuesBucket对象包含key和value字段，使用Promise异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

将值写入SingleKVStore数据库，使用callback异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>): Promise<void>
```

将valuesbucket类型的值写入SingleKVStore数据库，使用Promise异步回调。

**起始版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
