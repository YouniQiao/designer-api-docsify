# Authenticator

Provides APIs to operate the authenticator.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-appAccount-class Authenticator--><!--Device-appAccount-class Authenticator-End-->

**System capability:** SystemCapability.Account.AppAccount

## addAccountImplicitly

```TypeScript
addAccountImplicitly(
      authType: string,
      callerBundleName: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

Adds an application account implicitly based on the specified authentication type and options. This API uses an asynchronous callback to return the result. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ > instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Authenticator.createAccountImplicitly](arkts-basicservices-appaccount-authenticator-c.md#createaccountimplicitly)(options:

<!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | string | Yes | Authentication type. The custom type, The value cannot exceed 1024 characters. |
| callerBundleName | string | Yes | Bundle name of the authentication requester. |
| options | { [key: string]: any } | Yes | Options for the authentication. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void--><!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| authType | string | Yes | Authentication type. The custom type, The value cannot exceed 1024 characters. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Options for the authentication. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void
```

Authenticates an application account. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void--><!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| authType | string | Yes | Authentication type. The custom type, The value cannot exceed 1024 characters. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | Options for the authentication. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

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

Authenticates an application account to obtain the OAuth token. This API uses an asynchronous callback to return the result. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Authenticator.auth](arkts-basicservices-appaccount-authenticator-c.md#auth)(name:

<!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| authType | string | Yes | Authentication type. The custom type, The value cannot exceed 1024 characters. |
| callerBundleName | string | Yes | Bundle name of the authentication requester. |
| options | { [key: string]: any } | Yes | Options for the authentication. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void
```

Checks the account labels. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| labels | Array&lt;string&gt; | Yes | Labels to check. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

**Example**

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## checkAccountRemovable

```TypeScript
checkAccountRemovable(name: string, callback: AuthCallback): void
```

Checks whether an application account can be deleted. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

**Example**

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## createAccountImplicitly

```TypeScript
createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

Creates an application account implicitly based on the specified account owner. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void--><!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options for implicitly creating the account. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

## getRemoteObject

```TypeScript
getRemoteObject(): rpc.RemoteObject
```

Obtains the remote object of an authenticator. This API cannot be overloaded.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject--><!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject-End-->

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | Remote object of the authenticator, which is used for inter-process communication. |

**Example**

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void--><!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator properties to set. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

**Example**

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## verifyCredential

```TypeScript
verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

Verifies the credential of an application account. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void--><!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the application account. The value cannot exceed 512 characters. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options for credential verification. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authenticator callback used to return the result. |

**Example**

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

