# create

## Modules to Import

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(): DisplaySync
```

Creates a **DisplaySync** object, through which you can set the frame rate of the custom UI content.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DisplaySync](arkts-arkgraphics2d-displaysync-displaysync-i.md) | DisplaySync** object created. |

**Examples**

```TypeScript
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```
