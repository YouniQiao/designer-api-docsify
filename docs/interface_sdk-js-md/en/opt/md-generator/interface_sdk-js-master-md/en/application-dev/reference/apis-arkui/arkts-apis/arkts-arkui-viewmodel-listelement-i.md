# ListElement

List element

**Since:** 4

**Deprecated since:** -1

<!--Device-unnamed-export interface ListElement--><!--Device-unnamed-export interface ListElement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## rotation

```TypeScript
rotation(obj?: FocusParamObj): void
```

Requests or cancels the crown rotation focus for a component. If focus is set to true, the crown event focus is requested. If focus is set to false, the crown event focus is canceled. This attribute can be defaulted to true.

**Since:** 4

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-rotation(obj?: FocusParamObj): void--><!--Device-ListElement-rotation(obj?: FocusParamObj): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [FocusParamObj](arkts-arkui-viewmodel-focusparamobj-i.md) | No | { focus: true \|

## scrollTo

```TypeScript
scrollTo(position: ListScrollToOptions): void
```

Scrolls the list to the position of the item at the specified index.

**Since:** 4

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-ListElement-scrollTo(position: ListScrollToOptions): void--><!--Device-ListElement-scrollTo(position: ListScrollToOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [ListScrollToOptions](arkts-arkui-viewmodel-listscrolltooptions-i.md) | Yes |
