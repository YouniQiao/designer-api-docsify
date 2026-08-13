# offCountryCodeChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offCountryCodeChange

```TypeScript
function offCountryCodeChange(callback?: Callback<CountryCode>): void
```

Unregistering the callback function for listening to country code changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-geoLocationManager-function offCountryCodeChange(callback?: Callback<CountryCode>): void--><!--Device-geoLocationManager-function offCountryCodeChange(callback?: Callback<CountryCode>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CountryCode](arkts-location-geolocationmanager-countrycode-i.md)&gt; | No | Indicates the callback for reporting country code changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offCountryCodeChange} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301500](../errorcode-geoLocationManager.md#3301500-area-information-query-failed) | Failed to query the area information. |

