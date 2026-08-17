# OnAcquireFormStateFn

```TypeScript
type OnAcquireFormStateFn = (want: Want) => formInfo.FormState
```

Called to return a FormState object. &lt;p&gt;You must override this callback if you want this ability to return the actual form state. Otherwise, this method returns DEFAULT by default.&lt;/p&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState--><!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Indicates the description of the form for which the FormState is obtained. The description covers the bundle name, ability name, module name, form name, and form dimensions. |

**Return value:**

| Type | Description |
| --- | --- |
| formInfo.FormState | Returns the { |

