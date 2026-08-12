# LocatingRequiredData (System API)

Describes the structure of the data required for locating.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface LocatingRequiredData--><!--Device-geoLocationManager-export interface LocatingRequiredData-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## bluetoothData

```TypeScript
bluetoothData?: BluetoothScanInfo
```

Bluetooth scan info.

**Type:** [BluetoothScanInfo](arkts-location-geolocationmanager-bluetoothscaninfo-i-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-LocatingRequiredData-bluetoothData?: BluetoothScanInfo--><!--Device-LocatingRequiredData-bluetoothData?: BluetoothScanInfo-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## campedCellInfo

```TypeScript
campedCellInfo?: CellInfo
```

Indicates camped cell information.

**Type:** [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocatingRequiredData-campedCellInfo?: CellInfo--><!--Device-LocatingRequiredData-campedCellInfo?: CellInfo-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## neighboringCellInfo

```TypeScript
neighboringCellInfo?: CellInfo[]
```

Indicates neighboring cell information.

**Type:** [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocatingRequiredData-neighboringCellInfo?: CellInfo[]--><!--Device-LocatingRequiredData-neighboringCellInfo?: CellInfo[]-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## slotId

```TypeScript
slotId?: int
```

Indicates the card slot index number.The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocatingRequiredData-slotId?: int--><!--Device-LocatingRequiredData-slotId?: int-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

## wifiData

```TypeScript
wifiData?: WifiScanInfo
```

WiFi scan info.

**Type:** WifiScanInfo

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-LocatingRequiredData-wifiData?: WifiScanInfo--><!--Device-LocatingRequiredData-wifiData?: WifiScanInfo-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

