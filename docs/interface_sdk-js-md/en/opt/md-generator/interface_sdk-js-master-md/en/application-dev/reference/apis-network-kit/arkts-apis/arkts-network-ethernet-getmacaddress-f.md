# getMacAddress

## Modules to Import

```TypeScript
import { ethernet } from '@kit.NetworkKit';
```

## getMacAddress

```TypeScript
function getMacAddress(): Promise<Array<MacAddressInfo>>
```

Get the ethernet mac address list.

**Since:** 14

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_ETHERNET_LOCAL_MAC

<!--Device-ethernet-function getMacAddress(): Promise<Array<MacAddressInfo>>--><!--Device-ethernet-function getMacAddress(): Promise<Array<MacAddressInfo>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MacAddressInfo](arkts-network-ethernet-macaddressinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2201005](../errorcode-net-ethernet.md#2201005-device-information-not-exist) |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getMacAddress().then((data: Array<ethernet.MacAddressInfo>) => {
  console.info("getMacAddress promise data = " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error("getMacAddress promise error = " + JSON.stringify(error));
});
```
