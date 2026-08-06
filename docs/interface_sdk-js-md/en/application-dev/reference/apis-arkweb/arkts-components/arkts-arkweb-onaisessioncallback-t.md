# OnAISessionCallback

```TypeScript
type OnAISessionCallback = (state: AISessionResultType, content: string) => void
```

Callback type for AI session operations.Used to report the result of session creation or execution.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void--><!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The current result state.  |
| content | string | Yes | The detailed result or response content.  |

