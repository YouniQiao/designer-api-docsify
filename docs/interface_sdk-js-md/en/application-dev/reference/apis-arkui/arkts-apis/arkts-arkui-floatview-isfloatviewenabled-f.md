# isFloatViewEnabled

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## isFloatViewEnabled

```TypeScript
function isFloatViewEnabled(): boolean
```

判断当前设备是否支持标准悬浮窗功能。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function isFloatViewEnabled(): boolean--><!--Device-floatView-function isFloatViewEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前设备是否支持标准悬浮窗功能。true表示支持，false则表示不支持。 |

## Examples

```TypeScript
// Check whether the current device supports the float view feature.
let enable: boolean = floatView.isFloatViewEnabled();
console.info('Float view enabled is: ' + enable);
```

