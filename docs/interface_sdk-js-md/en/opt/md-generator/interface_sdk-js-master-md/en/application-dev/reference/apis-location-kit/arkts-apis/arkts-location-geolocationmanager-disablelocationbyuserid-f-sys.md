# disableLocationByUserId (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## disableLocationByUserId

```TypeScript
function disableLocationByUserId(userId: number): void
```

Turn off the location switch for a specified user.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_SECURE_SETTINGS and ohos.permission.CONTROL_LOCATION_SWITCH

<!--Device-geoLocationManager-function disableLocationByUserId(userId: int): void--><!--Device-geoLocationManager-function disableLocationByUserId(userId: int): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  // Disable the location switch for the specified system account. For example, if the account ID is below 101, you can disable the location switch for the account whose ID is 100.
  let userId: number = 100;
  geoLocationManager.disableLocationByUserId(userId);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
