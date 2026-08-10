# LazyForEachCustomComponentFreezeMode

冻结模式枚举，用于配置LazyForEach中已移出组件树的缓存自定义节点的冻结行为。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export enum LazyForEachCustomComponentFreezeMode--><!--Device-unnamed-export enum LazyForEachCustomComponentFreezeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

遵循Metadata中enableCustomComponentFreeze字段的配置来决定是否启用冻结。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachCustomComponentFreezeMode-AUTO = 0--><!--Device-LazyForEachCustomComponentFreezeMode-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISABLED

```TypeScript
DISABLED = 1
```

禁用已移出组件树的缓存自定义节点的冻结。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachCustomComponentFreezeMode-DISABLED = 1--><!--Device-LazyForEachCustomComponentFreezeMode-DISABLED = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ENABLED

```TypeScript
ENABLED = 2
```

启用已移出组件树的缓存自定义节点的冻结。开启后，缓存自定义组件的状态更新将被冻结。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachCustomComponentFreezeMode-ENABLED = 2--><!--Device-LazyForEachCustomComponentFreezeMode-ENABLED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

