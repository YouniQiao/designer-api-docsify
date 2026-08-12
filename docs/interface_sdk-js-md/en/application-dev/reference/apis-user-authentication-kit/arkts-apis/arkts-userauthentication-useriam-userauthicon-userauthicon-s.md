# UserAuthIcon

The **userAuthIcon** module is a UI component module of the OpenHarmony user identity and access management (UserIAM)system. It provides an out-of-the-box authentication icon component (**UserAuthIcon**). This component is used to display the face authentication or fingerprint authentication icon on the application UI. It supports custom icon colors and dimensions, and can directly launch the system authentication dialog box component when the icon is tapped.

This module applies to the following scenarios:

- Quickly integrating the face or fingerprint authentication entry into the application UI.  
- Displaying biometric authentication icons in a unified style.  
- Tapping the icon to trigger the system-level authentication process.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct UserAuthIcon--><!--Device-unnamed-export declare struct UserAuthIcon-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { UserAuthIcon } from '@kit.UserAuthenticationKit';
```

## build

```TypeScript
build(): void
```

The method to build the component.

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

Callback to be invoked when the icon is tapped.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-onIconClick?: ClickCallbackFunc--><!--Device-UserAuthIcon-onIconClick?: ClickCallbackFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## authParam

```TypeScript
authParam: userAuth.AuthParam
```

User authentication parameters.

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

Color of the icon. The default value is **\$r('sys.color.ohos_id_color_activated')**.

**Type:** ResourceColor

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

Height of the icon. The aspect ratio is 1:1. The default value is **64fp**. Percentage strings are not supported.

**Type:** Dimension

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

Callback used to return the user authentication result.&lt;br&gt;The application must request the `ohos.permission.ACCESS_BIOMETRIC` permission.Otherwise, it will only display the icon and cannot start the identity authentication components.

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

Parameters on the user authentication page.

**Type:** userAuth.WidgetParam

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserAuthIcon-widgetParam: userAuth.WidgetParam--><!--Device-UserAuthIcon-widgetParam: userAuth.WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

