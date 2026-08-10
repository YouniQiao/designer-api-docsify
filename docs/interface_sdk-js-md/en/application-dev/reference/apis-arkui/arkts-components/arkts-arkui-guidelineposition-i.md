# GuideLinePosition

guideLine位置参数，用于定义guideLine的位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface GuideLinePosition--><!--Device-unnamed-declare interface GuideLinePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end? : Dimension
```

guideLine距离容器右侧或者底部的距离。单位：vp。与start二选一，若同时声明则仅start生效。若容器的width被声明为"auto"，则Axis.Vertical类型的guideLine不支持使用end方式声明；若容器的height被声明为"auto"，则Axis.Horizontal类型的guideLine不支持使用end方式声明。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GuideLinePosition-end? : Dimension--><!--Device-GuideLinePosition-end? : Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start? : Dimension
```

guideLine距离容器左侧或者顶部的距离。单位：vp。

默认值：0。与end二选一，若同时声明则仅start生效。若容器的width被声明为"auto"，则Axis.Vertical类型的guideLine只能使用start方式声明（不允许使用百分比）；若容器的height被声明为"auto"，则Axis.Horizontal类型的guideLine只能使用start方式声明（不允许使用百分比）。

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GuideLinePosition-start? : Dimension--><!--Device-GuideLinePosition-start? : Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

