# ToolbarItem

工具栏可配置参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToolbarItem--><!--Device-unnamed-export declare interface ToolbarItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action?: () => void
```

当前选项被选中的事件回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-action?: () => void--><!--Device-ToolbarItem-action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activeIcon

```TypeScript
activeIcon?: ResourceStr
```

工具栏单个选项处于ACTIVE态时的图标资源路径。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-activeIcon?: ResourceStr--><!--Device-ToolbarItem-activeIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activeSymbolIcon

```TypeScript
activeSymbolIcon?: SymbolGlyphModifier
```

工具栏单个选项处于ACTIVE态时的symbol资源（优先级高于activeIcon）。  
**说明：**不支持通过[SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md/arkts-arkui-symbolglyphmodifier-t.md)对象的
[fontSize](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#fontsize)属性修改图标大小、  
[effectStrategy](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#effectstrategy)属性修改动效、[symbolEffect](../../../reference/apis-arkui/arkui-ts/ts-basic-components-symbolGlyph.md#symboleffect12)属性修改动效类型。

**Type:** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-activeSymbolIcon?: SymbolGlyphModifier--><!--Device-ToolbarItem-activeSymbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

工具栏单个选项的图标资源路径。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-icon?: ResourceStr--><!--Device-ToolbarItem-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status?: ToolbarItemStatus
```

工具栏单个选项的状态。默认值： ToolbarItemStatus.NORMAL。

**Type:** [ToolbarItemStatus](../arkts-components/arkts-arkui-toolbaritemstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-status?: ToolbarItemStatus--><!--Device-ToolbarItem-status?: ToolbarItemStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIcon

```TypeScript
symbolIcon?: SymbolGlyphModifier
```

工具栏单个选项的symbol资源（优先级高于icon）。

**Type:** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-symbolIcon?: SymbolGlyphModifier--><!--Device-ToolbarItem-symbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr | undefined
```

工具栏单个选项的显示文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-value: ResourceStr | undefined--><!--Device-ToolbarItem-value: ResourceStr | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

