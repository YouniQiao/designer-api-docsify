# setAppHttpProxy

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setAppHttpProxy

```TypeScript
function setAppHttpProxy(httpProxy: HttpProxy): void
```

设置应用级Http代理配置信息。

> **说明：**&gt;
> 若需使用本接口所配置的代理信息，则需在[HttpRequestOptions](arkts-network-http-httprequestoptions-i.md)字段中将usingProxy设置为true以启用代理转
> 发。本接口仅负责配置代理规则，不校验代理服务的有效性。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [httpProxy](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | [HttpProxy](arkts-network-ethernet-httpproxy-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
