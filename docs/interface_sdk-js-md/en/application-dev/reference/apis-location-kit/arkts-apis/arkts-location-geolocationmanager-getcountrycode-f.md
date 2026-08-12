# getCountryCode

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## getCountryCode

```TypeScript
function getCountryCode(callback: AsyncCallback<CountryCode>): void
```

Obtain the current country code.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-function getCountryCode(callback: AsyncCallback<CountryCode>): void--><!--Device-geoLocationManager-function getCountryCode(callback: AsyncCallback<CountryCode>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[CountryCode](arkts-location-geolocationmanager-countrycode-i.md)&gt; | Yes | Indicates the callback for reporting the country code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.getCountryCode} due to limited device capabilities. |
| [3301000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301500](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301500-area-information-query-failed) | Failed to query the area information. |

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-function getCountryCode(): Promise<CountryCode>--><!--Device-geoLocationManager-function getCountryCode(): Promise<CountryCode>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CountryCode](arkts-location-geolocationmanager-countrycode-i.md)&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.getCountryCode} due to limited device capabilities. |
| [3301000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301500](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301500-area-information-query-failed) | Failed to query the area information. |

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

