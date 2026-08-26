# removeAllNetwork (System API)

## Modules to Import

```TypeScript
import wifi from '@kit.ConnectivityKit';
import wifiext from '@kit.ConnectivityKitext';
import wifiManager from '@kit.ConnectivityKitManager';
import wifiManagerExt from '@kit.ConnectivityKitManagerExt';
```

## removeAllNetwork

```TypeScript
function removeAllNetwork(): boolean
```

Removes all the saved Wi-Fi configurations.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** removeAllDeviceConfigs

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

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
    wifi.removeAllNetwork();        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
