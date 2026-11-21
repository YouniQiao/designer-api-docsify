# ToolBarV2StyleOptions（系统接口）

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

## systemBackgroundMaterial

```TypeScript
systemBackgroundMaterial?: uiMaterial.Material
```

工具栏的系统材质效果。默认值：undefined。值为undefined或不设置时，不开启系统材质。

**类型：** [uiMaterial.Material](arkts-arkui-uimaterial-material-c.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2StyleOptions-systemBackgroundMaterial?: uiMaterial.Material--><!--Device-ToolBarV2StyleOptions-systemBackgroundMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## systemMaterialStyle

```TypeScript
systemMaterialStyle?: ToolBarV2MaterialStyle
```

工具栏的简化系统材质样式。如果两者systemBackgroundMaterial和systemMaterialStyle都设置了，systemBackgroundMaterial优先生效。默认值：undefined。值为undefined或不设置时，默认为ToolBarV2MaterialStyle.NONE效果。

**类型：** [ToolBarV2MaterialStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2materialstyle-e-sys.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2StyleOptions-systemMaterialStyle?: ToolBarV2MaterialStyle--><!--Device-ToolBarV2StyleOptions-systemMaterialStyle?: ToolBarV2MaterialStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
