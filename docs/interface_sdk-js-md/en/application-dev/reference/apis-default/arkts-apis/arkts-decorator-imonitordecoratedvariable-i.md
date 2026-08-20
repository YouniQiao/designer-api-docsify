# IMonitorDecoratedVariable

Defines @Monitor decorated variable interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IMonitorDecoratedVariable--><!--Device-unnamed-export declare interface IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(): void
```

Reset Monitor when the ComponentV2 instance is reused.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorDecoratedVariable-resetOnReuse(): void--><!--Device-IMonitorDecoratedVariable-resetOnReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
readonly path: string[]
```

Path for generated monitors, either generated or set by addMonitor parameters.

**Type:** string[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitorDecoratedVariable-readonly path: string[]--><!--Device-IMonitorDecoratedVariable-readonly path: string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

