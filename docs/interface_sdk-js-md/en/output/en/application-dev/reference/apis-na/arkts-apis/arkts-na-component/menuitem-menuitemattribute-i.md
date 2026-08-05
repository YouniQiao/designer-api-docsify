# MenuItemAttribute

Defines the MenuItem component attributes.

**Inheritance/Implementation:** MenuItemAttribute extends [CommonMethod](common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuItemAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of menu item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemAttribute-default attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of menu item. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentFont

```TypeScript
default contentFont(value: Font | undefined): this
```

Sets the content font style. Family and style are not supported currently and will be fixed in future.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default contentFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates the font style of content text. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentFontColor

```TypeScript
default contentFontColor(value: ResourceColor | undefined): this
```

Sets the font color of content text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default contentFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates the font color of content text. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## labelFont

```TypeScript
default labelFont(value: Font | undefined): this
```

Sets the label info font style. Family and style are not supported currently and will be fixed in future.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-default labelFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates the font style of label info text. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## labelFontColor

```TypeScript
default labelFontColor(value: ResourceColor | undefined): this
```

Sets the font color of label info text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-default labelFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates the font color of label info text. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((selected: boolean) => void) | undefined): this
```

Triggers a callback when a menu item is selected or unchecked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this--><!--Device-MenuItemAttribute-default onChange(callback: ((selected: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((selected: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectIcon

```TypeScript
default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this
```

Whether the relevant check icon is displayed when a menu item is selected. Use type ResourceStr or SymbolGlyphModifier to specify icon instead of the default check mark.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this--><!--Device-MenuItemAttribute-default selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| ResourceStr \| SymbolGlyphModifier \| undefined | Yes | Whether to display icon when selected.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_true: displays the default check mark when selected.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_false: does not displays icon when selected.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ResourceStr or SymbolGlyphModifier: displays the specified icon when selected. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selected

```TypeScript
default selected(value: boolean | undefined | Bindable<boolean>): this
```

Setting whether menuItem is selected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this--><!--Device-MenuItemAttribute-default selected(value: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined \| Bindable&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setMenuItemOptions

```TypeScript
default setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this
```

Set menuitem options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this--><!--Device-MenuItemAttribute-default setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| CustomBuilder | No | menuitem constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the MenuItemAttribute. |

## subMenuBuilder

```TypeScript
default subMenuBuilder(builder: CustomBuilder | undefined): this
```

Create the submenu for custom menu item.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default subMenuBuilder(builder: CustomBuilder | undefined): this--><!--Device-MenuItemAttribute-default subMenuBuilder(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Indicates the builder function for submenu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

