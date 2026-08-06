# enableWifi (System API)

## enableWifi

```TypeScript
function enableWifi(): boolean
```

Enables Wi-Fi.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.enableWifi

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function enableWifi(): boolean--><!--Device-wifi-function enableWifi(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Example**

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.enableWifi();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

