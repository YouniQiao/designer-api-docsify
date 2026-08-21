# ToolBarV2ItemImage

Declare type ToolBarV2ItemImage

**起始版本：** 18

<!--Device-unnamed-export declare class ToolBarV2ItemImage--><!--Device-unnamed-export declare class ToolBarV2ItemImage-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemImageOptions)
```

ToolBarV2ItemImage的构造函数。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)--><!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemImageOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemimageoptions-i.md) | 是 | 图标信息。 |

## activatedColor

```TypeScript
@Trace
  activatedColor?: ColorMetrics
```

Icon fillColor when the item is activated.

**类型：** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2ItemImage-@Trace  activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  activatedColor?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  color?: ColorMetrics
```

Define icon fillColor.

**类型：** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2ItemImage-@Trace  color?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  color?: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
@Trace
  src: ResourceStr
```

Define icon resource.

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr--><!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

