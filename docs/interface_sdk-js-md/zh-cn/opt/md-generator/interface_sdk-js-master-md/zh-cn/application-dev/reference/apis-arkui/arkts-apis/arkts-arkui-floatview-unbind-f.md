# unbind

## unbind

```TypeScript
function unbind(floatViewController: FloatViewController,
    floatingBallController: floatingBall.FloatingBallController): Promise<void>
```

解绑标准悬浮窗和闪控球。需要在[标准悬浮窗控制器](arkts-arkui-floatview-floatviewcontroller-i.md#FloatViewController)和 [闪控球控制器](arkts-arkui-floatingball-floatingballcontroller-i.md#FloatingBallController)均停止后才可解绑。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-floatView-function unbind(floatViewController: FloatViewController,    floatingBallController: floatingBall.FloatingBallController): Promise<void>--><!--Device-floatView-function unbind(floatViewController: FloatViewController,    floatingBallController: floatingBall.FloatingBallController): Promise<void>-End-->

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

## 示例

```TypeScript
// Entry.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { floatingBall, floatView } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
  private floatViewController: floatView.FloatViewController | undefined = undefined;
  // 创建控制器
  // ...
  public unbindController(): void {
    try {
      // 使用绑定时传入的闪控窗和闪控球控制器
      if (this.floatViewController && this.floatingBallController) {
        // 解绑闪控窗和闪控球
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
