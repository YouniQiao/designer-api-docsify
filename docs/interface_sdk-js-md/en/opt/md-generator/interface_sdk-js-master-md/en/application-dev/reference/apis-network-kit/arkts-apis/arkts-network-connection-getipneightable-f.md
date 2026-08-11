# getIpNeighTable

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getIpNeighTable

```TypeScript
function getIpNeighTable(): Promise<Array<NetIpMacInfo>>
```

Obtain the IP and MAC address correspondence table of the neighboring network.

**Since:** 22

**Required permissions:** ohos.permission.GET_NETWORK_INFO and ohos.permission.GET_IP_MAC_INFO

<!--Device-connection-function getIpNeighTable(): Promise<Array<NetIpMacInfo>>--><!--Device-connection-function getIpNeighTable(): Promise<Array<NetIpMacInfo>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;NetIpMacInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getIpNeighTable().then((data: connection.NetIpMacInfo[]) => {
  if (data.length !== 0) {
    console.info(`ipAddress:${data[0].ipAddress}`);
    console.info(`ifaceName:${data[0].iface}`);
    console.info(`macAddress:${data[0].macAddress}`);
  }
}).catch((error: BusinessError) => {
  console.error(`error fetching ip neigh table. Code:${error.code}, message:${error.message}`);
});
```
