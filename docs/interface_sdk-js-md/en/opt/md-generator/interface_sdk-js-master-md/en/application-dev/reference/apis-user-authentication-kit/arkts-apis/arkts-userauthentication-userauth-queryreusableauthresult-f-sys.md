# queryReusableAuthResult (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## queryReusableAuthResult

```TypeScript
function queryReusableAuthResult(authParam: AuthParam): Uint8Array
```

Queries whether there is any reusable identity authentication result. This API is used to query whether there is an authentication result that meets the reuse conditions before authentication is initiated. If such a result exists,the **AuthToken** that can be reused is returned directly, and the user does not need to perform authentication again.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-userAuth-function queryReusableAuthResult(authParam: AuthParam): Uint8Array--><!--Device-userAuth-function queryReusableAuthResult(authParam: AuthParam): Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [authParam](arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [12500008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500008-parameter-verification-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500017-authentication-result-reuse-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  const randData: Uint8Array = rand?.generateRandomSync(len)?.data;
  const reuseUnlockResult: userAuth.ReuseUnlockResult = {
    reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
    reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  let authToken = userAuth.queryReusableAuthResult(authParam);
  console.info('query reuse auth result successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`query reuse auth result failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
