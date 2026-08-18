# setLocationPrivacyConfirmStatus (System API)

## Modules to Import

```TypeScript
```

## setLocationPrivacyConfirmStatus

```TypeScript
function setLocationPrivacyConfirmStatus(type: LocationPrivacyType, isConfirmed: boolean): void
```

Set location privacy protocol confirmation status.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_SECURE_SETTINGS

<!--Device-geoLocationManager-function setLocationPrivacyConfirmStatus(type: LocationPrivacyType, isConfirmed: boolean): void--><!--Device-geoLocationManager-function setLocationPrivacyConfirmStatus(type: LocationPrivacyType, isConfirmed: boolean): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [LocationPrivacyType](arkts-location-geolocation-locationprivacytype-e.md) | Yes |
| [isConfirmed](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.setLocationPrivacyConfirmStatus(1, true);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
