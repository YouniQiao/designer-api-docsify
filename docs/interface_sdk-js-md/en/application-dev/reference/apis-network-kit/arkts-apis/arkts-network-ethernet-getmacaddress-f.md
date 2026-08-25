# getMacAddress

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## getMacAddress

```TypeScript
function getMacAddress(): Promise<Array<MacAddressInfo>>
```

Obtains the names and MAC addresses of all Ethernet NICs. This API uses a promise to return the result.  
**Required permission**: ohos.permission.GET_ETHERNET_LOCAL_MAC

**Since:** 14

**Required permissions:** ohos.permission.GET_ETHERNET_LOCAL_MAC

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MacAddressInfo](arkts-network-ethernet-macaddressinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2201005](../errorcode-net-ethernet.md#2201005-device-information-not-exist) |
