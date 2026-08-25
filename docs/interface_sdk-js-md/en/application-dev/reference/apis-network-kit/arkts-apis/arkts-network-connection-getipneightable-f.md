# getIpNeighTable

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getIpNeighTable

```TypeScript
function getIpNeighTable(): Promise<Array<NetIpMacInfo>>
```

Obtains information about entries in the IP neighbor table of the local device, including IPv4 and IPv6 entries. Each entry contains an IP address, a MAC address, and a network adapter name. This API uses a promise to return the result.

> **NOTE：**&gt;
> This interface is used to obtain the cached data of the IP neighbor table, not the data of all connections on the
> LAN.&gt;
> This API is used to check network exceptions and parse the mapping between IP addresses and MAC addresses.

**Since:** 22

**Required permissions:** ohos.permission.GET_NETWORK_INFO and ohos.permission.GET_IP_MAC_INFO

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[NetIpMacInfo](arkts-network-connection-netipmacinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
