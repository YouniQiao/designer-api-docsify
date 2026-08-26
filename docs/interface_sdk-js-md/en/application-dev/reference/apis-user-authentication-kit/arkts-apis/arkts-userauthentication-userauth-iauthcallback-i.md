# IAuthCallback

Provides callbacks to return the authentication result. This API defines the authentication result callback method, which is used to obtain the authentication result after the authentication is complete. By implementing the **onResult** method, the application can obtain the authentication token when the authentication is successful, or obtain the error code and related information when the authentication fails.

**Since:** 10

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import userAuth from '@kit.UserAuthenticationKit';
import UserAuthIcon from '@kit.UserAuthenticationKitIcon';
```

## onResult

```TypeScript
onResult(result: UserAuthResult): void
```

Called to return the authentication result. If the authentication is successful, you can obtain the token information through **UserAuthResult** for subsequent security operation verification. If the authentication fails, you can obtain the error code through the **result** field and take corresponding measures (for example, prompting the user to perform authentication again or guiding the user to register a credential).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [UserAuthResult](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-userauthresult-e.md) | Yes | Authentication result. It contains information such as the authentication result code, authentication token (when the authentication is successful), authentication type, and credential status. The application needs to check the **result.result** field to determine whether the authentication is successful.    - If the value of **result.result** is **SUCCESS(12500000)**, the authentication is successful. In this case, you can use **result.token** to perform the subsequent operations.    - If the value of **result.result** is another value, the authentication fails. In this case, you need to handle the error based on the specific error code. |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      }  else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
});
```
