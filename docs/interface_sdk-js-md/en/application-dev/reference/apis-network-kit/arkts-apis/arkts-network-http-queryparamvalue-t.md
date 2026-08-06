# QueryParamValue

```TypeScript
export type QueryParamValue = string | int | boolean | null | undefined
```

A single value that can be used as a query parameter.

Serialization rules when used in \_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_:  
- textual values: serialized as-is before URL encoding.  
- numeric values: converted to its string representation before URL encoding.  
- logical values: converted to "true" or "false" before URL encoding.  
- null or undefined: serialized as the key without \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ or a value (for example, \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ -  
    \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-http-export type QueryParamValue = string | int | boolean | null | undefined--><!--Device-http-export type QueryParamValue = string | int | boolean | null | undefined-End-->

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| string |  |
| int |  |
| boolean |  |
| null |  |
| undefined |  |

