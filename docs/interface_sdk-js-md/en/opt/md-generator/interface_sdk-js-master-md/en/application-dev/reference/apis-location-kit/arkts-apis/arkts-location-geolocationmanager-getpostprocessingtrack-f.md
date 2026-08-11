# getPostProcessingTrack

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getPostProcessingTrack

```TypeScript
function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>
```

Obtain post-processing trajectory information under specific sport mode. Only  
[SKIING](arkts-location-geolocationmanager-sportstype-e.md#skiing) is supported currently.

Before calling this API, you need to call  
[on('locationChange')](geoLocationManager.on('locationChange')) and set the input parameter  
[sportsType](arkts-location-geolocationmanager-continuouslocationrequest-i.md#sportstype) to the specific sport mode to start tracking.

Returns data within 24 hours since tracking started; Subsequent calls return only new records.

**Since:** 26.0.0

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>--><!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sportsType | [SportsType](arkts-location-geolocationmanager-sportstype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Location&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301200](../errorcode-geoLocationManager.md#3301200-failed-to-obtain-the-positioning-result) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |
