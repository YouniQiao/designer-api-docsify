# UserIdentityManager (System API)

Provides APIs for managing the user identity.

**Since:** 8

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

Adds credentials of specified types, including the credential type, subtype, and token (if a non-PIN credential is added).

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300008](../errorcode-account.md#12300008-restricted-account) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300115](../errorcode-account.md#12300115-user-authentication-passwords-reached-the-limit) |
| [12300116](../errorcode-account.md#12300116-failed-to-verify-the-credential-complexity) |

## cancel

```TypeScript
cancel(challenge: Uint8Array): void
```

Cancels an entry based on the challenge value.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## closeSession

```TypeScript
closeSession(accountId?: number): void
```

Closes this session to terminate IDM.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300008](../errorcode-account.md#12300008-restricted-account) |

## constructor

```TypeScript
constructor()
```

A **constructor()** used to create an instance for managing the user identity.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## delCred

```TypeScript
delCred(credentialId: Uint8Array, token: Uint8Array, callback: IIdmCallback): void
```

Deletes user credentials.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## delUser

```TypeScript
delUser(token: Uint8Array, callback: IIdmCallback): void
```

Deletes a user with an authentication token. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |

## getAuthInfo

```TypeScript
getAuthInfo(callback: AsyncCallback<Array<EnrolledCredInfo>>): void
```

Obtains authentication information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[EnrolledCredInfo](arkts-basicservices-osaccount-enrolledcredinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| 12300020 |

## getAuthInfo

```TypeScript
getAuthInfo(authType: AuthType, callback: AsyncCallback<Array<EnrolledCredInfo>>): void
```

Obtains authentication information of the specified type. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[EnrolledCredInfo](arkts-basicservices-osaccount-enrolledcredinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300020 |

## getAuthInfo

```TypeScript
getAuthInfo(authType: AuthType): Promise<Array<EnrolledCredInfo>>
```

Obtains authentication information. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[EnrolledCredInfo](arkts-basicservices-osaccount-enrolledcredinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300020 |

## getAuthInfo

```TypeScript
getAuthInfo(options?: GetAuthInfoOptions): Promise<Array<EnrolledCredInfo>>
```

Obtains authentication information. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetAuthInfoOptions](arkts-basicservices-osaccount-getauthinfooptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[EnrolledCredInfo](arkts-basicservices-osaccount-enrolledcredinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300020 |

## getEnrolledId

```TypeScript
getEnrolledId(authType: AuthType, accountId?: number): Promise<Uint8Array>
```

Obtains the ID of the enrolled credential based on the credential type and account ID (optional). This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.USE_USER_IDM

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
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300020 |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |

## offCredentialChanged

```TypeScript
offCredentialChanged(callback?: Callback<CredentialChangeInfo>): void
```

Unsubscribes from credential change events. If no callback is not specified, this API unsubscribes from all subscription records.

**Since:** 23

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[CredentialChangeInfo](arkts-basicservices-osaccount-credentialchangeinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## onCredentialChanged

```TypeScript
onCredentialChanged(credentialTypes: AuthType[], callback: Callback<CredentialChangeInfo>): void
```

Subscribes to one or more types of credential change events. This API uses a callback to return the credential change information.

**Since:** 23

**Required permissions:** ohos.permission.USE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| credentialTypes | [AuthType[]](arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[CredentialChangeInfo](arkts-basicservices-osaccount-credentialchangeinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |

## openSession

```TypeScript
openSession(callback: AsyncCallback<Uint8Array>): void
```

Opens a session to obtain the challenge value. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## openSession

```TypeScript
openSession(accountId?: number): Promise<Uint8Array>
```

Opens a session. This API returns a challenge value, which can be used to determine whether the subsequent identity authentication is in this session. This can prevent replay attacks. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300008](../errorcode-account.md#12300008-restricted-account) |

## updateCredential

```TypeScript
updateCredential(credentialInfo: CredentialInfo, callback: IIdmCallback): void
```

Updates credentials. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_USER_IDM

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300116](../errorcode-account.md#12300116-failed-to-verify-the-credential-complexity) |
