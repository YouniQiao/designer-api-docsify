# getConnectionPropertiesSync

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getConnectionPropertiesSync

```TypeScript
function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties
```

Queries the connection properties of a network.This method requires the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 10

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties--><!--Device-connection-function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConnectionProperties](arkts-network-connection-connectionproperties-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle: connection.NetHandle;
let connectionproperties: connection.ConnectionProperties;

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  netHandle = connection.getDefaultNetSync();
  connectionproperties = connection.getConnectionPropertiesSync(netHandle);
  console.info("Succeeded to get connectionproperties: " + JSON.stringify(connectionproperties));
});
```
