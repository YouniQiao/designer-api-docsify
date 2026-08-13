# getSignalLevel

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## getSignalLevel

```TypeScript
function getSignalLevel(rssi: int, band: int): int
```

Calculate the Wi-Fi signal level based on the Wi-Fi RSSI and frequency band.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function getSignalLevel(rssi: int, band: int): int--><!--Device-wifiManager-function getSignalLevel(rssi: int, band: int): int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rssi | int | Yes | Indicates the Wi-Fi RSSI. |
| band | int | Yes | Indicates the Wi-Fi frequency band. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns Wi-Fi signal level ranging from 0 to 4. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

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

