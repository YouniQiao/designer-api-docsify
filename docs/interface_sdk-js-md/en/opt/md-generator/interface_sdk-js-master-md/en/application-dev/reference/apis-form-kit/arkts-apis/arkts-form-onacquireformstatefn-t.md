# OnAcquireFormStateFn

```TypeScript
type OnAcquireFormStateFn = (want: Want) => formInfo.FormState
```

Called to return a FormState object. &lt;p&gt;You must override this callback if you want this ability to return the actual form state. Otherwise, this method returns DEFAULT by default.&lt;/p&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState--><!--Device-unnamed-type OnAcquireFormStateFn = (want: Want) => formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| formInfo.FormState |
