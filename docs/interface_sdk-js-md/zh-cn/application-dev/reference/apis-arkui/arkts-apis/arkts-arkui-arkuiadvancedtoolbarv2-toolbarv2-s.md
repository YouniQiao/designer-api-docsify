# ToolBarV2

Declare Component ToolBarV2

**起始版本：** 18

<!--Device-unnamed-export declare struct ToolBarV2--><!--Device-unnamed-export declare struct ToolBarV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## activatedIndex

```TypeScript
@Param
  activatedIndex?: number
```

Define toolbarV2 activate item index, default is -1.

**类型：** number

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-@Param  activatedIndex?: number--><!--Device-ToolBarV2-@Param  activatedIndex?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
@Param
  dividerModifier?: DividerModifier
```

Define divider Modifier.

**类型：** DividerModifier

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier--><!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
@Require
  @Param
  toolBarList: ToolBarV2Item[]
```

Define toolbarV2 item list.

**类型：** [ToolBarV2Item](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2item-c.md)[]

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]--><!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
@Param
  toolBarModifier?: ToolBarV2Modifier
```

Define toolbarV2 modifier.

**类型：** [ToolBarV2Modifier](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2modifier-c.md)

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier--><!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

