# UserRecognitionMgr

```TypeScript
interface UserRecognitionMgr
```

Provides APIs for querying and subscribing to user recognition results. Use [getUserRecognitionMgr](arkts-userauthentication-userauth-getuserrecognitionmgr-f.md) to obtain a **UserRecognitionMgr** instance.

**Since:** 26.0.1

<!--Device-userAuth-interface UserRecognitionMgr--><!--Device-userAuth-interface UserRecognitionMgr-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getUserRecognitionResult

```TypeScript
getUserRecognitionResult(): Promise<UserRecognitionResult>
```

Obtains the latest user recognition result. This API uses a promise to return the result.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API (ArkTS-Dyn only) :** This API can be used in atomic services since version 26.0.1.

<!--Device-UserRecognitionMgr-getUserRecognitionResult(): Promise<UserRecognitionResult>--><!--Device-UserRecognitionMgr-getUserRecognitionResult(): Promise<UserRecognitionResult>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[UserRecognitionResult](arkts-userauthentication-userauth-userrecognitionresult-i.md)&gt; | Promise used to return the recognition result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let mgr = userAuth.getUserRecognitionMgr();
if (mgr == null) {
  console.error('device does not support user recognition');
} else {
  mgr.getUserRecognitionResult()
    .then((result: userAuth.UserRecognitionResult) => {
      console.info(`status: ${result.status}, userId: ${result.userId}`);
    })
    .catch((err: BusinessError) => {
      console.error(`getUserRecognitionResult failed, Code: ${err?.code}, message: ${err?.message}`);
    });
}
```

## offUserRecognitionChange

```TypeScript
offUserRecognitionChange(callback?: UserRecognitionResultCallback): void
```

Unsubscribes from user recognition change events.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API (ArkTS-Dyn only) :** This API can be used in atomic services since version 26.0.1.

<!--Device-UserRecognitionMgr-offUserRecognitionChange(callback?: UserRecognitionResultCallback): void--><!--Device-UserRecognitionMgr-offUserRecognitionChange(callback?: UserRecognitionResultCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UserRecognitionResultCallback](arkts-userauthentication-userauth-userrecognitionresultcallback-t.md) | No | Callback to unregister. If this parameter is not specified, all registered callbacks are unsubscribed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let mgr = userAuth.getUserRecognitionMgr();
if (mgr == null) {
  console.error('device does not support user recognition');
} else {
  let callback: userAuth.UserRecognitionResultCallback = (result: userAuth.UserRecognitionResult) => {
    console.info(`status: ${result.status}, userId: ${result.userId}`);
  };
  mgr.onUserRecognitionChange(callback);
  // Cancel the specified callback.
  mgr.offUserRecognitionChange(callback);
  // Cancel all callbacks.
  mgr.offUserRecognitionChange();
}
```

## onUserRecognitionChange

```TypeScript
onUserRecognitionChange(callback: UserRecognitionResultCallback): void
```

Subscribes to user recognition change events.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API (ArkTS-Dyn only) :** This API can be used in atomic services since version 26.0.1.

<!--Device-UserRecognitionMgr-onUserRecognitionChange(callback: UserRecognitionResultCallback): void--><!--Device-UserRecognitionMgr-onUserRecognitionChange(callback: UserRecognitionResultCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UserRecognitionResultCallback](arkts-userauthentication-userauth-userrecognitionresultcallback-t.md) | Yes | Callback used to receive the recognition result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let mgr = userAuth.getUserRecognitionMgr();
if (mgr == null) {
  console.error('device does not support user recognition');
} else {
  let callback: userAuth.UserRecognitionResultCallback = (result: userAuth.UserRecognitionResult) => {
    console.info(`status: ${result.status}, userId: ${result.userId}`);
  };
  mgr.onUserRecognitionChange(callback);
}
```
