# RangingResult

Describes the contents of the ranging results.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-ranging-interface RangingResult--><!--Device-ranging-interface RangingResult-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## angle

```TypeScript
angle: RangingMeasurement
```

Azimuth angle output from ranging.

**类型：** [RangingMeasurement](arkts-connectivity-ranging-rangingmeasurement-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingResult-angle: RangingMeasurement--><!--Device-RangingResult-angle: RangingMeasurement-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## deviceId

```TypeScript
deviceId: string
```

Address of the ranging device.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingResult-deviceId: string--><!--Device-RangingResult-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## distance

```TypeScript
distance: RangingMeasurement
```

The distance measured by the ranging output.

**类型：** [RangingMeasurement](arkts-connectivity-ranging-rangingmeasurement-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingResult-distance: RangingMeasurement--><!--Device-RangingResult-distance: RangingMeasurement-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## rssi

```TypeScript
rssi: int
```

Received signal strength.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingResult-rssi: int--><!--Device-RangingResult-rssi: int-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

