# RangingStateChangeInfo

Describes the ranging state change information.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-ranging-interface RangingStateChangeInfo--><!--Device-ranging-interface RangingStateChangeInfo-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## cause

```TypeScript
cause: RangingStoppedCause
```

Cause of ranging stop.

**类型：** [RangingStoppedCause](arkts-connectivity-ranging-rangingstoppedcause-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingStateChangeInfo-cause: RangingStoppedCause--><!--Device-RangingStateChangeInfo-cause: RangingStoppedCause-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## deviceId

```TypeScript
deviceId?: string
```

Address of the ranging device.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingStateChangeInfo-deviceId?: string--><!--Device-RangingStateChangeInfo-deviceId?: string-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## handle

```TypeScript
handle?: int
```

Indicates the handle number of ranging monitoring.The value should be an integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingStateChangeInfo-handle?: int--><!--Device-RangingStateChangeInfo-handle?: int-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## state

```TypeScript
state: RangingState
```

Ranging state.

**类型：** [RangingState](arkts-connectivity-ranging-rangingstate-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangingStateChangeInfo-state: RangingState--><!--Device-RangingStateChangeInfo-state: RangingState-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

