# isLocationEnabledByUserId (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## isLocationEnabledByUserId

```TypeScript
function isLocationEnabledByUserId(userId: int): boolean
```

Obtaining the location switch status of a specified user.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean--><!--Device-geoLocationManager-function isLocationEnabledByUserId(userId: int): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of a specified user. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.isLocationEnabledByUserId} due to limited device capabilities. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

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

