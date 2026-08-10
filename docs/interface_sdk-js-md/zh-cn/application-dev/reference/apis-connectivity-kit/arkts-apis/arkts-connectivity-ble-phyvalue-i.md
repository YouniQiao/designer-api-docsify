# PhyValue

Describes the parameters of the Ble phy.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-ble-interface PhyValue--><!--Device-ble-interface PhyValue-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## phyMode

```TypeScript
phyMode?: CodedPhyMode
```

Preferred coded phy mode.

**类型：** [CodedPhyMode](arkts-connectivity-ble-codedphymode-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhyValue-phyMode?: CodedPhyMode--><!--Device-PhyValue-phyMode?: CodedPhyMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rxPhy

```TypeScript
rxPhy: BlePhy
```

Receiver phy.

**类型：** [BlePhy](arkts-connectivity-ble-blephy-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhyValue-rxPhy: BlePhy--><!--Device-PhyValue-rxPhy: BlePhy-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## txPhy

```TypeScript
txPhy: BlePhy
```

Transmitter phy.

**类型：** [BlePhy](arkts-connectivity-ble-blephy-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhyValue-txPhy: BlePhy--><!--Device-PhyValue-txPhy: BlePhy-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

