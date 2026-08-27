# Menu properties/events

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** MenuAttribute extends CommonMethod<MenuAttribute>

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## font

```TypeScript
font(value: Font)
```

Sets the size of all text within the menu.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Font | Yes | Size of all text within the menu.Default value:{size: 16,family: 'HarmonyOS Sans',weight: FontWeight.Medium,style: FontStyle.Normal} |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

Sets the font color of all text within the menu.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Font color of all text within the menu. |

## fontSize

```TypeScript
fontSize(value: Length)
```

Sets the size of all text within the menu.

> **NOTE：**

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [font](#font)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | Size of all text within the menu. If the value of the Length type is a number, the unit is fp. Percentage values are not supported. |

## menuItemDivider

```TypeScript
menuItemDivider(options: DividerStyleOptions | undefined)
```

Sets the style of the menu item divider. If this attribute is not set, the divider will not be displayed.

If the sum of **startMargin** and **endMargin** exceeds the component width, both **startMargin** and **endMargin** will be set to **0**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](../arkts-apis/arkts-arkui-dividerstyleoptions-i.md) \| undefined | Yes | Style of the menu item divider.   - **strokeWidth**: stroke width of the divider.   - **color**: color of the divider.   - **startMargin**: distance between the divider and the start edge of the menu item.   - **endMargin**: distance between the divider and the end edge of the menu item.   - **mode**: mode of the divider, which is **FLOATING_ABOVE_MENU** by default. |

## menuItemGroupDivider

```TypeScript
menuItemGroupDivider(options: DividerStyleOptions | undefined)
```

Sets the style of the top and bottom dividers for the menu item group. If this attribute is not set, the dividers will be displayed by default.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DividerStyleOptions](../arkts-apis/arkts-arkui-dividerstyleoptions-i.md) \| undefined | Yes | Style of the top and bottom dividers for the menu item group.   - **strokeWidth**: stroke width of the divider. The default value is 1 px.   - **color**: color of the divider. The default value is **#33000000**.   - **startMargin**: distance between the divider and the start edge of the menu item group. The default value is 16 vp.   - **endMargin**: distance between the divider and the end edge of the menu item group. The default value is 16 vp.   - **mode**: mode of the divider, which is **FLOATING_ABOVE_MENU** by default. |

## radius

```TypeScript
radius(value: Dimension | BorderRadiuses)
```

Sets the radius of the menu border corners.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [BorderRadiuses](../arkts-apis/arkts-arkui-borderradiuses-t.md) | Yes | Radius of the menu border corners.Default value: **8vp** for 2- in-1 devices and **20vp** for other devices Since API version 12, if the sum of the two maximum corner radii in the horizontal direction exceeds the menu width, or if the sum of the two maximum corner radii in the vertical direction exceeds the menu height, the default corner radius will be used for all four corners of the menu.When the Dimension type is used: Invalid input values will trigger a fallback to the default corner radius.When the BorderRadiuses type is used: Invalid input values will result in the menu having no rounded corners by default. |

## subMenuExpandingMode

```TypeScript
subMenuExpandingMode(mode: SubMenuExpandingMode)
```

Sets the submenu expanding mode of the menu.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SubMenuExpandingMode](arkts-arkui-submenuexpandingmode-e.md) | Yes | Submenu expanding mode of the menu.Default value: **SubMenuExpandingMode.SIDE_EXPAND |

## subMenuExpandSymbol

```TypeScript
subMenuExpandSymbol(symbol: SymbolGlyphModifier)
```

Sets the submenu expand symbol of the menu.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | SymbolGlyphModifier | Yes | Submenu expand symbol of the menu. 1. **SubMenuExpandingMode.SIDE_EXPAND**: The expand symbol is not displayed. 2. **SubMenuExpandingMode.EMBEDDED_EXPAND**: The symbol rotates 180° clockwise upon expansion. Default value: **\\$r('sys.symbol.chevron_down').fontSize('24vp')** 3. **SubMenuExpandingMode.STACK_EXPAND**: The symbol rotates 90° clockwise upon expansion. Default value: **\\$r('sys.symbol.chevron_forward').fontSize('20vp').padding('2vp') |
