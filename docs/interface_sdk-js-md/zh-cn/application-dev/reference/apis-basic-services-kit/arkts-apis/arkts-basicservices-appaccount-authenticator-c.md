# Authenticator

认证器基类。

**起始版本：** 8

**系统能力：** SystemCapability.Account.AppAccount

## 导入模块

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

> **说明：**&gt;
> 从API version 8开始支持, 从API version 9开始废弃。建议使用[createAccountImplicitly](#createaccountimplicitly)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createAccountImplicitly](#createaccountimplicitly)(options: CreateAccountImplicitlyOptions, callback: AuthCallback)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | string | 是 |
| callerBundleName | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

## auth

```TypeScript
auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| options | Record & lt;string, Object & gt; | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

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

> **说明：**&gt;
> 从API version 8开始支持, 从API version 9开始废弃。建议使用[auth](#auth)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [auth](#auth)(name: string, authType: string, options: Record&lt;string, Object&gt;, callback: AuthCallback)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| callerBundleName | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void
```

检查账号标签。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| labels | Array & lt;string & gt; | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

## checkAccountRemovable

```TypeScript
checkAccountRemovable(name: string, callback: AuthCallback): void
```

判断账号是否可以删除。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

## getRemoteObject

```TypeScript
getRemoteObject(): rpc.RemoteObject
```

获取认证器的远程对象，不可以重载实现。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 |
| --- |
| rpc.RemoteObject |

## setProperties

```TypeScript
setProperties(options: SetPropertiesOptions, callback: AuthCallback): void
```

设置认证器属性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

## verifyCredential

```TypeScript
verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

验证应用账号的凭据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |
