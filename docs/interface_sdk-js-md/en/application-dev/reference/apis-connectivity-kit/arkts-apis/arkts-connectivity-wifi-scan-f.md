# scan

## scan

```TypeScript
function scan(): boolean
```

Scans Wi-Fi hotspot.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This API works in asynchronous mode.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

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

**Example**

```TypeScript
import wifi from '@ohos.wifi';

try {
	wifi.scan();
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```

