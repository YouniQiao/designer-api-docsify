# AuthorizationManager (System API)

Defines the OS account authorization manager class.

**Since:** 24

<!--Device-osAccount-interface AuthorizationManager--><!--Device-osAccount-interface AuthorizationManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## acquireAuthorization

```TypeScript
acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>
```

Acquires an authorization for a process.

**Since:** 24

**Required permissions:** ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>--><!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |
| options | [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AcquireAuthorizationResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';
let options: osAccount.AcquireAuthorizationOptions = {
  challenge: new Uint8Array([1, 2, 3]),
  isReuseNeeded: true,
  isInteractionAllowed: true,
};
try {
  authorizationManager.acquireAuthorization(privilege, options).then((result: osAccount.AcquireAuthorizationResult) => {
    console.info(`acquireAuthorization successfully, resultCode: ${result.resultCode}`);
  }).catch((err: BusinessError) => {
    console.error(`acquireAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`acquireAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## hasAuthorization

```TypeScript
hasAuthorization(privilege: string): Promise<boolean>
```

Checks whether the current process has specified authorization.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>--><!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.hasAuthorization(privilege).then((isAuthorized: boolean) => {
    console.info(`Privilege: ${privilege} has been authorized: ${isAuthorized}`);
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`hasAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`hasAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## releaseAuthorization

```TypeScript
releaseAuthorization(privilege: string): Promise<void>
```

Releases the specified authorization for the current process.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>--><!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| privilege | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.releaseAuthorization(privilege).then(() => {
    console.info('releaseAuthorization success');
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`releaseAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`releaseAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```
