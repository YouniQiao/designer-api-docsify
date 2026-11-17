# create

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(): DisplaySync
```

Creates a DisplaySync object, through which you can set the frame rate of the custom UI content.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 26.0.1.

<!--Device-displaySync-function create(): DisplaySync--><!--Device-displaySync-function create(): DisplaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DisplaySync](arkts-arkgraphics2d-displaysync-displaysync-i.md) | Returns a DisplaySync object instance, which is used to set the frame rate range, register the frame callback function, and control the start and stop of the callback. |

**Examples**

```TypeScript
// Create a DisplaySync object.
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```
