# NavigationTitleMode

标题栏显示模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum NavigationTitleMode--><!--Device-unnamed-export declare enum NavigationTitleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Free

```TypeScript
Free = 0
```

当内容为满一屏的可滚动组件时，标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。

**说明：**

标题随着内容滚动大小联动的动效在title设置为ResourceStr和NavigationCommonTitle时生效，设置成其余自定义节点类型时字体样式无法变化，下拉时只影响标题栏偏移。

可滚动组件不满一屏时，如果想使用联动效果，就要使用滚动组件提供的  
[edgeEffect](../../../reference/apis-arkui/arkui-ts/ts-container-list.md#edgeeffect)接口将options参数设置为true。未滚动状态，标题栏高度与Full模式一致；滚动时，标题栏的最小高度与Mini模式一致。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleMode-Free = 0--><!--Device-NavigationTitleMode-Free = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Full

```TypeScript
Full
```

The title is full mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleMode-Full--><!--Device-NavigationTitleMode-Full-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Mini

```TypeScript
Mini
```

The title is mini mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleMode-Mini--><!--Device-NavigationTitleMode-Mini-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

