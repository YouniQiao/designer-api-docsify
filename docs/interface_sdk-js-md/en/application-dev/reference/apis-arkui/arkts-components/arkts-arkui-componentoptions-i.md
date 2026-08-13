# ComponentOptions

Defines the options of Component ClassDecorator.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-declare interface ComponentOptions--><!--Device-unnamed-declare interface ComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## freezeWhenInactive

```TypeScript
freezeWhenInactive : boolean
```

freeze UI state.

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ComponentOptions-freezeWhenInactive : boolean--><!--Device-ComponentOptions-freezeWhenInactive : boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## poolAccepts

```TypeScript
poolAccepts?: Function[]
```

Collection of custom components to be reused.

**Type:** Function[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ComponentOptions-poolAccepts?: Function[]--><!--Device-ComponentOptions-poolAccepts?: Function[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusePool

```TypeScript
reusePool?: ReusePoolOwnership
```

the reuse type of a custom component.

**Type:** [ReusePoolOwnership](arkts-arkui-reusepoolownership-t.md)

**Default:** perInstance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ComponentOptions-reusePool?: ReusePoolOwnership--><!--Device-ComponentOptions-reusePool?: ReusePoolOwnership-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

