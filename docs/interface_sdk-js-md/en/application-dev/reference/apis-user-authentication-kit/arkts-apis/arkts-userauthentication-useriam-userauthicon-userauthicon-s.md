# UserAuthIcon

**userAuthIcon**模块是OpenHarmony用户身份认证体系（UserIAM）的UI组件模块，提供了一个开箱即用的身份认证图标组件（UserAuthIcon）。该组件用于在应用UI中展示人脸认证或指纹认证的图标，支持自定义图标颜色和尺寸，点击图标可启动系统身份认证弹窗组件。

该模块主要用于以下场景：

- 在应用界面中快速集成人脸或指纹认证入口。  
- 需要统一风格的生物特征认证图标展示。  
- 点击图标可触发系统级身份认证流程。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct UserAuthIcon--><!--Device-unnamed-export declare struct UserAuthIcon-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { UserAuthIcon } from 'kits/@kit.UserAuthenticationKit';
```

## build

```TypeScript
build(): void
```

构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-build(): void--><!--Device-UserAuthIcon-build(): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## onIconClick

```TypeScript
onIconClick?: ClickCallbackFunc
```

图标点击回调。用户点击认证图标时触发此回调，可在回调中执行点击前的准备工作或记录用户行为日志。如果未设置此回调，点击图标后直接触发认证流程。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-onIconClick?: ClickCallbackFunc--><!--Device-UserAuthIcon-onIconClick?: ClickCallbackFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## authParam

```TypeScript
authParam: userAuth.AuthParam
```

用户认证相关参数。包含挑战值(challenge)、认证类型列表(authType)、认证可信等级(authTrustLevel)等配置。挑战值用于防重放攻击，认证类型指定可用的认证方式（如人脸、指纹、PIN），认证可信等级决定认证的安全强度。

**Type:** userAuth.AuthParam

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-authParam: userAuth.AuthParam--><!--Device-UserAuthIcon-authParam: userAuth.AuthParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## iconColor

```TypeScript
iconColor?: ResourceColor
```

图标颜色。设置认证图标的颜色，支持颜色值、资源引用等多种格式。默认使用系统激活色，开发者可根据应用主题自定义颜色，如使用Color.Blue或\$r('app.color.primary')。

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** $r('sys.color.ohos_id_color_activated')

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-iconColor?: ResourceColor--><!--Device-UserAuthIcon-iconColor?: ResourceColor-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## iconHeight

```TypeScript
iconHeight?: Dimension
```

图标高度。设置认证图标的高度，宽高比为1:1。不支持百分比字符串。建议根据界面布局选择合适的大小。

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 64fp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-iconHeight?: Dimension--><!--Device-UserAuthIcon-iconHeight?: Dimension-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## onAuthResult

```TypeScript
onAuthResult: userAuth.AuthCallbackOnResultFunc
```

认证结果回调。用户完成认证后触发此回调，回调参数包含认证结果码(result)、认证令牌(token)、认证类型(authType)等信息。应用需在此回调中处理认证结果，如认证通过时获取token用于后续安全操作，认证失败时提示用户重新尝试。

**注意：** 应用需申请`ohos.permission.ACCESS_BIOMETRIC`权限，否则应用将仅展示图标，无法正常拉起身份认证控件。

**Type:** userAuth.AuthCallbackOnResultFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-onAuthResult: userAuth.AuthCallbackOnResultFunc--><!--Device-UserAuthIcon-onAuthResult: userAuth.AuthCallbackOnResultFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## widgetParam

```TypeScript
widgetParam: userAuth.WidgetParam
```

用户认证界面配置相关参数。包含认证界面标题(title)、导航按钮文本(navigationButtonText)等配置，用于自定义认证弹窗的显示内容。

**Type:** userAuth.WidgetParam

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-widgetParam: userAuth.WidgetParam--><!--Device-UserAuthIcon-widgetParam: userAuth.WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

