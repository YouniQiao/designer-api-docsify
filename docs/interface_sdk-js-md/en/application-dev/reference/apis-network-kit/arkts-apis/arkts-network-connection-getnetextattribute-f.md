# getNetExtAttribute

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getNetExtAttribute

```TypeScript
function getNetExtAttribute(netHandle: NetHandle): Promise<string>
```

Obtains the extended attributes of the network specified by **netHandle** to determine its security level. This API uses a promise to return the result.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 20

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
