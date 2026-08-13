# UserAuth (System API)

Provides APIs for user authentication.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-class UserAuth--><!--Device-osAccount-class UserAuth-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

Performs authentication of the current user.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| 12300091 |
| 12300090 |
| [12300120](../../apis-basic-services-kit/errorcode-account.md#12300120-credential-expired) |
| 12300211 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-authentication-service-abnormal) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-authentication-service-not-found) |
| [12300112](../../apis-basic-services-kit/errorcode-account.md#12300112-authentication-service-does-not-respond) |
| 12300119 |
| [12300117](../../apis-basic-services-kit/errorcode-account.md#12300117-pin-expired) |
| 12300020 |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300105](../../apis-basic-services-kit/errorcode-account.md#12300105-trust-level-not-supported) |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [12300110](../../apis-basic-services-kit/errorcode-account.md#12300110-authentication-locked) |
| [12300013](../../apis-basic-services-kit/errorcode-account.md#12300013-network-exception) |
| [12300109](../../apis-basic-services-kit/errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.auth(challenge, authType, authTrustLevel, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      options: AuthOptions,
      callback: IUserAuthCallback
    ): Uint8Array
```

Starts user authentication based on the specified challenge value, authentication type (PIN, facial, or fingerprint authentication), authentication trust level, and optional parameters (such as the account ID and authentication intent).

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      options: AuthOptions,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      options: AuthOptions,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |
| options | [AuthOptions](arkts-basicservices-osaccount-authoptions-i-sys.md) | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| 12300091 |
| 12300090 |
| [12300120](../../apis-basic-services-kit/errorcode-account.md#12300120-credential-expired) |
| 12300211 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-authentication-service-abnormal) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-authentication-service-not-found) |
| [12300112](../../apis-basic-services-kit/errorcode-account.md#12300112-authentication-service-does-not-respond) |
| 12300119 |
| [12300117](../../apis-basic-services-kit/errorcode-account.md#12300117-pin-expired) |
| 12300020 |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300105](../../apis-basic-services-kit/errorcode-account.md#12300105-trust-level-not-supported) |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [12300110](../../apis-basic-services-kit/errorcode-account.md#12300110-authentication-locked) |
| [12300013](../../apis-basic-services-kit/errorcode-account.md#12300013-network-exception) |
| [12300109](../../apis-basic-services-kit/errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
let options: osAccount.AuthOptions = {
  accountId: 100
};
try {
  userAuth.auth(challenge, authType, authTrustLevel, options, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## authUser

```TypeScript
authUser(
      userId: number,
      challenge: Uint8Array,
      authType: AuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

Performs authentication of the specified user. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-authUser(      userId: int,      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-authUser(      userId: int,      challenge: Uint8Array,      authType: AuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| challenge | Uint8Array | Yes |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| 12300091 |
| 12300090 |
| [12300120](../../apis-basic-services-kit/errorcode-account.md#12300120-credential-expired) |
| 12300211 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-authentication-service-abnormal) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-authentication-service-not-found) |
| [12300112](../../apis-basic-services-kit/errorcode-account.md#12300112-authentication-service-does-not-respond) |
| 12300119 |
| [12300117](../../apis-basic-services-kit/errorcode-account.md#12300117-pin-expired) |
| 12300020 |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300105](../../apis-basic-services-kit/errorcode-account.md#12300105-trust-level-not-supported) |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [12300110](../../apis-basic-services-kit/errorcode-account.md#12300110-authentication-locked) |
| [12300013](../../apis-basic-services-kit/errorcode-account.md#12300013-network-exception) |
| [12300109](../../apis-basic-services-kit/errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let userID: number = 100;
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.authUser(userID, challenge, authType, authTrustLevel, {
    onResult: (result,extraInfo) => {
      console.info('authUser result = ' + result);
      console.info('authUser extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`authUser exception = code is ${err.code}, message is ${err.message}`);
}
```

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): void
```

Cancels an authentication.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-cancelAuth(contextID: Uint8Array): void--><!--Device-UserAuth-cancelAuth(contextID: Uint8Array): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextID | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
let challenge = new Uint8Array([0]);
let contextId: Uint8Array = userAuth.auth(challenge, osAccount.AuthType.PIN, osAccount.AuthTrustLevel.ATL1, {
  onResult: (result: number, extraInfo: osAccount.AuthResult) => {
    console.info('auth result = ' + result);
    console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
  }
});
try {
  userAuth.cancelAuth(contextId);
} catch (e) {
  const err = e as BusinessError;
  console.error(`cancelAuth exception = code is ${err.code}, message is ${err.message}`);
}
```

## constructor

```TypeScript
constructor()
```

A constructor used to create an instance for user authentication.

**Since:** 23

**Deprecated since:** -1

<!--Device-UserAuth-constructor()--><!--Device-UserAuth-constructor()-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let userAuth = new osAccount.UserAuth();
```

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): number
```

Obtains the available status of the authentication capability corresponding to the specified authentication type and trust level.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): int--><!--Device-UserAuth-getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300117](../../apis-basic-services-kit/errorcode-account.md#12300117-pin-expired) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  let status: number = userAuth.getAvailableStatus(authType, authTrustLevel);
  console.info('getAvailableStatus status = ' + status);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAvailableStatus exception = code is ${err.code}, message is ${err.message}`);
}
```

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void
```

Obtains the executor property based on the request. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void--><!--Device-UserAuth-getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let keys: Array<osAccount.GetPropertyType>  = [
  osAccount.GetPropertyType.AUTH_SUB_TYPE,
  osAccount.GetPropertyType.REMAIN_TIMES,
  osAccount.GetPropertyType.FREEZING_TIME
];
let request: osAccount.GetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  keys: keys
};
try {
  userAuth.getProperty(request, (err: BusinessError, result: osAccount.ExecutorProperty) => {
    if (err) {
      console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getProperty result = ' + JSON.stringify(result));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>
```

Obtains the executor property based on the request. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>--><!--Device-UserAuth-getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let keys: Array<osAccount.GetPropertyType> = [
  osAccount.GetPropertyType.AUTH_SUB_TYPE,
  osAccount.GetPropertyType.REMAIN_TIMES,
  osAccount.GetPropertyType.FREEZING_TIME
];
let request: osAccount.GetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  keys: keys
};
try {
  userAuth.getProperty(request).then((result: osAccount.ExecutorProperty) => {
    console.info('getProperty result = ' + JSON.stringify(result));
  }).catch((err: BusinessError) => {
    console.error(`getProperty error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## getPropertyByCredentialId

```TypeScript
getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>
```

Obtains the specified property information of the associated executor based on the credential ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>--><!--Device-UserAuth-getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialId | Uint8Array | Yes |
| keys | Array&lt;[GetPropertyType](arkts-basicservices-osaccount-getpropertytype-e-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let credInfo: osAccount.EnrolledCredInfo[] = [];
async function getProperty() {
  try {
    credInfo = await userIDM.getAuthInfo(osAccount.AuthType.PRIVATE_PIN);
  } catch (e) {
    const err = e as BusinessError;
    console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (credInfo.length == 0) {
    console.info('no credential infos');
    return;
  }
  let testCredentialId: Uint8Array = credInfo[0].credentialId;
  let keys: Array<osAccount.GetPropertyType> = [
    osAccount.GetPropertyType.AUTH_SUB_TYPE,
    osAccount.GetPropertyType.REMAIN_TIMES,
    osAccount.GetPropertyType.FREEZING_TIME
  ];
  try {
    let userAuth = new osAccount.UserAuth();
    userAuth.getPropertyByCredentialId(testCredentialId, keys).then((result: osAccount.ExecutorProperty) => {
      console.info('getPropertyByCredentialId result = ' + JSON.stringify(result));
    }).catch((err: BusinessError) => {
      console.error(`getPropertyByCredentialId error = code is ${err.code}, message is ${err.message}`);
    });
  } catch (e) {
    const err = e as BusinessError;
    console.error(`getPropertyByCredentialId exception = code is ${err.code}, message is ${err.message}`);
  }
}
```

## getVersion

```TypeScript
getVersion(): number
```

Obtains this version number.

**Since:** 23

**Deprecated since:** -1

<!--Device-UserAuth-getVersion(): int--><!--Device-UserAuth-getVersion(): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let userAuth = new osAccount.UserAuth();
let version: number = userAuth.getVersion();
console.info('getVersion version = ' + version);
```

## prepareRemoteAuth

```TypeScript
prepareRemoteAuth(remoteNetworkId: string): Promise<void>
```

Prepares for remote authentication. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-prepareRemoteAuth(remoteNetworkId: string): Promise<void>--><!--Device-UserAuth-prepareRemoteAuth(remoteNetworkId: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| remoteNetworkId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 12300091 |
| 12300090 |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let distributedDeviceMgr = distributedDeviceManager.createDeviceManager("com.example.bundleName");
distributedDeviceMgr.getAvailableDeviceList().then((data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
    try {
      if (data.length > 0 && data[0].networkId != null) {
        userAuth.prepareRemoteAuth(data[0].networkId).then(() => {
          console.info('prepareRemoteAuth successfully');
        }).catch((err: BusinessError) => {
          console.error(`prepareRemoteAuth failed, error = code is ${err.code}, message is ${err.message}`);
        });
      }
    } catch (e) {
      const err = e as BusinessError;
      console.error(`prepareRemoteAuth exception = code is ${err.code}, message is ${err.message}`);
    }
  }
)
```

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void
```

Sets the property for the initialization algorithm. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void--><!--Device-UserAuth-setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let request: osAccount.SetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  key: osAccount.SetPropertyType.INIT_ALGORITHM,
  setInfo: new Uint8Array([0])
};
try {
  userAuth.setProperty(request, (err: BusinessError) => {
    if (err) {
      console.error(`setProperty failed, error = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setProperty successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setProperty exception = code is ${err.code}, message is ${err.message}`);
}
```

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest): Promise<void>
```

Sets the property for the initialization algorithm. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

<!--Device-UserAuth-setProperty(request: SetPropertyRequest): Promise<void>--><!--Device-UserAuth-setProperty(request: SetPropertyRequest): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let request: osAccount.SetPropertyRequest = {
  authType: osAccount.AuthType.PIN,
  key: osAccount.SetPropertyType.INIT_ALGORITHM,
  setInfo: new Uint8Array([0])
};
try {
  userAuth.setProperty(request).then(() => {
    console.info('setProperty successfully');
  }).catch((err: BusinessError) => {
    console.error(`setProperty failed, error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setProperty exception = code is ${err.code}, message is ${err.message}`);
}
```
