# ShowWindowOptions

显示子窗口或系统窗口时的参数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-window-interface ShowWindowOptions--><!--Device-window-interface ShowWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## focusOnShow

```TypeScript
focusOnShow?: boolean
```

窗口调用[showWindow()](arkts-arkui-window-window-i.md#showwindow)显示时是否自动获焦，默认为true。该参数对主窗、模态窗、dialog窗口不生效。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ShowWindowOptions-focusOnShow?: boolean--><!--Device-ShowWindowOptions-focusOnShow?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

