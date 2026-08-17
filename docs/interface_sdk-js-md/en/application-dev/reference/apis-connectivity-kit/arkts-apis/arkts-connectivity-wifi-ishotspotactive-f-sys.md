# isHotspotActive (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## isHotspotActive

```TypeScript
function isHotspotActive(): boolean
```

Checks whether Wi-Fi hotspot is active on a device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isHotspotActive](arkts-connectivity-wifimanager-ishotspotactive-f.md#ishotspotactive)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function isHotspotActive(): boolean--><!--Device-wifi-function isHotspotActive(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let ret = wifi.isHotspotActive();
    console.info("result:" + ret);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

