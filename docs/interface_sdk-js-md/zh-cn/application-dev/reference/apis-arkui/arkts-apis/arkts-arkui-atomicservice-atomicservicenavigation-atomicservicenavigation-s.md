# AtomicServiceNavigation

作为Page页面的根容器使用，其内部默认包含了标题栏、内容区。其中，内容区在首页默认显示导航内容，在非首页显示  
[NavDestination]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_的子组件，首页和非首页通过路由进行切换。
    **说明：**  
    
    该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct AtomicServiceNavigation--><!--Device-unnamed-export declare struct AtomicServiceNavigation-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navDestinationBuilder

```TypeScript
navDestinationBuilder?: NavDestinationBuilder
```

创建NavDestination组件所需要的Builder数据。默认值为空，即无内容展示。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @BuilderParam

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-navDestinationBuilder?: NavDestinationBuilder--><!--Device-AtomicServiceNavigation-navDestinationBuilder?: NavDestinationBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## gradientBackground

```TypeScript
gradientBackground?: GradientBackground
```

渐变背景色选项。设置时各字段的默认值见GradientBackground。

**类型：** GradientBackground

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-gradientBackground?: GradientBackground--><!--Device-AtomicServiceNavigation-gradientBackground?: GradientBackground-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## hideTitleBar

```TypeScript
hideTitleBar?: boolean
```

设置是否隐藏标题栏。默认为false。false表示显示标题栏，true表示隐藏标题栏。

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-hideTitleBar?: boolean--><!--Device-AtomicServiceNavigation-hideTitleBar?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## menus

```TypeScript
menus?: CustomBuilder | Array<NavigationMenuItem>
```

宽屏场景下用户自定义插入的布局样式。默认值为空，不显示任何样式。屏幕宽度低于600vp为非宽屏场景，大于等于600vp为宽屏场景。

**类型：** CustomBuilder \| Array&lt;NavigationMenuItem&gt;

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**装饰器类型：** @BuilderParam

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-menus?: CustomBuilder | Array<NavigationMenuItem>--><!--Device-AtomicServiceNavigation-menus?: CustomBuilder | Array<NavigationMenuItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## minContentWidth

```TypeScript
minContentWidth?: Dimension
```

设置导航栏内容区最小宽度（双栏模式下生效）。默认值为360vp。

**类型：** Dimension

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-minContentWidth?: Dimension--><!--Device-AtomicServiceNavigation-minContentWidth?: Dimension-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: NavigationMode
```

设置导航栏的显示模式。默认值为Auto。支持Stack、Split与Auto模式。

**类型：** NavigationMode

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-mode?: NavigationMode--><!--Device-AtomicServiceNavigation-mode?: NavigationMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## modeChangeCallback

```TypeScript
modeChangeCallback?: Callback<NavigationMode>
```

当Navigation首次显示或者单双栏状态发生变化时触发该回调。默认值为空。

**类型：** Callback&lt;NavigationMode&gt;

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-modeChangeCallback?: Callback<NavigationMode>--><!--Device-AtomicServiceNavigation-modeChangeCallback?: Callback<NavigationMode>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navBarWidth

```TypeScript
navBarWidth?: Length
```

设置导航栏宽度。默认值为240vp。仅在Navigation组件分栏时生效。

**类型：** Length

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-navBarWidth?: Length--><!--Device-AtomicServiceNavigation-navBarWidth?: Length-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navBarWidthRange

```TypeScript
navBarWidthRange?: [
    Dimension,
    Dimension
  ]
```

设置导航栏最小和最大宽度（双栏模式下生效）。默认值：最小为240vp，最大为组件宽度的40%，且不大于432vp，如果只设置一个值，则未设置的值按照默认值计算。单位：vp。

**类型：** [     Dimension,     Dimension   ]

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-navBarWidthRange?: [    Dimension,    Dimension  ]--><!--Device-AtomicServiceNavigation-navBarWidthRange?: [    Dimension,    Dimension  ]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navPathStack

```TypeScript
navPathStack?: NavPathStack
```

路由栈信息。默认值为new NavPathStack()。

**类型：** NavPathStack

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @State

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-navPathStack?: NavPathStack--><!--Device-AtomicServiceNavigation-navPathStack?: NavPathStack-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## navigationContent

```TypeScript
navigationContent?: Callback<void>
```

Navigation容器内容。默认值为空，无内容展示。

**类型：** Callback&lt;void&gt;

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @BuilderParam

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-navigationContent?: Callback<void>--><!--Device-AtomicServiceNavigation-navigationContent?: Callback<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## sideBarContent

```TypeScript
sideBarContent?: Callback<void>
```

侧边栏的内容。默认值为空。

**类型：** Callback&lt;void&gt;

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**装饰器类型：** @BuilderParam

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-sideBarContent?: Callback<void>--><!--Device-AtomicServiceNavigation-sideBarContent?: Callback<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## sideBarOptions

```TypeScript
sideBarOptions?: SideBarOptions
```

侧边栏的功能选项。默认值为{ sideBarBackground: \$r('sys.color.ohos\_id\_color\_sub\_background'), sideBarIcon: \$r('sys.symbol.open\_sidebar') }。

**类型：** SideBarOptions

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-sideBarOptions?: SideBarOptions--><!--Device-AtomicServiceNavigation-sideBarOptions?: SideBarOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## stateChangeCallback

```TypeScript
stateChangeCallback?: Callback<boolean>
```

导航栏显示状态切换时触发该回调。true表示导航栏显示，false表示导航栏隐藏。默认值为空。

**类型：** Callback&lt;boolean&gt;

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-stateChangeCallback?: Callback<boolean>--><!--Device-AtomicServiceNavigation-stateChangeCallback?: Callback<boolean>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

设置页面标题。默认值为空字符串。当titleOptions的titleBarType字段设置为TitleBarType.ROUND\_ICON或者TitleBarType.SQUARED\_ICON，且设置了titleIcon时，title标题内容将不会显示。

**类型：** ResourceStr

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-title?: ResourceStr--><!--Device-AtomicServiceNavigation-title?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## titleOptions

```TypeScript
titleOptions?: TitleOptions
```

标题栏选项。默认值为{ isBlurEnabled: true }。当titleBarType字段设置为TitleBarType.ROUND\_ICON或者TitleBarType.SQUARED\_ICON，且设置了titleIcon时，title标题内容将不会显示。

**类型：** TitleOptions

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**装饰器类型：** @Prop

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AtomicServiceNavigation-titleOptions?: TitleOptions--><!--Device-AtomicServiceNavigation-titleOptions?: TitleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

