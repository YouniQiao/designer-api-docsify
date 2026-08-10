# AdvertiseSetting

Describes the settings for BLE advertising.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.AdvertiseSetting

<!--Device-bluetoothManager-interface AdvertiseSetting--><!--Device-bluetoothManager-interface AdvertiseSetting-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## connectable

```TypeScript
connectable?: boolean
```

Indicates whether the BLE is connectable, default is {@code true}

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.AdvertiseSetting#connectable

<!--Device-AdvertiseSetting-connectable?: boolean--><!--Device-AdvertiseSetting-connectable?: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Minimum slot value for the advertising interval, which is {@code 32} (20 ms)Maximum slot value for the advertising interval, which is {@code 16777215} (10485.759375s)Default slot value for the advertising interval, which is {@code 1600} (1s)

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.AdvertiseSetting#interval

<!--Device-AdvertiseSetting-interval?: number--><!--Device-AdvertiseSetting-interval?: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## txPower

```TypeScript
txPower?: number
```

Minimum transmission power level for advertising, which is {@code -127}Maximum transmission power level for advertising, which is {@code 1}Default transmission power level for advertising, which is {@code -7}

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.AdvertiseSetting#txPower

<!--Device-AdvertiseSetting-txPower?: number--><!--Device-AdvertiseSetting-txPower?: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

