# ToolBarOption

定义工具栏的列表内容和属性。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ToolBarOption--><!--Device-unnamed-export declare class ToolBarOption-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ItemState, ToolBar, ToolBarOption, ToolBarOptions, ToolBarModifier } from '@kit.ArkUI';
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## accessibilityDescription

```TypeScript
public accessibilityDescription?: ResourceStr
```

工具栏子项的无障碍描述。用于向用户详细解释当前组件的功能和操作后果，特别是当这些信息无法仅从组件文本直接获知时。组件被选中时，将依次播报文本属性和无障碍说明属性的内容。

默认值为“单指双击即可执行”。

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public accessibilityDescription?: ResourceStr--><!--Device-ToolBarOption-public accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

工具栏子项无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换为"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"

**类型：** string

**默认值：** "auto"

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public accessibilityLevel?: string--><!--Device-ToolBarOption-public accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

工具栏子项的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报。开发人员可为不包含文字信息的组件设置无障碍文本，使屏幕朗读选中此组件时播报该文本内容。

默认值为当前项content属性内容。

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public accessibilityText?: ResourceStr--><!--Device-ToolBarOption-public accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

工具栏子项点击事件。不传入时点击子项不会触发任何操作。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public action?: () => void--><!--Device-ToolBarOption-public action?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activatedIconColor

```TypeScript
public activatedIconColor?: ResourceColor
```

工具栏子项激活态的图标填充颜色。

默认值为\$r('sys.color.icon_emphasize')。

当设置了toolBarSymbolOptions属性时，该参数不生效。

**类型：** [ResourceColor](../../apis-default/arkts-apis/arkts-resourcecolor-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public activatedIconColor?: ResourceColor--><!--Device-ToolBarOption-public activatedIconColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activatedTextColor

```TypeScript
public activatedTextColor?: ResourceColor
```

工具栏子项激活态的文本颜色。

默认值为\$r('sys.color.font_emphasize')。

**类型：** [ResourceColor](../../apis-default/arkts-apis/arkts-resourcecolor-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public activatedTextColor?: ResourceColor--><!--Device-ToolBarOption-public activatedTextColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
public content: ResourceStr
```

工具栏子项的文本。

**类型：** [ResourceStr](../../apis-default/arkts-apis/arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public content: ResourceStr--><!--Device-ToolBarOption-public content: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
public icon?: Resource
```

工具栏子项的图标。

默认不设置或者设置为undefined，图标不显示。

当设置了toolBarSymbolOptions属性时，icon属性将不生效。

**类型：** [Resource](../../apis-default/arkts-apis/arkts-resource-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public icon?: Resource--><!--Device-ToolBarOption-public icon?: Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconColor

```TypeScript
public iconColor?: ResourceColor
```

工具栏子项的图标填充颜色。

默认值为\$r('sys.color.icon_primary')。

当设置了toolBarSymbolOptions属性时，该参数不生效。

**类型：** [ResourceColor](../../apis-default/arkts-apis/arkts-resourcecolor-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public iconColor?: ResourceColor--><!--Device-ToolBarOption-public iconColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
public state?: ItemState
```

工具栏子项的状态。

默认为ItemState.ENABLE。

**类型：** [ItemState](arkts-arkui-arkui-advanced-toolbar-itemstate-e.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public state?: ItemState--><!--Device-ToolBarOption-public state?: ItemState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
public textColor?: ResourceColor
```

工具栏子项的文本颜色。

默认值为\$r('sys.color.font_primary')。

**类型：** [ResourceColor](../../apis-default/arkts-apis/arkts-resourcecolor-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public textColor?: ResourceColor--><!--Device-ToolBarOption-public textColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarSymbolOptions

```TypeScript
public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions
```

工具栏子项的图标属性，symbol类型。设置此参数后，icon属性将不生效。

**类型：** [ToolBarSymbolGlyphOptions](arkts-arkui-arkui-advanced-toolbar-toolbarsymbolglyphoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarOption-public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions--><!--Device-ToolBarOption-public toolBarSymbolOptions?: ToolBarSymbolGlyphOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

