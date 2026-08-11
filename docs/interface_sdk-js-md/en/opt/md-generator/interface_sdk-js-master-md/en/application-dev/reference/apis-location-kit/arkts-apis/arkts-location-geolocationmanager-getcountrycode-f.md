# getCountryCode

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getCountryCode

```TypeScript
function getCountryCode(callback: AsyncCallback<CountryCode>): void
```

Obtain the current country code.

**Since:** 9

<!--Device-geoLocationManager-function getCountryCode(callback: AsyncCallback<CountryCode>): void--><!--Device-geoLocationManager-function getCountryCode(callback: AsyncCallback<CountryCode>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CountryCode&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301500](../errorcode-geoLocationManager.md#3301500-area-information-query-failed) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.getCountryCode((err, result) => {
    if (err) {
      console.error('getCountryCode: err=' + JSON.stringify(err));
    }
    if (result) {
      console.info('getCountryCode: result=' + JSON.stringify(result));
    }
  });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## getCountryCode

```TypeScript
function getCountryCode(): Promise<CountryCode>
```

Obtain the current country code.

**Since:** 9

<!--Device-geoLocationManager-function getCountryCode(): Promise<CountryCode>--><!--Device-geoLocationManager-function getCountryCode(): Promise<CountryCode>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CountryCode&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301500](../errorcode-geoLocationManager.md#3301500-area-information-query-failed) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  geoLocationManager.getCountryCode()
    .then((result) => {
      console.info('promise, getCountryCode: result=' + JSON.stringify(result));
    })
    .catch((error: BusinessError) => {
      console.error('promise, getCountryCode: error=' + JSON.stringify(error));
    });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
