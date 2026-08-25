# unbind

## 导入模块

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## unbind

```TypeScript
function unbind(floatViewController: FloatViewController,
    floatingBallController: floatingBall.FloatingBallController): Promise<void>
```

解绑标准悬浮窗和闪控球。需要在[标准悬浮窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md)和 [闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md)均停止后才可解绑。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | 是 |
| floatingBallController | floatingBall.FloatingBallController | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |
