# ReusePoolOwnership

重用池所有权的枚举

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare enum ReusePoolOwnership--><!--Device-unnamed-export declare enum ReusePoolOwnership-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SHARED

```TypeScript
SHARED = 'shared'
```

共享所有权。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReusePoolOwnership-SHARED = 'shared'--><!--Device-ReusePoolOwnership-SHARED = 'shared'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PER_INSTANCE

```TypeScript
PER_INSTANCE = 'perInstance'
```

重用池是每个实例拥有的，而不是共享的。这是自定义组件复用池的默认模式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReusePoolOwnership-PER_INSTANCE = 'perInstance'--><!--Device-ReusePoolOwnership-PER_INSTANCE = 'perInstance'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFF

```TypeScript
OFF = 'off'
```

复用池关闭。这是自定义组件复用池的默认模式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReusePoolOwnership-OFF = 'off'--><!--Device-ReusePoolOwnership-OFF = 'off'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

