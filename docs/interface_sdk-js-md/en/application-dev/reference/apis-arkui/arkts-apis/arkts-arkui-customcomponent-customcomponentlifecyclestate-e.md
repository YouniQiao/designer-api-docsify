# CustomComponentLifecycleState

Enum for Lifecycle State type

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## INIT

```TypeScript
INIT = 0
```

Lifecycle init state. Custom components are in this state when they are created. The next state after the init state is the appear state, which will trigger aboutToAppear.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## APPEARED

```TypeScript
APPEARED = 1
```

Lifecycle appeared state. Custom components are in this stage when they are about to be built. The next state after the appeared state is the built state, which will trigger onDidBuild.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BUILT

```TypeScript
BUILT = 2
```

Lifecycle built state. The next state after the built state could be the recycled state or disappeared state.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RECYCLED

```TypeScript
RECYCLED = 3
```

Lifecycle recycled state. Custom components are in the state of being recycled or reused. The next state after the recycle state could be the built state or the disappeared state.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISAPPEARED

```TypeScript
DISAPPEARED = 4
```

Lifecycle disappeared state. The disappeared state is the end state of a custom component's lifecycle. The init, built and recycled states could transfer to the disappeared state.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
