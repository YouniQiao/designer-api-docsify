# findMatchingWlan

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## findMatchingWlan

```TypeScript
function findMatchingWlan(
      wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>
```

Check whether the WLAN scan results match the WLAN BSSID list,return information about the WLAN device that is successfully matched.

**Since:** 26.0.0

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function findMatchingWlan(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>--><!--Device-geoLocationManager-function findMatchingWlan(      wlanBssidArray: Array<string>, rssiThreshold: int, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wlanBssidArray | Array&lt;string&gt; | Yes |
| rssiThreshold | number | Yes |
| needStartScan | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;MatchingWlanInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301800](../errorcode-geoLocationManager.md#3301800-failed-to-start-wifi-or-bluetooth-scanning) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |
