# SideBarContainerType

容器内侧边栏样式枚举。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare enum SideBarContainerType--><!--Device-unnamed-declare enum SideBarContainerType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Embed

```TypeScript
Embed = 0
```

侧边栏嵌入到组件内，和内容区并列显示。适用于需要同时展示侧边栏和内容区的场景。

整体容器大小不变时，显示侧边栏会导致内容区缩小，隐藏侧边栏会扩大内容区。

组件尺寸小于[minContentWidth](SideBarContainerAttribute#minContentWidth) +  
[minSideBarWidth](SideBarContainerAttribute#minSideBarWidth(value: number))，并且未设置showSideBar时，默认不显示侧边栏。

设置了showSideBar属性时，以showSideBar属性设置的值为准。

未设置minSideBarWidth或minContentWidth时，采用对应接口的默认值进行计算。

组件在自动隐藏后，如果通过点击控制按钮唤出侧边栏，则侧边栏悬浮在内容区上显示。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SideBarContainerType-Embed = 0--><!--Device-SideBarContainerType-Embed = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Overlay

```TypeScript
Overlay = 1
```

侧边栏浮在内容区上面，不会影响内容区的大小。适用于需要临时展示侧边栏的场景。&lt;br/&gt;组件尺寸小于minContentWidth时，内容区会被截断显示。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SideBarContainerType-Overlay = 1--><!--Device-SideBarContainerType-Overlay = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 2
```

组件尺寸大于等于minSideBarWidth + minContentWidth时，采用Embed模式显示。

组件尺寸小于minSideBarWidth + minContentWidth时，采用Overlay模式显示。适用于需要响应式布局或多设备适配的场景。

未设置minSideBarWidth或minContentWidth时，会使用未设置接口的默认值进行计算，若计算的值小于600vp，则使用600vp作为模式切换的临界值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SideBarContainerType-AUTO = 2--><!--Device-SideBarContainerType-AUTO = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISPLACE

```TypeScript
DISPLACE = 3
```

侧边栏和内容区并列显示，内容区超出部分移出组件外。侧边栏展开时，内容区显示灰色蒙层（颜色为#33000000）并被禁用事件，点击内容区可收起侧边栏。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SideBarContainerType-DISPLACE = 3--><!--Device-SideBarContainerType-DISPLACE = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

