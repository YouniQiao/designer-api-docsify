# AdvertisingParams

Describes the advertising parameters.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ble-interface AdvertisingParams--><!--Device-ble-interface AdvertisingParams-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## advertisingData

```TypeScript
advertisingData: AdvertiseData
```

Indicates the advertising data.

**类型：** [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingParams-advertisingData: AdvertiseData--><!--Device-AdvertisingParams-advertisingData: AdvertiseData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## advertisingResponse

```TypeScript
advertisingResponse?: AdvertiseData
```

Indicates the advertising response.

**类型：** [AdvertiseData](arkts-connectivity-bluetoothmanager-advertisedata-i.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingParams-advertisingResponse?: AdvertiseData--><!--Device-AdvertisingParams-advertisingResponse?: AdvertiseData-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## advertisingSettings

```TypeScript
advertisingSettings: AdvertiseSetting
```

Indicates the advertising settings.

**类型：** [AdvertiseSetting](arkts-connectivity-ble-advertisesetting-i.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingParams-advertisingSettings: AdvertiseSetting--><!--Device-AdvertisingParams-advertisingSettings: AdvertiseSetting-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## duration

```TypeScript
duration?: int
```

Indicates the duration for advertising continuously.The duration, in 10ms unit. Valid range is from 1 (10ms) to 65535 (655,350 ms).If this parameter is not specified or is set to 0, advertisement is continuously sent.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingParams-duration?: int--><!--Device-AdvertisingParams-duration?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

