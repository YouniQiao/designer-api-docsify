# PickedColorInfo

```TypeScript
export interface PickedColorInfo
```

全局取色结果对象，包含取色的基本信息。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface PickedColorInfo--><!--Device-unnamed-export interface PickedColorInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## brightness

```TypeScript
brightness?: number
```

颜色的亮度。单位为：尼特。默认值：0。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-PickedColorInfo-brightness?: number--><!--Device-PickedColorInfo-brightness?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color: common2D.Color
```

色值。

**类型：** [common2D.Color](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-common2d-color-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-PickedColorInfo-color: common2D.Color--><!--Device-PickedColorInfo-color: common2D.Color-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## colorSpace

```TypeScript
colorSpace: colorSpaceManager.ColorSpace
```

色域空间。

**类型：** [colorSpaceManager.ColorSpace](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-colorspacemanager-colorspace-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-PickedColorInfo-colorSpace: colorSpaceManager.ColorSpace--><!--Device-PickedColorInfo-colorSpace: colorSpaceManager.ColorSpace-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

时间戳，自系统启动以来经过的时间，单位：ms。单位为：毫秒。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-PickedColorInfo-timestamp: number--><!--Device-PickedColorInfo-timestamp: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
