# navigation

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [Navigation](arkts-arkui-navigation-navigation-f.md#navigation) | 绑定导航控制器到Navigation组件，适用于使用[NavPathStack](arkts-arkui-navigation-navpathstack-c.md#NavPathStack)配合  [navDestination](arkts-arkui-navigation-navigationattribute-i.md#navDestination)属性进行页面路由。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) | 路由页面信息。 |
| [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。  从API version 12开始，NavPathStack允许被继承，派生类对象可以替代基类NavPathStack对象使用。使用示例参见  [示例10](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation copy.md#示例10定义导航控制器派生类)。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [HomePathInfo](arkts-arkui-navigation-homepathinfo-i.md) | 主页NavDestination的信息。 |
| [MoreButtonOptions](arkts-arkui-navigation-morebuttonoptions-i.md) | 更多图标的菜单选项。 |
| [NavContentInfo](arkts-arkui-navigation-navcontentinfo-i.md) | 跳转Destination信息。 |
| [NavigationAnimatedTransition](arkts-arkui-navigation-navigationanimatedtransition-i.md) | 自定义转场动画协议，开发者需实现该协议来定义Navigation路由跳转的跳转动画。 |
| [NavigationAttribute](arkts-arkui-navigation-navigationattribute-i.md) | 除支持[通用属性](./../../@internal/component/ets/common)外，还支持以下属性： |
| [NavigationCommonTitle](arkts-arkui-navigation-navigationcommontitle-i.md) | Navigation通用标题。 |
| [NavigationCustomTitle](arkts-arkui-navigation-navigationcustomtitle-i.md) | Navigation自定义标题。 |
| [NavigationDividerStyle](arkts-arkui-navigation-navigationdividerstyle-i.md) | Navigation分割线颜色及上下边距。 |
| [NavigationInterception](arkts-arkui-navigation-navigationinterception-i.md) | Navigation跳转拦截对象。 |
| [NavigationMenuItem](arkts-arkui-navigation-navigationmenuitem-i.md) | 导航菜单项，包括菜单图标和菜单信息。 |
| [NavigationMenuOptions](arkts-arkui-navigation-navigationmenuoptions-i.md) | 页面右上角菜单选项。 |
| [NavigationModuleInfo](arkts-arkui-navigation-navigationmoduleinfo-i.md) | Navigation的模块信息。 |
| [NavigationOptions](arkts-arkui-navigation-navigationoptions-i.md) | 路由栈操作选项。 |
| [NavigationTitleOptions](arkts-arkui-navigation-navigationtitleoptions-i.md) | 标题栏选项。 |
| [NavigationToolbarOptions](arkts-arkui-navigation-navigationtoolbaroptions-i.md) | 工具栏选项。 |
| [NavigationTransitionProxy](arkts-arkui-navigation-navigationtransitionproxy-i.md) | 自定义转场动画代理对象。 |
| [PopInfo](arkts-arkui-navigation-popinfo-i.md) | 下一个页面返回的回调信息载体。 |
| [ScrollEffectOptions](arkts-arkui-navigation-scrolleffectoptions-i.md) | 标题栏滑动效果类型。 |
| [ToolbarItem](arkts-arkui-navigation-toolbaritem-i.md) | 工具栏可配置参数。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BarStyle](arkts-arkui-navigation-barstyle-e.md) | 标题栏或工具栏的布局样式。NavDestination的工具栏不支持设置该属性。 |
| [LaunchMode](arkts-arkui-navigation-launchmode-e.md) | 路由栈操作模式。 |
| [NavBarPosition](arkts-arkui-navigation-navbarposition-e.md) | 导航页位置。 |
| [NavigationMode](arkts-arkui-navigation-navigationmode-e.md) | 导航页显示模式。Navigation处于分栏显示状态时，导航页和内容区之间会显示分割线。 |
| [NavigationOperation](arkts-arkui-navigation-navigationoperation-e.md) | 页面跳转类型。 |
| [NavigationTitleMode](arkts-arkui-navigation-navigationtitlemode-e.md) | 标题栏显示模式。 |
| [ScrollEffectType](arkts-arkui-navigation-scrolleffecttype-e.md) | 标题栏滑动模糊效果类型。 |
| [ToolbarItemStatus](arkts-arkui-navigation-toolbaritemstatus-e.md) | 工具栏单个选项的状态。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [InterceptionCallback](arkts-arkui-interceptioncallback-t.md) | Navigation页面跳转前的拦截回调。 |
| [InterceptionModeCallback](arkts-arkui-interceptionmodecallback-t.md) | Navigation单双栏显示状态发生变更时的拦截回调。 |
| [InterceptionShowCallback](arkts-arkui-interceptionshowcallback-t.md) | Navigation页面跳转前和页面跳转后的拦截回调。 |
| [NavBar](arkts-arkui-navbar-t.md) | Navigation首页名字。 |
| [SystemBarStyle](arkts-arkui-systembarstyle-t.md) | 状态栏的属性。在设置页面级状态栏属性时使用。 |
| [UpdateTransitionCallback](arkts-arkui-updatetransitioncallback-t.md) | 交互转场动画进度。 |

