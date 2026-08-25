# SystemWindowOptions (System API)

Describes the parameters for creating a system window.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## windowType

```TypeScript
windowType: WindowType
```

Window type. There is no default value. If null is passed in, the window fails to be created. **TYPE_DIALOG** is not supported.

**Type:** WindowType

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.
