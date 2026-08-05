# OnExecuteAIAction

```TypeScript
type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void
```

Triggered when executing an AI session action. Enables custom implementation of AI model execution.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void--><!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The session task ID.  |
| params | string | Yes | Contextual data passed during execution (in JSON string format).  |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback function to notify the system of the execution result.  |

