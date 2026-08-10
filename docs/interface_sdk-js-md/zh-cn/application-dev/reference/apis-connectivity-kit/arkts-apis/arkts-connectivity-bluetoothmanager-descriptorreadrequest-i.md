# DescriptorReadRequest

Describes the parameters of the Gatt client's descriptor read request.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest

<!--Device-bluetoothManager-interface DescriptorReadRequest--><!--Device-bluetoothManager-interface DescriptorReadRequest-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#characteristicUuid

<!--Device-DescriptorReadRequest-characteristicUuid: string--><!--Device-DescriptorReadRequest-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorReadRequest instance

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#descriptorUuid

<!--Device-DescriptorReadRequest-descriptorUuid: string--><!--Device-DescriptorReadRequest-descriptorUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#deviceId

<!--Device-DescriptorReadRequest-deviceId: string--><!--Device-DescriptorReadRequest-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#offset

<!--Device-DescriptorReadRequest-offset: number--><!--Device-DescriptorReadRequest-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#serviceUuid

<!--Device-DescriptorReadRequest-serviceUuid: string--><!--Device-DescriptorReadRequest-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorReadRequest#transId

<!--Device-DescriptorReadRequest-transId: number--><!--Device-DescriptorReadRequest-transId: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

