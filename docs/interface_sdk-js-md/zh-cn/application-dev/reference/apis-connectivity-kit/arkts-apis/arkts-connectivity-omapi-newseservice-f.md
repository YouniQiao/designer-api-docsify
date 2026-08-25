# newSEService

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## newSEService('serviceState')

```TypeScript
function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService
```

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式进行的。使用callback异步回调。仅当指定的回调或者当[isConnected](arkts-connectivity-omapi-seservice-i.md#isconnected)方法返回true时，该返回SEService对象是可用的。

**起始版本：** 10

**废弃版本：** 12

**替代接口：** [createService](arkts-connectivity-omapi-createservice-f.md)

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'serviceState' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [SEService](arkts-connectivity-omapi-seservice-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
