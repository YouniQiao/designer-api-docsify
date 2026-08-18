# getSignalLevel

## Modules to Import

```TypeScript
```

## getSignalLevel

```TypeScript
function getSignalLevel(rssi: number, band: number): number
```

Calculates the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getSignalLevel](arkts-connectivity-wifimanager-getsignallevel-f.md#getsignallevel)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getSignalLevel(rssi: number, band: number): number--><!--Device-wifi-function getSignalLevel(rssi: number, band: number): number-End-->

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
