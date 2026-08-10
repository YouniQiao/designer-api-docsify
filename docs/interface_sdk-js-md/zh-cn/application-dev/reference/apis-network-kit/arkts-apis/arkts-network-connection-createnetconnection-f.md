# createNetConnection

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## createNetConnection

```TypeScript
function createNetConnection(netSpecifier?: NetSpecifier, timeout?: int): NetConnection
```

Create a network connection with optional netSpecifier and timeout.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-connection-function createNetConnection(netSpecifier?: NetSpecifier, timeout?: int): NetConnection--><!--Device-connection-function createNetConnection(netSpecifier?: NetSpecifier, timeout?: int): NetConnection-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netSpecifier | [NetSpecifier](arkts-network-connection-netspecifier-i.md) | 否 | Indicates the network specifier. See {@link NetSpecifier}. |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | The time in milliseconds to attempt looking for a suitable network before {@link NetConnection#netUnavailable} is called. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetConnection](arkts-network-connection-netconnection-i.md) | the NetConnection of the NetSpecifier. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';

// 示例1：仅关注默认网络, 无需指定netSpecifier参数，timeout参数未传入说明未使用超时时间，此时timeout为0。
let netConnection = connection.createNetConnection();

// 示例2：仅关注蜂窝网络，需要指定网络类型为蜂窝网络。
let timeout = 1000;
let netConnectionCellular = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
  }
}, timeout);

// 示例3：关注蜂窝或Wi-Fi网络，需要指定网络类型为蜂窝网络和Wi-Fi网络。
let netConnectionCellularAndWifi = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR,
      connection.NetBearType.BEARER_WIFI]
  }
});
```

