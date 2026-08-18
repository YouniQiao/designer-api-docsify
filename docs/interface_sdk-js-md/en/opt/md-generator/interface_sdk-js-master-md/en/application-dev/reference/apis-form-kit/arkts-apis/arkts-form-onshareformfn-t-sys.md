# OnShareFormFn (System API)

```TypeScript
type OnShareFormFn = (formId: string) => Record<string, Object>
```

Called when the system shares the form.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnShareFormFn = (formId: string) => Record<string, Object>--><!--Device-unnamed-type OnShareFormFn = (formId: string) => Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; |
