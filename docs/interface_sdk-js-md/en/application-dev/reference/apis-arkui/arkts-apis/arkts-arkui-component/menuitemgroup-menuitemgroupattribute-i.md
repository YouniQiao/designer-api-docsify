# MenuItemGroupAttribute

Defines the MenuItemGroup component attribute functions.

**Inheritance/Implementation:** MenuItemGroupAttribute extends [CommonMethod](common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MenuItemGroupAttribute extends CommonMethod--><!--Device-unnamed-export declare interface MenuItemGroupAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemGroupAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-MenuItemGroupAttribute-attributeModifier(        modifier: AttributeModifier<MenuItemGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setMenuItemGroupOptions

```TypeScript
default setMenuItemGroupOptions(value?: MenuItemGroupOptions): this
```

Set menuitemgroup options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MenuItemGroupAttribute-default setMenuItemGroupOptions(value?: MenuItemGroupOptions): this--><!--Device-MenuItemGroupAttribute-default setMenuItemGroupOptions(value?: MenuItemGroupOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | menuitemgroup constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the MenuItemGroupAttribute. |

