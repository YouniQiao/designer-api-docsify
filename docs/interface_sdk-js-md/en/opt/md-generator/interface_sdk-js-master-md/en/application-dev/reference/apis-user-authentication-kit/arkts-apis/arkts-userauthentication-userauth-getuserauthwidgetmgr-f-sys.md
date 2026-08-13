# getUserAuthWidgetMgr (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getUserAuthWidgetMgr

```TypeScript
function getUserAuthWidgetMgr(version: number): UserAuthWidgetMgr
```

Obtains the authentication widget manager object. It is used to obtain the **UserAuthWidgetMgr** instance, which can be used to register custom authentication widgets with the system for unified management. > **NOTE：**> Each **UserAuthWidgetMgr** instance can manage one authentication widget. To manage multiple widgets, you need to > obtain multiple instances.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SUPPORT_USER_AUTH

<!--Device-userAuth-function getUserAuthWidgetMgr(version: int): UserAuthWidgetMgr--><!--Device-userAuth-function getUserAuthWidgetMgr(version: int): UserAuthWidgetMgr-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| version | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UserAuthWidgetMgr](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuthWidgetMgrVersion = 1;
try {
  let userAuthWidgetMgr = userAuth.getUserAuthWidgetMgr(userAuthWidgetMgrVersion);
  console.info('get userAuthWidgetMgr instance successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`userAuth widgetMgr failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
