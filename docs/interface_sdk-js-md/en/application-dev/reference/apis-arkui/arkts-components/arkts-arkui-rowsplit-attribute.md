# RowSplit properties/events

In addition to the universal attributes, the following attributes are supported.The universal events are supported.

**Inheritance/Implementation:** RowSplitAttribute extends CommonMethod<RowSplitAttribute>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## resizeable

```TypeScript
resizeable(value: boolean)
```

Sets whether the divider can be dragged.

> The divider of **RowSplit** can change the width of the left and right child components, but only to the
> extent that the resultant width falls within the maximum and minimum widths of the child components.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
