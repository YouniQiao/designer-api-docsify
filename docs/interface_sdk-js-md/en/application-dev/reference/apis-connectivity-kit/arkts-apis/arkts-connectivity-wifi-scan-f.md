# scan

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## scan

```TypeScript
function scan(): boolean
```

Scans Wi-Fi hotspot.

&lt;p&gt;This API works in asynchronous mode.&lt;/p&gt;

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.scan

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function scan(): boolean--><!--Device-wifi-function scan(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.scan();
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```

