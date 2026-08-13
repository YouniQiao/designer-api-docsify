# bind

## Modules to Import

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## bind

```TypeScript
function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,
    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>
```

Binds the float view and floating ball. You need to create the [float view controller](arkts-arkui-floatview-floatviewcontroller-i.md#FloatViewController) and [floating ball controller](arkts-arkui-floatingball-floatingballcontroller-i.md#FloatingBallController) first, and neither of them has been started. This API uses a promise to return the result. > **NOTE：**> > - After the binding is successful, calling [start()](arkts-arkui-floatview-floatviewcontroller-i.md#start) or > [startFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#startFloatingBall) will > create both a float view and the floating ball window, and trigger the status callback registered for the > corresponding window. However, only one window is displayed at a time, and the display sequence depends on which > controller's start API is called first. > > - After the binding is successful, users can switch between the float view and the floating ball window by > clicking. > > - After the binding is successful, calling the stop API ([stop()](arkts-arkui-floatview-floatviewcontroller-i.md#stop) or > [stopFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#stopFloatingBall)) of > either controller will destroy both the float view and the floating ball window, and trigger the status callback > registered for the corresponding window.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>--><!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | Yes |
| floatingBallController | floatingBall.FloatingBallController | Yes |
| floatingBallParams | floatingBall.FloatingBallParams | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |

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
