# UserIdentityManager (System API)

Provides APIs for user IDM.

**Since:** 8

<!--Device-osAccount-class UserIdentityManager--><!--Device-osAccount-class UserIdentityManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## addCredential

```TypeScript
addCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void
```

Adds credential information, including the credential type, subtype, and token (if a non-PIN credential is added).

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-addCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void--><!--Device-UserIdentityManager-addCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialInfo | [CredentialInfo](arkts-basicservices-osaccount-credentialinfo-i-sys.md) | Yes |
| callback | [IIdmCallback](arkts-basicservices-osaccount-iidmcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 12300091 |
| 12300090 |
| [12300115](../../apis-basic-services-kit/errorcode-account.md#12300115-user-authentication-passwords-reached-the-limit) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 12300020 |
| [12300116](../../apis-basic-services-kit/errorcode-account.md#12300116-failed-to-verify-the-credential-complexity) |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [12300109](../../apis-basic-services-kit/errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let password: Uint8Array = new Uint8Array([0, 0, 0, 0, 0, 0]);
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
pinAuth.registerInputer({
  onGetData: (authSubType: osAccount.AuthSubType, callback: osAccount.IInputData) => {
    callback.onSetData(authSubType, password);
  }
});
let credentialInfo: osAccount.CredentialInfo = {
  credType: osAccount.AuthType.PIN,
  credSubType: osAccount.AuthSubType.PIN_SIX,
  token: new Uint8Array([]),
  additionalInfo: 'xxx'
};
let userIDM = new osAccount.UserIdentityManager();
userIDM.openSession((err: BusinessError, challenge: Uint8Array) => {
  try {
  userIDM.addCredential(credentialInfo, {
    onResult: (result: number, extraInfo: osAccount.RequestResult) => {
      console.info('addCredential result = ' + result);
      console.info('addCredential extraInfo = ' + extraInfo);
    }
  });
  } catch (e) {
    const err = e as BusinessError;
    console.error(`addCredential exception = code is ${err.code}, message is ${err.message}`);
  }
});
```

## cancel

```TypeScript
cancel(challenge: Uint8Array): void
```

Cancels an entry based on the challenge value.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-cancel(challenge: Uint8Array): void--><!--Device-UserIdentityManager-cancel(challenge: Uint8Array): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let challenge: Uint8Array = new Uint8Array([0]);
try {
  userIDM.cancel(challenge);
} catch (e) {
  const err = e as BusinessError;
  console.error(`cancel code is ${err.code}, message is ${err.message}`);
}
```

## closeSession

```TypeScript
closeSession(accountId?: number): void
```

Closes this session to terminate IDM.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-closeSession(accountId?: int): void--><!--Device-UserIdentityManager-closeSession(accountId?: int): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
let userIDM = new osAccount.UserIdentityManager();
let accountId = 100;
userIDM.closeSession(accountId);
```

## constructor

```TypeScript
constructor()
```

A **constructor()** used to create an instance for user IDM.

**Since:** 8

<!--Device-UserIdentityManager-constructor()--><!--Device-UserIdentityManager-constructor()-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let userIDM = new osAccount.UserIdentityManager();
```

## delCred

```TypeScript
delCred(credentialId: Uint8Array, token: Uint8Array, callback: IIdmCallback): void
```

Deletes user credential information.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-delCred(credentialId: Uint8Array, token: Uint8Array, callback: IIdmCallback): void--><!--Device-UserIdentityManager-delCred(credentialId: Uint8Array, token: Uint8Array, callback: IIdmCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialId | Uint8Array | Yes |
| token | Uint8Array | Yes |
| callback | [IIdmCallback](arkts-basicservices-osaccount-iidmcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let credentialId: Uint8Array = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0]);
let token: Uint8Array = new Uint8Array([0]);
try {
  userIDM.delCred(credentialId, token, {
    onResult: (result: number, extraInfo: osAccount.RequestResult) => {
        console.info('delCred result = ' + result);
        console.info('delCred extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`delCred exception = code is ${err.code}, message is ${err.message}`);
}
```

## delUser

```TypeScript
delUser(token: Uint8Array, callback: IIdmCallback): void
```

Deletes a user with an authentication token. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-delUser(token: Uint8Array, callback: IIdmCallback): void--><!--Device-UserIdentityManager-delUser(token: Uint8Array, callback: IIdmCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | Uint8Array | Yes |
| callback | [IIdmCallback](arkts-basicservices-osaccount-iidmcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let token: Uint8Array = new Uint8Array([0]);
try {
  userIDM.delUser(token, {
    onResult: (result: number, extraInfo: osAccount.RequestResult) => {
      console.info('delUser result = ' + result);
      console.info('delUser extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`delUser exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAuthInfo

```TypeScript
getAuthInfo(callback: AsyncCallback<Array<EnrolledCredInfo>>): void
```

Obtains authentication information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-getAuthInfo(callback: AsyncCallback<Array<EnrolledCredInfo>>): void--><!--Device-UserIdentityManager-getAuthInfo(callback: AsyncCallback<Array<EnrolledCredInfo>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;EnrolledCredInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
try {
  userIDM.getAuthInfo((err: BusinessError, result: osAccount.EnrolledCredInfo[]) => {
    if (err) {
      console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthInfo result = ' + JSON.stringify(result));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAuthInfo

```TypeScript
getAuthInfo(authType: AuthType, callback: AsyncCallback<Array<EnrolledCredInfo>>): void
```

Obtains authentication information of the specified type. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-getAuthInfo(authType: AuthType, callback: AsyncCallback<Array<EnrolledCredInfo>>): void--><!--Device-UserIdentityManager-getAuthInfo(authType: AuthType, callback: AsyncCallback<Array<EnrolledCredInfo>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;EnrolledCredInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
try {
  userIDM.getAuthInfo(osAccount.AuthType.PIN,
    (err: BusinessError, result: osAccount.EnrolledCredInfo[]) => {
    if (err) {
      console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthInfo result = ' + JSON.stringify(result));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAuthInfo

```TypeScript
getAuthInfo(authType: AuthType): Promise<Array<EnrolledCredInfo>>
```

Obtains authentication information. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-getAuthInfo(authType: AuthType): Promise<Array<EnrolledCredInfo>>--><!--Device-UserIdentityManager-getAuthInfo(authType: AuthType): Promise<Array<EnrolledCredInfo>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;EnrolledCredInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
try {
  userIDM.getAuthInfo(osAccount.AuthType.PIN).then((result: osAccount.EnrolledCredInfo[]) => {
    console.info('getAuthInfo result = ' + JSON.stringify(result))
  }).catch((err: BusinessError) => {
    console.error(`getAuthInfo error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAuthInfo

```TypeScript
getAuthInfo(options?: GetAuthInfoOptions): Promise<Array<EnrolledCredInfo>>
```

Obtains authentication information. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-getAuthInfo(options?: GetAuthInfoOptions): Promise<Array<EnrolledCredInfo>>--><!--Device-UserIdentityManager-getAuthInfo(options?: GetAuthInfoOptions): Promise<Array<EnrolledCredInfo>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetAuthInfoOptions](arkts-basicservices-osaccount-getauthinfooptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;EnrolledCredInfo&gt;&gt; |

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

let userIDM = new osAccount.UserIdentityManager();
let options: osAccount.GetAuthInfoOptions = {
  authType: osAccount.AuthType.PIN,
  accountId: 100,
};
try {
  userIDM.getAuthInfo(options).then((result: osAccount.EnrolledCredInfo[]) => {
    console.info('getAuthInfo result = ' + JSON.stringify(result))
  }).catch((err: BusinessError) => {
    console.error(`getAuthInfo error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

## getEnrolledId

```TypeScript
getEnrolledId(authType: AuthType, accountId?: number): Promise<Uint8Array>
```

Obtains the ID of the enrolled credential based on the credential type and account ID (optional). This API uses a  promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-getEnrolledId(authType: AuthType, accountId?: int): Promise<Uint8Array>--><!--Device-UserIdentityManager-getEnrolledId(authType: AuthType, accountId?: int): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| accountId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Uint8Array&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
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
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let accountId = 100;
try {
  userIDM.getEnrolledId(authType, accountId).then((enrolledId: Uint8Array) => {
    console.info('getEnrolledId enrolledId = ' + JSON.stringify(enrolledId));
  }).catch((err: BusinessError) => {
    console.error(`getEnrolledId error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getEnrolledId exception = code is ${err.code}, message is ${err.message}`);
}
```

## offCredentialChanged

```TypeScript
offCredentialChanged(callback?: Callback<CredentialChangeInfo>): void
```

Unsubscribes from credential change events. If no callback is not specified, this API unsubscribes from all subscription records.

**Since:** 23

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-offCredentialChanged(callback?: Callback<CredentialChangeInfo>): void--><!--Device-UserIdentityManager-offCredentialChanged(callback?: Callback<CredentialChangeInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;CredentialChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let identityMgr: osAccount.UserIdentityManager = new osAccount.UserIdentityManager();

const callback: Callback<osAccount.CredentialChangeInfo> = (changeInfo: osAccount.CredentialChangeInfo): void => {
  console.info('credentialType: ' + changeInfo.credentialType
    + ', changeType: ' + changeInfo.changeType
    + ', accountId: ' + changeInfo.accountId
    + ', addedCredentialId: ' + changeInfo.addedCredentialId
    + ', deletedCredentialId: ' + changeInfo.deletedCredentialId
    + ', isSilent: ' + changeInfo.isSilent
  )
}

try {
  identityMgr.onCredentialChanged([osAccount.AuthType.PIN, osAccount.AuthType.FACE], callback);
  console.info('Subscribe to the credential changes successfully');
} catch (e) {
  const err = e as BusinessError;
  console.error(`Failed to subscribe to the credential changes, code is ${err.code}, message is ${err.message}`)
}

try {
  identityMgr.offCredentialChanged(callback);
  console.info('Unsubscribe from the credential changes successfully');
} catch (e) {
  const err = e as BusinessError;
  console.error(`Failed to unsubscribe from the credential changes, code is ${err.code}, message is ${err.message}`)
}
```

## onCredentialChanged

```TypeScript
onCredentialChanged(credentialTypes: AuthType[], callback: Callback<CredentialChangeInfo>): void
```

Subscribes to one or more credential change events. This API uses a callback to return the credential change information.

**Since:** 23

**Required permissions:** ohos.permission.USE_USER_IDM

<!--Device-UserIdentityManager-onCredentialChanged(credentialTypes: AuthType[], callback: Callback<CredentialChangeInfo>): void--><!--Device-UserIdentityManager-onCredentialChanged(credentialTypes: AuthType[], callback: Callback<CredentialChangeInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialTypes | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md)[] | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;CredentialChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let identityMgr: osAccount.UserIdentityManager = new osAccount.UserIdentityManager();

const callback: Callback<osAccount.CredentialChangeInfo> = (changeInfo: osAccount.CredentialChangeInfo): void => {
  console.info('credentialType: ' + changeInfo.credentialType
    + ', changeType: ' + changeInfo.changeType
    + ', accountId: ' + changeInfo.accountId
    + ', addedCredentialId: ' + changeInfo.addedCredentialId
    + ', deletedCredentialId: ' + changeInfo.deletedCredentialId
    + ', isSilent: ' + changeInfo.isSilent
  )
}

try {
  identityMgr.onCredentialChanged([osAccount.AuthType.PIN, osAccount.AuthType.FACE], callback);
  console.info('Subscribe to the credential changes successfully');
} catch (e) {
  const err = e as BusinessError;
  console.error(`Failed to subscribe to the credential changes, code is ${err.code}, message is ${err.message}`)
}
```

## openSession

```TypeScript
openSession(callback: AsyncCallback<Uint8Array>): void
```

Opens a session to obtain the challenge value. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-openSession(callback: AsyncCallback<Uint8Array>): void--><!--Device-UserIdentityManager-openSession(callback: AsyncCallback<Uint8Array>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
try {
  userIDM.openSession((err: BusinessError, challenge: Uint8Array) => {
    if (err) {
      console.error(`openSession exception = code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('openSession challenge = ' + JSON.stringify(challenge));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`openSession exception = code is ${err.code}, message is ${err.message}`);
}
```

## openSession

```TypeScript
openSession(accountId?: number): Promise<Uint8Array>
```

Opens a session. This API returns a challenge value, which can be used to determine whether the subsequent identity authentication is in this session. This can prevent replay attacks. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-openSession(accountId?: int): Promise<Uint8Array>--><!--Device-UserIdentityManager-openSession(accountId?: int): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Uint8Array&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let accountId = 100;
try {
  userIDM.openSession(accountId).then((challenge: Uint8Array) => {
    console.info('openSession challenge = ' + JSON.stringify(challenge));
  }).catch((err: BusinessError) => {
    console.error(`openSession error = code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`openSession exception = code is ${err.code}, message is ${err.message}`);
}
```

## updateCredential

```TypeScript
updateCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void
```

Updates credential information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

<!--Device-UserIdentityManager-updateCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void--><!--Device-UserIdentityManager-updateCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialInfo | [CredentialInfo](arkts-basicservices-osaccount-credentialinfo-i-sys.md) | Yes |
| callback | [IIdmCallback](arkts-basicservices-osaccount-iidmcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300106](../../apis-basic-services-kit/errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300111](../../apis-basic-services-kit/errorcode-account.md#12300111-authentication-timed-out) |
| [12300109](../../apis-basic-services-kit/errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-credential-not-found) |
| [12300101](../../apis-basic-services-kit/errorcode-account.md#12300101-incorrect-credential) |
| [12300116](../../apis-basic-services-kit/errorcode-account.md#12300116-failed-to-verify-the-credential-complexity) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userIDM = new osAccount.UserIdentityManager();
let userAuth: osAccount.UserAuth = new osAccount.UserAuth();
let pinAuth: osAccount.PINAuth = new osAccount.PINAuth();
let password: Uint8Array = new Uint8Array([0, 0, 0, 0, 0, 0]);
let credentialInfo: osAccount.CredentialInfo = {
  credType: osAccount.AuthType.PIN,
  credSubType: osAccount.AuthSubType.PIN_SIX,
  token: new Uint8Array([]),
};
pinAuth.registerInputer({
  onGetData: (authSubType: osAccount.AuthSubType, callback: osAccount.IInputData) => {
    callback.onSetData(authSubType, password);
  }
});
userIDM.openSession((err: BusinessError, challenge: Uint8Array) => {
  userAuth.auth(challenge, credentialInfo.credType, osAccount.AuthTrustLevel.ATL1, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      if (result != osAccount.ResultCode.SUCCESS) {
        return;
      }
      if (extraInfo.token != null) {
        credentialInfo.token = extraInfo.token;
      }
      try {
        userIDM.updateCredential(credentialInfo, {
          onResult: (result: number, extraInfo: osAccount.RequestResult) => {
            console.info('updateCredential result = ' + result);
            console.info('updateCredential extraInfo = ' + extraInfo);
          }
        });
      } catch (e) {
        const err = e as BusinessError;
        console.error(`updateCredential exception = code is ${err.code}, message is ${err.message}`);
      }
    }
  });
});
```
