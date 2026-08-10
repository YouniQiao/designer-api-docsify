# AdvertiseSetting

Describes the settings for BLE advertising.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ble-interface AdvertiseSetting--><!--Device-ble-interface AdvertiseSetting-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## connectable

```TypeScript
connectable?: boolean
```

Indicates whether the BLE is connectable, default is {@code true}

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdvertiseSetting-connectable?: boolean--><!--Device-AdvertiseSetting-connectable?: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: int
```

Minimum slot value for the advertising interval, which is {@code 32} (20 ms)Maximum slot value for the advertising interval, which is {@code 16777215} (10485.759375s)Default slot value for the advertising interval, which is {@code 1600} (1s)

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdvertiseSetting-interval?: int--><!--Device-AdvertiseSetting-interval?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## isExtended

```TypeScript
isExtended?: boolean
```

Indicates whether the advertisement is extended, default is {@code false}

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AdvertiseSetting-isExtended?: boolean--><!--Device-AdvertiseSetting-isExtended?: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## txPower

```TypeScript
txPower?: int
```

Minimum transmission power level for advertising, which is {@code -127}Maximum transmission power level for advertising, which is {@code 1}Default transmission power level for advertising, which is {@code -7}

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdvertiseSetting-txPower?: int--><!--Device-AdvertiseSetting-txPower?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

