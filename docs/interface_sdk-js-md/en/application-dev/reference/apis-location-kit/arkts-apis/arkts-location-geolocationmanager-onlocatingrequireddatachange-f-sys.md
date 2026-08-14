# onLocatingRequiredDataChange (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## onLocatingRequiredDataChange

```TypeScript
function onLocatingRequiredDataChange(config: LocatingRequiredDataConfig, 
      callback: Callback<Array<LocatingRequiredData>>): void
```

Subscribe to changes in WiFi/BT scanning information, and use the WiFi/BT scanning information for localization.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onLocatingRequiredDataChange(config: LocatingRequiredDataConfig,       callback: Callback<Array<LocatingRequiredData>>): void--><!--Device-geoLocationManager-function onLocatingRequiredDataChange(config: LocatingRequiredDataConfig,       callback: Callback<Array<LocatingRequiredData>>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [LocatingRequiredDataConfig](arkts-location-geolocationmanager-locatingrequireddataconfig-i-sys.md) | Yes | Indicates the locating required data configuration parameters. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[LocatingRequiredData](arkts-location-geolocationmanager-locatingrequireddata-i-sys.md)&gt;&gt; | Yes | Indicates the callback for reporting WiFi/BT scan info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.onLocatingRequiredDataChange} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301800](../errorcode-geoLocationManager.md#3301800-failed-to-start-wifi-or-bluetooth-scanning) | Failed to start WiFi or Bluetooth scanning. |

