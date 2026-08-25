# Authenticator

Defines an authenticator.

**Since:** 8

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## addAccountImplicitly

```TypeScript
addAccountImplicitly(
      authType: string,
      callerBundleName: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

Adds an application account implicitly based on the specified authentication type and options. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [createAccountImplicitly](#createaccountimplicitly)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAccountImplicitly](#createaccountimplicitly)(options: CreateAccountImplicitlyOptions, callback: AuthCallback)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | string | Yes |
| callerBundleName | string | Yes |
| options | { [key: string]: any } | Yes |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| options | Record & lt;string, Object & gt; | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## authenticate

```TypeScript
authenticate(
      name: string,
      authType: string,
      callerBundleName: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

Authenticates an application account to obtain the OAuth token. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [auth](#auth)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [auth](#auth)(name: string, authType: string, options: Record&lt;string, Object&gt;, callback: AuthCallback)

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| callerBundleName | string | Yes |
| options | { [key: string]: any } | Yes |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void
```

Checks the account labels. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| labels | Array & lt;string & gt; | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## checkAccountRemovable

```TypeScript
checkAccountRemovable(name: string, callback: AuthCallback): void
```

Checks whether an application account can be deleted. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

Creates an application account implicitly based on the specified account owner. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## getRemoteObject

```TypeScript
getRemoteObject(): rpc.RemoteObject
```

Obtains the remote object of an authenticator. This API cannot be overloaded.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## setProperties

```TypeScript
setProperties(options: SetPropertiesOptions, callback: AuthCallback): void
```

Sets the authenticator properties. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## verifyCredential

```TypeScript
verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

Verifies the credential of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |
