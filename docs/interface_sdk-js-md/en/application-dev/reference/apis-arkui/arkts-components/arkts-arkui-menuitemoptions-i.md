# MenuItemOptions

Provides information about the menu item.

**Since:** 9

<!--Device-unnamed-declare interface MenuItemOptions--><!--Device-unnamed-declare interface MenuItemOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

Builder for a level-2 menu.

**Type:** CustomBuilder

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemOptions-builder?: CustomBuilder--><!--Device-MenuItemOptions-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

Content of the menu item.

**Type:** ResourceStr

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemOptions-content?: ResourceStr--><!--Device-MenuItemOptions-content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endIcon

```TypeScript
endIcon?: ResourceStr
```

End icon of the menu item. Symbol icons are not supported. If the symbol icon is used, **symbolEndIcon** must be used.

**Type:** ResourceStr

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemOptions-endIcon?: ResourceStr--><!--Device-MenuItemOptions-endIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## labelInfo

```TypeScript
labelInfo?: ResourceStr
```

Label information at the end of the menu item, such as shortcut keys like Ctrl+C.

**Type:** ResourceStr

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemOptions-labelInfo?: ResourceStr--><!--Device-MenuItemOptions-labelInfo?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startIcon

```TypeScript
startIcon?: ResourceStr
```

Start icon of the menu item. Symbol icons are not supported. If a symbol icon is used, **symbolStartIcon** must be used.

**Type:** ResourceStr

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemOptions-startIcon?: ResourceStr--><!--Device-MenuItemOptions-startIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolEndIcon

```TypeScript
symbolEndIcon?: SymbolGlyphModifier
```

Symbol icon at the end of a menu item. When this parameter is set, the icon set through **endIcon** is not displayed.

**Type:** SymbolGlyphModifier

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MenuItemOptions-symbolEndIcon?: SymbolGlyphModifier--><!--Device-MenuItemOptions-symbolEndIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStartIcon

```TypeScript
symbolStartIcon?: SymbolGlyphModifier
```

Symbol icon at the start of a menu item. When this parameter is set, the icon set through **startIcon** is not displayed.

**Type:** SymbolGlyphModifier

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MenuItemOptions-symbolStartIcon?: SymbolGlyphModifier--><!--Device-MenuItemOptions-symbolStartIcon?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

