# on (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## on('privateModeChange')

```TypeScript
function on(type: 'privateModeChange', callback: Callback<boolean>): void
```

Subscribes to privacy mode changes of this display. When there is a privacy window in the foreground of the display, the display is in privacy mode, and the content in the privacy window cannot be captured or recorded.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-display-function on(type: 'privateModeChange', callback: Callback<boolean>): void--><!--Device-display-function on(type: 'privateModeChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateModeChange' | Yes | Event type. The value is fixed at **'privateModeChange'**, indicating that the privacy mode of the display is changed. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to return whether the privacy mode of the display is changed. **true** if changed, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<boolean> = (data: boolean) => {
  console.info(`Listening enabled. Data: ${data}`);
};
try {
  display.on("privateModeChange", callback);
} catch (exception) {
  console.error(`Failed to register callback. Code: ${exception.code} , message : ${exception.message}`);
}
```

