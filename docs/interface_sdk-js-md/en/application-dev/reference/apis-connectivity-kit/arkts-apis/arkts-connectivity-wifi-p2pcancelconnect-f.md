# p2pCancelConnect

## Modules to Import

```TypeScript
import wifi from '@kit.ConnectivityKit';
import wifiext from '@kit.ConnectivityKitext';
import wifiManager from '@kit.ConnectivityKitManager';
import wifiManagerExt from '@kit.ConnectivityKitManagerExt';
```

## p2pCancelConnect

```TypeScript
function p2pCancelConnect(): boolean
```

Canceling a P2P connection.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [p2pCancelConnect](arkts-connectivity-wifimanager-p2pcancelconnect-f.md)

**Required permissions:** ohos.permission.GET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.p2pCancelConnect();  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
