# unbind

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## unbind

```TypeScript
function unbind(floatViewController: FloatViewController,
    floatingBallController: floatingBall.FloatingBallController): Promise<void>
```

Unbinds the float view and floating ball. The unbinding can be performed only after both the  
[float view controller](arkts-arkui-floatview-floatviewcontroller-i.md) and  
[floating ball controller](arkts-arkui-floatingball-floatingballcontroller-i.md) are stopped. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function unbind(floatViewController: FloatViewController,    floatingBallController: floatingBall.FloatingBallController): Promise<void>--><!--Device-floatView-function unbind(floatViewController: FloatViewController,    floatingBallController: floatingBall.FloatingBallController): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | Yes |
| floatingBallController | floatingBall.FloatingBallController | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
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
  public unbindController(): void {
    try {
      // Use the float view controller and floating ball controller passed during the binding.
      if (this.floatViewController && this.floatingBallController) {
        // Unbind the float view and the floating ball.
        floatView.unbind(this.floatViewController!, this.floatingBallController!).then(() => {
          console.info('Succeeded in unbinding float view and floating ball.');
        }).catch((err: BusinessError): void => {
          console.error(`Failed to unbind float view and floating ball. Cause:${err.code}, message:${err.message}`);
        });
      }
    } catch (e) {
      console.error(`Failed to unbind float view and floating ball. Cause:${e.code}, message:${e.message}`);
    }
  }
}
```
