# onLocationChange

## onLocationChange

```TypeScript
function onLocationChange(request: LocationRequest | ContinuousLocationRequest,
  callback: Callback<Location>): void
```

Subscribe location changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void--><!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ContinuousLocationRequest | Yes | Indicates the location request parameters.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 23 |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Location&gt; | Yes | Indicates the callback for reporting the location result.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call \_\_\_ESCAPED\_DOLLAR\_\_\_{geoLocationManager.onLocationChange} due to limited device capabilities.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |

