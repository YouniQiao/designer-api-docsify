# CursorConfig

自定义光标配置。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-pointer-interface CursorConfig--><!--Device-pointer-interface CursorConfig-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## followSystem

```TypeScript
followSystem : boolean
```

是否根据系统设置调整光标大小。false表示使用自定义光标样式大小，true表示根据系统设置调整光标大小，可调整范围为：[光标资源图大小，256×256]。

**Type:** boolean

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-CursorConfig-followSystem : boolean--><!--Device-CursorConfig-followSystem : boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

