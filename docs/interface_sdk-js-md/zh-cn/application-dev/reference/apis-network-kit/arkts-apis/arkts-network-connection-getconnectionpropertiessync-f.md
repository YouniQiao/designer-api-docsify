# getConnectionPropertiesSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getConnectionPropertiesSync

```TypeScript
function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties
```

Queries the connection properties of a network.This method requires the {@code ohos.permission.GET_NETWORK_INFO} permission.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties--><!--Device-connection-function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | 是 | Indicates the network to be queried. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionProperties](arkts-network-connection-connectionproperties-i.md) | Returns the connection properties of a network. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let connectionproperties = connection.getConnectionPropertiesSync(netHandle);
  console.info("Succeeded to get connectionproperties: " + JSON.stringify(connectionproperties));
});
```

