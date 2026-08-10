# IMonitorDecoratedVariable

Defines @Monitor decorated variable interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IMonitorDecoratedVariable--><!--Device-unnamed-export declare interface IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(): void
```

ComponentV2被重用时重置Monitor。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorDecoratedVariable-resetOnReuse(): void--><!--Device-IMonitorDecoratedVariable-resetOnReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
readonly path: string[]
```

获取所有被监听的状态变量的路径。

**Type:** string[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorDecoratedVariable-readonly path: string[]--><!--Device-IMonitorDecoratedVariable-readonly path: string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

