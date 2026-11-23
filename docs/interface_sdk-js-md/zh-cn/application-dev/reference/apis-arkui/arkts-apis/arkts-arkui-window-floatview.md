# @ohos.window.floatView

闪控窗是悬浮在桌面/应用界面上的小型窗口，提供灵活的窗口管理能力。

本模块提供闪控窗能力，包括判断设备是否支持闪控窗功能、创建闪控窗控制器以启动、更新或停止闪控窗等。

**适用场景：**

闪控窗适用于需要在独立小窗口中持续展示应用内容或提供快捷操作的场景。例如：

- 股市盯盘应用：用户在浏览其他应用时，通过闪控窗实时查看股票行情变化，无需频繁切换应用。  
- 手机直播应用：主播在直播过程中使用闪控窗展示自定义的互动面板或控制界面，方便实时操作和互动。

**相关比对**：[闪控球和闪控窗的对比](../../../windowmanager/window-type-overview.md#闪控球和闪控窗的对比)、[全局悬浮窗和闪控窗的对比](../../../windowmanager/window-type-overview.md#全局悬浮窗和闪控窗的对比)

> **说明：** 
> 
> - 针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](../../../reference/common/js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。
> 
> - 本模块接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace floatView--><!--Device-unnamed-declare namespace floatView-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [bind](arkts-arkui-floatview-bind-f.md#bind-1) | 绑定闪控窗和闪控球。需要先创建[闪控窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md)和[闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md)，且均未启动。使用Promise异步回调。 |
| [create](arkts-arkui-floatview-create-f.md#create-1) | 创建闪控窗控制器。使用Promise异步回调。 |
| [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md#getfloatviewlimits-1) | 根据传入的模板类型获取对应闪控窗窗口的限制，单位为px。 |
| [isFloatViewEnabled](arkts-arkui-floatview-isfloatviewenabled-f.md#isfloatviewenabled-1) | 判断当前设备是否支持闪控窗功能。 |
| [unbind](arkts-arkui-floatview-unbind-f.md#unbind-1) | 解绑闪控窗和闪控球。需要在[闪控窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md)和[闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md)均停止后才可解绑。使用Promise异步回调。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) | 创建闪控窗控制器时需要提供的参数配置。 |
| [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | 闪控窗控制器实例。用于启动、停止闪控窗以及注册回调等操作。 |
| [FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md) | 闪控窗窗口的限制。 |
| [FloatViewProperties](arkts-arkui-floatview-floatviewproperties-i.md) | 闪控窗窗口的属性。 |
| [FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md) | 闪控窗矩形区域变化信息。 |
| [FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md) | 闪控窗状态变化信息。 |
| [RatioLimit](arkts-arkui-floatview-ratiolimit-i.md) | 闪控窗的宽高比限制范围。宽高比比值由窗口矩形区域的宽除以高获得。 |
| [TemplateProperty](arkts-arkui-floatview-templateproperty-i.md) | 切换闪控窗模板并修改窗口尺寸时需要提供的参数配置。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [FloatViewState](arkts-arkui-floatview-floatviewstate-e.md) | 闪控窗状态的枚举。 |
| [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md) | 闪控窗模板类型的枚举。 |
