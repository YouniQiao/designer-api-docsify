# Authenticator

认证器基类。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-appAccount-class Authenticator--><!--Device-appAccount-class Authenticator-End-->

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

根据指定的鉴权类型和可选项，隐式地添加应用账号。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持, 从API version 9开始废弃。建议使用[createAccountImplicitly](#createaccountimplicitly9-2)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Authenticator.createAccountImplicitly](arkts-basicservices-appaccount-authenticator-c.md#createaccountimplicitly)(options:

<!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-addAccountImplicitly(      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | string | Yes | 应用账号的鉴权类型。自定义数据，最大长度为1024个字符。 |
| callerBundleName | string | Yes | 鉴权请求方的包名。 |
| options | { [key: string]: any } | Yes | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void--><!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| authType | string | Yes | 应用账号的鉴权类型。自定义数据，最大长度为1024个字符。 |
| options | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes | 鉴权所需要的可选项。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void--><!--Device-Authenticator-auth(name: string, authType: string, options: Record<string, RecordData>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| authType | string | Yes | 应用账号的鉴权类型。自定义数据，最大长度为1024个字符。 |
| options | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 鉴权所需要的可选项。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

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

对应用账号进行鉴权，获取OAuth令牌。使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持, 从API version 9开始废弃。建议使用[auth](#auth9-2)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.Authenticator.auth](arkts-basicservices-appaccount-authenticator-c.md#auth)(name:

<!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-Authenticator-authenticate(      name: string,      authType: string,      callerBundleName: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| authType | string | Yes | 应用账号的鉴权类型。自定义数据，最大长度为1024个字符。 |
| callerBundleName | string | Yes | 鉴权请求方的包名。 |
| options | { [key: string]: any } | Yes | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void
```

检查账号标签。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| labels | Array&lt;string&gt; | Yes | 标签数组。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## checkAccountRemovable

```TypeScript
checkAccountRemovable(name: string, callback: AuthCallback): void
```

判断账号是否可以删除。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void--><!--Device-Authenticator-checkAccountRemovable(name: string, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## createAccountImplicitly

```TypeScript
createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void--><!--Device-Authenticator-createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | Yes | 隐式创建账号的选项。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调对象，用于返回创建结果。 |

## getRemoteObject

```TypeScript
getRemoteObject(): rpc.RemoteObject
```

获取认证器的远程对象，不可以重载实现。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject--><!--Device-Authenticator-getRemoteObject(): rpc.RemoteObject-End-->

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | 认证器Authenticator的远程对象。用于跨进程通信。 |

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

设置认证器属性。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void--><!--Device-Authenticator-setProperties(options: SetPropertiesOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | Yes | 设置属性的可选项。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

## verifyCredential

```TypeScript
verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

验证应用账号的凭据。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void--><!--Device-Authenticator-verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 应用账号的名称。最大长度为512个字符。 |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | Yes | 验证凭据的可选项。 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | Yes | 认证器回调，用于返回鉴权结果。 |

## Examples

This API must be used together with the getRemoteObject API. For details, see the example of the [getRemoteObject](#getremoteobject9) API.

