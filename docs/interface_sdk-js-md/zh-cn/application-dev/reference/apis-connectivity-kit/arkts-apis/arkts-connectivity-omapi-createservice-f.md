# createService

## 导入模块

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## createService

```TypeScript
function createService(): Promise<SEService>
```

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式。使用Promise异步回调。仅当[isConnected](arkts-connectivity-omapi-seservice-i.md#isconnected)方法返回true时，该返回SEService对象是可用的。

**起始版本：** 12

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SEService](arkts-connectivity-omapi-seservice-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
