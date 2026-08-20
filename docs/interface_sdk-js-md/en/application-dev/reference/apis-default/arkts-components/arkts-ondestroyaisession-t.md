# OnDestroyAISession

```TypeScript
export type OnDestroyAISession = (id: string) => void
```

Triggered when an AI session is destroyed. Used for cleaning up resources associated with custom AI models.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnDestroyAISession = (id: string) => void--><!--Device-unnamed-export type OnDestroyAISession = (id: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The session task ID. |

