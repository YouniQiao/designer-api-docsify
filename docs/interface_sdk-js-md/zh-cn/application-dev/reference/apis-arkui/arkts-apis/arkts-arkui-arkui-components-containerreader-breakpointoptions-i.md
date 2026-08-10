# BreakpointOptions

Defines the breakpoint configuration options for container dimension analysis.Specifies threshold values that trigger different layout behaviors based on container size.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface BreakpointOptions--><!--Device-unnamed-export declare interface BreakpointOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from 'kits/@kit.ArkUI';
```

## height

```TypeScript
height?: Array<double>
```

Optional array of height breakpoint values in vp units.Defines the height thresholds for container height analysis.

**类型：** Array&lt;double&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BreakpointOptions-height?: Array<double>--><!--Device-BreakpointOptions-height?: Array<double>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Array<double>
```

Optional array of width breakpoint values in vp units.Defines the width thresholds for container width analysis.

**类型：** Array&lt;double&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BreakpointOptions-width?: Array<double>--><!--Device-BreakpointOptions-width?: Array<double>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

