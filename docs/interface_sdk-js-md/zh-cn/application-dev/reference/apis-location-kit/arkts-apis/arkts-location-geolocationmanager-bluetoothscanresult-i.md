# BluetoothScanResult

Describes the contents of the bluetooth scan results.

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface BluetoothScanResult--><!--Device-geoLocationManager-export interface BluetoothScanResult-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## connectable

```TypeScript
connectable: boolean
```

Connectable of the scanned device

**类型：** boolean

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanResult-connectable: boolean--><!--Device-BluetoothScanResult-connectable: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Core

## data

```TypeScript
data?: ArrayBuffer
```

The raw data of broadcast packet

**类型：** ArrayBuffer

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanResult-data?: ArrayBuffer--><!--Device-BluetoothScanResult-data?: ArrayBuffer-End-->

**系统能力：** SystemCapability.Location.Location.Core

## deviceId

```TypeScript
deviceId: string
```

Address of the scanned device

**类型：** string

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanResult-deviceId: string--><!--Device-BluetoothScanResult-deviceId: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

## deviceName

```TypeScript
deviceName: string
```

The local name of the scanned device

**类型：** string

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanResult-deviceName: string--><!--Device-BluetoothScanResult-deviceName: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

## rssi

```TypeScript
rssi: int
```

RSSI of the scanned device

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanResult-rssi: int--><!--Device-BluetoothScanResult-rssi: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

