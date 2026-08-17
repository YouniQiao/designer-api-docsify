# onBluetoothScanResultChange

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## onBluetoothScanResultChange

```TypeScript
function onBluetoothScanResultChange(callback: Callback<BluetoothScanResult>): void
```

Registers and listens to bluetooth scanning results for location services.

**Since:** 23

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onBluetoothScanResultChange(callback: Callback<BluetoothScanResult>): void--><!--Device-geoLocationManager-function onBluetoothScanResultChange(callback: Callback<BluetoothScanResult>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BluetoothScanResult](arkts-location-geolocationmanager-bluetoothscanresult-i.md)&gt; | Yes | Indicates the callback for reporting Bluetooth scan info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.onBluetoothScanResultChange} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |

