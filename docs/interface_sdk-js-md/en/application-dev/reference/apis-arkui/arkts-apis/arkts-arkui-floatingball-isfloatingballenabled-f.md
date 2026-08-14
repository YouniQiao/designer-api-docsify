# isFloatingBallEnabled

## Modules to Import

```TypeScript
import { floatingBall } from 'floatingBall';
```

## isFloatingBallEnabled

```TypeScript
function isFloatingBallEnabled(): boolean
```

Checks whether the device supports floating balls.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

