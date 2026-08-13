# MenuItemConfiguration

MenuItemConfiguration used by menu item content modifier.

**Inheritance/Implementation:** MenuItemConfiguration extends CommonConfiguration<MenuItemConfiguration>

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface MenuItemConfiguration--><!--Device-unnamed-export declare interface MenuItemConfiguration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerSelect

```TypeScript
triggerSelect(index: int, value: string): void
```

Select this menu item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-triggerSelect(index: int, value: string): void--><!--Device-MenuItemConfiguration-triggerSelect(index: int, value: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The value of menu item index. |
| value | string | Yes | The value of menu item text. |

## icon

```TypeScript
icon?: ResourceStr
```

Indicates the icon of this menu item.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-icon?: ResourceStr--><!--Device-MenuItemConfiguration-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

Indicates the index of the menu item.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-index: int--><!--Device-MenuItemConfiguration-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected: boolean
```

Indicates whether this menu item is selected or not.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-selected: boolean--><!--Device-MenuItemConfiguration-selected: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIcon

```TypeScript
symbolIcon?: SymbolGlyphModifier
```

Indicates the symbol icon of this menu item.

**Type:** [SymbolGlyphModifier](../../apis-arkui/arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-symbolIcon?: SymbolGlyphModifier--><!--Device-MenuItemConfiguration-symbolIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr
```

Indicates the text of this menu item.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemConfiguration-value: ResourceStr--><!--Device-MenuItemConfiguration-value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

