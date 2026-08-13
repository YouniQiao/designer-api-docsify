# getSignalLevel

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getSignalLevel

```TypeScript
function getSignalLevel(rssi: number, band: number): number
```

Calculate the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getSignalLevel(rssi: int, band: int): int--><!--Device-wifiManager-function getSignalLevel(rssi: int, band: int): int-End-->

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

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let rssi = 0;
    let band = 0;
    let level = wifiManager.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
