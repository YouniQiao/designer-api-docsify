# GridRow properties/events

In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** GridRowAttribute extends CommonMethod<GridRowAttribute>

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alignItems

```TypeScript
alignItems(value: ItemAlign)
```

Sets the alignment mode of the **GridCol** components along the vertical main axis of the **GridRow** component. The alignment mode of the **GridCol** component can also be set using **alignSelf(ItemAlign)**. If both of the preceding methods are used, the setting of **alignSelf(ItemAlign)** prevails.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ItemAlign](../arkts-apis/arkts-arkui-enums-itemalign-e.md) | Yes |

## onBreakpointChange

```TypeScript
onBreakpointChange(callback: (breakpoints: string) => void)
```

Triggered when the breakpoint changes.

> **NOTE：**
> &gt;
> When [breakpointsreference](#breakpointsreference) is set to **BreakpointsReference.ComponentSize**, you are not
> advised to dynamically change the padding or margin
> attribute value of the **GridRow** component in the **onBreakpointChange** callback.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (breakpoints: string) = & gt; void | Yes |
