# OobData（系统接口）

Out Of Band data used in Bluetooth device pairing.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-connection-interface OobData--><!--Device-connection-interface OobData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## confirmationHash

```TypeScript
confirmationHash: Uint8Array
```

Confirmation data in OOB pairing, with a size of 16 octets.

**类型：** Uint8Array

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OobData-confirmationHash: Uint8Array--><!--Device-OobData-confirmationHash: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceId

```TypeScript
deviceId: BluetoothAddress
```

The address of remote Bluetooth device.

**类型：** [BluetoothAddress](arkts-connectivity-ble-bluetoothaddress-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OobData-deviceId: BluetoothAddress--><!--Device-OobData-deviceId: BluetoothAddress-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceName

```TypeScript
deviceName?: string
```

The name of the remote Bluetooth device.

**类型：** string

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OobData-deviceName?: string--><!--Device-OobData-deviceName?: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## deviceRole

```TypeScript
deviceRole?: DeviceRole
```

The role of the remote Bluetooth device.

**类型：** [DeviceRole](../../apis-audio-kit/arkts-apis/arkts-audio-audio-devicerole-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OobData-deviceRole?: DeviceRole--><!--Device-OobData-deviceRole?: DeviceRole-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## randomizerHash

```TypeScript
randomizerHash?: Uint8Array
```

Randomizer data in OOB pairing, with a size of 16 octets.

**类型：** Uint8Array

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OobData-randomizerHash?: Uint8Array--><!--Device-OobData-randomizerHash?: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

