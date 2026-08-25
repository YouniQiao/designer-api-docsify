# createCloudServiceStub（系统接口）

## 导入模块

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## createCloudServiceStub

```TypeScript
function createCloudServiceStub(instance: CloudService): Promise<rpc.RemoteObject>
```

根据CloudService类的实例创建对应的RemoteObject对象，系统内部通过该对象调用CloudService的实现接口。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| instance | [CloudService](arkts-arkdata-cloudextension-cloudservice-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |
