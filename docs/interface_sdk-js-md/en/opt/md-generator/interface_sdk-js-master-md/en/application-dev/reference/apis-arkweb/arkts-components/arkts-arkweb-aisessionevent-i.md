# AISessionEvent

Custom AI session model integration for Web components. Users can define custom AI session behaviors via this interface.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-unnamed-declare interface AISessionEvent--><!--Device-unnamed-declare interface AISessionEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## aiSessionType

```TypeScript
aiSessionType: AISessionType
```

The type of AI session.

**Type:** [AISessionType](arkts-arkweb-aisessiontype-e.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-aiSessionType: AISessionType--><!--Device-AISessionEvent-aiSessionType: AISessionType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onCreateAISession

```TypeScript
onCreateAISession: OnCreateAISession
```

Triggered when an AI session is created. Allows custom model initialization and result handling. Return `true` to bypass the default system behavior; return `false` to proceed with the default logic.

**Type:** [OnCreateAISession](arkts-arkweb-oncreateaisession-t.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onCreateAISession: OnCreateAISession--><!--Device-AISessionEvent-onCreateAISession: OnCreateAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onDestroyAISession

```TypeScript
onDestroyAISession: OnDestroyAISession
```

Triggered when an AI session is destroyed. Used for cleaning up resources associated with custom AI models.

**Type:** [OnDestroyAISession](arkts-arkweb-ondestroyaisession-t.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession--><!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onExecuteAIAction

```TypeScript
onExecuteAIAction: OnExecuteAIAction
```

Triggered when executing an AI session action. Enables custom implementation of AI model execution.

**Type:** [OnExecuteAIAction](arkts-arkweb-onexecuteaiaction-t.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction--><!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction-End-->

**System capability:** SystemCapability.Web.Webview.Core
