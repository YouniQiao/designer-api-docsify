# stopBluetoothSearch

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## stopBluetoothSearch

```TypeScript
function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void
```

Stop Bluetooth scanning and searching.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void--><!--Device-geoLocationManager-function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[BluetoothScanResult](arkts-location-geolocationmanager-bluetoothscanresult-i.md)&gt; | No | Callback used to return \\${BluetoothScanResult}. It should be the same as the callback passed to \\${geoLocationManager.startBluetoothSearch}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.stopBluetoothSearch} due to limited device capabilities. |
| [3301000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

