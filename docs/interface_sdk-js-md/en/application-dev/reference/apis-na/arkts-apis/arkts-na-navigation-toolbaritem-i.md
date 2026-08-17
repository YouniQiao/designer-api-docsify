# ToolbarItem

Defines configurable parameters for toolbar item.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ToolbarItem--><!--Device-unnamed-export declare interface ToolbarItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action?: () => void
```

Trigger by navigation toolbar item click.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-action?: () => void--><!--Device-ToolbarItem-action?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activeIcon

```TypeScript
activeIcon?: ResourceStr
```

The icon of navigation toolbar item in active state.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-activeIcon?: ResourceStr--><!--Device-ToolbarItem-activeIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activeSymbolIcon

```TypeScript
activeSymbolIcon?: SymbolGlyphModifier
```

The symbol of navigation toolbar item in active state.

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-activeSymbolIcon?: SymbolGlyphModifier--><!--Device-ToolbarItem-activeSymbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

The icon of navigation toolbar item.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-icon?: ResourceStr--><!--Device-ToolbarItem-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status?: ToolbarItemStatus
```

The state of navigation toolbar item. Default value: ToolbarItemStatus.NORMAL.

**Type:** [ToolbarItemStatus](arkts-na-navigation-toolbaritemstatus-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-status?: ToolbarItemStatus--><!--Device-ToolbarItem-status?: ToolbarItemStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIcon

```TypeScript
symbolIcon?: SymbolGlyphModifier
```

The symbol of navigation toolbar item.

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-symbolIcon?: SymbolGlyphModifier--><!--Device-ToolbarItem-symbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr | undefined
```

The value of navigation toolbar item, default value is "", undefined means set to default value.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolbarItem-value: ResourceStr | undefined--><!--Device-ToolbarItem-value: ResourceStr | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

