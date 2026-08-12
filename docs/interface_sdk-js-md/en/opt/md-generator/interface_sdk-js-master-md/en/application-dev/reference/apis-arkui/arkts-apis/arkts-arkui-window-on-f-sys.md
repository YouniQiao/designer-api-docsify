# on (System API)

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## on('systemBarTintChange')

```TypeScript
function on(type: 'systemBarTintChange', callback: Callback<SystemBarTintState>): void
```

Subscribes to the property change event of the status bar and navigation bar.

**Since:** 8

<!--Device-window-function on(type: 'systemBarTintChange', callback: Callback<SystemBarTintState>): void--><!--Device-window-function on(type: 'systemBarTintChange', callback: Callback<SystemBarTintState>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemBarTintChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
  window.on('systemBarTintChange', (data) => {
    console.info('Succeeded in enabling the listener for systemBarTint changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for systemBarTint changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## on('gestureNavigationEnabledChange')

```TypeScript
function on(type: 'gestureNavigationEnabledChange', callback: Callback<boolean>): void
```

Subscribes to the gesture navigation status change event.

**Since:** 10

<!--Device-window-function on(type: 'gestureNavigationEnabledChange', callback: Callback<boolean>): void--><!--Device-window-function on(type: 'gestureNavigationEnabledChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'gestureNavigationEnabledChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
  window.on('gestureNavigationEnabledChange', (data) => {
    console.info(`Succeeded in enabling the listener for gesture navigation status changes. Data: ${data}`);
  });
} catch (exception) {
  console.error(`Failed to enable the listener for gesture navigation status changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## on('waterMarkFlagChange')

```TypeScript
function on(type: 'waterMarkFlagChange', callback: Callback<boolean>): void
```

Subscribes to the watermark status change event.

**Since:** 10

<!--Device-window-function on(type: 'waterMarkFlagChange', callback: Callback<boolean>): void--><!--Device-window-function on(type: 'waterMarkFlagChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'waterMarkFlagChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
  window.on('waterMarkFlagChange', (data) => {
    console.info(`Succeeded in enabling the listener for watermark flag changes. Data: ${data}`);
  });
} catch (exception) {
  console.error(`Failed to enable the listener for watermark flag changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```
