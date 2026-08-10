# RangingMeasurement

Describes the measurement result.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-ranging-interface RangingMeasurement--><!--Device-ranging-interface RangingMeasurement-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## confidence

```TypeScript
confidence: RangingConfidence
```

Confidence level of measurement results.

**类型：** [RangingConfidence](arkts-connectivity-ranging-rangingconfidence-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingMeasurement-confidence: RangingConfidence--><!--Device-RangingMeasurement-confidence: RangingConfidence-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## value

```TypeScript
value: int
```

Measurement result value. The value is expressed in centimeters.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingMeasurement-value: int--><!--Device-RangingMeasurement-value: int-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

