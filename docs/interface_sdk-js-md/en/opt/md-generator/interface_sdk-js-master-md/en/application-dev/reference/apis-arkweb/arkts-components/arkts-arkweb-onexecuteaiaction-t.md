# OnExecuteAIAction

```TypeScript
type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void
```

Triggered when executing an AI session action.Enables custom implementation of AI model execution.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void--><!--Device-unnamed-type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| params | string | Yes |
| result | [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) | Yes |
