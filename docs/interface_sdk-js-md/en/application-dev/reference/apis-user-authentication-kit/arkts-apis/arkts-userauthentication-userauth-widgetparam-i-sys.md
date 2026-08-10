# WidgetParam

用户认证界面配置相关参数。该接口用于配置认证界面的显示样式和交互方式，包括标题、导航按钮文本、窗口模式等。通过合理配置这些参数，可以为用户提供清晰的认证引导和良好的交互体验。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-userAuth-interface WidgetParam--><!--Device-userAuth-interface WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## appWindow

```TypeScript
appWindow?: window.Window
```

应用窗口对象。用于以模应用弹窗方式显示身份认证对话框，适用于需要通过窗口对象控制认证对话框显示的场景。如果已提供此参数，则uiContext将被忽略。

**Type:** window.Window

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WidgetParam-appWindow?: window.Window--><!--Device-WidgetParam-appWindow?: window.Window-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## windowMode

```TypeScript
windowMode?: WindowModeType
```

用户认证界面的显示类型。DIALOG_BOX适用于大多数认证场景（用户体验较好），FULLSCREEN适用于需要沉浸式认证体验或认证信息较多的场景。不传入时默认为WindowModeType.DIALOG_BOX。

**Type:** [WindowModeType](arkts-userauthentication-userauth-windowmodetype-e-sys.md)

**Default:** WindowModeType.DIALOG_BOX

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WidgetParam-windowMode?: WindowModeType--><!--Device-WidgetParam-windowMode?: WindowModeType-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

