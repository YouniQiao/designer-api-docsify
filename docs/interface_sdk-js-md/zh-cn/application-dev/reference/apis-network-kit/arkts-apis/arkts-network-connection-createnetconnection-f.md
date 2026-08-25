# createNetConnection

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## createNetConnection

```TypeScript
function createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection
```

创建一个NetConnection对象，可用于监听网络状态。[netSpecifier](arkts-network-connection-netspecifier-i.md)表示需要监听网络的网络特征；timeout是超时时间（单位：毫秒)； netSpecifier是timeout的必要条件，两者都没有则表示关注默认网络。

> **说明：**&gt;
> 若需要监听网络状态，创建一个NetConnection对象后，还需调用[register](arkts-network-connection-netconnection-i.md#register)注册指定网络状态变化的通知。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| netSpecifier | [NetSpecifier](arkts-network-connection-netspecifier-i.md) | 否 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| [NetConnection](arkts-network-connection-netconnection-i.md) |
