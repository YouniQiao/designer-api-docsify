# UserAuth (System API)

Provides APIs for user authentication.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
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

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |
| [12300105](../errorcode-account.md#12300105-trust-level-not-supported) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| [12300117](../errorcode-account.md#12300117-pin-expired) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-credential-expired) |
| 12300211 |

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

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |
| [12300105](../errorcode-account.md#12300105-trust-level-not-supported) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| [12300117](../errorcode-account.md#12300117-pin-expired) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-credential-expired) |
| 12300211 |

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

Authenticates a specified user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |
| [12300105](../errorcode-account.md#12300105-trust-level-not-supported) |
| [12300106](../errorcode-account.md#12300106-authentication-type-not-supported) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| [12300117](../errorcode-account.md#12300117-pin-expired) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-credential-expired) |
| 12300211 |

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): void
```

Cancels an authentication.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextID | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## constructor

```TypeScript
constructor()
```

A constructor used to create an instance for user authentication.

**Since:** 8

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): number
```

Obtains the available status of the authentication capability corresponding to the specified authentication type and trust level.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300117](../errorcode-account.md#12300117-pin-expired) |

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void
```

Obtains the executor property based on the request. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300020 |

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>
```

Obtains the executor property based on the request. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300020 |

## getPropertyByCredentialId

```TypeScript
getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>
```

Obtains the specified property information of the associated executor based on the credential ID. This API uses a promise to return the result.

**Since:** 14

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300020 |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## getVersion

```TypeScript
getVersion(): number
```

Obtains this version number.

**Since:** 8

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

## prepareRemoteAuth

```TypeScript
prepareRemoteAuth(remoteNetworkId: string): Promise<void>
```

Prepares for remote authentication. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300090 |
| 12300091 |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void
```

Sets the property for the initialization algorithm. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest): Promise<void>
```

Sets the property for the initialization algorithm. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
