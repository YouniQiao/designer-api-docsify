# Authenticator

Provides APIs to operate the authenticator.

**Since:** 8

<!--Device-appAccount-class Authenticator--><!--Device-appAccount-class Authenticator-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from '@kit.BasicServicesKit';
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

> **NOTE：**
> 
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [createAccountImplicitly](../../../reference/apis-basic-services-kit/js-apis-appAccount.md#createaccountimplicitly9-2)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createAccountImplicitly](appAccount.Authenticator.createAccountImplicitly(options:)

<!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

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

<!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void--><!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| authType | string | Yes |
| options | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |
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

> **NOTE：**
> 
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [auth](../../../reference/apis-basic-services-kit/js-apis-appAccount.md#auth9-2) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [auth](appAccount.Authenticator.auth(name:)

<!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

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

<!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| labels | Array & lt;string & gt; | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## checkAccountRemovable

```TypeScript
checkAccountRemovable(name: string, callback: AuthCallback): void
```

Checks whether an application account can be deleted. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## createAccountImplicitly

```TypeScript
createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

Creates an application account implicitly based on the specified account owner. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void--><!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void-End-->

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

<!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject--><!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject-End-->

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  verifyCredential(name: string,
    options: appAccount.VerifyCredentialOptions, callback: appAccount.AuthCallback) {
      let want: Want = {
        bundleName: 'com.example.accountjsdemo',
        abilityName: 'com.example.accountjsdemo.VerifyAbility',
        parameters: {
          name: name
        }
      };
      callback.onRequestRedirected(want);
  }

  setProperties(options: appAccount.SetPropertiesOptions, callback: appAccount.AuthCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.SetPropertiesAbility',
      parameters: {
        options: options
      }
    };
    callback.onRequestRedirected(want);
  }

  checkAccountLabels(name: string, labels: string[], callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }

  checkAccountRemovable(name: string, callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }
}

export default {
  onConnect(want: Want): rpc.RemoteObject { // serviceAbility lifecycle function, which needs to be placed in serviceAbility.
    let authenticator = new MyAuthenticator();
    return authenticator.getRemoteObject();
  }
}
```

## setProperties

```TypeScript
setProperties(options: SetPropertiesOptions, callback: AuthCallback): void
```

Sets the authenticator properties. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void--><!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## verifyCredential

```TypeScript
verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

Verifies the credential of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void--><!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | Yes |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.
