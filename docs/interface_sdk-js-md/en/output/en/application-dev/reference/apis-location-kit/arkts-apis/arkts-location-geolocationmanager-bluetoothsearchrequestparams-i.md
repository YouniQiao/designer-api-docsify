# BluetoothSearchRequestParams

Indicates request parameters for Bluetooth search function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

<!--Device-geoLocationManager-export interface BluetoothSearchRequestParams--><!--Device-geoLocationManager-export interface BluetoothSearchRequestParams-End-->

**System capability:** SystemCapability.Location.Location.Core

## deviceIdArray

```TypeScript
deviceIdArray: Array<string>
```

Indicates the list of Bluetooth device ID that need to be search.

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BluetoothSearchRequestParams-deviceIdArray: Array<string>--><!--Device-BluetoothSearchRequestParams-deviceIdArray: Array<string>-End-->

**System capability:** SystemCapability.Location.Location.Core

## rssiThreshold

```TypeScript
rssiThreshold?: int
```

Indicates the Bluetooth RSSI threshold, only search Bluetooth BSSID with RSSI greater than this threshold. The value range is all integers.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BluetoothSearchRequestParams-rssiThreshold?: int--><!--Device-BluetoothSearchRequestParams-rssiThreshold?: int-End-->

**System capability:** SystemCapability.Location.Location.Core

