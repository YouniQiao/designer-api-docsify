# AISessionEvent

Custom AI session model integration for Web components.Users can define custom AI session behaviors via this interface.

**Since:** 26.0.0

<!--Device-unnamed-declare interface AISessionEvent--><!--Device-unnamed-declare interface AISessionEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## aiSessionType

```TypeScript
aiSessionType: AISessionType
```

The type of AI session.

**Type:** AISessionType

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-aiSessionType: AISessionType--><!--Device-AISessionEvent-aiSessionType: AISessionType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onCreateAISession

```TypeScript
onCreateAISession: OnCreateAISession
```

Triggered when an AI session is created.Allows custom model initialization and result handling.Return `true` to bypass the default system behavior;return `false` to proceed with the default logic.

**Type:** OnCreateAISession

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onCreateAISession: OnCreateAISession--><!--Device-AISessionEvent-onCreateAISession: OnCreateAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onDestroyAISession

```TypeScript
onDestroyAISession: OnDestroyAISession
```

Triggered when an AI session is destroyed.Used for cleaning up resources associated with custom AI models.

**Type:** OnDestroyAISession

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession--><!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onExecuteAIAction

```TypeScript
onExecuteAIAction: OnExecuteAIAction
```

Triggered when executing an AI session action.Enables custom implementation of AI model execution.

**Type:** OnExecuteAIAction

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction--><!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction-End-->

**System capability:** SystemCapability.Web.Webview.Core

