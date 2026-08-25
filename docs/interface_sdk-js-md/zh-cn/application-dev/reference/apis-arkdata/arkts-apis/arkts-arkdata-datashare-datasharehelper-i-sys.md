# DataShareHelper（系统接口）

DataShare管理工具实例，可使用此实例访问或管理服务端的数据。在调用DataShareHelper提供的方法前，需要先通过 [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f-sys.md) 构建一个实例。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## addTemplate

```TypeScript
addTemplate(uri: string, subscriberId: string, template: Template): void
```

添加一个指定订阅者的数据模板。仅支持静默访问。静默场景下，调用此接口时，传入的uri、subscriberId和template参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| subscriberId | string | 是 |
| template | [Template](arkts-arkdata-datashare-template-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

将批量数据插入数据库。使用callback异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>): Promise<number>
```

将批量数据插入数据库。使用Promise异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## batchUpdate

```TypeScript
batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<number>>>
```

批量更新数据库中的数据记录，所有操作的总数(即operations对象的键值对)不得超过4000个，超出限制将导致更新失败；该接口的事务性取决于provider（数据提供方）。使用Promise异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的operations参数的大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operations | Record & lt;string, Array & lt;UpdateOperation & gt; & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, Array & lt;number & gt; & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## close

```TypeScript
close(): Promise<void>
```

关闭DataShareHelper实例，调用后该实例失效。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

从数据库中删除一条或多条数据记录。使用callback异步回调。非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

从数据库中删除一条或多条数据记录。使用Promise异步回调。非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## delTemplate

```TypeScript
delTemplate(uri: string, subscriberId: string): void
```

删除一个指定订阅者的数据模板。仅支持静默访问。静默场景下，调用此接口时，传入的uri和subscriberId参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| subscriberId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string, callback: AsyncCallback<string>): void
```

将指定的URI转换为非规范化URI。使用callback异步回调。暂不支持静默访问。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string): Promise<string>
```

将指定的URI转换为非规范化URI。使用Promise异步回调。暂不支持静默访问。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## getPublishedData

```TypeScript
getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void
```

获取给定的APP和模板指定的数据。仅支持静默访问。使用callback异步回调。静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## getPublishedData

```TypeScript
getPublishedData(bundleName: string): Promise<Array<PublishedItem>>
```

获取给定的APP和模板指定的数据。仅支持静默访问。使用Promise异步回调。静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## insert

```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<number>): void
```

将单条数据插入数据库。使用callback异步回调。非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## insert

```TypeScript
insert(uri: string, value: ValuesBucket): Promise<number>
```

将单条数据插入数据库。使用Promise异步回调。非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## normalizeUri

```TypeScript
normalizeUri(uri: string, callback: AsyncCallback<string>): void
```

将给定的DataShare URI转换为规范化URI，规范化URI可供跨设备使用，DataShare URI仅供本地环境中使用。使用callback异步回调。暂不支持静默访问。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## normalizeUri

```TypeScript
normalizeUri(uri: string): Promise<string>
```

将给定的DataShare URI转换为规范化URI，规范化URI可供跨设备使用，DataShare URI仅供本地环境中使用。使用Promise异步回调。暂不支持静默访问。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## notifyChange

```TypeScript
notifyChange(uri: string, callback: AsyncCallback<void>): void
```

通知已注册的观察者指定URI对应的数据资源已发生变更。使用callback异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## notifyChange

```TypeScript
notifyChange(uri: string): Promise<void>
```

通知已注册的观察者指定URI对应的数据资源已发生变更。使用Promise异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## notifyChange

```TypeScript
notifyChange(data: ChangeInfo): Promise<void>
```

通知已注册的观察者指定URI对应的数据资源已发生变更类型及变更内容。使用Promise异步回调。暂不支持静默访问。非静默场景下，调用此接口时，传入的data参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [ChangeInfo](arkts-arkdata-relationalstore-changeinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## off('dataChange')

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口 on相对应。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## off

```TypeScript
off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口 on 相对应。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## off('rdbDataChange')

```TypeScript
off(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback?: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

取消订阅指定URI和模板对应的数据变更事件。仅支持静默访问。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rdbDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## off('publishedDataChange')

```TypeScript
off(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback?: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

取消订阅已发布数据的数据变更通知。仅支持静默访问。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishedDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## on('dataChange')

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册了观察者，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知。使用callback异步回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限 为51次。触发通知：非静默场景下，调用[notifyChange](#notifychange)方法，就会触发对指定URI订阅者的通知；或者静默场景 下，使用指定URI的静默访问修改了数据，也会自动触发通知。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## on

```TypeScript
on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册变更通知，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的uri、变更的数据内容。使用callback回调。该功能不支持跨用 户订阅通知。同一应用内对单个URI的重复订阅上限为51次。触发通知：非静默场景下，调用[notifyChange](#notifychange)方法，就会触发对指定URI订阅者的通知；或 者静默场景下，使用指定URI的静默访问修改了数据，也会自动触发通知, 但此时callback通知中的changeInfo无效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## on('rdbDataChange')

```TypeScript
on(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

订阅指定URI和模板对应的数据变更事件。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rdbDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## on('publishedDataChange')

```TypeScript
on(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

订阅已发布数据的数据变更通知。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishedDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       version: number,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

发布数据，将数据更新至数据库。需传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用callback异步回调。静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| version | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

发布数据，将数据更新至数据库。仅支持静默访问。使用callback异步回调。静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## publish

```TypeScript
publish(data: Array<PublishedItem>, bundleName: string, version?: number): Promise<Array<OperationResult>>
```

发布数据，将数据更新至数据库。可以选择传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用Promise异步回调。静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| version | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>,
       callback: AsyncCallback<DataShareResultSet>
     ): void
```

查询数据库中的数据。使用callback异步回调。非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见 [通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和 [通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>
     ): Promise<DataShareResultSet>
```

查询数据库中的数据。使用Promise异步回调。非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见 [通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和 [通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## update

```TypeScript
update(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       value: ValuesBucket,
       callback: AsyncCallback<number>
     ): void
```

更新数据库中的数据记录。使用callback异步回调。非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |

## update

```TypeScript
update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<number>
```

更新数据库中的数据记录。使用Promise异步回调。非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
