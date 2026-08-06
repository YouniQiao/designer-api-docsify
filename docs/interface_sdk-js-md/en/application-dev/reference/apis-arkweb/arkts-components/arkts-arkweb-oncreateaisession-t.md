# OnCreateAISession

```TypeScript
type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean
```

Triggered when an AI session is created.Allows custom model initialization and result handling.Return \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ to bypass the default system behavior;return \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ to proceed with the default logic.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean--><!--Device-unnamed-type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The session task ID.  |
| params | string | Yes | Contextual data passed during creation.  |
| result | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback function to notify the system of the creation result.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Whether to use custom logic. \_\_\_INLINE\_CODE\_USD\_0\_\_\_ = use custom, \_\_\_INLINE\_CODE\_USD\_1\_\_\_ = proceed with default.  |

