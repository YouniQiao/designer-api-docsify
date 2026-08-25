# DataObject

表示一个分布式数据对象。在使用以下接口前，需调用[create()](arkts-arkdata-distributeddataobject-create-f.md)获取DataObject对象。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## 导入模块

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void
```

绑定分布式对象中的单个资产与其对应的数据库信息，当前版本只支持分布式对象中的资产与关系型数据库的绑定。使用callback方式异步回调。当分布式对象中包含的资产和关系型数据库中包含的资产指向同一个实体资产文件，即两个资产的Uri相同时，就会存在冲突，我们把这种资产称为融合资产。如果需要分布式数据管理进行融合资产的冲突解决，需要先进行资产的绑定。当应用退出 session后，绑定关系随之消失。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>
```

绑定分布式对象中的单个资产与其对应的数据库信息，当前版本只支持分布式对象中的资产与关系型数据库的绑定。使用Promise方式作为异步回调。当分布式对象中包含的资产和关系型数据库中包含的资产指向同一个实体资产文件，即两个资产的Uri相同时，就会存在冲突，我们把这种资产称为融合资产。如果需要分布式数据管理进行融合资产的冲突解决，需要先进行资产的绑定。当应用退出 session后，绑定关系随之消失。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void
```

当不再进行数据变更监听时，使用此接口删除对象的变更监听。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('status')

```TypeScript
off(
      type: 'status',
      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

当不再进行对象上下线监听时，使用此接口删除对象的上下线监听。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('change')

```TypeScript
off(type: 'change', callback?: DataObserver): void
```

当不再进行数据变更监听时，使用此接口删除分布式对象数据变更监听的回调实例。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | 否 |

## off('status')

```TypeScript
off(type: 'status', callback?: StatusObserver): void
```

当不再进行分布式对象状态变更监听时，使用此接口删除分布式对象状态变更的回调实例。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | 否 |

## off('progressChanged')

```TypeScript
off(type: 'progressChanged', callback?: ProgressObserver): void
```

当不再进行资产传输进度监听时，使用此接口删除资产传输进度监听的回调实例。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressChanged' | 是 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | 否 |

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void
```

监听分布式数据对象的数据变更。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('status')

```TypeScript
on(
      type: 'status',
      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

监听分布式数据对象的上下线。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('change')

```TypeScript
on(type: 'change', callback: DataObserver): void
```

监听分布式对象的数据变更。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | 是 |

## on('status')

```TypeScript
on(type: 'status', callback: StatusObserver): void
```

监听分布式对象的状态变更。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | 是 |

## on('progressChanged')

```TypeScript
on(type: 'progressChanged', callback: ProgressObserver): void
```

监听资产传输进度。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressChanged' | 是 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | 是 |

## revokeSave

```TypeScript
revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void
```

撤回保存的分布式数据对象。使用callback方式作为异步方法。如果对象保存在本地设备，那么将删除所有受信任设备上所保存的数据。如果对象保存在其他设备，那么将删除本地设备上的数据。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## revokeSave

```TypeScript
revokeSave(): Promise<RevokeSaveSuccessResponse>
```

撤回保存的分布式数据对象。使用Promise方式作为异步方法。如果对象保存在本地设备，那么将删除所有受信任设备上所保存的数据。如果对象保存在其他设备，那么将删除本地设备上的数据。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## save

```TypeScript
save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void
```

保存分布式数据对象。使用callback方式异步回调。对象数据保存成功后，当应用存在时不会释放对象数据，当应用退出后，重新进入应用时，恢复保存在设备上的数据。有以下几种情况时，保存的数据将会被释放：  
- 存储时间超过24小时。  
- 应用卸载。  
- 成功恢复数据之后。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## save

```TypeScript
save(deviceId: string): Promise<SaveSuccessResponse>
```

保存分布式数据对象。使用Promise方式作为异步回调。对象数据保存成功后，当应用存在时不会释放对象数据，当应用退出后，重新进入应用时，恢复保存在设备上的数据。有以下几种情况时，保存的数据将会被释放：  
- 存储时间超过24小时。  
- 应用卸载。  
- 成功恢复数据之后。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## setAsset

```TypeScript
setAsset(assetKey: string, uri: string): Promise<void>
```

设置分布式对象中的单个资产的属性信息，该接口必须在[setSessionId](#setsessionid)接 口调用前使用。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-参数错误) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-已设置分布式对象的sessionid) |

## setAssets

```TypeScript
setAssets(assetsKey: string, uris: Array<string>): Promise<void>
```

设置分布式对象中的多个资产的属性信息，该接口必须在[setSessionId](#setsessionid)接 口调用前使用。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsKey | string | 是 |
| uris | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-参数错误) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-已设置分布式对象的sessionid) |

## setSessionId

```TypeScript
setSessionId(sessionId: string, callback: AsyncCallback<void>): void
```

设置sessionId，使用callback方式异步回调。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |

## setSessionId

```TypeScript
setSessionId(callback: AsyncCallback<void>): void
```

退出所有已加入的session，使用callback方式异步回调。

**起始版本：** 9

**需要权限：** 
- API版本9 - 19：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |

## setSessionId

```TypeScript
setSessionId(sessionId?: string): Promise<void>
```

设置sessionId或退出分布式组网，使用Promise异步回调。当传入""、null或不传入参数时，表示退出分布式组网。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自 动同步。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |
