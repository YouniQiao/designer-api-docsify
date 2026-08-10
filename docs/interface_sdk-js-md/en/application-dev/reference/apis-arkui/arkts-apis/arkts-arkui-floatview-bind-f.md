# bind

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## bind

```TypeScript
function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,
    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>
```

绑定标准悬浮窗和闪控球。需要先创建[标准悬浮窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md)和  
[闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md)，且均未启动。使用Promise异步回调。

> **说明：**
> 
> - 绑定成功后，调用[start()](arkts-arkui-floatview-floatviewcontroller-i.md#start)或
> [startFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#startfloatingball)均会同时创
> 建标准悬浮窗窗口和闪控球窗口，并触发对应窗口已注册的状态回调。但同一时刻仅展示其中一个窗口，展示顺序取决于先调用哪个控制器的启动接口。
> 
> - 绑定成功后，用户可通过点击操作在标准悬浮窗窗口与闪控球之间进行切换。
> 
> - 绑定成功后，调用任一控制器的停止接口（[stop()](arkts-arkui-floatview-floatviewcontroller-i.md#stop)或
> [stopFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#stopfloatingball)）会同时销毁标
> 准悬浮窗窗口和闪控球窗口，并触发对应窗口已注册的状态回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>--><!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | Yes | 标准悬浮窗控制器。 |
| floatingBallController | floatingBall.FloatingBallController | Yes | 闪控球控制器。 |
| floatingBallParams | floatingBall.FloatingBallParams | Yes | 闪控球参数。绑定时设置的参数会覆盖掉闪控球控制器启动时已保存的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible cause: Invalid floating ball params. |
| 801 | Capability not supported on this device. Possible cause: Call api on unsupported device. |
| 201 | Permission verification failed. Possible cause: The application does not have the permission required to call the API. |
| 1300025 | The floating ball state does not support this operation. Possible cause: 1. The floating ball has started but not stopped yet. 2. The floating ball controller has been bound. |
| 1300031 | The floatView state does not support this operation. Possible cause: 1. The float view has started but not stopped yet. 2. The float view controller has been bound. |

## Examples

```TypeScript
// Entry.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { floatingBall, floatView } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
  private floatViewController: floatView.FloatViewController | undefined = undefined;
  // Create a controller.
  // ...
  public bindController(): void {
    let floatingBallParams: floatingBall.FloatingBallParams = {
      template: floatingBall.FloatingBallTemplate.EMPHATIC,
      title: 'title',
      content: 'content'
    };

    try {
      if (this.floatViewController && this.floatingBallController) {
        // Bind the float view and the floating ball.
        floatView.bind(this.floatViewController!, this.floatingBallController!, floatingBallParams).then(() => {
          console.info('Succeeded in binding float view and floating ball.');
        }).catch((err: BusinessError): void => {
          console.error(`Failed to bind float view and floating ball. Cause:${err.code}, message:${err.message}`);
        });
      }
    } catch (e) {
      console.error(`Failed to bind float view and floating ball. Cause:${e.code}, message:${e.message}`);
    }
  }
}
```

