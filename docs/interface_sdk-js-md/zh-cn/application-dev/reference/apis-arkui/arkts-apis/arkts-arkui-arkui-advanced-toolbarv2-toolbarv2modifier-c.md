# ToolBarV2Modifier

```TypeScript
export declare class ToolBarV2Modifier
```

声明ToolBar中使用的ToolBarV2Modifier。提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在子项数量小于5个时生效）、是否显示按压态（stateEffect）的方法。

**起始版本：** 18

<!--Device-unnamed-export declare class ToolBarV2Modifier--><!--Device-unnamed-export declare class ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier
```

设置工具栏的背景色。调用该方法可自定义绘制。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2Modifier-backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-backgroundColor(backgroundColor: ColorMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundColor | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | 是 | ToolBarV2的背景色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置背景色后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## height

```TypeScript
height(height: LengthMetrics): ToolBarV2Modifier
```

设置工具栏的高度。调用该方法可自定义绘制，此高度不包含分割线高度。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2Modifier-height(height: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-height(height: LengthMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) | 是 | ToolBarV2的高度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置高度后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## padding

```TypeScript
padding(padding: LengthMetrics): ToolBarV2Modifier
```

设置工具栏的左右内边距。调用该方法可自定义绘制。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2Modifier-padding(padding: LengthMetrics): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-padding(padding: LengthMetrics): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| padding | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) | 是 | 左右内边距。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置内边距后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |

## stateEffect

```TypeScript
stateEffect(stateEffect: boolean): ToolBarV2Modifier
```

设置是否显示按压态效果。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2Modifier-stateEffect(stateEffect: boolean): ToolBarV2Modifier--><!--Device-ToolBarV2Modifier-stateEffect(stateEffect: boolean): ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateEffect | boolean | 是 | 按压态效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | 设置按压态效果后的ToolBarV2Modifier对象，可用于链式调用其他方法进一步自定义工具栏样式。 |
