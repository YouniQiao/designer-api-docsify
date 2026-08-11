# on (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## on('locatingRequiredDataChange')

```TypeScript
function on(type: 'locatingRequiredDataChange', config: LocatingRequiredDataConfig, 
      callback: Callback<Array<LocatingRequiredData>>): void
```

Subscribe to changes in WiFi/BT scanning information,and use the WiFi/BT scanning information for localization.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function on(type: 'locatingRequiredDataChange', config: LocatingRequiredDataConfig,       callback: Callback<Array<LocatingRequiredData>>): void--><!--Device-geoLocationManager-function on(type: 'locatingRequiredDataChange', config: LocatingRequiredDataConfig,       callback: Callback<Array<LocatingRequiredData>>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'locatingRequiredDataChange' | Yes | Indicates the location service event to be subscribed to. |
| config | [LocatingRequiredDataConfig](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) | Yes | Indicates the locating required data configuration parameters. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;LocatingRequiredData&gt;&gt; | Yes | Indicates the callback for reporting WiFi/BT scan info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.on('locatingRequiredDataChange')} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301800](../errorcode-geoLocationManager.md#3301800-failed-to-start-wifi-or-bluetooth-scanning) | Failed to start WiFi or Bluetooth scanning. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code: Array<geoLocationManager.LocatingRequiredData>): void => {
  console.info('locatingRequiredDataChange: ' + JSON.stringify(code));
}
let config: geoLocationManager.LocatingRequiredDataConfig = { 'type': 1, 'needStartScan': true, 'scanInterval': 10000 };
try {
  geoLocationManager.on('locatingRequiredDataChange', config, callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## on('locationIconStatusChange')

```TypeScript
function on(type: 'locationIconStatusChange', callback: Callback<LocationIconStatus>): void
```

Subscribe location icon status changed.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-geoLocationManager-function on(type: 'locationIconStatusChange', callback: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function on(type: 'locationIconStatusChange', callback: Callback<LocationIconStatus>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'locationIconStatusChange' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LocationIconStatus&gt; | Yes | Indicates the callback for reporting the location icon status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.on(' locationIconStatusChange')} due to limited device capabilities. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let callback = (code: geoLocationManager.LocationIconStatus): void => {
  console.info('LocationIconStatus: ' + JSON.stringify(code));
}
try {
  geoLocationManager.on('locationIconStatusChange', callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

