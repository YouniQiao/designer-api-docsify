# CloudService（系统接口）

提供对接同步云服务的类。开发者需要继承此类并实现类的接口，系统内部通过该类的接口连接并使用同步云服务。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## connectAssetLoader

```TypeScript
connectAssetLoader(bundleName: string, database: Database): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取AssetLoader的RemoteObject对象，可以通过createAssetLoaderStub接口进行创建，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| database | [Database](arkts-arkdata-cloudextension-database-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |

## connectDB

```TypeScript
connectDB(bundleName: string, database: Database): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取CloudDB的RemoteObject对象，可以通过createCloudDBStub接口进行创建，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| database | [Database](arkts-arkdata-cloudextension-database-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |

## connectShareCenter

```TypeScript
connectShareCenter(userId: number, bundleName: string): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取ShareCenter的RemoteObject对象，可以通过createShareServiceStub接口进行创建，使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |

## getAppBriefInfo

```TypeScript
getAppBriefInfo(): Promise<Record<string, AppBriefInfo>>
```

获取简要应用信息。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, [AppBriefInfo](arkts-arkdata-cloudextension-appbriefinfo-i-sys.md)&gt;&gt; |

## getAppSchema

```TypeScript
getAppSchema(bundleName: string): Promise<Result<AppSchema>>
```

获取应用Schema（数据库模式）信息。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Result&lt;[AppSchema](arkts-arkdata-cloudextension-appschema-i-sys.md)&gt;&gt; |

## getServiceInfo

```TypeScript
getServiceInfo(): Promise<ServiceInfo>
```

获取服务器上的信息。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ServiceInfo](arkts-arkdata-cloudextension-serviceinfo-i-sys.md)&gt; |

## subscribe

```TypeScript
subscribe(
      subInfo: Record<string, Array<Database>>,
      expirationTime: number
    ): Promise<Result<SubscribeInfo>>
```

订阅云数据库的变化通知。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subInfo | Record&lt;string, Array&lt;[Database](arkts-arkdata-cloudextension-database-i-sys.md)&gt;&gt; | 是 |
| expirationTime | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;SubscribeInfo & gt; & gt; |

## unsubscribe

```TypeScript
unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<number>
```

取消已订阅的云数据变化通知。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| unsubscribeInfo | Record & lt;string, Array & lt;string & gt; & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
