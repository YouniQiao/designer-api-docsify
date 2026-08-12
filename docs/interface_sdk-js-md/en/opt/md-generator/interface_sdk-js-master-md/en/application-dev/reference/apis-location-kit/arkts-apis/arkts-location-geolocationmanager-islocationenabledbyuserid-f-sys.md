# isLocationEnabledByUserId (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## isLocationEnabledByUserId

```TypeScript
function isLocationEnabledByUserId(userId: number): boolean
```

Obtaining the location switch status of a specified user.

**Since:** 18

<!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean--><!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  // Check whether the location switch is enabled for the specified system account. For example, if the account ID is below 101, you can check whether the location switch is enabled for the account whose ID is 100.
  let userId: number = 100;
  let locationEnabled = geoLocationManager.isLocationEnabledByUserId(userId);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
