# FloatingBallController

Implements a floating ball controller instance, which is used to start, update, and stop floating balls, and register callbacks.

Before calling any of the following APIs, you must use [floatingBall.create()](arkts-arkui-floatingball-create-f.md#create) to create a floating ball controller instance.

**Since:** 20

<!--Device-floatingBall-interface FloatingBallController--><!--Device-floatingBall-interface FloatingBallController-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
```

## getFloatingBallWindowInfo

```TypeScript
getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>
```

Obtains the floating ball window information. This API uses a promise to return the result.

**Since:** 20

<!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>--><!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FloatingBallWindowInfo](arkts-arkui-floatingball-floatingballwindowinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300002-abnormal-window-state) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300004-unauthorized-operation) |
| [1300025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Unregisters the listener for lifecycle state changes of the floating ball.

**Since:** 20

<!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatingBallState](arkts-arkui-floatingball-floatingballstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Unregisters the listener for click events of the floating ball.

**Since:** 20

<!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void--><!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'click' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

## offDestroy

```TypeScript
offDestroy(callback?: Callback<string>): void
```

Unregister floating ball destroy event listener.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void--><!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<FloatingBallState>): void
```

Registers a listener for lifecycle state changes of the floating ball. To prevent memory leaks, remember to unregister the listener when it is no longer needed.

**Since:** 20

<!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatingBallState](arkts-arkui-floatingball-floatingballstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Registers a listener for click events of the floating ball. To prevent memory leaks, remember to unregister the listener when it is no longer needed.

**Since:** 20

<!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void--><!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'click' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

## onDestroy

```TypeScript
onDestroy(callback: Callback<string>): void
```

Register floating ball destroy event listener.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void--><!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

## restoreMainWindow

```TypeScript
restoreMainWindow(want: Want): Promise<void>
```

Restores the main window of the application and loads the specified page. This API uses a promise to return the result. This API can be called only after the floating ball is tapped. If the application has the  
**ohos.permission.AUTO_RESTORE_MAIN_WINDOW** permission, this API can be called directly without tapping the floating ball.

**Since:** 20

**Required permissions:** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>--><!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300002-abnormal-window-state) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300004-unauthorized-operation) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1300026](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300026-failure-in-launch-an-application-window-via-a-floating-ball) |
| [1300025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Sets whether the floating ball is visible in the application. This API uses a promise to return the result.

- When the application is on the recent tasks screen (the  
[lifecycle state](../../../windowmanager/window-overview.md#lifecycle-states) is **PAUSED**), the floating ball is invisible.  
- By default (when this API is not called) or when this API is called with the value **true** passed in, the  
floating ball is visible except on the recent tasks screen.  
- When this API is called with the value **false** passed in, the floating ball is invisible when the application  
is in the foreground (the [lifecycle state](../../../windowmanager/window-overview.md#lifecycle-states) is  
**SHOWN** or **RESUMED**) and is visible when the application is in the background (the  
[lifecycle state](../../../windowmanager/window-overview.md#lifecycle-states) is **HIDDEN**).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>--><!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isVisible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Starts the floating ball. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300034](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300034-operation-of-the-float-view-conflicts-with-those-of-other-floating-windows) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300021-failure-in-starting-multiple-floating-balls) |
| [1300020](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300020-failure-in-creating-a-floating-ball-window) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1300025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Stops the floating ball. This API uses a promise to return the result.

**Since:** 20

<!--Device-FloatingBallController-stopFloatingBall(): Promise<void>--><!--Device-FloatingBallController-stopFloatingBall(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

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

Updates the floating ball. This API uses a promise to return the result.

**Since:** 20

<!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300002-abnormal-window-state) |
| [1300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300004-unauthorized-operation) |
| [1300027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300027-cannot-change-template-type-when-updating-the-floating-ball) |
| [1300025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300024-abnormal-floating-ball-window-state) |
| [1300028](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300028-floating-ball-based-on-a-static-template-cannot-be-updated) |

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
