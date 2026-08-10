# OnAISessionCallback

```TypeScript
type OnAISessionCallback = (state: AISessionResultType, content: string) => void
```

AI会话操作结果回调函数类型。用于报告会话创建或执行的结果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void--><!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [AISessionResultType](../arkts-apis/arkts-arkweb-web-aisessionresulttype-e.md) | Yes | The current result state. |
| content | string | Yes | The detailed result or response content. |

