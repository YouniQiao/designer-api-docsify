# p2pCancelConnect

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## p2pCancelConnect

```TypeScript
function p2pCancelConnect(): boolean
```

Canceling a P2P connection.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.p2pCancelConnect

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function p2pCancelConnect(): boolean--><!--Device-wifi-function p2pCancelConnect(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.p2pCancelConnect();  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
