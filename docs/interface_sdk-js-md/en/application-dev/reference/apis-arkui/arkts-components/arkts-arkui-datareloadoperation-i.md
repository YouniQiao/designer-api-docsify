# DataReloadOperation

重载所有数据操作，并配置是否允许在更新过程中复用旧的子组件。当onDatasetChange含有DataOperationType.RELOAD操作时，其余操作全部失效，框架会自己调用keyGenerator进行键值比对。

配置允许在更新过程中复用旧的子组件，并和[@Reusable](../../../ui/state-management/arkts-reusable.md)/  
[@ReusableV2](../../../ui/state-management/arkts-new-reusableV2.md)配合使用时，优先使用复用池中的组件，若复用池中无可复用的组件，而LazyForEach的旧子组件中有可复用的组件，该组件将被回收，并复用为新的子组件。当LazyForEach的旧子组件中也没有可复用的组件时，将创建新的子组件。

配置允许在更新过程中复用旧的子组件，未使用@Reusable/@ReusableV2时，键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件。

配置不允许在更新过程中复用旧的子组件，键值没有变化的数据项会使用原先的子组件，键值发生变化的数据项，若使用了@Reusable/@ReusableV2且复用池中有可用的组件，将复用旧组件，否则将创建新的子组件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataReloadOperation--><!--Device-unnamed-interface DataReloadOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuseImmediately

```TypeScript
reuseImmediately?: boolean
```

是否允许在更新过程中复用旧的子组件。

true：允许在更新过程中复用旧的子组件。

false：不允许在更新过程中复用旧的子组件。

默认值：false

当值为undefined或null时，取默认值。

**Type:** boolean

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DataReloadOperation-reuseImmediately?: boolean--><!--Device-DataReloadOperation-reuseImmediately?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.RELOAD
```

数据全部重载类型。

**Type:** DataOperationType.RELOAD

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataReloadOperation-type: DataOperationType.RELOAD--><!--Device-DataReloadOperation-type: DataOperationType.RELOAD-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

