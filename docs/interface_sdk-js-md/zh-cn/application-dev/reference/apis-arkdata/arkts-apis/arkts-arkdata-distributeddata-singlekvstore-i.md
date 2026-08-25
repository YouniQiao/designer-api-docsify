# SingleKVStore

单版本数据库，继承自[KVStore](arkts-arkdata-distributeddata-kvstoretype-e.md)数据库，提供查询数据和同步数据的方法。 单版本数据库，不对数据所属设备进行区分，不同设备使用相同键写入数据会互相覆盖。比如，可以使用单版本数据库实现个人日历、联系人数据在不同设备间的数据同步。 在调用SingleKVStore的方法前，需要先通过 getKVStore 构建一个SingleKVStore实例。

**继承/实现关系：** SingleKVStore extends [KVStore](arkts-arkdata-distributeddata-kvstore-i.md)

**起始版本：** 7

**废弃版本：** 9

**替代接口：** SingleKVStore

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
```

## closeResultSet

```TypeScript
closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void
```

关闭由 [SingleKVStore.getResultSet](#getresultset) 返回的KvStoreResultSet对象，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** closeResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## closeResultSet

```TypeScript
closeResultSet(resultSet: KvStoreResultSet): Promise<void>
```

关闭由 [SingleKVStore.getResultSet](#getresultset) 返回的KvStoreResultSet对象，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** closeResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## get

```TypeScript
get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void
```

获取指定键的值，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** get

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array \| string \| boolean \| number & gt; | 是 |

## get

```TypeScript
get(key: string): Promise<Uint8Array | string | boolean | number>
```

获取指定键的值，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** get

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array \ | string \| boolean \| number & gt; |

## getEntries

```TypeScript
getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void
```

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getEntries

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

## getEntries

```TypeScript
getEntries(keyPrefix: string): Promise<Entry[]>
```

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getEntries

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

## getEntries

```TypeScript
getEntries(query: Query, callback: AsyncCallback<Entry[]>): void
```

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getEntries

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

## getEntries

```TypeScript
getEntries(query: Query): Promise<Entry[]>
```

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getEntries

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void
```

从KvStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; | 是 |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string): Promise<KvStoreResultSet>
```

从KVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; |

## getResultSet

```TypeScript
getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void
```

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; | 是 |

## getResultSet

```TypeScript
getResultSet(query: Query): Promise<KvStoreResultSet>
```

获取与指定Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSet

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; |

## getResultSize

```TypeScript
getResultSize(query: Query, callback: AsyncCallback<number>): void
```

获取与指定Query对象匹配的结果数，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSize

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getResultSize

```TypeScript
getResultSize(query: Query): Promise<number>
```

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getResultSize

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getSecurityLevel

```TypeScript
getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void
```

获取数据库的安全级别，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getSecurityLevel

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SecurityLevel&gt; | 是 |

## getSecurityLevel

```TypeScript
getSecurityLevel(): Promise<SecurityLevel>
```

获取数据库的安全级别，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getSecurityLevel

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;SecurityLevel & gt; |

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

**起始版本：** 8

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'syncComplete' | 是 |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void
```

删除指定设备的数据，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用<!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP1End-->deviceManager模块的接口均为系统接口，仅系统应用可用。
> 
> deviceId具体获取方式请参考[sync接口示例](#sync)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** removeDeviceData

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string): Promise<void>
```

删除指定设备的数据，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用<!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP1End-->deviceManager模块的接口均为系统接口，仅系统应用可用。
> 
> deviceId具体获取方式请参考[sync接口示例](#sync)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** removeDeviceData

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSyncParam

```TypeScript
setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void
```

设置数据库同步允许的默认延迟，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSyncParam

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| defaultAllowedDelayMs | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setSyncParam

```TypeScript
setSyncParam(defaultAllowedDelayMs: number): Promise<void>
```

设置数据库同步允许的默认延迟，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSyncParam

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| defaultAllowedDelayMs | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## sync

```TypeScript
sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void
```

在手动同步方式下，触发数据库同步。

> **说明：**&gt;
> 其中deviceIds为<!--RP2-->[DeviceInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-deviceinfo-i-sys.md)中的
> networkId, 通过调用
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP2End-->deviceManager模块的接口均为系统接口，仅系统应用可用。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** sync

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceIds | string[] | 是 |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| delayMs | number | 否 |
