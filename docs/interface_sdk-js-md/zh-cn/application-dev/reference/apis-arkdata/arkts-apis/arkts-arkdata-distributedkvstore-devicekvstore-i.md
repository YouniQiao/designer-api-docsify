# DeviceKVStore

设备协同数据库，继承自SingleKVStore，提供查询数据和端端同步数据的方法，可以使用SingleKVStore的方法例如：put、putBatch等。设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。在调用DeviceKVStore的方法前，需要先通过 getKVStore 构建一个DeviceKVStore实例。

**继承/实现关系：** DeviceKVStore extends [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md)

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## get

```TypeScript
get(key: string, callback: AsyncCallback<boolean | string | number | number | Uint8Array>): void
```

获取本设备指定键的值，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean \| string \| number \| number \| Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## get

```TypeScript
get(key: string): Promise<boolean | string | number | number | Uint8Array>
```

获取本设备指定键的值，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean \ | string \| number \| number \| Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## get

```TypeScript
get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | number | Uint8Array>): void
```

获取与指定设备ID和Key匹配的值，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean \| string \| number \| number \| Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## get

```TypeScript
get(deviceId: string, key: string): Promise<boolean | string | number | number | Uint8Array>
```

获取与指定设备ID和Key匹配的值，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean \ | string \| number \| number \| Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void
```

获取匹配本设备指定键前缀的所有键值对，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(keyPrefix: string): Promise<Entry[]>
```

获取匹配本设备指定键前缀的所有键值对，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void
```

获取与指定设备ID和Key前缀匹配的所有键值对，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>
```

获取与指定设备ID和Key前缀匹配的所有键值对，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(query: Query, callback: AsyncCallback<Entry[]>): void
```

获取本设备与指定Query对象匹配的键值对列表，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(query: Query): Promise<Entry[]>
```

获取本设备与指定Query对象匹配的键值对列表，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void
```

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(deviceId: string, query: Query): Promise<Entry[]>
```

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void
```

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用callback异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](arkts-arkdata-distributedkvstore-singlekvstore-i.md#closeresultset) 关闭结果集释放资源。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string): Promise<KVStoreResultSet>
```

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用Promise异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](arkts-arkdata-distributedkvstore-singlekvstore-i.md#closeresultset) 关闭结果集释放资源。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>
```

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(query: Query): Promise<KVStoreResultSet>
```

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用callback异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](arkts-arkdata-distributedkvstore-singlekvstore-i.md#closeresultset) 关闭结果集释放资源。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>
```

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](arkts-arkdata-distributedkvstore-singlekvstore-i.md#closeresultset) 关闭结果集释放资源。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |

## getResultSize

```TypeScript
getResultSize(query: Query, callback: AsyncCallback<number>): void
```

获取与本设备指定Query对象匹配的结果数，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSize

```TypeScript
getResultSize(query: Query): Promise<number>
```

获取与本设备指定Query对象匹配的结果数，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSize

```TypeScript
getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void
```

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSize

```TypeScript
getResultSize(deviceId: string, query: Query): Promise<number>
```

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。

> **说明：**&gt;
> 其中deviceId通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
