# isHotspotActive (System API)

## isHotspotActive

```TypeScript
function isHotspotActive(): boolean
```

Checks whether Wi-Fi hotspot is active on a device.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.isHotspotActive

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function isHotspotActive(): boolean--><!--Device-wifi-function isHotspotActive(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Example**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let ret = wifi.isHotspotActive();
    console.info("result:" + ret);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

