# WindowSnapshotAnimationConfig

Configuration for window snapshot animation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-window-interface WindowSnapshotAnimationConfig--><!--Device-window-interface WindowSnapshotAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'window';
```

## delay

```TypeScript
delay?: long
```

The delay before the window snapshot fade-out animation begins (ms). If left unspecified, the parameter defaults to a value determined by the system animation context: 350 for transitions between WindowStatusType.FLOATING and WindowStatusType.FULLSCREEN window status. 50 for all other screenshot animation scenarios. The valid range for this parameter is 0-350.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSnapshotAnimationConfig-delay?: long--><!--Device-WindowSnapshotAnimationConfig-delay?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## duration

```TypeScript
duration?: long
```

The duration of the window snapshot fade-out animation (ms). If left unspecified, the parameter defaults to a value determined by the system animation context: 400 for transitions between WindowStatusType.FLOATING and WindowStatusType.FULLSCREEN window status. 250 for all other screenshot animation scenarios. The valid range for this parameter is 0-400.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSnapshotAnimationConfig-duration?: long--><!--Device-WindowSnapshotAnimationConfig-duration?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

