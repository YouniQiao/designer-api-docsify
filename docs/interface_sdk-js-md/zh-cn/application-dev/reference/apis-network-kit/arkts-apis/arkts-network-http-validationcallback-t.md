# ValidationCallback

```TypeScript
export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>
```

自定义远程验证。 该API使用Promise异步返回结果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [ValidationContext](arkts-network-http-validationcontext-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean \| Promise & lt;boolean & gt; |
