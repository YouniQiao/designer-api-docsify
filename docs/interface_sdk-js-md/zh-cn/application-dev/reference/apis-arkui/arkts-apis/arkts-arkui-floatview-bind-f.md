# bind

## 导入模块

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## bind

```TypeScript
function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,
    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>
```

绑定标准悬浮窗和闪控球。需要先创建[标准悬浮窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md)和 [闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md)，且均未启动。使用Promise异步回调。

> **说明：**&gt;
> - 绑定成功后，调用[start()](arkts-arkui-floatview-floatviewcontroller-i.md#start)或
> [startFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#startfloatingball)均会同时创
> 建标准悬浮窗窗口和闪控球窗口，并触发对应窗口已注册的状态回调。但同一时刻仅展示其中一个窗口，展示顺序取决于先调用哪个控制器的启动接口。&gt;
> - 绑定成功后，用户可通过点击操作在标准悬浮窗窗口与闪控球之间进行切换。&gt;
> - 绑定成功后，调用任一控制器的停止接口（[stop()](arkts-arkui-floatview-floatviewcontroller-i.md#stop)或
> [stopFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#stopfloatingball)）会同时销毁标
> 准悬浮窗窗口和闪控球窗口，并触发对应窗口已注册的状态回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | 是 |
| floatingBallController | floatingBall.FloatingBallController | 是 |
| floatingBallParams | floatingBall.FloatingBallParams | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300031](../errorcode-window.md#1300031-闪控窗状态不支持该操作) |

**示例**

```TypeScript
// Entry.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { floatingBall } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
  private floatViewController: floatView.FloatViewController | undefined = undefined;
  // 创建控制器
  // ...
  public bindController(): void {
    let floatingBallParams: floatingBall.FloatingBallParams = {
      template: floatingBall.FloatingBallTemplate.EMPHATIC,
      title: 'title',
      content: 'content'
    };

    try {
      if (this.floatViewController && this.floatingBallController) {
        floatView.bind(this.floatViewController!, this.floatingBallController!, floatingBallParams).then(() => {
          console.info('Succeeded in binding float view and floating ball.');
        }).catch((err: BusinessError): void => {
          console.error(`Failed to bind float view and floating ball. Cause:${err.code}, message:${err.message}`);
        });
      }
    } catch(e) {
      console.error(`Failed to bind float view and floating ball. Cause:${e.code}, message:${e.message}`);
    }
  }
}
```
