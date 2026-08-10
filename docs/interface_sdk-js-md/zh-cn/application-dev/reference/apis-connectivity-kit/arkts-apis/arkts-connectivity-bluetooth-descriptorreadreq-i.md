# DescriptorReadReq

Describes the parameters of the Gatt client's descriptor read request.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest

<!--Device-bluetooth-interface DescriptorReadReq--><!--Device-bluetooth-interface DescriptorReadReq-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.characteristicUuid

<!--Device-DescriptorReadReq-characteristicUuid: string--><!--Device-DescriptorReadReq-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorReadReq instance

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.descriptorUuid

<!--Device-DescriptorReadReq-descriptorUuid: string--><!--Device-DescriptorReadReq-descriptorUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.deviceId

<!--Device-DescriptorReadReq-deviceId: string--><!--Device-DescriptorReadReq-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**类型：** number

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.offset

<!--Device-DescriptorReadReq-offset: number--><!--Device-DescriptorReadReq-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.serviceUuid

<!--Device-DescriptorReadReq-serviceUuid: string--><!--Device-DescriptorReadReq-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**类型：** number

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorReadRequest.transId

<!--Device-DescriptorReadReq-transId: number--><!--Device-DescriptorReadReq-transId: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

