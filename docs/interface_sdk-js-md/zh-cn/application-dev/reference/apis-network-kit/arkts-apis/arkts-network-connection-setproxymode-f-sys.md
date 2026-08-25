# setProxyMode（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setProxyMode

```TypeScript
function setProxyMode(mode: ProxyMode): Promise<void>
```

设置代理模式。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [ProxyMode](arkts-network-connection-proxymode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
