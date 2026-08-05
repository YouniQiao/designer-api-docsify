# ImeChangeWithUserIdCallback (System API)

```TypeScript
export type ImeChangeWithUserIdCallback =
      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: int) => void
```

The callback of the inputmethod change event which carries the user ID whose inputmethod is changed.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-export type ImeChangeWithUserIdCallback =      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: int) => void--><!--Device-inputMethod-export type ImeChangeWithUserIdCallback =      (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, userId: int) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputMethodProperty | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the property of current inputmethod.  |
| inputMethodSubtype | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the subtype of current inputmethod.  |
| userId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | the user ID whose inputmethod is changed.  |

