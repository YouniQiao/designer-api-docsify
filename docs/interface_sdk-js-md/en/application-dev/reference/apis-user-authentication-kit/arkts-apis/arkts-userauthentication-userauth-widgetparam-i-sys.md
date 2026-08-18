# WidgetParam

Represents the information presented on the user authentication page. This API is used to configure the display style and interaction mode of the authentication screen, including the title, navigation button text, and window mode. By properly setting these parameters, you can provide clear authentication guidance and good interaction experience for users.

**Since:** 23

<!--Device-userAuth-interface WidgetParam--><!--Device-userAuth-interface WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { UserAuthIcon } from '@kit.UserAuthenticationKit';
import { UserAuthIcon } from '@kit.UserAuthenticationKit';
```

## appWindow

```TypeScript
appWindow?: window.Window
```

Application window object. It is used to display the identity authentication dialog box as an application modal dialog. It is suitable for scenarios where the authentication dialog box needs to be controlled through a window object. If this parameter is provided, **uiContext** will be ignored.

**Type:** window.Window

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WidgetParam-appWindow?: window.Window--><!--Device-WidgetParam-appWindow?: window.Window-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

## windowMode

```TypeScript
windowMode?: WindowModeType
```

Window type of the user authentication screen. **DIALOG_BOX** is suitable for most authentication scenarios (with better user experience), and **FULLSCREEN** is suitable for scenarios that require an immersive authentication experience or involve more authentication information. If not specified, the default value is **WindowModeType.DIALOG_BOX**.

**Type:** [WindowModeType](arkts-userauthentication-userauth-windowmodetype-e-sys.md)

**Default:** WindowModeType.DIALOG_BOX

**Since:** 23

<!--Device-WidgetParam-windowMode?: WindowModeType--><!--Device-WidgetParam-windowMode?: WindowModeType-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

