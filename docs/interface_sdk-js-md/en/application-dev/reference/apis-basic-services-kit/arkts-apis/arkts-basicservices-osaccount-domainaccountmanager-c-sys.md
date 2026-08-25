# DomainAccountManager

Provides APIs for domain account management.

**Since:** 18

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## auth

```TypeScript
static auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void
```

Authenticates a domain account.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| credential | Uint8Array | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## auth

```TypeScript
static auth(
      domainAccountInfo: DomainAccountInfo,
      credential: Uint8Array,
      options: DomainAccountAuthOptions,
      callback: IUserAuthCallback): void
```

Authenticates a specified domain account. You can specify authentication options, such as server parameters. This API uses an asynchronous callback to return the result.

**Since:** 24

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| credential | Uint8Array | Yes |
| options | [DomainAccountAuthOptions](arkts-basicservices-osaccount-domainaccountauthoptions-i-sys.md) | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## authWithPopup

```TypeScript
static authWithPopup(callback: IUserAuthCallback): void
```

Authenticates a domain account in a pop-up window.

**Since:** 10

**Required permissions:** 
- API version 10: ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## authWithPopup

```TypeScript
static authWithPopup(localId: number, callback: IUserAuthCallback): void
```

Authenticates a domain account in a pop-up window.

**Since:** 10

**Required permissions:** 
- API version 10: ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300101](../errorcode-account.md#12300101-incorrect-credential) |
| [12300109](../errorcode-account.md#12300109-authentication-credential-enrollment-or-update-canceled) |
| [12300110](../errorcode-account.md#12300110-authentication-locked) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300112](../errorcode-account.md#12300112-authentication-service-does-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## getAccessToken

```TypeScript
static getAccessToken(businessParams: Record<string, Object>, callback: AsyncCallback<Uint8Array>): void
```

Obtains the business access token of a domain account. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [businessParams](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Record & lt;string, Object & gt; | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## getAccessToken

```TypeScript
static getAccessToken(businessParams: Record<string, Object>): Promise<Uint8Array>
```

Obtains the business access token of a domain account. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [businessParams](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## getAccountInfo

```TypeScript
static getAccountInfo(options: GetDomainAccountInfoOptions, callback: AsyncCallback<DomainAccountInfo>): void
```

Obtains information about a specified domain account. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.GET_DOMAIN_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetDomainAccountInfoOptions](arkts-basicservices-osaccount-getdomainaccountinfooptions-i-sys.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## getAccountInfo

```TypeScript
static getAccountInfo(options: GetDomainAccountInfoOptions): Promise<DomainAccountInfo>
```

Obtains information about a specified domain account. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.GET_DOMAIN_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetDomainAccountInfoOptions](arkts-basicservices-osaccount-getdomainaccountinfooptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## hasAccount

```TypeScript
static hasAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<boolean>): void
```

Checks whether a domain account exists. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## hasAccount

```TypeScript
static hasAccount(domainAccountInfo: DomainAccountInfo): Promise<boolean>
```

Checks whether a domain account exists. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300013](../errorcode-account.md#12300013-network-exception) |
| [12300014](../errorcode-account.md#12300014-domain-account-not-authenticated) |
| [12300111](../errorcode-account.md#12300111-authentication-timed-out) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
| 12300211 |

## isAuthenticationExpired

```TypeScript
static isAuthenticationExpired(domainAccountInfo: DomainAccountInfo): Promise<boolean>
```

Checks whether the authentication of a domain account has expired. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## registerPlugin

```TypeScript
static registerPlugin(plugin: DomainPlugin): void
```

Registers a domain plug-in.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plugin | [DomainPlugin](arkts-basicservices-osaccount-domainplugin-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 12300201 |

## unregisterPlugin

```TypeScript
static unregisterPlugin(): void
```

Unregisters this domain plug-in.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## updateAccountToken

```TypeScript
static updateAccountToken(
      domainAccountInfo: DomainAccountInfo,
      token: Uint8Array,
      callback: AsyncCallback<void>
    ): void
```

Updates the token of a domain account. An empty token means an invalid token. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| token | Uint8Array | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## updateAccountToken

```TypeScript
static updateAccountToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array): Promise<void>
```

Updates the token of a domain account. An empty token means an invalid token. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| token | Uint8Array | Yes |

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
| [12300003](../errorcode-account.md#12300003-account-not-found) |
