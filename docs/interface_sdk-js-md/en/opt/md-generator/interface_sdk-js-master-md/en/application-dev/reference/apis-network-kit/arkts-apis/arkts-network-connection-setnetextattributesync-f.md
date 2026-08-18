# setNetExtAttributeSync

## Modules to Import

```TypeScript
```

## setNetExtAttributeSync

```TypeScript
function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void
```

Set the network extended attribute for a [NetHandle](arkts-network-connection-nethandle-i.md#nethandle) object. To invoke this method, you must have the {@code ohos.permission.SET_NET_EXT_ATTRIBUTE} permission.

**Since:** 20

**Required permissions:** ohos.permission.SET_NET_EXT_ATTRIBUTE

<!--Device-connection-function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void--><!--Device-connection-function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | Yes |
| netExtAttribute | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netExtAttribute: string = "xxx";
let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  connection.setNetExtAttributeSync(netHandle, netExtAttribute);
}
```
