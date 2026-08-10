# SwipeEdgeEffect

滑动效果枚举。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare enum SwipeEdgeEffect--><!--Device-unnamed-declare enum SwipeEdgeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Spring

```TypeScript
Spring
```

ListItem划动距离超过划出组件大小后可以继续划动。

如果设置了删除区域，ListItem划动距离超过删除阈值后可以继续划动，

松手后按照弹簧阻尼曲线回弹。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeEdgeEffect-Spring--><!--Device-SwipeEdgeEffect-Spring-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None
```

ListItem划动距离不能超过划出组件大小。

如果设置了删除区域，ListItem划动距离不能超过删除阈值，

并且在设置删除回调的情况下，达到删除阈值后松手触发删除回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeEdgeEffect-None--><!--Device-SwipeEdgeEffect-None-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

