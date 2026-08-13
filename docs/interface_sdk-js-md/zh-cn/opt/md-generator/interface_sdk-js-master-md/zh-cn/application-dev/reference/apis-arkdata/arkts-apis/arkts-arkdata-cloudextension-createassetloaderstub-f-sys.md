# createAssetLoaderStub（系统接口）

## createAssetLoaderStub

```TypeScript
function createAssetLoaderStub(instance: AssetLoader): Promise<rpc.RemoteObject>
```

根据AssetLoader类的实例创建对应的RemoteObject对象，系统内部通过该对象调用AssetLoader的实现接口，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cloudExtension-function createAssetLoaderStub(instance: AssetLoader): Promise<rpc.RemoteObject>--><!--Device-cloudExtension-function createAssetLoaderStub(instance: AssetLoader): Promise<rpc.RemoteObject>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| instance | [AssetLoader](arkts-arkdata-cloudextension-assetloader-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';

class MyAssetLoader implements cloudExtension.AssetLoader {
  // ...
}

class MyCloudService implements cloudExtension.CloudService {
  constructor() {}
  // ...   
  async connectAssetLoader(bundleName: string, database: cloudExtension.Database): Promise<rpc.RemoteObject> {
    console.info(`connect asset loader, bundle: ${bundleName}`);
    return cloudExtension.createAssetLoaderStub(new MyAssetLoader());
  }
}
```
