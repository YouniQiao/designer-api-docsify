# BluetoothScanInfo（系统接口）

Describes the contents of the Bluetooth scan results.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface BluetoothScanInfo--><!--Device-geoLocationManager-export interface BluetoothScanInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## deviceName

```TypeScript
deviceName: string
```

The local name of the device.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanInfo-deviceName: string--><!--Device-BluetoothScanInfo-deviceName: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## macAddress

```TypeScript
macAddress: string
```

Mac address of the scanned device.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanInfo-macAddress: string--><!--Device-BluetoothScanInfo-macAddress: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## rssi

```TypeScript
rssi: int
```

RSSI of the remote device.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanInfo-rssi: int--><!--Device-BluetoothScanInfo-rssi: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timestamp

```TypeScript
timestamp: long
```

Time stamp.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-BluetoothScanInfo-timestamp: long--><!--Device-BluetoothScanInfo-timestamp: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

