# DynamicRangeModeOptions

Defines the dynamic range mode used for current snapshot taking.By default, the system draws snapshot in STANDARD mode. You can set the dynamicRangeMode parameter and set isAuto to false, for using one specific dynamic range mode.Also you can just set isAuto to true for letting the system to determine the dynamic range mode automaticly.When isAuto is set to true, value set by the dynamicRangeMode field will be ignored.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-componentSnapshot-export interface DynamicRangeModeOptions--><!--Device-componentSnapshot-export interface DynamicRangeModeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeMode
```

Set one specific dynamic range mode that you want to use.

**类型：** [DynamicRangeMode](../arkts-components/arkts-arkui-dynamicrangemode-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DynamicRangeModeOptions-dynamicRangeMode?: DynamicRangeMode--><!--Device-DynamicRangeModeOptions-dynamicRangeMode?: DynamicRangeMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isAuto

```TypeScript
isAuto?: boolean
```

Indicate that if the system should decide the dynamic range mode automatically.If set this to true, the one specified by dynamicRangeMode parameter will be ignored.

When setting isAuto to true, it is recommended to also set the waitUntilRenderFinished field in SnapshotOptions to true to ensure that the system can properly detect the mode being used.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DynamicRangeModeOptions-isAuto?: boolean--><!--Device-DynamicRangeModeOptions-isAuto?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

