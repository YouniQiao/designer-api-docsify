# OnAISessionCallback

```TypeScript
export type OnAISessionCallback = (state: AISessionResultType, content: string) => void
```

Callback type for AI session operations. Used to report the result of session creation or execution.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [AISessionResultType](arkts-arkweb-web-aisessionresulttype-e.md) | 是 |
| content | string | 是 |
