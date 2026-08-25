# @ohos.window.floatingBall

该模块提供闪控球的基础功能，包括判断设备是否支持闪控球功能，以及创建闪控球控制器来启动、更新或停止闪控球。适用于跨应用的题目搜索、账单记录、商品比价、抢单、翻译场景，以及金融类应用的实时盯盘场景，以小窗模式呈现内容。闪控球以悬浮小组件 形式显示在其他应用之上，即时呈现应用的关键信息。

> **说明：**&gt;
> - 针对系统能力SystemCapability.Window.SessionManager，请先使用
> [canIUse()](arkts-arkui-global-caniuse-f.md)接口判断当前设备是否支持此syscap及对应接口。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create](arkts-arkui-floatingball-create-f.md) |
| [isFloatingBallEnabled](arkts-arkui-floatingball-isfloatingballenabled-f.md) |

### 接口

| 名称 |
| --- |
| [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) |
| [FloatingBallController](arkts-arkui-floatingball-floatingballcontroller-i.md) |
| [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) |
| [FloatingBallWindowInfo](arkts-arkui-floatingball-floatingballwindowinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [FloatingBallState](arkts-arkui-floatingball-floatingballstate-e.md) |
| [FloatingBallTemplate](arkts-arkui-floatingball-floatingballtemplate-e.md) |
| [FloatingBallTextUpdateAnimationType](arkts-arkui-floatingball-floatingballtextupdateanimationtype-e.md) |
