# SideBarContainerType

容器内侧边栏样式枚举。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum SideBarContainerType--><!--Device-unnamed-export declare enum SideBarContainerType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Embed

```TypeScript
Embed = 0
```

侧边栏嵌入到组件内，和内容区并列显示。

整体容器大小不变时，显示侧边栏会导致内容区缩小，隐藏侧边栏会扩大内容区。

组件尺寸小于[minContentWidth](SideBarContainerAttribute.minContentWidth) +   
[minSideBarWidth](SideBarContainerAttribute.minSideBarWidth)，并且未设置showSideBar时，侧边栏自动隐藏。

未设置minSideBarWidth或者minContentWidth采用未设置接口的默认值进行计算。

组件在自动隐藏后，如果通过点击控制按钮唤出侧边栏，则侧边栏悬浮在内容区上显示。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerType-Embed = 0--><!--Device-SideBarContainerType-Embed = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Overlay

```TypeScript
Overlay = 1
```

侧边栏浮在内容区上面，不会影响内容区的大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerType-Overlay = 1--><!--Device-SideBarContainerType-Overlay = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 2
```

组件尺寸大于等于minSideBarWidth + minContentWidth时，采用Embed模式显示。

组件尺寸小于minSideBarWidth + minContentWidth时，采用Overlay模式显示。

未设置minSideBarWidth或minContentWidth时，会使用未设置接口的默认值进行计算，若计算的值小于600vp，则使用600vp做为模式切换的断点值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerType-AUTO = 2--><!--Device-SideBarContainerType-AUTO = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISPLACE

```TypeScript
DISPLACE =3
```

侧边栏位移。侧边栏是可见的，内容将离开屏幕，为侧边栏腾出空间。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SideBarContainerType-DISPLACE =3--><!--Device-SideBarContainerType-DISPLACE =3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

