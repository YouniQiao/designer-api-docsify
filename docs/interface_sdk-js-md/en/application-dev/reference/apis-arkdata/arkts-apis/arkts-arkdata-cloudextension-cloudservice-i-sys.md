# CloudService (System API)

提供对接同步云服务的类。开发者需要继承此类并实现类的接口，系统内部通过该类的接口连接并使用同步云服务。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface CloudService--><!--Device-cloudExtension-export interface CloudService-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## connectAssetLoader

```TypeScript
connectAssetLoader(bundleName: string, database: Database): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取AssetLoader的RemoteObject对象，可以通过createAssetLoaderStub接口进行创建，使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-connectAssetLoader(bundleName: string, database: Database): Promise<rpc.RemoteObject>--><!--Device-CloudService-connectAssetLoader(bundleName: string, database: Database): Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用包名。 |
| database | [Database](arkts-arkdata-cloudextension-database-i-sys.md) | Yes | 需要连接的数据库。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;rpc.RemoteObject&gt; | Promise对象，返回AssetLoader的RemoteObject对象。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

class MyAssetLoader implements cloudExtension.AssetLoader {
  // ...
}

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  async connectAssetLoader(bundleName: string, database: cloudExtension.Database): Promise<rpc.RemoteObject> {
    // ...
    console.info(`connect asset loader, bundle: ${bundleName}`);
    return cloudExtension.createAssetLoaderStub(new MyAssetLoader());
  }
}
```

## connectDB

```TypeScript
connectDB(bundleName: string, database: Database): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取CloudDB的RemoteObject对象，可以通过createCloudDBStub接口进行创建，使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-connectDB(bundleName: string, database: Database): Promise<rpc.RemoteObject>--><!--Device-CloudService-connectDB(bundleName: string, database: Database): Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用包名。 |
| database | [Database](arkts-arkdata-cloudextension-database-i-sys.md) | Yes | 需要连接的数据库。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;rpc.RemoteObject&gt; | Promise对象，返回CloudDB的RemoteObject对象。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

class MyCloudDB implements cloudExtension.CloudDB {
  // ...
}

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
    // ...
  async connectDB(bundleName: string, database: cloudExtension.Database): Promise<rpc.RemoteObject> {
    console.info(`connect DB, bundleName: ${bundleName}`);
    return cloudExtension.createCloudDBStub(new MyCloudDB());
  }
}
```

## connectShareCenter

ArkTS-Dyn:
```TypeScript
connectShareCenter(userId: number, bundleName: string): Promise<rpc.RemoteObject>
```

ArkTS-Sta:
```TypeScript
connectShareCenter(userId: int, bundleName: string): Promise<rpc.RemoteObject>
```

系统内部通过该接口获取ShareCenter的RemoteObject对象，可以通过createShareServiceStub接口进行创建，使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-connectShareCenter(userId: int, bundleName: string): Promise<rpc.RemoteObject>--><!--Device-CloudService-connectShareCenter(userId: int, bundleName: string): Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示用户账号ID。 |
| bundleName | string | Yes | 应用包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;rpc.RemoteObject&gt; | Promise对象，返回ShareCenter的RemoteObject对象。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

class MyShareCenter implements cloudExtension.ShareCenter {
  constructor() {}
  // ...
}

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  async connectShareCenter(userId: number, bundleName: string): Promise<rpc.RemoteObject> {
    console.info(`connect share center, bundle: ${bundleName}`);
    return cloudExtension.createShareServiceStub(new MyShareCenter());
  }
}
```

## getAppBriefInfo

```TypeScript
getAppBriefInfo(): Promise<Record<string, AppBriefInfo>>
```

获取简要应用信息。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-getAppBriefInfo(): Promise<Record<string, AppBriefInfo>>--><!--Device-CloudService-getAppBriefInfo(): Promise<Record<string, AppBriefInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, AppBriefInfo&gt;&gt; | Promise对象，返回以bundleName为键、AppBriefInfo为值的键值对。 in KV pairs. |

## Examples

```TypeScript
class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  // ...
  async getAppBriefInfo(): Promise<Record<string, cloudExtension.AppBriefInfo>> {
    console.info(`get app brief info`);
    // ...
    return {
      "test_bundle":
      {
        appId: "test_appID",
        bundleName: "test_bundlename",
        cloudSwitch: true,
        instanceId: 0,
      }
    };
  }
}
```

## getAppSchema

```TypeScript
getAppSchema(bundleName: string): Promise<Result<AppSchema>>
```

获取应用Schema（数据库模式）信息。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-getAppSchema(bundleName: string): Promise<Result<AppSchema>>--><!--Device-CloudService-getAppSchema(bundleName: string): Promise<Result<AppSchema>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;AppSchema&gt;&gt; | Promise对象，返回数据库的schema信息。 |

## Examples

```TypeScript
class MyCloudService implements cloudExtension.CloudService {
  constructor() {
  }
  // ...
  async getAppSchema(bundleName: string): Promise<cloudExtension.Result<cloudExtension.AppSchema>> {
    console.info(`get app schema, bundleName:${bundleName}`);
    // ...
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: "get app schema success",
      value: {
        bundleName: "test_bundleName",
        version: 1,
        databases: []
      }
    };
  }
}
```

## getServiceInfo

```TypeScript
getServiceInfo(): Promise<ServiceInfo>
```

获取服务器上的信息。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-getServiceInfo(): Promise<ServiceInfo>--><!--Device-CloudService-getServiceInfo(): Promise<ServiceInfo>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ServiceInfo&gt; | Promise对象，返回获取的服务器信息。 |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

let testSpace: number = 100;
let testUserId: number = 1;

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  // ...
  async getServiceInfo(): Promise<cloudExtension.ServiceInfo> {
    console.info(`get service info`);
    // ...
    return {
      enableCloud: true,
      id: "test_id",
      totalSpace: testSpace,
      remainingSpace: testSpace,
      user: testUserId,
    };
  }
}
```

## subscribe

ArkTS-Dyn:
```TypeScript
subscribe(
      subInfo: Record<string, Array<Database>>,
      expirationTime: number
    ): Promise<Result<SubscribeInfo>>
```

ArkTS-Sta:
```TypeScript
subscribe(
      subInfo: Record<string, Array<Database>>,
      expirationTime: long
    ): Promise<Result<SubscribeInfo>>
```

订阅云数据库的变化通知。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-subscribe(      subInfo: Record<string, Array<Database>>,      expirationTime: long    ): Promise<Result<SubscribeInfo>>--><!--Device-CloudService-subscribe(      subInfo: Record<string, Array<Database>>,      expirationTime: long    ): Promise<Result<SubscribeInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;Database&gt;&gt; | Yes | 需要订阅的数据，由应用包名称和数据库信息组成的键值对。 |
| expirationTime | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 表示订阅到期时间（ms）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;SubscribeInfo&gt;&gt; | Promise对象，返回订阅的结果，包含订阅的过期时间和订阅信息。 |

## Examples

```TypeScript
let testTime: number = 10;
class MyCloudService implements cloudExtension.CloudService {
  constructor() {
  }
  // ...
  async subscribe(subInfo: Record<string, Array<cloudExtension.Database>>, expirationTime: number): Promise<cloudExtension.Result<cloudExtension.SubscribeInfo>> {
    console.info(`subscribe expirationTime: ${expirationTime}`);
    // ...
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: "subscribe success",
      value: {
        expirationTime: testTime,
        subscribe: {}
      }
    };
  }
}
```

## unsubscribe

ArkTS-Dyn:
```TypeScript
unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<number>
```

ArkTS-Sta:
```TypeScript
unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<int>
```

取消已订阅的云数据变化通知。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudService-unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<int>--><!--Device-CloudService-unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unsubscribeInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;string&gt;&gt; | Yes | 需要取消订阅的数据信息，由应用包名和数据库名组成的键值对。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回取消订阅结果的错误码。 |

## Examples

```TypeScript
class MyCloudService implements cloudExtension.CloudService {
  constructor() {
  }
  // ...
  async unsubscribe(unsubscribeInfo: Record<string, Array<string>>): Promise<number> {
    console.info(`unsubscribe`);
    // ...
    return cloudExtension.ErrorCode.SUCCESS;
  }
}
```

