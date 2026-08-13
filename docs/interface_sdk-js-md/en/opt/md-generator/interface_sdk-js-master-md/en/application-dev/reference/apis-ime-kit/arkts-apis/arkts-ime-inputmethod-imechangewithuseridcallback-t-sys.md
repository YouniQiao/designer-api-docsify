# ImeChangeWithUserIdCallback (System API)

```TypeScript
export type ImeChangeWithUserIdCallback =
      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: number) => void
```

The callback of the inputmethod change event which carries the user ID whose inputmethod is changed.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-export type ImeChangeWithUserIdCallback =      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: int) => void--><!--Device-inputMethod-export type ImeChangeWithUserIdCallback =      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |
| inputMethodSubtype | [InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md) | Yes |
| userId | number | Yes |
