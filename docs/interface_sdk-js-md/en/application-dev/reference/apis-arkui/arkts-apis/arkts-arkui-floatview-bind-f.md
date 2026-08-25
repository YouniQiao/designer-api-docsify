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

Binds the float view and floating ball. You need to create the [float view controller](arkts-arkui-floatview-floatviewcontroller-i.md) and [floating ball controller](arkts-arkui-floatingball-floatingballcontroller-i.md) first, and neither of them has been started. This API uses a promise to return the result.

> **NOTE：**&gt;
> - After the binding is successful, calling [start()](arkts-arkui-floatview-floatviewcontroller-i.md#start) or
> [startFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#startfloatingball) will
> create both a float view and the floating ball window, and trigger the status callback registered for the
> corresponding window. However, only one window is displayed at a time, and the display sequence depends on which
> controller's start API is called first.&gt;
> - After the binding is successful, users can switch between the float view and the floating ball window by
> clicking.&gt;
> - After the binding is successful, calling the stop API ([stop()](arkts-arkui-floatview-floatviewcontroller-i.md#stop) or
> [stopFloatingBall()](arkts-arkui-floatingball-floatingballcontroller-i.md#stopfloatingball)) of
> either controller will destroy both the float view and the floating ball window, and trigger the status callback
> registered for the corresponding window.

**Since:** 26.0.0

**Required permissions:** ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |
