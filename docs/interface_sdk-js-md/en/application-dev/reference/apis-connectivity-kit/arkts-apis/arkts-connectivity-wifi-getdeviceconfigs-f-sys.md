# getDeviceConfigs (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## getDeviceConfigs

```TypeScript
function getDeviceConfigs(): Array<WifiDeviceConfig>
```

Obtains the list of all existing Wi-Fi configurations.<p>You can obtain only the Wi-Fi configurations you created on your own application.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [getDeviceConfigs](arkts-connectivity-wifimanager-getdeviceconfigs-f.md)

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION and ohos.permission.GET_WIFI_CONFIG

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;WifiDeviceConfig & gt; |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let configs = wifi.getDeviceConfigs();
    console.info("configs:" + JSON.stringify(configs));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
