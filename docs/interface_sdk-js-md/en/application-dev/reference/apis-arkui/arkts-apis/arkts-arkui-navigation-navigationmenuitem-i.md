# NavigationMenuItem

导航菜单项，包括菜单图标和菜单信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationMenuItem--><!--Device-unnamed-export declare interface NavigationMenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action?: () => void
```

当前选项被选中的事件回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMenuItem-action?: () => void--><!--Device-NavigationMenuItem-action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: string | Resource
```

API version 9：显示菜单栏单个选项的文本。

从API version 10开始，不显示菜单栏单个选项的文本。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMenuItem-icon?: string | Resource--><!--Device-NavigationMenuItem-icon?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
isEnabled?: boolean
```

使能状态，默认使能（false未使能，true使能）。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMenuItem-isEnabled?: boolean--><!--Device-NavigationMenuItem-isEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIcon

```TypeScript
symbolIcon?: SymbolGlyphModifier
```

菜单栏单个选项的symbol资源（优先级高于icon）。  
**说明：**不支持通过[SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md/arkts-arkui-symbolglyphmodifier-t.md)对象的
[fontSize](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#fontsize)属性修改图标大小、  
[effectStrategy](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#effectstrategy)属性修改动效、[symbolEffect](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#symboleffect12)属性修改动效类型。

**Type:** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMenuItem-symbolIcon?: SymbolGlyphModifier--><!--Device-NavigationMenuItem-symbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string | Resource
```

API version 9：显示菜单栏单个选项的文本。

从API version 10开始，不显示菜单栏单个选项的文本。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationMenuItem-value: string | Resource--><!--Device-NavigationMenuItem-value: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

