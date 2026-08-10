# ExtensionWindowConfig (System API)

创建扩展窗口时需要配置的参数。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-window-interface ExtensionWindowConfig--><!--Device-window-interface ExtensionWindowConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## subWindowOptions

```TypeScript
subWindowOptions?: SubWindowOptions
```

创建子窗口的参数。无默认参数，当windowAttribute配置为SUB_WINDOW时必选，否则会导致窗口创建失败。

**Type:** [SubWindowOptions](arkts-arkui-window-subwindowoptions-i-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtensionWindowConfig-subWindowOptions?: SubWindowOptions--><!--Device-ExtensionWindowConfig-subWindowOptions?: SubWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## systemWindowOptions

```TypeScript
systemWindowOptions?: SystemWindowOptions
```

创建系统窗口的参数。无默认参数，当windowAttribute配置为SYSTEM_WINDOW时必选，否则会导致窗口创建失败。

**Type:** [SystemWindowOptions](arkts-arkui-window-systemwindowoptions-i-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtensionWindowConfig-systemWindowOptions?: SystemWindowOptions--><!--Device-ExtensionWindowConfig-systemWindowOptions?: SystemWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## windowAttribute

```TypeScript
windowAttribute: ExtensionWindowAttribute
```

窗口的属性。用于配置创建的窗口是子窗口还是系统窗口。当windowAttribute配置为SUB_WINDOW时须配置subWindowOptions，当windowAttribute配置为SYSTEM_WINDOW时须配置systemWindowOptions，否则创建窗口失败。

**Type:** [ExtensionWindowAttribute](arkts-arkui-window-extensionwindowattribute-e-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtensionWindowConfig-windowAttribute: ExtensionWindowAttribute--><!--Device-ExtensionWindowConfig-windowAttribute: ExtensionWindowAttribute-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## windowName

```TypeScript
windowName: string
```

窗口名。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtensionWindowConfig-windowName: string--><!--Device-ExtensionWindowConfig-windowName: string-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## windowRect

```TypeScript
windowRect: Rect
```

窗口矩形区域。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtensionWindowConfig-windowRect: Rect--><!--Device-ExtensionWindowConfig-windowRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

