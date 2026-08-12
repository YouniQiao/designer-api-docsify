# isFloatingBallEnabled

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
```

## isFloatingBallEnabled

```TypeScript
function isFloatingBallEnabled(): boolean
```

Checks whether the device supports floating balls.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-floatingBall-function isFloatingBallEnabled(): boolean--><!--Device-floatingBall-function isFloatingBallEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of floating balls. **true** if supported, **false** otherwise. |

## Examples

```TypeScript
let enable: boolean = floatingBall.isFloatingBallEnabled();
console.info('Floating ball enabled is: ' + enable);
```

