# getIpNeighTable

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getIpNeighTable

```TypeScript
function getIpNeighTable(): Promise<Array<NetIpMacInfo>>
```

Obtain the IP and MAC address correspondence table of the neighboring network.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.GET_NETWORK_INFO and ohos.permission.GET_IP_MAC_INFO

<!--Device-connection-function getIpNeighTable(): Promise<Array<NetIpMacInfo>>--><!--Device-connection-function getIpNeighTable(): Promise<Array<NetIpMacInfo>>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;NetIpMacInfo&gt;&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getIpNeighTable().then((data: connection.NetIpMacInfo[]) => {
  if (data.length !== 0) {
    console.info(`Succeeded to get ipAddress: ${JSON.stringify(data.ipAddress)}`);
    console.info(`Succeeded to get iface: ${JSON.stringify(data.iface)}`);
    console.info(`Succeeded to get macAddress: ${JSON.stringify(data.macAddress)}`);
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to get ip neigh table. Code:${error.code}, message:${error.message}`);
});
```

