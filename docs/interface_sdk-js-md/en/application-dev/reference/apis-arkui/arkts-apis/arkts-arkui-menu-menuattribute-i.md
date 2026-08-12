# MenuAttribute

Defines the Menu component attribute functions.

**Inheritance/Implementation:** MenuAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MenuAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default attributeModifier(        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuAttribute-default attributeModifier(        modifier: AttributeModifier<MenuAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuAttribute](arkts-arkui-menu-menuattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## font

```TypeScript
default font(value: Font | undefined): this
```

Sets the font style.Family and style are not supported currently and will be fixed in future.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default font(value: Font | undefined): this--><!--Device-MenuAttribute-default font(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes | Indicates the font style of menu item. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Sets the Menu font color.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default fontColor(value: ResourceColor | undefined): this--><!--Device-MenuAttribute-default fontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Indicates the font color of menu item. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## menuItemDivider

```TypeScript
default menuItemDivider(options: DividerStyleOptions | undefined): this
```

Set the divider of menu item

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default menuItemDivider(options: DividerStyleOptions | undefined): this--><!--Device-MenuAttribute-default menuItemDivider(options: DividerStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## menuItemGroupDivider

```TypeScript
default menuItemGroupDivider(options: DividerStyleOptions | undefined): this
```

Set the divider of menu item group

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default menuItemGroupDivider(options: DividerStyleOptions | undefined): this--><!--Device-MenuAttribute-default menuItemGroupDivider(options: DividerStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](arkts-arkui-dividerstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radius

```TypeScript
default radius(value: Dimension | BorderRadiuses | undefined): this
```

Sets the radius of the corner around the menu.When the radius is more than the menu width, the default border radius is used.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default radius(value: Dimension | BorderRadiuses | undefined): this--><!--Device-MenuAttribute-default radius(value: Dimension | BorderRadiuses | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| undefined | Yes | the border radius. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setMenuOptions

```TypeScript
default setMenuOptions(): this
```

Set menu options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default setMenuOptions(): this--><!--Device-MenuAttribute-default setMenuOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the MenuAttribute. |

## subMenuExpandSymbol

```TypeScript
default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this
```

Set the expand symbol of sub-menu.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this--><!--Device-MenuAttribute-default subMenuExpandSymbol(symbol: SymbolGlyphModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md) \| undefined | Yes | Use SymbolGlyphModifier to display symbol. Use undefined to display default symbol. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## subMenuExpandingMode

```TypeScript
default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this
```

Set the expanding mode of sub-menu

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuAttribute-default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this--><!--Device-MenuAttribute-default subMenuExpandingMode(mode: SubMenuExpandingMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SubMenuExpandingMode](arkts-arkui-menu-submenuexpandingmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

