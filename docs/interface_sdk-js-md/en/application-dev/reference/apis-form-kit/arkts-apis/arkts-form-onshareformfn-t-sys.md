# OnShareFormFn (System API)

```TypeScript
type OnShareFormFn = (formId: string) => Record<string, Object>
```

Called when the system shares the form.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnShareFormFn = (formId: string) => Record<string, Object>--><!--Device-unnamed-type OnShareFormFn = (formId: string) => Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Returns the wantParams object.  |

