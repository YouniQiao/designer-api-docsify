# GeometryTransitionOptions

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface GeometryTransitionOptions--><!--Device-unnamed-declare interface GeometryTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hierarchyStrategy

```TypeScript
hierarchyStrategy?: TransitionHierarchyStrategy
```

决定共享元素动画过程中in/out组件在组件树上层级位置的移动策略，默认值：TransitionHierarchyStrategy.ADAPTIVE。

实际影响绑定的in/out组件相对其他组件的前后重叠关系，常规情况下慎重修改。

建议在发现共享元素动画过程中出现组件前后重叠关系错误时需要调整再设置此参数。

**系统接口：** 此接口为系统接口。

**Type:** [TransitionHierarchyStrategy](../arkts-apis/arkts-arkui-common-transitionhierarchystrategy-e-sys.md)

**Default:** TransitionHierarchyStrategy.ADAPTIVE

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12 - 12.

<!--Device-GeometryTransitionOptions-hierarchyStrategy?: TransitionHierarchyStrategy--><!--Device-GeometryTransitionOptions-hierarchyStrategy?: TransitionHierarchyStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

