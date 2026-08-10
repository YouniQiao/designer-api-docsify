# LocatingRequiredData（系统接口）

Describes the structure of the data required for locating.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface LocatingRequiredData--><!--Device-geoLocationManager-export interface LocatingRequiredData-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## bluetoothData

```TypeScript
bluetoothData?: BluetoothScanInfo
```

Bluetooth scan info.

**类型：** [BluetoothScanInfo](arkts-location-geolocationmanager-bluetoothscaninfo-i-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredData-bluetoothData?: BluetoothScanInfo--><!--Device-LocatingRequiredData-bluetoothData?: BluetoothScanInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## campedCellInfo

```TypeScript
campedCellInfo?: CellInfo
```

Indicates camped cell information.

**类型：** [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredData-campedCellInfo?: CellInfo--><!--Device-LocatingRequiredData-campedCellInfo?: CellInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## neighboringCellInfo

```TypeScript
neighboringCellInfo?: CellInfo[]
```

Indicates neighboring cell information.

**类型：** [CellInfo](arkts-location-geolocationmanager-cellinfo-i-sys.md)[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredData-neighboringCellInfo?: CellInfo[]--><!--Device-LocatingRequiredData-neighboringCellInfo?: CellInfo[]-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## slotId

```TypeScript
slotId?: int
```

Indicates the card slot index number.The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LocatingRequiredData-slotId?: int--><!--Device-LocatingRequiredData-slotId?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## wifiData

```TypeScript
wifiData?: WifiScanInfo
```

WiFi scan info.

**类型：** [WifiScanInfo](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-wifi-wifiscaninfo-i.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-LocatingRequiredData-wifiData?: WifiScanInfo--><!--Device-LocatingRequiredData-wifiData?: WifiScanInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

