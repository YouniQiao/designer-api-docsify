# AppAccountManager

Defines the application account manager, which is used to manage account information of applications.

**Since:** 7

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## addAccount

```TypeScript
addAccount(name: string, callback: AsyncCallback<void>): void
```

Adds an application account with the given name. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [createAccount](#createaccount)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createAccount](#createaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## addAccount

```TypeScript
addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

Adds an application account name and additional information. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [createAccount](#createaccount)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createAccount](#createaccount)(name: string, options: CreateAccountOptions, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| extraInfo | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## addAccount

```TypeScript
addAccount(name: string, extraInfo?: string): Promise<void>
```

Adds an application account name and additional information. This API uses a promise to return the result.

> **NOTE：**
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [createAccount](#createaccount)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createAccount](#createaccount)(name: string, options?: CreateAccountOptions)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| extraInfo | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## addAccountImplicitly

```TypeScript
addAccountImplicitly(
      owner: string,
      authType: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

Adds an application account implicitly based on the specified owner. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [createAccountImplicitly](#createaccountimplicitly)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAccountImplicitly](#createaccountimplicitly)(owner: string, callback: AuthCallback)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| authType | string | Yes |
| options | { [key: string]: any } | Yes |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes |

## auth

```TypeScript
auth(name: string, owner: string, authType: string, callback: AuthCallback): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## auth

```TypeScript
auth(
      name: string,
      owner: string,
      authType: string,
      options: Record<string, Object>,
      callback: AuthCallback
    ): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| options | Record & lt;string, Object & gt; | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## authenticate

```TypeScript
authenticate(
      name: string,
      owner: string,
      authType: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [auth](#auth)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [auth](#auth)(name: string, owner: string, authType: string, callback: AuthCallback)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| options | { [key: string]: any } | Yes |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void
```

Checks whether an application account has specific labels. This API uses an asynchronous callback to return the result. The labels are checked by the authenticator of the target application.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| labels | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>
```

Checks whether an application account has specific labels. This API uses a promise to return the result. The labels are checked by the authenticator of the target application.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| labels | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

Checks whether the caller can access the account data that belongs to the target application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string): Promise<boolean>
```

Checks whether the caller can access the account data that belongs to the target application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void
```

Checks whether data synchronization is enabled for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkDataSyncEnabled](#checkdatasyncenabled)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string): Promise<boolean>
```

Checks whether data synchronization is enabled for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkDataSyncEnabled](#checkdatasyncenabled) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

Checks the visibility of an authorization token of the specified authentication type to an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

Checks the visibility of an authorization token of the specified authentication type to an application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void
```

Checks whether data synchronization is enabled for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string): Promise<boolean>
```

Checks whether data synchronization is enabled for an application account. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      callback: AsyncCallback<boolean>
    ): void
```

Checks the visibility of an authorization token of the specified authentication type to an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [checkAuthTokenVisibility](#checkauthtokenvisibility)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string, callback: AsyncCallback&lt;boolean&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

Checks the visibility of an authorization token of the specified authentication type to an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [checkAuthTokenVisibility](#checkauthtokenvisibility)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## createAccount

```TypeScript
createAccount(name: string, callback: AsyncCallback<void>): void
```

Creates an application account with the given name. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300004](../errorcode-account.md#12300004-account-already-exists) |
| [12300007](../errorcode-account.md#12300007-account-count-reached-the-limit) |

## createAccount

```TypeScript
createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void
```

Creates an application account with custom data. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300004](../errorcode-account.md#12300004-account-already-exists) |
| [12300007](../errorcode-account.md#12300007-account-count-reached-the-limit) |

## createAccount

```TypeScript
createAccount(name: string, options?: CreateAccountOptions): Promise<void>
```

Creates an application account with custom data. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300004](../errorcode-account.md#12300004-account-already-exists) |
| [12300007](../errorcode-account.md#12300007-account-count-reached-the-limit) |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, callback: AuthCallback): void
```

Creates an application account automatically by the authenticator based on the specified owner. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300007](../errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

Creates an application account automatically by the authenticator based on the specified account owner and options. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300007](../errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## deleteAccount

```TypeScript
deleteAccount(name: string, callback: AsyncCallback<void>): void
```

Deletes an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [removeAccount](#removeaccount)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeAccount](#removeaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## deleteAccount

```TypeScript
deleteAccount(name: string): Promise<void>
```

Deletes an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [removeAccount](#removeaccount)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeAccount](#removeaccount)(name: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

Deletes the authorization token of the specified authentication type for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| token | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

Deletes the authorization token of the specified authentication type for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void
```

Deletes the credential for the specified type of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string): Promise<void>
```

Deletes the credential for the specified type of an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

Deletes the authorization token of the specified authentication type for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [deleteAuthToken](#deleteauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| token | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

Deletes the authorization token of the specified authentication type for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [deleteAuthToken](#deleteauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

Disables access to the third-party application with the specified package name using the specified third-party application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setAppAccess](#setappaccess)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string): Promise<void>
```

Disables an application account from accessing an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setAppAccess](#setappaccess)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

Enables an application to access an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setAppAccess](#setappaccess)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string): Promise<void>
```

Enables an application to access an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setAppAccess](#setappaccess)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

Obtains the credential of an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCredential](#getcredential)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCredential](#getcredential)(name: string, credentialType: string, callback: AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string): Promise<string>
```

Obtains the credential of an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCredential](#getcredential)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCredential](#getcredential)(name: string, credentialType: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void
```

Obtains additional information of an application account. Additional information refers to other information that can be converted to the string type. It cannot contain sensitive information, such as the application account password and token. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCustomData](#getcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string): Promise<string>
```

Obtains additional information of an application account. Additional information refers to other information that can be converted to the string type. It cannot contain sensitive information, such as the application account password and token. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCustomData](#getcustomdata) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCustomData](#getcustomdata)(name: string, key: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

Obtains the application accounts that can be accessed by the invoker based on the application account owner. This API uses an asynchronous callback to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications or have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>
```

Obtains the application accounts that can be accessed by the invoker based on the application account owner. This API uses a promise to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications or have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

Obtains information about all accessible application accounts. This API uses an asynchronous callback to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getAllAccounts](#getallaccounts)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAllAccounts](#getallaccounts)(callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_ALL_APP_ACCOUNTS

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>
```

Obtains information about all accessible application accounts. This API uses a promise to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getAllAccounts](#getallaccounts) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAllAccounts](#getallaccounts)()

**Required permissions:** ohos.permission.GET_ALL_APP_ACCOUNTS

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

## getAllAccounts

```TypeScript
getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

Obtains information about all accessible application accounts. This API uses an asynchronous callback to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications or have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getAllAccounts

```TypeScript
getAllAccounts(): Promise<Array<AppAccountInfo>>
```

Obtains information about all accessible application accounts. This API uses a promise to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications or have gained the ohos.permission.GET_ALL_APP_ACCOUNTS permission.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getAllAccounts

```TypeScript
getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

Obtains the application accounts that can be accessed by the invoker based on the application account owner. This API uses an asynchronous callback to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getAccountsByOwner](#getaccountsbyowner)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAccountsByOwner](#getaccountsbyowner)(owner: string, callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**Required permissions:** ohos.permission.GET_ALL_APP_ACCOUNTS

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

## getAllAccounts

```TypeScript
getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>
```

Obtains the application accounts that can be accessed by the invoker based on the application account owner. This API uses a promise to return the result. This method applies to the following accounts: Accounts of this application. Accounts of third-party applications. To obtain such information, your application must have gained authorization from the third-party applications.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getAccountsByOwner](#getaccountsbyowner) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAccountsByOwner](#getaccountsbyowner)(owner: string)

**Required permissions:** ohos.permission.GET_ALL_APP_ACCOUNTS

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void
```

Obtains all tokens visible to the invoker for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>
```

Obtains all tokens visible to the invoker for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void
```

Obtains all tokens visible to the invoker for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAllAuthTokens](#getallauthtokens)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string, callback: AsyncCallback&lt;Array&lt;AuthTokenInfo&gt;&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; | Yes |

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>
```

Obtains all tokens visible to the invoker for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAllAuthTokens](#getallauthtokens) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; |

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void
```

Obtains the associated data of an application account based on the specified key. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCustomData](#getcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string): Promise<string>
```

Obtains data to be associated with an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getCustomData](#getcustomdata) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCustomData](#getcustomdata)(name: string, key: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void
```

Obtains the authenticator callback for an authentication session. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300108](../errorcode-account.md#12300108-authentication-session-not-found) |

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string): Promise<AuthCallback>
```

Obtains the authenticator callback for an authentication session. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300108](../errorcode-account.md#12300108-authentication-session-not-found) |

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void
```

Obtains the authenticator callback for an authentication session. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthCallback](#getauthcallback)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthCallback](#getauthcallback)(sessionId: string, callback: AsyncCallback&lt;AuthCallback&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; | Yes |

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>
```

Obtains the authenticator callback for an authentication session. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthCallback](#getauthcallback) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthCallback](#getauthcallback)(sessionId: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; |

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

Obtains the authenticator information of an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [queryAuthenticatorInfo](#queryauthenticatorinfo)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string, callback: AsyncCallback&lt;AuthenticatorInfo&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | Yes |

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

Obtains the authenticator information of an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [queryAuthenticatorInfo](#queryauthenticatorinfo) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

## getAuthList

```TypeScript
getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

Obtains the authorization list of the specified authentication type for an application account. The authorization list contains all authorized bundles. The token authorization list is set by [setAuthTokenVisibility](#setauthtokenvisibility). This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## getAuthList

```TypeScript
getAuthList(name: string, authType: string): Promise<Array<string>>
```

Obtains the authorization list of the specified authentication type for an application account. The authorization list contains all authorized bundles. The token authorization list is set by [setAuthTokenVisibility](#setauthtokenvisibility). This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

Obtains the authorization token of the specified authentication type for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string): Promise<string>
```

Obtains the authorization token of the specified authentication type for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |

## getCredential

```TypeScript
getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

Obtains the credential of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## getCredential

```TypeScript
getCredential(name: string, credentialType: string): Promise<string>
```

Obtains the credential of an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300102](../errorcode-account.md#12300102-credential-not-found) |

## getCustomData

```TypeScript
getCustomData(name: string, key: string, callback: AsyncCallback<string>): void
```

Obtains the custom data of an application account based on the specified key. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400002](../errorcode-account.md#12400002-custom-data-not-found) |

## getCustomData

```TypeScript
getCustomData(name: string, key: string): Promise<string>
```

Obtains the custom data of an application account based on the specified key. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400002](../errorcode-account.md#12400002-custom-data-not-found) |

## getCustomDataSync

```TypeScript
getCustomDataSync(name: string, key: string): string
```

Obtains the custom data of an application account based on the specified key. The API returns the result synchronously.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400002](../errorcode-account.md#12400002-custom-data-not-found) |

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

Obtains the authorization list of the specified authentication type for an application account. The authorization list contains all authorized bundles. The token authorization list is set by [setOAuthTokenVisibility](#setoauthtokenvisibility). This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthList](#getauthlist)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthList](#getauthlist)(name: string, authType: string, callback: AsyncCallback&lt;Array&lt;string&gt;&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string): Promise<Array<string>>
```

Obtains the authorization list of the specified authentication type for an application account. The authorization list contains all authorized bundles. The token authorization list is set by [setOAuthTokenVisibility](#setoauthtokenvisibility). This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthList](#getauthlist) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthList](#getauthlist)(name: string, authType: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

Obtains the authorization token of the specified authentication type for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthToken](#getauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string, callback: AsyncCallback&lt;string&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string): Promise<string>
```

Obtains the authorization token of the specified authentication type for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getAuthToken](#getauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| authType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void
```

Unsubscribes from account information changes.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> off('accountChange')
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [off](#offaccountchange)(type: 'accountChange', callback?: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | No |

## off('accountChange')

```TypeScript
off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void
```

Unsubscribes from account information changes.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'accountChange' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## on('change')

```TypeScript
on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

Subscribes to account information changes of apps.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> on('accountChange')
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [on](#onaccountchange)(type: 'accountChange', owners: Array&lt;string&gt;, callback: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| owners | Array & lt;string & gt; | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

## on('accountChange')

```TypeScript
on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

Subscribes to account information changes of apps.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'accountChange' | Yes |
| owners | Array & lt;string & gt; | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

Obtains the authenticator information of an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

Obtains the authenticator information of an application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |

## removeAccount

```TypeScript
removeAccount(name: string, callback: AsyncCallback<void>): void
```

Removes an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## removeAccount

```TypeScript
removeAccount(name: string): Promise<void>
```

Removes an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

Selects the accounts that can be accessed by the invoker based on the options. This API uses an asynchronous callback to return the result. If the options contain label constraints, the authenticator of the target application provides the capability of checking the labels.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>
```

Selects the accounts that can be accessed by the invoker based on the options. This API uses a promise to return the result. If the options contain label constraints, the authenticator of the target application provides the capability of checking the labels.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void
```

Sets a credential for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCredential](#setcredential)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCredential](#setcredential)(name: string, credentialType: string, credential: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| credential | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>
```

Sets a credential for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCredential](#setcredential)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCredential](#setcredential)(name: string, credentialType: string, credential: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| credential | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

Sets additional information for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCustomData](#setcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| extraInfo | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string): Promise<void>
```

Sets additional information for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCustomData](#setcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| extraInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void
```

Sets the access to the data of an account for an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |
| isAccessible | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |
| [12400005](../errorcode-account.md#12400005-bundles-in-the-oauth-list-reached-the-limit) |

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>
```

Sets the access to the data of an account for an application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| bundleName | string | Yes |
| isAccessible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |
| [12400005](../errorcode-account.md#12400005-bundles-in-the-oauth-list-reached-the-limit) |

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void
```

Sets data synchronization for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setDataSyncEnabled](#setdatasyncenabled)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| isEnable | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>
```

Sets data synchronization for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setDataSyncEnabled](#setdatasyncenabled)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| isEnable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

Sets data to be associated with an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCustomData](#setcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string): Promise<void>
```

Sets data to be associated with an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setCustomData](#setcustomdata)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, callback: AuthCallback): void
```

Sets the authenticator attributes of an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void
```

Sets the authenticator attributes of an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| owner | string | Yes |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

Sets an authorization token of the specific authentication type for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| token | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400004](../errorcode-account.md#12400004-token-count-reached-the-limit) |

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string): Promise<void>
```

Sets an authorization token of the specific authentication type for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400004](../errorcode-account.md#12400004-token-count-reached-the-limit) |

## setAuthTokenVisibility

```TypeScript
setAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      isVisible: boolean,
      callback: AsyncCallback<void>
    ): void
```

Sets the visibility of an authorization token to an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| isVisible | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |
| [12400005](../errorcode-account.md#12400005-bundles-in-the-oauth-list-reached-the-limit) |

## setAuthTokenVisibility

```TypeScript
setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

Sets the visibility of an authorization token to an application. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| isVisible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300107](../errorcode-account.md#12300107-authentication-type-not-found) |
| [12400001](../errorcode-account.md#12400001-application-not-found) |
| [12400005](../errorcode-account.md#12400005-bundles-in-the-oauth-list-reached-the-limit) |

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string,
                             callback: AsyncCallback<void>): void
```

Sets a credential for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| credential | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string): Promise<void>
```

Sets a credential for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| credentialType | string | Yes |
| credential | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

Sets custom data for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400003](../errorcode-account.md#12400003-custom-data-records-reached-the-limit) |

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string): Promise<void>
```

Sets custom data for an application account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12400003](../errorcode-account.md#12400003-custom-data-records-reached-the-limit) |

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

Sets data synchronization for an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| isEnabled | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>
```

Sets data synchronization for an application account. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| isEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

Sets an authorization token of the specific authentication type for an application account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [setAuthToken](#setauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| token | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string): Promise<void>
```

Sets an authorization token of the specific authentication type for an application account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [setAuthToken](#setauthtoken)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setOAuthTokenVisibility

```TypeScript
setOAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      isVisible: boolean,
      callback: AsyncCallback<void>
    ): void
```

Sets the visibility of an authorization token to an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [setAuthTokenVisibility](#setauthtokenvisibility)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setAuthTokenVisibility](#setauthtokenvisibility)( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback&lt;void&gt; )

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| isVisible | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setOAuthTokenVisibility

```TypeScript
setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

Sets the visibility of an authorization token to an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [setAuthTokenVisibility](#setauthtokenvisibility)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setAuthTokenVisibility](#setauthtokenvisibility)(name: string, authType: string, bundleName: string, isVisible: boolean)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| bundleName | string | Yes |
| isVisible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, callback: AuthCallback): void
```

Verifies the validity of a specified account credential. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

Verifies the credential of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| owner | string | Yes |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300113](../errorcode-account.md#12300113-authentication-service-not-found) |
| [12300114](../errorcode-account.md#12300114-authentication-service-abnormal) |
