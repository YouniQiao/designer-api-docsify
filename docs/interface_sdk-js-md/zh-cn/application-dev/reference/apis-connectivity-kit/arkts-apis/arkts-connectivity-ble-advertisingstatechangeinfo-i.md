# AdvertisingStateChangeInfo

Advertising state change information.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-ble-interface AdvertisingStateChangeInfo--><!--Device-ble-interface AdvertisingStateChangeInfo-End-->

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

<!--Device-AdvertisingStateChangeInfo-advertisingId: int--><!--Device-AdvertisingStateChangeInfo-advertisingId: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: AdvertisingState
```

Indicates the advertising state.

**类型：** [AdvertisingState](arkts-connectivity-ble-advertisingstate-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AdvertisingStateChangeInfo-state: AdvertisingState--><!--Device-AdvertisingStateChangeInfo-state: AdvertisingState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

