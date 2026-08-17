# CursorConfig

Defines custom cursor configuration.

**Since:** 23

<!--Device-pointer-interface CursorConfig--><!--Device-pointer-interface CursorConfig-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
import { pointer } from 'pointer';
```

## followSystem

```TypeScript
followSystem : boolean
```

Whether to adjust the cursor size based on system settings. The value **true** means to adjust the cursor size based on system settings, and the value **false** means to use the custom cursor size. The adjustment range is [size of the cursor image, 256 x 256].

**Type:** boolean

**Since:** 23

<!--Device-CursorConfig-followSystem : boolean--><!--Device-CursorConfig-followSystem : boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

