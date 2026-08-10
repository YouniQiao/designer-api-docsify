# GeometryTransitionOptions

Defines the options of geometry transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GeometryTransitionOptions--><!--Device-unnamed-export declare interface GeometryTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hierarchyStrategy

```TypeScript
hierarchyStrategy?: TransitionHierarchyStrategy
```

决定共享元素动画过程中in/out组件在组件树上层级位置的移动策略，默认值：TransitionHierarchyStrategy.ADAPTIVE。

实际影响绑定的in/out组件相对其他组件的前后重叠关系，常规情况下慎重修改。

建议在发现共享元素动画过程中出现组件前后重叠关系错误时需要调整再设置此参数。

**系统接口：** 此接口为系统接口。

**Type:** [TransitionHierarchyStrategy](arkts-arkui-common-transitionhierarchystrategy-e-sys.md)

**Default:** TransitionHierarchyStrategy.ADAPTIVE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeometryTransitionOptions-hierarchyStrategy?: TransitionHierarchyStrategy--><!--Device-GeometryTransitionOptions-hierarchyStrategy?: TransitionHierarchyStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

