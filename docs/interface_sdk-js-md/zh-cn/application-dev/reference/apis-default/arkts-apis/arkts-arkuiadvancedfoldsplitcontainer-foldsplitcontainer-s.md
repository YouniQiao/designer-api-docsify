# FoldSplitContainer

实现折叠屏二分栏、三分栏在展开态、悬停态以及折叠态的区域控制的分栏布局。

@interface FoldSplitContainer

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct FoldSplitContainer--><!--Device-unnamed-export declare struct FoldSplitContainer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
    build(): void
```

构造组件的方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@Builder    build(): void--><!--Device-FoldSplitContainer-@Builder    build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## animationOptions

```TypeScript
@PropRef
    animationOptions?: AnimateParam
```

设置动画效果相关的参数。

**类型：** [AnimateParam](arkts-common-animateparam-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@PropRef    animationOptions?: AnimateParam--><!--Device-FoldSplitContainer-@PropRef    animationOptions?: AnimateParam-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## expandedLayoutOptions

```TypeScript
@PropRef
    expandedLayoutOptions: ExpandedRegionLayoutOptions
```

展开态布局信息。

**类型：** [ExpandedRegionLayoutOptions](arkts-arkuiadvancedfoldsplitcontainer-expandedregionlayoutoptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@PropRef    expandedLayoutOptions: ExpandedRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    expandedLayoutOptions: ExpandedRegionLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## extra

```TypeScript
@BuilderParam
    extra?: RegionBuilder
```

扩展区域回调函数，不传入的情况，没有对应区域。

**类型：** [RegionBuilder](arkts-regionbuilder-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@BuilderParam    extra?: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    extra?: RegionBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## foldedLayoutOptions

```TypeScript
@PropRef
    foldedLayoutOptions: FoldedRegionLayoutOptions
```

折叠态布局信息。

**类型：** [FoldedRegionLayoutOptions](arkts-arkuiadvancedfoldsplitcontainer-foldedregionlayoutoptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@PropRef    foldedLayoutOptions: FoldedRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    foldedLayoutOptions: FoldedRegionLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## hoverModeLayoutOptions

```TypeScript
@PropRef
    hoverModeLayoutOptions: HoverModeRegionLayoutOptions
```

悬停态布局信息。

**类型：** [HoverModeRegionLayoutOptions](arkts-arkuiadvancedfoldsplitcontainer-hovermoderegionlayoutoptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@PropRef    hoverModeLayoutOptions: HoverModeRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    hoverModeLayoutOptions: HoverModeRegionLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onHoverStatusChange

```TypeScript
onHoverStatusChange?: OnHoverStatusChangeHandler
```

折叠屏进入或退出悬停模式时触发的回调函数。

**类型：** [OnHoverStatusChangeHandler](arkts-onhoverstatuschangehandler-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler--><!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primary

```TypeScript
@BuilderParam
    primary: RegionBuilder
```

主要区域回调函数。

**类型：** [RegionBuilder](arkts-regionbuilder-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@BuilderParam    primary: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    primary: RegionBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondary

```TypeScript
@BuilderParam
    secondary: RegionBuilder
```

次要区域回调函数。

**类型：** [RegionBuilder](arkts-regionbuilder-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FoldSplitContainer-@BuilderParam    secondary: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    secondary: RegionBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

