# ComponentOptions

自定义组件参数，用于配置是否支持组件冻结和全局复用池，适用于需要优化自定义组件性能表现和提升组件复用效率的场景。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface ComponentOptions--><!--Device-unnamed-declare interface ComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## freezeWhenInactive

```TypeScript
freezeWhenInactive : boolean
```

配置自定义组件支持组件冻结。true：开启组件冻结，false：不开启组件冻结。当开发者未指定ComponentOptions时，freezeWhenInactive将使用false作为默认值。

从API version 11开始，支持通过此参数配置[@Component](../../../ui/state-management/arkts-create-custom-components.md#component)组件冻结。示例可见[自定义组件冻结](../../../ui/state-management/arkts-custom-components-freeze.md)。

从API version 12开始，支持通过此参数配置  
[@ComponentV2](../../../ui/state-management/arkts-create-custom-components.md#componentv2)组件冻结。示例可见  
[自定义组件冻结](../../../ui/state-management/arkts-custom-components-freezeV2.md)。

**Type:** boolean

**Default:** false

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ComponentOptions-freezeWhenInactive : boolean--><!--Device-ComponentOptions-freezeWhenInactive : boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## poolAccepts

```TypeScript
poolAccepts?: Function[]
```

指定全局复用池可以接纳（即允许被复用）的自定义组件名称列表。当reusePool参数被设置时，系统会根据poolAccepts中列出的组件名称，将匹配的可复用组件缓存到该全局复用池中供后续复用。reusePool参数被设置时，poolAccepts必须为非空数组，单独设置poolAccepts不会使全局复用生效。当poolAccepts和reusePool都没有赋值时，全局复用不生效。

**Type:** Function[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ComponentOptions-poolAccepts?: Function[]--><!--Device-ComponentOptions-poolAccepts?: Function[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusePool

```TypeScript
reusePool?: ReusePoolOwnership
```

在自定义组件上配置全局复用池的类型，适用于应用中存在多个同类型可复用自定义组件、需要在组件实例间共享或隔离复用资源以提升复用效率的场景。如果不传入，则全局复用池不会生效。reusePool需与poolAccepts配合使用，reusePool参数被设置时，poolAccepts必须为非空数组，否则全局复用不生效。

**Type:** [ReusePoolOwnership](../arkts-apis/arkts-arkui-customcomponent-reusepoolownership-e.md)

**Default:** perInstance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ComponentOptions-reusePool?: ReusePoolOwnership--><!--Device-ComponentOptions-reusePool?: ReusePoolOwnership-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

