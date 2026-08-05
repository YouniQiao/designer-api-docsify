# ValidationCallback

```TypeScript
export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>
```

Self defined remote validation. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-http-export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>--><!--Device-http-export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Certificate context.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean \| Promise&lt;boolean&gt; | Returns a boolean value indicating whether the validation is successful. |

