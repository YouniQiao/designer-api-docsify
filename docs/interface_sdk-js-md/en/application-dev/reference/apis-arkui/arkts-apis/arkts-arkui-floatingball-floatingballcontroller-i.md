# FloatingBallController

Implements a floating ball controller instance, which is used to start, update, and stop floating balls, and register callbacks.Before calling any of the following APIs, you must use [floatingBall.create()](arkts-arkui-floatingball-create-f.md) to create a floating ball controller instance.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## getFloatingBallWindowInfo

```TypeScript
getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>
```

Obtains the floating ball window information. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FloatingBallWindowInfo](arkts-arkui-floatingball-floatingballwindowinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<FloatingBallState>): void
```

Unregisters the listener for lifecycle state changes of the floating ball.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatingBallState](arkts-arkui-floatingball-floatingballstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## off('click')

```TypeScript
off(type: 'click', callback?: Callback<void>): void
```

Unregisters the listener for click events of the floating ball.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'click' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## offDestroy

```TypeScript
offDestroy(callback?: Callback<string>): void
```

Unregister floating ball destroy event listener.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<FloatingBallState>): void
```

Registers a listener for lifecycle state changes of the floating ball. To prevent memory leaks, remember to unregister the listener when it is no longer needed.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatingBallState](arkts-arkui-floatingball-floatingballstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300022](../errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## on('click')

```TypeScript
on(type: 'click', callback: Callback<void>): void
```

Registers a listener for click events of the floating ball. To prevent memory leaks, remember to unregister the listener when it is no longer needed.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'click' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300022](../errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## onDestroy

```TypeScript
onDestroy(callback: Callback<string>): void
```

Register floating ball destroy event listener.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300022](../errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## restoreMainWindow

```TypeScript
restoreMainWindow(want: Want): Promise<void>
```

Restores the main window of the application and loads the specified page. This API uses a promise to return the result. This API can be called only after the floating ball is tapped. If the application has the **ohos.permission.AUTO_RESTORE_MAIN_WINDOW** permission, this API can be called directly without tapping the floating ball.

**Since:** 20

**Required permissions:** ohos.permission.USE_FLOAT_BALL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300026](../errorcode-window.md#1300026-failure-in-launch-an-application-window-via-a-floating-ball) |

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
is in the foreground (the [lifecycle state](../../../windowmanager/window-overview.md#lifecycle-states) is **SHOWN** or **RESUMED**) and is visible when the application is in the background (the [lifecycle state](../../../windowmanager/window-overview.md#lifecycle-states) is **HIDDEN**).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## startFloatingBall

```TypeScript
startFloatingBall(params: FloatingBallParams): Promise<void>
```

Starts the floating ball. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.USE_FLOAT_BALL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300020](../errorcode-window.md#1300020-failure-in-creating-a-floating-ball-window) |
| [1300021](../errorcode-window.md#1300021-failure-in-starting-multiple-floating-balls) |
| [1300022](../errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300034](../errorcode-window.md#1300034-operation-of-the-float-view-conflicts-with-those-of-other-floating-windows) |

## stopFloatingBall

```TypeScript
stopFloatingBall(): Promise<void>
```

Stops the floating ball. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300022](../errorcode-window.md#1300022-repeated-floating-ball-operation) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |

## updateFloatingBall

```TypeScript
updateFloatingBall(params: FloatingBallParams): Promise<void>
```

Updates the floating ball. This API uses a promise to return the result.

**Since:** 20

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
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |
| [1300024](../errorcode-window.md#1300024-abnormal-floating-ball-window-state) |
| [1300025](../errorcode-window.md#1300025-unsupported-operation-in-the-current-floating-ball-state) |
| [1300027](../errorcode-window.md#1300027-cannot-change-template-type-when-updating-the-floating-ball) |
| [1300028](../errorcode-window.md#1300028-floating-ball-based-on-a-static-template-cannot-be-updated) |
