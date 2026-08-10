# AdvertisingEnableParams

Parameter for dynamically enable advertising.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ble-interface AdvertisingEnableParams--><!--Device-ble-interface AdvertisingEnableParams-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## advertisingId

```TypeScript
advertisingId: int
```

Indicates the ID of current advertising.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingEnableParams-advertisingId: int--><!--Device-AdvertisingEnableParams-advertisingId: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## duration

```TypeScript
duration?: int
```

Indicates the duration for advertising continuously.The duration, in 10ms unit. Valid range is from 1 (10ms) to 65535 (655,350 ms).If this parameter is not specified or is set to 0, advertise is continuously sent.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingEnableParams-duration?: int--><!--Device-AdvertisingEnableParams-duration?: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

