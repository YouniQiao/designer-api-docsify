# WindowCreateParams

Describes the window parameters during application startup.

**Since:** 20

<!--Device-window-interface WindowCreateParams--><!--Device-window-interface WindowCreateParams-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## animationParams

```TypeScript
animationParams?: StartAnimationParams
```

The params of start animation

**Type:** StartAnimationParams

**Since:** 20

<!--Device-WindowCreateParams-animationParams?: StartAnimationParams--><!--Device-WindowCreateParams-animationParams?: StartAnimationParams-End-->

**System capability:** SystemCapability.Window.SessionManager

## needAnimation

```TypeScript
needAnimation?: boolean
```

Whether to need start animation

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowCreateParams-needAnimation?: boolean--><!--Device-WindowCreateParams-needAnimation?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

