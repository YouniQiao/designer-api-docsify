# AISessionEvent

自定义AI会话配置对象，用于定义AI会话的生命周期回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface AISessionEvent--><!--Device-unnamed-declare interface AISessionEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onCreateAISession

```TypeScript
onCreateAISession: OnCreateAISession
```

AI会话创建时触发的回调函数。返回`true`跳过系统默认行为，返回`false`继续执行系统默认逻辑。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onCreateAISession: OnCreateAISession--><!--Device-AISessionEvent-onCreateAISession: OnCreateAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onDestroyAISession

```TypeScript
onDestroyAISession: OnDestroyAISession
```

AI会话销毁时触发的回调函数，用于清理与自定义AI模型关联的资源。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession--><!--Device-AISessionEvent-onDestroyAISession: OnDestroyAISession-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onExecuteAIAction

```TypeScript
onExecuteAIAction: OnExecuteAIAction
```

AI会话执行操作时触发的回调函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction--><!--Device-AISessionEvent-onExecuteAIAction: OnExecuteAIAction-End-->

**System capability:** SystemCapability.Web.Webview.Core

## aiSessionType

```TypeScript
aiSessionType: AISessionType
```

AI会话类型。

**Type:** [AISessionType](../arkts-apis/arkts-arkweb-web-aisessiontype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AISessionEvent-aiSessionType: AISessionType--><!--Device-AISessionEvent-aiSessionType: AISessionType-End-->

**System capability:** SystemCapability.Web.Webview.Core

