# ColorModeOptions

Defines the color mode used for current snapshot taking.By default, the system draws snapshot in sRGB mode. Therefore, snapshot for components with wide color display mode enabled will lose some effect. If you know the color space used in the component to be taken snapshot,you can specify the colorSpace parameter and set isAuto to false, for achieving the expected screenshot effect.But it is difficult to know which color space is used by the component to be taken. Therefore, in general,you can just set isAuto to true for letting the system to determine the color space to use based on the actual situation automaticly. When isAuto is set to true, value set by the colorSpace field will be ignored.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-componentSnapshot-export interface ColorModeOptions--><!--Device-componentSnapshot-export interface ColorModeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## colorSpace

```TypeScript
colorSpace?: colorSpaceManager.ColorSpace
```

Set one specific color space which want to be used.

**类型：** colorSpaceManager.ColorSpace

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorModeOptions-colorSpace?: colorSpaceManager.ColorSpace--><!--Device-ColorModeOptions-colorSpace?: colorSpaceManager.ColorSpace-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isAuto

```TypeScript
isAuto?: boolean
```

Indicate that if the system should decide the color space automatically.If set this to true, the one specified by colorSpace parameter will be ignored.

When setting isAuto to true, it is recommended to also set the waitUntilRenderFinished field in SnapshotOptions to true to ensure that the system can properly detect the mode being used.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorModeOptions-isAuto?: boolean--><!--Device-ColorModeOptions-isAuto?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

