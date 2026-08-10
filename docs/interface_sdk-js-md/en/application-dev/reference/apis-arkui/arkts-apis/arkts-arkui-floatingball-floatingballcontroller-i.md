# FloatingBallController

闪控球控制器实例，用于启动、更新、停止闪控球以及注册回调等操作。

下列API示例中都需先使用[floatingBall.create()](arkts-arkui-floatingball-create-f.md#create)方法获取到闪控球控制器实例（即floatingBallController），再通过此实例调用对应方法。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-floatingBall-interface FloatingBallController--><!--Device-floatingBall-interface FloatingBallController-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## getFloatingBallWindowInfo

```TypeScript
getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>
```

获得闪控球窗口信息，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>--><!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FloatingBallWindowInfo&gt; | Promise对象，返回闪控球窗口信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300002 | This window state is abnormal. Possible cause: Internal error, the window type is not a floating ball. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300004 | Unauthorized operation. Possible cause: The process ID calling the API does not match the process ID of the session that created the floating ball. |
| 1300025 | The floating ball state does not support this operation. Possible cause: The floating ball is not started. |
| 1300024 | The floating ball window state is abnormal. Possible causes: &lt;br&gt;1. The floating ball controller has been destroyed. &lt;br&gt;2. The floating ball window is not created or has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the window information of the floating ball.
floatingBallController.getFloatingBallWindowInfo().then((data: floatingBall.FloatingBallWindowInfo) => {
  console.info('Succeeded in getting floating ball window info. Info: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to get floating ball window info. Cause code: ${err.code}, message: ${err.message}`);
});
```

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<FloatingBallState>): void
```

取消闪控球生命周期状态变化的监听事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | 监听事件，固定为'stateChange'，即闪控球生命周期状态变化事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | No | 回调函数。返回当前的闪控球生命周期状态。若传入参数，则停止该监听。若未传入参数，则停止所有闪控球生命周期状态变化的监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the callback function for status changes (the callback function must be the same as that registered).
let onStateChange = (state: floatingBall.FloatingBallState) => {
  console.info('Floating ball stateChange: ' + state);
};
try {
  // Unregister the callback for listening to floating ball state changes.
  floatingBallController.off('stateChange', onStateChange);
} catch (e) {
  console.error(`Failed to off stateChange floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## off('click')

```TypeScript
off(type: 'click', callback?: Callback<void>): void
```

取消闪控球点击的监听事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void--><!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'click' | Yes | 监听事件，固定为'click'，即闪控球点击事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 回调函数。当点击闪控球事件发生时的回调。该回调函数不返回任何参数。若传入参数，则关闭特定的监听。若未传入参数，则关闭所有闪控球点击的监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the callback function for the click event (the callback function must be the same as that registered).
let onClick = () => {
  console.info('Floating ball onClick');
};
try {
  // Unregister the callback for listening to click events of the floating ball.
  floatingBallController.off('click', onClick);
} catch (e) {
  console.error(`Failed to off click floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## offClick

```TypeScript
offClick(callback?: Callback<void>): void
```

Unregister floating ball click event listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FloatingBallController-offClick(callback?: Callback<void>): void--><!--Device-FloatingBallController-offClick(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Indicates the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## offDestroy

```TypeScript
offDestroy(callback?: Callback<string>): void
```

取消闪控球销毁事件的监听。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void--><!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 回调函数。若传入参数，则取消该监听；若未传入参数，则取消所有闪控球销毁事件的监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible cause: Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the callback function for the destruction event (the callback function must be the same as that registered).
let onDestroy = (reason: string) => {
  console.info('Floating ball has destroyed, reason: ' + reason);
};
try {
  // Unregister the callback for listening to floating ball destruction events.
  floatingBallController?.offDestroy(onDestroy);
} catch (e) {
  console.error(`Failed to offDestroy floating ball. Cause:${e.code}, message:${e.message}`);
}
// Unregister all callbacks.
try {
  floatingBallController?.offDestroy();
} catch (e) {
  console.error(`Failed to offDestroy all listeners. Cause:${e.code}, message:${e.message}`);
}
```

## offStateChange

```TypeScript
offStateChange(callback?: Callback<FloatingBallState>): void
```

Unregister floating ball stateChange event listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FloatingBallController-offStateChange(callback?: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-offStateChange(callback?: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | No | Indicates the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<FloatingBallState>): void
```

注册闪控球生命周期状态变化的监听事件。不再使用时，取消监听以避免内存泄漏。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | 监听事件，固定为'stateChange'，即闪控球生命周期状态变化事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | Yes | 回调函数。返回当前的闪控球生命周期状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the callback function for status changes.
let onStateChange = (state: floatingBall.FloatingBallState) => {
  console.info('Floating ball stateChange: ' + state);
};
try {
  // Register the callback for listening to floating ball state changes.
  floatingBallController.on('stateChange', onStateChange);
} catch (e) {
  console.error(`Failed to on stateChange floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## on('click')

```TypeScript
on(type: 'click', callback: Callback<void>): void
```

注册闪控球的点击监听事件，不使用时，取消监听以避免内存泄漏。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void--><!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'click' | Yes | 监听事件，固定为'click'，即闪控球点击事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。当点击闪控球事件发生时的回调。该回调函数不返回任何参数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the click event callback function.
let onClick = () => {
  console.info('Floating ball onClick');
};
try {
  // Register the callback for listening to click events of the floating ball.
  floatingBallController.on('click', onClick);
} catch (e) {
  console.error(`Failed to on click floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## onClick

```TypeScript
onClick(callback: Callback<void>): void
```

Register floating ball click event listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FloatingBallController-onClick(callback: Callback<void>): void--><!--Device-FloatingBallController-onClick(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Used to handle {'click'} command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## onDestroy

```TypeScript
onDestroy(callback: Callback<string>): void
```

注册闪控球销毁事件的监听。当闪控球销毁时，回调函数会接收到销毁原因的字符串。不再使用时，调用[offDestroy](#offdestroy)接口取消监听以避免内存泄漏。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void--><!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 回调函数。返回闪控球停止的原因。停止原因包括： &lt;br&gt;- "APP_STOP"：应用主动停止。 &lt;br&gt;- "DUMPSTER_STOP"：拖动到垃圾桶触发停止。 &lt;br&gt;- "LONG_PRESS_SINGLE_STOP"：长按单个闪控球触发停止。 &lt;br&gt;- "LONG_PRESS_ALL_STOP"：长按全部闪控球触发停止。 &lt;br&gt;- "MAIN_WINDOW_DESTROY_STOP"：context关联的主窗口被销毁后触发停止。 &lt;br&gt;- "SQUEEZE"：超出设备闪控球数量上限，被其他闪控球挤占停止。 &lt;br&gt;- "FLOAT_VIEW_STOP"：与标准悬浮窗绑定后，绑定状态下跟随标准悬浮窗停止。 &lt;br&gt;- "STOP_IN_SIDEBAR"：在侧边栏中被停止。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible cause: Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## Examples

```TypeScript
// Define the callback function for the destruction event.
let onDestroy = (reason: string) => {
  console.info('Floating ball has destroyed, reason: ' + reason);
};
try {
  // Register the callback for listening to floating ball destruction events.
  floatingBallController?.onDestroy(onDestroy);
} catch (e) {
  console.error(`Failed to onDestroy floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## onStateChange

```TypeScript
onStateChange(callback: Callback<FloatingBallState>): void
```

Register floating ball stateChange event listener.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-FloatingBallController-onStateChange(callback: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-onStateChange(callback: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | Yes | Used to handle {'stateChange'} command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified. &lt;br&gt;2.Callback is null or not callable. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball controller has been destroyed. |

## restoreMainWindow

```TypeScript
restoreMainWindow(want: Want): Promise<void>
```

恢复应用主窗口并加载指定页面。使用Promise异步回调。仅支持在点击闪控球后调用；若应用拥有`ohos.permission.AUTO_RESTORE_MAIN_WINDOW`权限，可以无需点击直接调用该接口。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>--><!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 加载指定页面的Want。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300019 | Wrong parameters for operating the floating ball. Possible cause: Want parameter is null or invalid. |
| 1300002 | This window state is abnormal. Possible cause: Internal error, the window type is not a floating ball. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300004 | Unauthorized operation. Possible cause: The process ID calling the API does not match the process ID of the session that created the floating ball. |
| 201 | Permission verification failed, usually returned by VerifyAccessToken. |
| 1300026 | Failed to restore the main window. Possible causes: 1. Invalid parameter. The provided bundleName does not match the caller's application bundleName. 2. The application lacks the ohos.permission.AUTO_RESTORE_MAIN_WINDOW permission, and no user interaction (click) on the floating ball has occurred. |
| 1300025 | The floating ball state does not support this operation. Possible cause: The floating ball is not started. |
| 1300024 | The floating ball window state is abnormal. Possible causes: &lt;br&gt;1.The floating ball controller has been destroyed. &lt;br&gt;2.The floating ball window is not created or has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

// Set the Want parameter of the main window to be restored.
let want: Want = {
  bundleName: 'xxx.xxx.xxx',
  abilityName: 'EntryAbility'
};
try {
  // Restore the main window of the application and load the specified page.
  floatingBallController.restoreMainWindow(want).then(() => {
    console.info('Succeeded in restoring floating ball main window.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to restore floating ball main window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  console.error(`Failed to restore floating ball main window. Cause:${e.code}, message:${e.message}`);
}
```

## setFloatingBallVisibilityInApp

```TypeScript
setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>
```

设置闪控球在应用内是否可见。使用Promise异步回调。

- 当应用处于多任务界面时（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为PAUSED），闪控球不可见。  
- 默认情况（即未调用此接口设置时）和调用此接口传入true时：除多任务界面外，闪控球均可见。  
- 调用此接口传入false时：当应用处于前台（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为SHOWN或者RESUMED）时，闪控球不可见；当应用处于  
 后台（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为HIDDEN）时，闪控球可见。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>--><!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVisible | boolean | Yes | true表示闪控球在应用内可见；false表示闪控球在应用内不可见。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300023 | Floating ball internal error. Possible cause: The floating ball controller is null. |
| 1300024 | The floating ball window state is abnormal. Possible causes: The floating ball window has not been created or has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Set the floating ball to be invisible in the application.
floatingBallController?.setFloatingBallVisibilityInApp(false).then(() => {
  console.info('Succeeded in setting floating ball visibility.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set floating ball visibility. Cause code: ${err.code}, message: ${err.message}`);
});
```

## startFloatingBall

```TypeScript
startFloatingBall(params: FloatingBallParams): Promise<void>
```

启动闪控球，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | Yes | 启动闪控球的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1. FloatingBallParams parameter is null. &lt;br&gt;2. Parameter is invalid, such as invalid icon object, template type, or title (empty or exceeds 64 bytes). |
| 1300034 | This operation conflicts with other floating windows. Possible cause: App has already started float view.<br>**Applicable version:** 26.0.0 and later |
| 1300023 | Floating ball internal error. Possible causes: &lt;br&gt;1.The floating ball controller has been destroyed. &lt;br&gt;2.Internal error, failed to show the floating ball window. Such as insufficient resources or abnormal window service. |
| 1300022 | Repeated floating ball operation. |
| 1300021 | Failed to start multiple floating ball windows. |
| 1300020 | Failed to create the floating ball window. Possible cause: The main window is not shown. |
| 201 | Permission verification failed, usually returned by VerifyAccessToken. |
| 1300025 | The floating ball state does not support this operation. Possible cause: The floating ball state is stopping. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball window is not created or has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Set the parameters for starting the floating ball.
let startParams: floatingBall.FloatingBallParams = {
  template: floatingBall.FloatingBallTemplate.EMPHATIC,
  title: 'title',
  content: 'content'
};
try {
  // Start the floating ball.
  floatingBallController.startFloatingBall(startParams).then(() => {
    console.info('Succeeded in starting floating ball.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start floating ball. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to start floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## stopFloatingBall

```TypeScript
stopFloatingBall(): Promise<void>
```

停止闪控球，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallController-stopFloatingBall(): Promise<void>--><!--Device-FloatingBallController-stopFloatingBall(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300022 | Repeated floating ball operation. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball window is not created or has been destroyed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Stop the floating ball.
floatingBallController.stopFloatingBall().then(() => {
  console.info('Succeeded in stopping floating ball.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop floating ball. Cause:${err.code}, message:${err.message}`);
});
```

## updateFloatingBall

```TypeScript
updateFloatingBall(params: FloatingBallParams): Promise<void>
```

更新闪控球，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | Yes | 更新闪控球的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. Possible cause: Internal IPC error. |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.FloatingBallParams parameter is null. &lt;br&gt;2.Parameter is invalid, such as invalid icon object, template type, or title (empty or exceeds 64 bytes). |
| 1300002 | This window state is abnormal. Possible cause: Internal error, the window type is not a floating ball. |
| 1300023 | Floating ball internal error. Possible cause: System error, such as a null pointer, insufficient memory. |
| 1300004 | Unauthorized operation. Possible cause: The process ID calling the API does not match the process ID of the session that created the floating ball. |
| 1300027 | When updating the floating ball, the template type cannot be changed. |
| 1300025 | The floating ball state does not support this operation. Possible cause: The floating ball is not started. |
| 1300024 | The floating ball window state is abnormal. Possible cause: The floating ball window is not created or has been destroyed. |
| 1300028 | Updating static template-based floating balls is not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Set the parameters for updating the floating ball.
let updateParams: floatingBall.FloatingBallParams = {
  template: floatingBall.FloatingBallTemplate.EMPHATIC,
  title: 'title2',
  content: 'content2'
};
try {
  // Update the floating ball.
  floatingBallController.updateFloatingBall(updateParams).then(() => {
    console.info('Succeeded in updating floating ball.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update floating ball. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to update floating ball. Cause:${e.code}, message:${e.message}`);
}
```

