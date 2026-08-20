# MenuItemAttribute

Defines the MenuItem component attributes.

@extends CommonMethod @interface MenuItemAttribute

**Inheritance/Implementation:** MenuItemAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface MenuItemAttribute--><!--Device-unnamed-export declare interface MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MenuItemAttribute](arkts-menuitem-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentFont

```TypeScript
contentFont(value: Font | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-contentFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-contentFont(value: Font | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentFontColor

```TypeScript
contentFontColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-contentFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-contentFontColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## labelFont

```TypeScript
labelFont(value: Font | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-labelFont(value: Font | undefined): this--><!--Device-MenuItemAttribute-labelFont(value: Font | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## labelFontColor

```TypeScript
labelFontColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-labelFontColor(value: ResourceColor | undefined): this--><!--Device-MenuItemAttribute-labelFontColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: ((selected: boolean) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-onChange(callback: ((selected: boolean) => void) | undefined): this--><!--Device-MenuItemAttribute-onChange(callback: ((selected: boolean) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((selected: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectIcon

```TypeScript
selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this--><!--Device-MenuItemAttribute-selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selected

```TypeScript
selected(value: boolean | undefined | Bindable<boolean>): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-selected(value: boolean | undefined | Bindable<boolean>): this--><!--Device-MenuItemAttribute-selected(value: boolean | undefined | Bindable<boolean>): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setMenuItemOptions

```TypeScript
setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this--><!--Device-MenuItemAttribute-setMenuItemOptions(value?: MenuItemOptions | CustomBuilder): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemOptions](arkts-menuitem-menuitemoptions-i.md) \| [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## subMenuBuilder

```TypeScript
subMenuBuilder(builder: CustomBuilder | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-MenuItemAttribute-subMenuBuilder(builder: CustomBuilder | undefined): this--><!--Device-MenuItemAttribute-subMenuBuilder(builder: CustomBuilder | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set menuitem options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemAttribute-default--><!--Device-MenuItemAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

