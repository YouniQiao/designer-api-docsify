# OnAISessionCallback

```TypeScript
type OnAISessionCallback = (state: AISessionResultType, content: string) => void
```

AI session operation result callback function type. Used to report the result of session creation or execution.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void--><!--Device-unnamed-type OnAISessionCallback = (state: AISessionResultType, content: string) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [AISessionResultType](arkts-arkweb-aisessionresulttype-e.md) | Yes |
| content | string | Yes |
