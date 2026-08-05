# off (System API)

## off('systemBarTintChange')

```TypeScript
function off(type: 'systemBarTintChange', callback?: Callback<SystemBarTintState>): void
```

Unsubscribes from the property change event of the status bar and navigation bar.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-window-function off(type: 'systemBarTintChange', callback?: Callback<SystemBarTintState>): void--><!--Device-window-function off(type: 'systemBarTintChange', callback?: Callback<SystemBarTintState>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemBarTintChange' | Yes | Event type. The value is fixed at **'systemBarTintChange'**, indicating the property change event of the status bar and navigation bar. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SystemBarTintState&gt; | No | Callback used to return the properties of the status bar and navigation bar. If a value is passed in, the corresponding subscription is canceled. If no value is passed in,all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1. Incorrect parameter types;2. Parameter verification failed. |

**Example**

```TypeScript
const callback = (systemBarTintState: window.SystemBarTintState) => {
  // ...
}
try {
  window.on('systemBarTintChange', callback);

  window.off('systemBarTintChange', callback);
  // Unregister all the callbacks that have been registered through on().
  window.off('systemBarTintChange');
} catch (exception) {
  console.error(`Failed to enable or disable the listener for systemBarTint changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## off('gestureNavigationEnabledChange')

```TypeScript
function off(type: 'gestureNavigationEnabledChange', callback?: Callback<boolean>): void
```

Unsubscribes from the gesture navigation status change event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-window-function off(type: 'gestureNavigationEnabledChange', callback?: Callback<boolean>): void--><!--Device-window-function off(type: 'gestureNavigationEnabledChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'gestureNavigationEnabledChange' | Yes | the event of gesture navigation enabled changes. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | No | Callback function that has been used for the subscription. If a value is |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1. Incorrect parameter types;2. Parameter verification failed. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |

**Example**

```TypeScript
const callback = (bool: boolean) => {
  // ...
}
try {
  window.on('gestureNavigationEnabledChange', callback);
  window.off('gestureNavigationEnabledChange', callback);
  // Unregister all the callbacks that have been registered through on().
  window.off('gestureNavigationEnabledChange');
} catch (exception) {
  console.error(`Failed to enable or disable the listener for gesture navigation status changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## off('waterMarkFlagChange')

```TypeScript
function off(type: 'waterMarkFlagChange', callback?: Callback<boolean>): void
```

Unsubscribes from the watermark status change event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-window-function off(type: 'waterMarkFlagChange', callback?: Callback<boolean>): void--><!--Device-window-function off(type: 'waterMarkFlagChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'waterMarkFlagChange' | Yes | the event of watermark flag change. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | No | Callback function that has been used for the subscription. If a value is |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1. Incorrect parameter types;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Parameter verification failed. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |

**Example**

```TypeScript
const callback = (bool: boolean) => {
  // ...
}
try {
  window.on('waterMarkFlagChange', callback);
  window.off('waterMarkFlagChange', callback);
  // Unregister all the callbacks that have been registered through on().
  window.off('waterMarkFlagChange');
} catch (exception) {
  console.error(`Failed to enable or disable the listener for watermark flag changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

