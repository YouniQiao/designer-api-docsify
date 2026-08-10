# CommonController

公共控制器，可以控制promptAction相关组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-promptAction-export class CommonController--><!--Device-promptAction-export class CommonController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## close

```TypeScript
close(): void
```

关闭显示的自定义弹窗，若已关闭，则不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonController-close(): void--><!--Device-CommonController-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

控制器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonController-constructor()--><!--Device-CommonController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getState

```TypeScript
getState(): CommonState
```

获取自定义弹窗的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonController-getState(): CommonState--><!--Device-CommonController-getState(): CommonState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) | 返回对应的弹窗状态。 |

