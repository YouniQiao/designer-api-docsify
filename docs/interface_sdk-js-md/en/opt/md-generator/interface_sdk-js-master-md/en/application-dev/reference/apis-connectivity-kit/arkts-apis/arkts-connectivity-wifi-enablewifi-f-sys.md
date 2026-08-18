# enableWifi (System API)

## Modules to Import

```TypeScript
```

## enableWifi

```TypeScript
function enableWifi(): boolean
```

Enables Wi-Fi.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [enableWifi](arkts-connectivity-wifimanager-enablewifi-f.md#enablewifi)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function enableWifi(): boolean--><!--Device-wifi-function enableWifi(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.enableWifi();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
