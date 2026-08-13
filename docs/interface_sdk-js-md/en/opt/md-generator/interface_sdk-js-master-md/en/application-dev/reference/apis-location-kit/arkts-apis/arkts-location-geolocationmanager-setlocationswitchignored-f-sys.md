# setLocationSwitchIgnored (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## setLocationSwitchIgnored

```TypeScript
function setLocationSwitchIgnored(isIgnored: boolean): void
```

Set the app locating behavior not controlled by the location switch.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION_SWITCH_IGNORED

<!--Device-geoLocationManager-function setLocationSwitchIgnored(isIgnored: boolean): void--><!--Device-geoLocationManager-function setLocationSwitchIgnored(isIgnored: boolean): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isIgnored | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isIgnored: boolean = true;
  geoLocationManager.setLocationSwitchIgnored(isIgnored);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
