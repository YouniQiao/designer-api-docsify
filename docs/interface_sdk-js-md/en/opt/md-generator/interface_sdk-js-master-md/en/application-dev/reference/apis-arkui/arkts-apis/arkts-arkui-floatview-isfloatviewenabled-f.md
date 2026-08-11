# isFloatViewEnabled

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## isFloatViewEnabled

```TypeScript
function isFloatViewEnabled(): boolean
```

Checks whether the device supports the float view.

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Description|
|------------|------------|
| boolean |

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function isFloatViewEnabled(): boolean--><!--Device-floatView-function isFloatViewEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// Check whether the current device supports the float view feature.
let enable: boolean = floatView.isFloatViewEnabled();
console.info('Float view enabled is: ' + enable);
```
