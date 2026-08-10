# OnAcquireFormDataFn (System API)

```TypeScript
type OnAcquireFormDataFn = (formId: string) => Record<string, Object>
```

Called when the system acquire the form data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAcquireFormDataFn = (formId: string) => Record<string, Object>--><!--Device-unnamed-type OnAcquireFormDataFn = (formId: string) => Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form. |

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Returns the wantParams object. |

