# ToolBarV2StyleOptions

```TypeScript
export interface ToolBarV2StyleOptions
```

定义ToolBarV2StyleConfigs的构造函数选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export interface ToolBarV2StyleOptions--><!--Device-unnamed-export interface ToolBarV2StyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

工具栏背景模糊样式。默认值：undefined。不设置时，无模糊效果。

**类型：** [BlurStyle](../arkts-components/arkts-arkui-common-comp-blurstyle-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ToolBarV2StyleOptions-backgroundBlurStyle?: BlurStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ColorMetrics
```

工具栏背景颜色。默认值：undefined。不设置时，默认为$r('sys.color.comp_background_primary')。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-backgroundColor?: ColorMetrics--><!--Device-ToolBarV2StyleOptions-backgroundColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ColorMetrics
```

工具栏的边框颜色。默认值：undefined。值为undefined或不设置时，无颜色。

**类型：** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-borderColor?: ColorMetrics--><!--Device-ToolBarV2StyleOptions-borderColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics
```

工具栏的边框圆角半径。默认值：undefined。值为undefined或不设置时，圆角半径为工具栏交叉轴长度的一半。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-borderRadius?: LengthMetrics--><!--Device-ToolBarV2StyleOptions-borderRadius?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: LengthMetrics
```

工具栏的边框宽度。默认值：undefined。值为undefined或不设置时，无宽度。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-borderWidth?: LengthMetrics--><!--Device-ToolBarV2StyleOptions-borderWidth?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: LengthMetrics
```

工具栏项里的文本的默认字体大小。默认值：undefined。值为undefined或不设置时，字体大小为$r('sys.float.ohos_id_text_size_caption')。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-fontSize?: LengthMetrics--><!--Device-ToolBarV2StyleOptions-fontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## groupSpace

```TypeScript
groupSpace?: LengthMetrics
```

工具栏的组间距。工具栏分组与分组之间、分组与独立项之间的间距。默认值: undefined。值为undefined或不设置时，默认间距为12vp，取值范围在[8vp, 20vp]。

**类型：** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-groupSpace?: LengthMetrics--><!--Device-ToolBarV2StyleOptions-groupSpace?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemSize

```TypeScript
itemSize?: Size
```

工具栏的项的大小。默认值：undefined。值为undefined或不设置时，主轴长56vp，交叉轴长48vp。

**类型：** Size

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-itemSize?: Size--><!--Device-ToolBarV2StyleOptions-itemSize?: Size-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## padding

```TypeScript
padding?: ToolBarV2PaddingOptions
```

工具栏内边距。

**类型：** [ToolBarV2PaddingOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2paddingoptions-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-padding?: ToolBarV2PaddingOptions--><!--Device-ToolBarV2StyleOptions-padding?: ToolBarV2PaddingOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## stateEffect

```TypeScript
stateEffect?: boolean
```

是否使能按压效果。默认值：true。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ToolBarV2StyleOptions-stateEffect?: boolean--><!--Device-ToolBarV2StyleOptions-stateEffect?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
