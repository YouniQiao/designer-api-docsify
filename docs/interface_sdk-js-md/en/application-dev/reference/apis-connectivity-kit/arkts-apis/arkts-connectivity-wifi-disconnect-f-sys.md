# disconnect (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## disconnect

```TypeScript
function disconnect(): boolean
```

Disconnect Wi-Fi network.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [disconnect](arkts-connectivity-wifimanager-disconnect-f.md#disconnect)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function disconnect(): boolean--><!--Device-wifi-function disconnect(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.disconnect();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

