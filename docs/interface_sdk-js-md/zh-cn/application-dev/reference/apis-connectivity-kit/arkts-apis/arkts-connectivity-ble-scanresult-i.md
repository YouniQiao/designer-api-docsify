# ScanResult

Describes the contents of the scan results.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface ScanResult--><!--Device-ble-interface ScanResult-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address?: BluetoothAddress
```

The address object of a BLE peripheral device, including the address type.

**类型：** [BluetoothAddress](arkts-connectivity-ble-bluetoothaddress-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScanResult-address?: BluetoothAddress--><!--Device-ScanResult-address?: BluetoothAddress-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## advertiseFlags

```TypeScript
advertiseFlags?: int
```

This field is used to identify the discovery mode and supported capabilities of the peer device.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-advertiseFlags?: int--><!--Device-ScanResult-advertiseFlags?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## advertisingDataMap

```TypeScript
advertisingDataMap?: Map<int, Uint8Array>
```

Map of advertising data fields.

**类型：** ArkTS-Dyn: Map&lt;number, Uint8Array&gt;  <br>ArkTS-Sta：Map&lt;int, Uint8Array&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-advertisingDataMap?: Map<int, Uint8Array>--><!--Device-ScanResult-advertisingDataMap?: Map<int, Uint8Array>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## connectable

```TypeScript
connectable: boolean
```

Connectable of the remote device

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-connectable: boolean--><!--Device-ScanResult-connectable: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## data

```TypeScript
data: ArrayBuffer
```

The raw data of broadcast packet

**类型：** ArrayBuffer

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-data: ArrayBuffer--><!--Device-ScanResult-data: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Address of the scanned device

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-deviceId: string--><!--Device-ScanResult-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceName

```TypeScript
deviceName: string
```

The local name of the BLE device

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-deviceName: string--><!--Device-ScanResult-deviceName: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## manufacturerDataMap

```TypeScript
manufacturerDataMap?: Map<int, Uint8Array>
```

Map of manufacturer data.

**类型：** ArkTS-Dyn: Map&lt;number, Uint8Array&gt;  <br>ArkTS-Sta：Map&lt;int, Uint8Array&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-manufacturerDataMap?: Map<int, Uint8Array>--><!--Device-ScanResult-manufacturerDataMap?: Map<int, Uint8Array>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rssi

```TypeScript
rssi: int
```

RSSI of the remote device

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-rssi: int--><!--Device-ScanResult-rssi: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceDataMap

```TypeScript
serviceDataMap?: Map<string, Uint8Array>
```

Map of service data.

**类型：** Map&lt;string, Uint8Array&gt;

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-serviceDataMap?: Map<string, Uint8Array>--><!--Device-ScanResult-serviceDataMap?: Map<string, Uint8Array>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuids

```TypeScript
serviceUuids?: string[]
```

The list of service uuid.

**类型：** string[]

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-serviceUuids?: string[]--><!--Device-ScanResult-serviceUuids?: string[]-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## txPowerLevel

```TypeScript
txPowerLevel?: int
```

The tx power level of the packet in dBm.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-ScanResult-txPowerLevel?: int--><!--Device-ScanResult-txPowerLevel?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

