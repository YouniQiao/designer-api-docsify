# offLocationChange

## offLocationChange

```TypeScript
function offLocationChange(callback?: Callback<Location>): void
```

Unsubscribe location changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23 - 24: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void--><!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Location&gt; | No | Indicates the callback for reporting the location result.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. Introduced in API 9 and will not be threw above API 24.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 - 24 |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call \_\_\_ESCAPED\_DOLLAR\_\_\_{geoLocationManager.offLocationChange} due to limited device capabilities.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 23 and later |

