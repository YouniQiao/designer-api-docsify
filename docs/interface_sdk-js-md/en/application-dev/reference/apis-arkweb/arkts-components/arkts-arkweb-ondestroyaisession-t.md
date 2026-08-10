# OnDestroyAISession

```TypeScript
type OnDestroyAISession = (id: string) => void
```

AI会话销毁回调函数类型。用于清理与自定义AI模型关联的资源。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnDestroyAISession = (id: string) => void--><!--Device-unnamed-type OnDestroyAISession = (id: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 会话任务ID。 |

