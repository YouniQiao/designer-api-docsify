# ValidationCallback

```TypeScript
export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>
```

Self defined remote validation.This API uses a promise to return the result.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-http-export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>--><!--Device-http-export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [ValidationContext](arkts-network-http-validationcontext-i.md) | 是 | Certificate context. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean \| Promise&lt;boolean&gt; | Returns a boolean value indicating whether the validation is successful. Promise used to return the result. The value true indicates valid, and false indicates invalid. |

