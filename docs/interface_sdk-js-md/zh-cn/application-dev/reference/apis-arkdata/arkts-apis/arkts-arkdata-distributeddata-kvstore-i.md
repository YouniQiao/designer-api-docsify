# KVStore

KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。 在调用KVStore的方法前，需要先通过 getKVStore 构建一个KVStore实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** SingleKVStore

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
```

## commit

```TypeScript
commit(callback: AsyncCallback<void>): void
```

提交KVStore数据库中的事务，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** commit

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## commit

```TypeScript
commit(): Promise<void>
```

提交KVStore数据库中的事务，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** commit

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

从数据库中删除指定键值的数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** delete

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## delete

```TypeScript
delete(key: string): Promise<void>
```

从数据库中删除指定键值的数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** delete

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## deleteBatch

```TypeScript
deleteBatch(keys: string[], callback: AsyncCallback<void>): void
```

批量删除KVStore数据库中的键值对，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** deleteBatch

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## deleteBatch

```TypeScript
deleteBatch(keys: string[]): Promise<void>
```

批量删除KVStore数据库中的键值对，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** deleteBatch

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## enableSync

```TypeScript
enableSync(enabled: boolean, callback: AsyncCallback<void>): void
```

设定是否开启同步，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** enableSync

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## enableSync

```TypeScript
enableSync(enabled: boolean): Promise<void>
```

设定是否开启同步，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** enableSync

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## off

```TypeScript
off(event: 'dataChange', listener?: Callback<ChangeNotification>): void
```

取消订阅数据变更通知。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** off

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | 否 |

## off

```TypeScript
off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void
```

取消订阅同步完成事件回调通知。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** off

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'syncComplete' | 是 |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 否 |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void
```

订阅指定类型的数据变更通知。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** on

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | 是 |

## on

```TypeScript
on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void
```

订阅同步完成事件回调通知。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** on

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'syncComplete' | 是 |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

## put

```TypeScript
put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void
```

添加指定类型键值对到数据库，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** put

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | Uint8Array \| string \| number \| boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## put

```TypeScript
put(key: string, value: Uint8Array | string | number | boolean): Promise<void>
```

添加指定类型键值对到数据库，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** put

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | Uint8Array \| string \| number \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## putBatch

```TypeScript
putBatch(entries: Entry[], callback: AsyncCallback<void>): void
```

批量插入键值对到KVStore数据库中，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** putBatch

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| entries | [Entry[]](arkts-arkdata-distributeddata-entry-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## putBatch

```TypeScript
putBatch(entries: Entry[]): Promise<void>
```

批量插入键值对到KVStore数据库中，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** putBatch

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| entries | [Entry[]](arkts-arkdata-distributeddata-entry-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## rollback

```TypeScript
rollback(callback: AsyncCallback<void>): void
```

在KVStore数据库中回滚事务，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** rollback

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## rollback

```TypeScript
rollback(): Promise<void>
```

在KVStore数据库中回滚事务，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** rollback

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSyncRange

```TypeScript
setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void
```

设置同步范围标签，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSyncRange

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localLabels | string[] | 是 |
| remoteSupportLabels | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setSyncRange

```TypeScript
setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>
```

设置同步范围标签，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSyncRange

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localLabels | string[] | 是 |
| remoteSupportLabels | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## startTransaction

```TypeScript
startTransaction(callback: AsyncCallback<void>): void
```

启动KVStore数据库中的事务，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** startTransaction

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## startTransaction

```TypeScript
startTransaction(): Promise<void>
```

启动KVStore数据库中的事务，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** startTransaction

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
