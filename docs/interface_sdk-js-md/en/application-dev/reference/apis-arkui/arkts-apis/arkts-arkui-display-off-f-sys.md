# off (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## off('privateModeChange')

```TypeScript
function off(type: 'privateModeChange', callback?: Callback<boolean>): void
```

Unsubscribes from privacy mode changes of this display.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-display-function off(type: 'privateModeChange', callback?: Callback<boolean>): void--><!--Device-display-function off(type: 'privateModeChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateModeChange' | Yes | Event type. The value is fixed at **'privateModeChange'**, indicating that the privacy mode of the display is changed. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | No | Callback used to return whether the privacy mode of the display is changed. **true** if changed, **false** otherwise. If this parameter is not specified, all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
try {
  display.off("privateModeChange");
} catch (exception) {
  console.error(`Failed to unregister callback. Code: ${exception.code} , message : ${exception.message}`);
}
```

