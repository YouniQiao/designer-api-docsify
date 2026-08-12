# getUserAuthWidgetMgr (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getUserAuthWidgetMgr

```TypeScript
function getUserAuthWidgetMgr(version: int): UserAuthWidgetMgr
```

Obtains the authentication widget manager object. It is used to obtain the **UserAuthWidgetMgr** instance, which can be used to register custom authentication widgets with the system for unified management.

> **NOTE：**

> Each **UserAuthWidgetMgr** instance can manage one authentication widget. To manage multiple widgets, you need to
> obtain multiple instances.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SUPPORT_USER_AUTH

<!--Device-userAuth-function getUserAuthWidgetMgr(version: int): UserAuthWidgetMgr--><!--Device-userAuth-function getUserAuthWidgetMgr(version: int): UserAuthWidgetMgr-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| version | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Version number of the authentication widget. Currently, only version 1 is supported. The widget version determines the communication protocol and supported features between the widget and the framework. |

**Return value:**

| Type | Description |
| --- | --- |
| [UserAuthWidgetMgr](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) | Authentication widget manager object. It can be used to subscribe to and unsubscribe from commands from the user authentication framework. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Called by non-system application. |
| [12500002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuthWidgetMgrVersion = 1;
try {
  let userAuthWidgetMgr = userAuth.getUserAuthWidgetMgr(userAuthWidgetMgrVersion);
  console.info('get userAuthWidgetMgr instance success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`userAuth widgetMgr catch error: Code is ${err?.code}, message is ${err?.message}`);
}
```

