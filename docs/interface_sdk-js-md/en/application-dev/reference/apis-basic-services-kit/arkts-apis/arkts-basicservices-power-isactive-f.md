# isActive

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## isActive

```TypeScript
function isActive(): boolean
```

Checks whether the current device is active.  
- A device with a screen is active when the screen is on and inactive when the screen is off.  
- A device without a screen is active when it exits the sleep mode and inactive when it enters the sleep mode.

**Since:** 9

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
