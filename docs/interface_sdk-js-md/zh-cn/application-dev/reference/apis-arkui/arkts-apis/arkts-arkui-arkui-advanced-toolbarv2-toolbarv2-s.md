# ToolBarV2

Declare Component ToolBarV2

**起始版本：** 18

**装饰器类型：** @ComponentV2

<!--Device-unnamed-export declare struct ToolBarV2--><!--Device-unnamed-export declare struct ToolBarV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ToolBarV2ItemImageOptions, ToolBarV2Item, ToolBarV2ItemText, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemAction, ToolBarV2ItemOptions, ToolBarV2, ToolBarV2SymbolGlyph, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemState, ToolBarV2ItemTextOptions, ToolBarV2Modifier } from '@kit.ArkUI';
```

## activatedIndex

```TypeScript
activatedIndex?: number
```

Define toolbarV2 activate item index, default is -1.

**类型：** number

**起始版本：** 18

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-activatedIndex?: number--><!--Device-ToolBarV2-activatedIndex?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
dividerModifier?: DividerModifier
```

Define divider Modifier.

**类型：** DividerModifier

**起始版本：** 18

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-dividerModifier?: DividerModifier--><!--Device-ToolBarV2-dividerModifier?: DividerModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
toolBarList: ToolBarV2Item[]
```

Define toolbarV2 item list.

**类型：** ToolBarV2Item[]

**起始版本：** 18

**装饰器类型：** @Require、@Param

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-toolBarList: ToolBarV2Item[]--><!--Device-ToolBarV2-toolBarList: ToolBarV2Item[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
toolBarModifier?: ToolBarV2Modifier
```

Define toolbarV2 modifier.

**类型：** ToolBarV2Modifier

**起始版本：** 18

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ToolBarV2-toolBarModifier?: ToolBarV2Modifier--><!--Device-ToolBarV2-toolBarModifier?: ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

