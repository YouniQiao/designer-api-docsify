# isFloatingBallEnabled

## Modules to Import

```TypeScript
```

## isFloatingBallEnabled

```TypeScript
function isFloatingBallEnabled(): boolean
```

Checks whether the device supports floating balls.

**Since:** 23

<!--Device-floatingBall-function isFloatingBallEnabled(): boolean--><!--Device-floatingBall-function isFloatingBallEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
// Check whether the current device supports the floating ball feature.
let enable: boolean = floatingBall.isFloatingBallEnabled();
console.info('Floating ball enabled is: ' + enable);
```
