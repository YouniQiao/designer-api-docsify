# flushCachedGnssLocations

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(callback: AsyncCallback<void>): void
```

All prepared GNSS locations are returned to the application through the callback function,and the bottom-layer buffer is cleared.

**Since:** 9

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function flushCachedGnssLocations(callback: AsyncCallback<void>): void--><!--Device-geoLocationManager-function flushCachedGnssLocations(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301200](../errorcode-geoLocationManager.md#3301200-failed-to-obtain-the-positioning-result) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.flushCachedGnssLocations((err) => {
    if (err) {
      console.error('flushCachedGnssLocations: err=' + JSON.stringify(err));
    }
  });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(): Promise<void>
```

All prepared GNSS locations are returned to the application,and the bottom-layer buffer is cleared.

**Since:** 9

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function flushCachedGnssLocations(): Promise<void>--><!--Device-geoLocationManager-function flushCachedGnssLocations(): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301200](../errorcode-geoLocationManager.md#3301200-failed-to-obtain-the-positioning-result) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  geoLocationManager.flushCachedGnssLocations().then(() => {
    console.info('promise, flushCachedGnssLocations success');
  })
    .catch((error: BusinessError) => {
      console.error('promise, flushCachedGnssLocations: error=' + JSON.stringify(error));
    });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
