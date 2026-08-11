# getNetExtAttribute

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getNetExtAttribute

```TypeScript
function getNetExtAttribute(netHandle: NetHandle): Promise<string>
```

Get the network extended attribute for a {@link NetHandle} object.To invoke this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 20

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getNetExtAttribute(netHandle: NetHandle): Promise<string>--><!--Device-connection-function getNetExtAttribute(netHandle: NetHandle): Promise<string>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetExtAttribute(netHandle).then((netExtAttribute: string) => {
    console.info("getNetExtAttribute: " + netExtAttribute);
  }).catch((error: BusinessError) => {
    console.error("getNetExtAttribute failed, err: " + error.code);
  })
});
```
