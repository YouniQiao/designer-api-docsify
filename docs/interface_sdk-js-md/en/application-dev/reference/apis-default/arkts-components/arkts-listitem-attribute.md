# ListItemAttribute

The ListItemAttribute.

**Inheritance/Implementation:** ListItemAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ListItemAttribute--><!--Device-unnamed-export declare interface ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ListItemAttribute-attributeModifier(modifier: AttributeModifier<ListItemAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ListItemAttribute](arkts-listitem-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSelect

```TypeScript
onSelect(event: ((isSelected: boolean) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this--><!--Device-ListItemAttribute-onSelect(event: ((isSelected: boolean) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((isSelected: boolean) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectable

```TypeScript
selectable(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-selectable(value: boolean | undefined): this--><!--Device-ListItemAttribute-selectable(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selected

```TypeScript
selected(value: boolean | Bindable<boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this--><!--Device-ListItemAttribute-selected(value: boolean | Bindable<boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setListItemOptions

```TypeScript
setListItemOptions(value?: ListItemOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-setListItemOptions(value?: ListItemOptions): this--><!--Device-ListItemAttribute-setListItemOptions(value?: ListItemOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-listitem-listitemoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## swipeAction

```TypeScript
swipeAction(value: SwipeActionOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ListItemAttribute-swipeAction(value: SwipeActionOptions | undefined): this--><!--Device-ListItemAttribute-swipeAction(value: SwipeActionOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwipeActionOptions](arkts-listitem-swipeactionoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Called attributeModifier.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListItemAttribute-default--><!--Device-ListItemAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

