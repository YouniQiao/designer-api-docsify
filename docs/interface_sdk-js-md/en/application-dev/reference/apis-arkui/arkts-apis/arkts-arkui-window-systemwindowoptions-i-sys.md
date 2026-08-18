# SystemWindowOptions (System API)

Describes the parameters for creating a system window.

**Since:** 23

<!--Device-window-interface SystemWindowOptions--><!--Device-window-interface SystemWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
import { floatView } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
```

## windowType

```TypeScript
windowType: WindowType
```

Window type. There is no default value. If null is passed in, the window fails to be created. **TYPE_DIALOG** is not supported.

**Type:** WindowType

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemWindowOptions-windowType: WindowType--><!--Device-SystemWindowOptions-windowType: WindowType-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

