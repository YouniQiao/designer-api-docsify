# QueryParamValue

```TypeScript
export type QueryParamValue = string | int | boolean | null | undefined
```

A single value that can be used as a query parameter.

Serialization rules when used in {@link QueryParamObject}:  
- textual values: serialized as-is before URL encoding.  
- numeric values: converted to its string representation before URL encoding.  
- logical values: converted to "true" or "false" before URL encoding.  
- null or undefined: serialized as the key without `=` or a value (for example, `{ a: null }` -> `a`).

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-http-export type QueryParamValue = string | int | boolean | null | undefined--><!--Device-http-export type QueryParamValue = string | int | boolean | null | undefined-End-->

**系统能力：** SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| string |  |
| int |  |
| boolean |  |
| null |  |
| undefined |  |

