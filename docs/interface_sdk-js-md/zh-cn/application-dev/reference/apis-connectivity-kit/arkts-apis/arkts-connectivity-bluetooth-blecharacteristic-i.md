# BLECharacteristic

Describes the Gatt characteristic.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLECharacteristic

<!--Device-bluetooth-interface BLECharacteristic--><!--Device-bluetooth-interface BLECharacteristic-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a BLECharacteristic instance

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLECharacteristic.characteristicUuid

<!--Device-BLECharacteristic-characteristicUuid: string--><!--Device-BLECharacteristic-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## characteristicValue

```TypeScript
characteristicValue: ArrayBuffer
```

The value of a BLECharacteristic instance

**类型：** ArrayBuffer

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLECharacteristic.characteristicValue

<!--Device-BLECharacteristic-characteristicValue: ArrayBuffer--><!--Device-BLECharacteristic-characteristicValue: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptors

```TypeScript
descriptors: Array<BLEDescriptor>
```

The list of {@link BLEDescriptor} contained in the characteristic

**类型：** Array&lt;BLEDescriptor&gt;

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLECharacteristic.descriptors

<!--Device-BLECharacteristic-descriptors: Array<BLEDescriptor>--><!--Device-BLECharacteristic-descriptors: Array<BLEDescriptor>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the {@link GattService} instance to which the characteristic belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.BLECharacteristic.serviceUuid

<!--Device-BLECharacteristic-serviceUuid: string--><!--Device-BLECharacteristic-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

