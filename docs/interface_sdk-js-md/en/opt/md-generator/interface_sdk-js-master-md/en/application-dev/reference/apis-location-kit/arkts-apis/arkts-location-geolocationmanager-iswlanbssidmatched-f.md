# isWlanBssidMatched

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## isWlanBssidMatched

```TypeScript
function isWlanBssidMatched(
      wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>
```

Check whether the WLAN scan results match the WLAN BSSID list.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-geoLocationManager-function isWlanBssidMatched(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<boolean>--><!--Device-geoLocationManager-function isWlanBssidMatched(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<boolean>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wlanBssidArray | Array & lt;string & gt; | Yes |
| rssiThreshold | number | Yes |
| [needStartScan](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301800](../errorcode-geoLocationManager.md#3301800-failed-to-start-wifi-or-bluetooth-scanning) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let wlanBssidArray: Array<string> = ["02:1b:32:23:ea:91", "02:1b:32:23:ea:93"];
  let rssiThreshold: number = -70;
  let needStartScan: boolean = true;
  geoLocationManager.isWlanBssidMatched(wlanBssidArray, rssiThreshold, needStartScan).then((res) => {
    console.info("Wlan Bssid Matched Result:" + res);
  })
} catch (error) {
  console.error("isWlanBssidMatched: errCode" + error.code + ", errMessage" + error.message);
}
```
