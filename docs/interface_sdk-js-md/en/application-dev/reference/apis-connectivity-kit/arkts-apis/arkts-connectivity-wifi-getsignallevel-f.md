# getSignalLevel

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## getSignalLevel

```TypeScript
function getSignalLevel(rssi: number, band: number): number
```

Calculates the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md)

**Required permissions:** ohos.permission.GET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rssi | number | Yes |
| band | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
	let rssi = 0;
	let band = 0;
	let level = wifi.getSignalLevel(rssi,band);
	console.info("level:" + JSON.stringify(level));
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```
