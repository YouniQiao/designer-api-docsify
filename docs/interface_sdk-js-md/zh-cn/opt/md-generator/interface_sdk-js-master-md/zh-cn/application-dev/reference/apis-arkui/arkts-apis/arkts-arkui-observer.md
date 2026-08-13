# @ohos.arkui.observer

UIObserver提供了UI组件行为变化的无感监听能力，支持监听Navigation页面状态变化（NavDestination）、滚动事件、路由页面状态、屏幕像素密度变化、绘制指令下发、布局完成、页面切换等多种UI组件行为。 开发者可以通过该模块实现对UI组件状态的实时感知和追踪，适用于需要监控页面生命周期、处理滚动事件、优化渲染性能等场景，帮助开发者更好地理解和管理UI组件的行为变化。无感监听是指在组件状态变化时， 系统自动触发回调函数通知开发者，无需开发者手动轮询或主动查询组件状态。监听器通过注册回调函数实现，当目标组件状态改变时，系统内部的事件分发机制会调用已注册的回调函数，携带状态变化信息。 > **说明：** > - 以下API需先使用UIContext中的[getUIObserver](arkts-arkui-arkui-uicontext-uicontext-c.md#getUIObserver)方法获取到UIObserver对象，再通过该对象调用对应方法。 > - UIObserver仅能监听到本进程内的UI组件状态变化信息， > - 不支持获取&lt;!--Del--&gt;UIExtensionComponent等&lt;!--DelEnd--&gt;跨进程场景的信息。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [off_densityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md#off_densityUpdate) |
| [off_didLayout](arkts-arkui-uiobserver-offdidlayout-f.md#off_didLayout) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#off_navDestinationSwitch) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#off_navDestinationSwitch) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#off_navDestinationUpdate) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#off_navDestinationUpdate) |
| [off_routerPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md#off_routerPageUpdate) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#off_scrollEvent) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#off_scrollEvent) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#off_tabContentUpdate) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#off_tabContentUpdate) |
| [off_willDraw](arkts-arkui-uiobserver-offwilldraw-f.md#off_willDraw) |
| [on_densityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md#on_densityUpdate) |
| [on_didLayout](arkts-arkui-uiobserver-ondidlayout-f.md#on_didLayout) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#on_navDestinationSwitch) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#on_navDestinationSwitch) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#on_navDestinationUpdate) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#on_navDestinationUpdate) |
| [on_routerPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md#on_routerPageUpdate) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#on_scrollEvent) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#on_scrollEvent) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#on_tabContentUpdate) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#on_tabContentUpdate) |
| [on_willDraw](arkts-arkui-uiobserver-onwilldraw-f.md#on_willDraw) |

### 类

| 名称 |
| --- |
| [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) |
| [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md) |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-c.md) |

### 接口

| 名称 |
| --- |
| [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md) |
| [NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md) |
| [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) |
| [NavigationInfo](arkts-arkui-uiobserver-navigationinfo-i.md) |
| [ObserverOptions](arkts-arkui-uiobserver-observeroptions-i.md) |
| [ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md) |
| [TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md) |
| [TextChangeEventInfo](arkts-arkui-uiobserver-textchangeeventinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
