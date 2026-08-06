# OnAcquireFormStateFn

```TypeScript
type OnAcquireFormStateFn = (want: Want) => formInfo.FormState
```

Called to return a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ object.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_You must override this callback if you want this ability to return the actual form state. Otherwise,this method returns \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ by default.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState--><!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the description of the form for which the \_\_\_JSDOC\_LINK\_USD\_0\_\_\_ is obtained. The description covers the bundle name, ability name, module name, form name, and form dimensions.  |

**Return value:**

| Type | Description |
| --- | --- |
| formInfo.FormState | Returns the { |

