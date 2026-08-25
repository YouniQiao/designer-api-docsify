# WindowSnapshotAnimationConfig

Configuration for window snapshot animation.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## delay

```TypeScript
delay?: long
```

The delay before the window snapshot fade-out animation begins (ms). If left unspecified, the parameter defaults to a value determined by the system animation context: 350 for transitions between WindowStatusType.FLOATING and WindowStatusType.FULLSCREEN window status. 50 for all other screenshot animation scenarios. The valid range for this parameter is 0-350.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

## duration

```TypeScript
duration?: long
```

The duration of the window snapshot fade-out animation (ms). If left unspecified, the parameter defaults to a value determined by the system animation context: 400 for transitions between WindowStatusType.FLOATING and WindowStatusType.FULLSCREEN window status. 250 for all other screenshot animation scenarios. The valid range for this parameter is 0-400.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager
