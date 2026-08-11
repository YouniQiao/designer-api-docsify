# @ohos.arkui.observer

UIObserver提供了UI组件行为变化的无感监听能力，支持监听Navigation页面状态变化（NavDestination）、滚动事件、路由页面状态、屏幕像素密度变化、绘制指令下发、布局完成、页面切换等多种UI组件行为。开发者可以通过该模块实现对UI组件状态的实时感知和追踪，适用于需要监控页面生命周期、处理滚动事件、优化渲染性能等场景，帮助开发者更好地理解和管理UI组件的行为变化。无感监听是指在组件状态变化时，系统自动触发回调函数通知开发者，无需开发者手动轮询或主动查询组件状态。监听器通过注册回调函数实现，当目标组件状态改变时，系统内部的事件分发机制会调用已注册的回调函数，携带状态变化信息。

> **说明：**

> - 以下API需先使用UIContext中的{@link getUIObserver()}方法获取到UIObserver对象，再通过该对象调用对应方法。

> - UIObserver仅能监听到本进程内的UI组件状态变化信息，
> - 不支持获取&lt;!--Del--&gt;[UIExtensionComponent](ui_extension_component)等&lt;!--DelEnd--&gt;跨进程场景的信息。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 汇总

### 函数

| 名称 |
| --- |
| [off](arkts-arkui-uiobserver-off-f.md#off) |
| [off](arkts-arkui-uiobserver-off-f.md#off-1) |
| [off](arkts-arkui-uiobserver-off-f.md#off-2) |
| [off](arkts-arkui-uiobserver-off-f.md#off-3) |
| [off](arkts-arkui-uiobserver-off-f.md#off-4) |
| [off](arkts-arkui-uiobserver-off-f.md#off-5) |
| [off](arkts-arkui-uiobserver-off-f.md#off-6) |
| [off](arkts-arkui-uiobserver-off-f.md#off-7) |
| [off](arkts-arkui-uiobserver-off-f.md#off-8) |
| [off](arkts-arkui-uiobserver-off-f.md#off-9) |
| [off](arkts-arkui-uiobserver-off-f.md#off-10) |
| [off](arkts-arkui-uiobserver-off-f.md#off-11) | 取消监听Navigation的页面切换事件。与[uiObserver.off](uiObserver.off( type: 'navDestinationSwitch', context:UIAbilityContext \|
| [on](arkts-arkui-uiobserver-on-f.md#on) |
| [on](arkts-arkui-uiobserver-on-f.md#on-1) |
| [on](arkts-arkui-uiobserver-on-f.md#on-2) |
| [on](arkts-arkui-uiobserver-on-f.md#on-3) |
| [on](arkts-arkui-uiobserver-on-f.md#on-4) |
| [on](arkts-arkui-uiobserver-on-f.md#on-5) |
| [on](arkts-arkui-uiobserver-on-f.md#on-6) |
| [on](arkts-arkui-uiobserver-on-f.md#on-7) |
| [on](arkts-arkui-uiobserver-on-f.md#on-8) |
| [on](arkts-arkui-uiobserver-on-f.md#on-9) |
| [on](arkts-arkui-uiobserver-on-f.md#on-10) |
| [on](arkts-arkui-uiobserver-on-f.md#on-11) | 监听Navigation的页面切换事件。与[uiObserver.on](uiObserver.on( type: 'navDestinationSwitch', context: UIAbilityContext \|

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
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) | routerPage生命周期触发时对应的状态。RouterPageState用于[RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md)中，作为  [routerPageUpdate](uiObserver.on(type: 'routerPageUpdate', context: UIAbilityContext \|
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
