# OnDestroyAISession

```TypeScript
type OnDestroyAISession = (id: string) => void
```

Triggered when an AI session is destroyed. Used for cleaning up resources associated with custom AI models.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnDestroyAISession = (id: string) => void--><!--Device-unnamed-type OnDestroyAISession = (id: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
