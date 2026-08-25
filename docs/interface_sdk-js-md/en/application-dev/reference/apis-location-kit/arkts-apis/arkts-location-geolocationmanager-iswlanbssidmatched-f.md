# isWlanBssidMatched

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isWlanBssidMatched

```TypeScript
function isWlanBssidMatched(
      wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>
```

Check whether the WLAN scan results match the WLAN BSSID list.

**Since:** 21

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 21.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |
| [3301800](../errorcode-geoLocationManager.md#3301800-failed-to-start-wi-fi-or-bluetooth-scanning) |
