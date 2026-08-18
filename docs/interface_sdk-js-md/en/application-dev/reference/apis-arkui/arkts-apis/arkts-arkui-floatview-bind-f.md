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

Binds the float view and floating ball. You need to create the [float view controller](arkts-arkui-floatview-floatviewcontroller-i.md#floatviewcontroller) and [floating ball controller](arkts-arkui-floatingball-floatingballcontroller-i.md#floatingballcontroller) first, and neither of them has been started. This API uses a promise to return the result. > **NOTE：**> > - After the binding is successful, calling [start()](arkts-arkui-floatview-floatviewcontroller-i.md#start) or > [startFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#startfloatingball) will > create both a float view and the floating ball window, and trigger the status callback registered for the > corresponding window. However, only one window is displayed at a time, and the display sequence depends on which > controller's start API is called first. > > - After the binding is successful, users can switch between the float view and the floating ball window by > clicking. > > - After the binding is successful, calling the stop API ([stop()](arkts-arkui-floatview-floatviewcontroller-i.md#stop) or > [stopFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#stopfloatingball)) of > either controller will destroy both the float view and the floating ball window, and trigger the status callback > registered for the corresponding window.

**Since:** 26.0.0

**Required permissions:** ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>--><!--Device-floatView-function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController,    floatingBallParams: floatingBall.FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| floatViewController | [FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md) | Yes | Float view controller. |
| floatingBallController | floatingBall.FloatingBallController | Yes | Floating ball controller. |
| floatingBallParams | floatingBall.FloatingBallParams | Yes | Floating ball parameters. The parameters set during binding will overwrite the parameters saved when the floating ball controller is started. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) | Wrong parameters for operating the floating ball. Possible cause: Invalid floating ball params. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported on this device. Possible cause: Call api on unsupported device. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. Possible cause: The application does not have the permission required to call the API. |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) | The floating ball state does not support this operation. Possible cause: 1. The floating ball has started but not stopped yet. 2. The floating ball controller has been bound. |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) | The floatView state does not support this operation. Possible cause: 1. The float view has started but not stopped yet. 2. The float view controller has been bound. |

