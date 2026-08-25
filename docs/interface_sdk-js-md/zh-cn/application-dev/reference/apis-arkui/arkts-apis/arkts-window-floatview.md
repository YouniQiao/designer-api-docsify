# @ohos.window.floatView

标准悬浮窗是悬浮在桌面/应用界面上的小型窗口，提供灵活的窗口管理能力。本模块提供标准悬浮窗能力，包括判断设备是否支持标准悬浮窗功能、创建标准悬浮窗控制器以启动、更新或停止标准悬浮窗等。  
**适用场景：**标准悬浮窗适用于需要在独立小窗口中持续展示应用内容或提供快捷操作的场景。例如：  
- 股市盯盘应用：用户在浏览其他应用时，通过标准悬浮窗实时查看股票行情变化，无需频繁切换应用。  
- 手机直播应用：主播在直播过程中使用标准悬浮窗展示自定义的互动面板或控制界面，方便实时操作和互动。  
**与闪控球联动：**本模块可与[@ohos.window.floatingBall](arkts-window-floatingball.md)（闪控球）联合使用。通过 [floatView.bind](arkts-arkui-floatview-bind-f.md)接口将标准悬浮窗控制器与闪控球控制器绑定后，用户点击闪控球可展开为标准悬浮窗，点击标准悬浮窗左上角的缩小按钮可收起为闪控球，实现两种窗口形态的相互切换。  
**全局悬浮窗和标准悬浮窗对比**  
- 共同点：全局悬浮窗和标准悬浮窗均为一种特殊的应用辅助窗口，具备在应用主窗口和对应Ability退至后台后仍然可以在前台显示的能力。可以用于应用退至后台后，使用其继续显示UI。  
- 区别：  
- 全局悬浮窗由开发者管理并实现UI绘制，无统一UI及动效。  
- 标准悬浮窗由系统管理并统一绘制UI，动效更为高端精致。  
- 标准悬浮窗支持与[闪控球](arkts-window-floatingball.md)互相绑定联合使用，实现更复杂场景。  
**起始版本：** 26.0.0

> **说明：**&gt;
> - 针对系统能力SystemCapability.Window.SessionManager，请先使用
> [canIUse()](../../../reference/common/js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。&gt;
> - 本模块接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [bind](arkts-arkui-floatview-bind-f.md) |
| [create](arkts-arkui-floatview-create-f.md) |
| [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) |
| [isFloatViewEnabled](arkts-arkui-floatview-isfloatviewenabled-f.md) |
| [unbind](arkts-arkui-floatview-unbind-f.md) |

### 接口

| 名称 |
| --- |
| [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) |
| [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) |
| [FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md) |
| [FloatViewProperties](arkts-arkui-floatview-floatviewproperties-i.md) |
| [FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md) |
| [FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md) |
| [RatioLimit](arkts-arkui-floatview-ratiolimit-i.md) |
| [TemplateProperty](arkts-arkui-floatview-templateproperty-i.md) |

### 枚举

| 名称 |
| --- |
| [FloatViewState](arkts-arkui-floatview-floatviewstate-e.md) |
| [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md) |
