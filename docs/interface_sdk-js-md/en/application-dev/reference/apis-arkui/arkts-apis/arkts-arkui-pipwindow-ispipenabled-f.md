# isPiPEnabled

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## isPiPEnabled

```TypeScript
function isPiPEnabled(): boolean
```

Checks whether the current device supports the PiP feature.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPWindow-function isPiPEnabled(): boolean--><!--Device-PiPWindow-function isPiPEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the PiP feature is supported. **true** if supported, **false** otherwise. |

## Examples

```TypeScript
let enable: boolean = PiPWindow.isPiPEnabled();
console.info('isPipEnabled:' + enable);
```

