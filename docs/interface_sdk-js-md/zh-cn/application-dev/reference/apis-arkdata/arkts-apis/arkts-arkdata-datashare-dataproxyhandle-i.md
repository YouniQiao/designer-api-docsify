# DataProxyHandle

数据代理操作句柄的实例，可使用此实例访问或管理共享配置信息。在调用DataProxyHandle提供的方法前，需要先通过 [createDataProxyHandle](arkts-arkdata-datashare-createdataproxyhandle-f.md)构建一个实例。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

## 导入模块

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## delete

```TypeScript
delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

根据URI删除指定的共享配置项。使用Promise异步回调。只有配置发布方能删除共享配置项。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | string[] | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## deleteMyPublishedData

```TypeScript
deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>
```

删除当前发布者发布的所有共享配置项。使用Promise异步回调。只有配置发布方能删除共享配置项。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## get

```TypeScript
get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>
```

根据URI获取指定的共享配置项。使用Promise异步回调。只有发布者和允许列表中指定的应用可以访问该共享配置项。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | string[] | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataProxyGetResult](arkts-arkdata-datashare-dataproxygetresult-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## getValues

```TypeScript
getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>
```

获取指定 URI 下的所有多值类型数据。只有发布者和位于 [allowList](arkts-arkdata-datashare-proxydata-i.md#allowlist) 中的应用程序才能获取此数据。该 API 使用 Promise 异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ValueType](arkts-arkdata-valuetype-t.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |
| [15700015](../errorcode-datashare.md#15700015-访问uri权限错误) |

## off

```TypeScript
off(
      event: 'dataChange',
      uris: string[],
      config: DataProxyConfig,
      callback?: AsyncCallback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

取消订阅指定URI对应代理数据变更事件。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| uris | string[] | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## on

```TypeScript
on(
      event: 'dataChange',
      uris: string[],
      config: DataProxyConfig,
      callback: AsyncCallback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

订阅指定URI对应共享配置变更事件。若订阅者已注册变更通知，当配置发布方修改配置时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的URI、变更的共享配置内容。使用callback异步回调。该功能不允许跨用户 订阅通知，不允许订阅未发布的配置。订阅成功后若权限被收回，则后续不再通知订阅者。触发通知：配置发布方调用[publish](#publish)、 [delete](#delete)、 [delete](#delete)接口发布、删除指定配置或者删除所有配置时会自动触 发通知。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| uris | string[] | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## publish

```TypeScript
publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

发布共享配置项。使用Promise异步回调。发布后，发布者和允许列表中指定的应用可以访问该共享配置项。如果要发布的URI已经存在，则更新对应的共享配置项。如果发布的配置项中存在任一URI的长度超出上限或者格式校验失败，则当前发 布操作失败。只有发布者才允许更新共享配置项。API版本26.0.0之前，每个应用支持最多32个共享配置；从API版本26.0.0开始，每个应用支持最多64个共享配置。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [ProxyData[]](arkts-arkdata-datashare-proxydata-i.md) | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |

## putValue

```TypeScript
putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise<void>
```

将一个值写入到已发布的数据中。该操作仅支持对多值类型数据执行。若传入的**key**不存在，则添加新的值；若传入的**key**已存在，则更新该key对应的值。默认情况下，单条数据（即URI）在单次应用中最多可添加10个值，每 个值 最大长度为4096字节。同时，单条数据（即一个URI）在单次应用中所有值总长度受限于数据发布时指定的**maxValueLength**参数值。请注意，该API中**maxValueLength**参数不生效。该API使用Pr omise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| key | number | 是 |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |
| [15700015](../errorcode-datashare.md#15700015-访问uri权限错误) |

## removeValue

```TypeScript
removeValue(uri: string, key: number, config: DataProxyConfig): Promise<void>
```

移除键对应的值。该操作仅能对多值类型数据执行。仅能移除本应用添加过的值。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| key | number | 是 |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [15700014](../errorcode-datashare.md#15700014-配置共享参数错误) |
| [15700015](../errorcode-datashare.md#15700015-访问uri权限错误) |
