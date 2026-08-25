# getSystemNetPortStates

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getSystemNetPortStates

```TypeScript
function getSystemNetPortStates(): Promise<NetPortStatesInfo>
```

Obtains information about all TCP and UDP ports currently listened by the system, and the PID and UID of the processes that listen for the ports. Both IPv4 and IPv6 addresses are supported.

> **NOTE：**&gt;
> This API is used to obtain information about the TCP and UDP ports currently listened by the system. The detailed
> fields are as follows:&gt;
> TCP port fields: local address, local port, remote address, remote port, TCP connection status, process PID, and
> process UID&gt;
> UDP port fields: local address, local port, process PID, and process UID

**Since:** 24

**Required permissions:** ohos.permission.GET_IP_MAC_INFO

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[NetPortStatesInfo](arkts-network-connection-netportstatesinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
