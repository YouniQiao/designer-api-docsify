# isLocationPrivacyConfirmed (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## isLocationPrivacyConfirmed

```TypeScript
function isLocationPrivacyConfirmed(type: LocationPrivacyType): boolean
```

Querying location privacy protocol confirmation status.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-geoLocationManager-function isLocationPrivacyConfirmed(type: LocationPrivacyType): boolean--><!--Device-geoLocationManager-function isLocationPrivacyConfirmed(type: LocationPrivacyType): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | LocationPrivacyType | Yes | Indicates location privacy protocol type. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${ geoLocationManager.isLocationPrivacyConfirmed} due to limited device capabilities. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isConfirmed = geoLocationManager.isLocationPrivacyConfirmed(1);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

