# create

## Modules to Import

```TypeScript
import { displaySync } from 'kits/@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(): DisplaySync
```

创建DisplaySync对象，通过此对象设置UI自绘制内容帧率。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-displaySync-function create(): DisplaySync--><!--Device-displaySync-function create(): DisplaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DisplaySync](arkts-arkgraphics2d-displaysync-displaysync-i.md) | 返回DisplaySync对象实例，用于设置帧率范围、注册帧回调函数以及控制回调的启动和停止。 |

## Examples

```TypeScript
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```

