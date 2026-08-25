# AppAccountManager

应用账号管理器，可用于管理应用自身的账号信息。

**起始版本：** 7

**系统能力：** SystemCapability.Account.AppAccount

## 导入模块

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## addAccount

```TypeScript
addAccount(name: string, callback: AsyncCallback<void>): void
```

根据账号名添加应用账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [createAccount](#createaccount)替
> 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## addAccount

```TypeScript
addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

根据账号名和额外信息添加应用账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [createAccount](#createaccount)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, options: CreateAccountOptions, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## addAccount

```TypeScript
addAccount(name: string, extraInfo?: string): Promise<void>
```

根据账号名和额外信息添加应用账号。使用Promise异步回调。

> **说明：**
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [createAccount](#createaccount)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, options?: CreateAccountOptions)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 否 |

**返回值：**

| 类型 |
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

根据指定的账号所有者隐式地添加应用账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [createAccountImplicitly](#createaccountimplicitly)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createAccountImplicitly](#createaccountimplicitly)(owner: string, callback: AuthCallback)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| authType | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

## auth

```TypeScript
auth(name: string, owner: string, authType: string, callback: AuthCallback): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

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

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| options | Record & lt;string, Object & gt; | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

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

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [auth](#auth)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [auth](#auth)(name: string, owner: string, authType: string, callback: AuthCallback)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否满足特定的标签集合。使用callback异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| labels | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>
```

检查指定应用账号是否满足特定的标签集合。使用Promise异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| labels | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

检查指定应用对特定账号的数据是否可访问。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string): Promise<boolean>
```

检查指定应用对特定账号的数据是否可访问。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkDataSyncEnabled](#checkdatasyncenabled)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string, callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string): Promise<boolean>
```

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkDataSyncEnabled](#checkdatasyncenabled)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string): Promise<boolean>
```

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      callback: AsyncCallback<boolean>
    ): void
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [checkAuthTokenVisibility](#checkauthtokenvisibility)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [checkAuthTokenVisibility](#checkauthtokenvisibility)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## createAccount

```TypeScript
createAccount(name: string, callback: AsyncCallback<void>): void
```

根据账号名创建应用账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |

## createAccount

```TypeScript
createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void
```

根据账号名和可选项创建应用账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |

## createAccount

```TypeScript
createAccount(name: string, options?: CreateAccountOptions): Promise<void>
```

根据账号名和可选项创建应用账号。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, callback: AuthCallback): void
```

根据指定的账号所有者，由认证器自动完成应用账号创建流程。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

根据指定的账号所有者和可选项，由认证器自动完成应用账号创建流程。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## deleteAccount

```TypeScript
deleteAccount(name: string, callback: AsyncCallback<void>): void
```

删除应用账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [removeAccount](#removeaccount)替
> 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeAccount](#removeaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## deleteAccount

```TypeScript
deleteAccount(name: string): Promise<void>
```

删除应用账号。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [removeAccount](#removeaccount)替
> 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeAccount](#removeaccount)(name: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定类型的凭据信息。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string): Promise<void>
```

删除指定应用账号的特定类型的凭据信息。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [deleteAuthToken](#deleteauthtoken)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [deleteAuthToken](#deleteauthtoken)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

禁止指定第三方应用账号对指定包名称的第三方应用进行访问。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setAppAccess](#setappaccess)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string): Promise<void>
```

禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setAppAccess](#setappaccess)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

允许指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setAppAccess](#setappaccess)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string): Promise<void>
```

允许指定第三方应用账号的名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setAppAccess](#setappaccess)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的凭据。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCredential](#getcredential)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCredential](#getcredential)(name: string, credentialType: string, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string): Promise<string>
```

获取指定应用账号的凭据。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCredential](#getcredential)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCredential](#getcredential)(name: string, credentialType: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCustomData](#getcustomdata)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string): Promise<string>
```

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCustomData](#getcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权，或 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权，或 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

获取所有可访问的应用账号信息。使用callback异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getAllAccounts](#getallaccounts)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllAccounts](#getallaccounts)(callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>
```

获取所有可访问的应用账号信息。使用Promise异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#getallaccounts)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllAccounts](#getallaccounts)()

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

## getAllAccounts

```TypeScript
getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

获取所有可访问的应用账号信息。使用callback异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权，或 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getAllAccounts

```TypeScript
getAllAccounts(): Promise<Array<AppAccountInfo>>
```

获取所有可访问的应用账号信息。使用Promise异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权，或 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getAllAccounts

```TypeScript
getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getAccountsByOwner](#getaccountsbyowner)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccountsByOwner](#getaccountsbyowner)(owner: string, callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

## getAllAccounts

```TypeScript
getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。 此方法适用于以下账户： 本应用的账户。 第三方应用的账户。要获取此类信息， 您的应用必须已获得第三方应用的授权。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getAccountsByOwner](#getaccountsbyowner)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccountsByOwner](#getaccountsbyowner)(owner: string)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void
```

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>
```

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void
```

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAllAuthTokens](#getallauthtokens)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string, callback: AsyncCallback&lt;Array&lt;AuthTokenInfo&gt;&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; | 是 |

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>
```

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAllAuthTokens](#getallauthtokens)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; |

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void
```

根据指定键名获取特定应用账号的关联数据。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCustomData](#getcustomdata)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string): Promise<string>
```

获取指定应用账号的关联数据。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getCustomData](#getcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void
```

获取鉴权会话的认证器回调对象。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300108](../errorcode-account.md#12300108-认证会话不存在) |

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string): Promise<AuthCallback>
```

获取鉴权会话的认证器回调对象。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300108](../errorcode-account.md#12300108-认证会话不存在) |

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void
```

获取鉴权会话的认证器回调。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthCallback](#getauthcallback)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthCallback](#getauthcallback)(sessionId: string, callback: AsyncCallback&lt;AuthCallback&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; | 是 |

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>
```

获取鉴权会话的认证器回调。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthCallback](#getauthcallback)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthCallback](#getauthcallback)(sessionId: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; |

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

获取指定应用的认证器信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [queryAuthenticatorInfo](#queryauthenticatorinfo)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string, callback: AsyncCallback&lt;AuthenticatorInfo&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | 是 |

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

获取指定应用的认证器信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [queryAuthenticatorInfo](#queryauthenticatorinfo)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

## getAuthList

```TypeScript
getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setAuthTokenVisibility](#setauthtokenvisibility) 来设置）。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## getAuthList

```TypeScript
getAuthList(name: string, authType: string): Promise<Array<string>>
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setAuthTokenVisibility](#setauthtokenvisibility) 来设置）。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string): Promise<string>
```

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |

## getCredential

```TypeScript
getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的凭据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |

## getCredential

```TypeScript
getCredential(name: string, credentialType: string): Promise<string>
```

获取指定应用账号的凭据。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |

## getCustomData

```TypeScript
getCustomData(name: string, key: string, callback: AsyncCallback<string>): void
```

根据指定键名获取特定应用账号的自定义数据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400002](../errorcode-account.md#12400002-自定义数据不存在) |

## getCustomData

```TypeScript
getCustomData(name: string, key: string): Promise<string>
```

根据指定键名获取特定应用账号的自定义数据。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400002](../errorcode-account.md#12400002-自定义数据不存在) |

## getCustomDataSync

```TypeScript
getCustomDataSync(name: string, key: string): string
```

根据指定键名获取特定应用账号的自定义数据。使用同步方式返回结果。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400002](../errorcode-account.md#12400002-自定义数据不存在) |

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setOAuthTokenVisibility](#setoauthtokenvisibility) 来设置）。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthList](#getauthlist)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthList](#getauthlist)(name: string, authType: string, callback: AsyncCallback&lt;Array&lt;string&gt;&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string): Promise<Array<string>>
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setOAuthTokenVisibility](#setoauthtokenvisibility) 来设置）。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthList](#getauthlist)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthList](#getauthlist)(name: string, authType: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthToken](#getauthtoken)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string): Promise<string>
```

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getAuthToken](#getauthtoken)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void
```

取消订阅账号信息变更事件。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> off('accountChange')
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [off](#offaccountchange)(type: 'accountChange', callback?: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 否 |

## off('accountChange')

```TypeScript
off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void
```

取消订阅账号信息变更事件。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'accountChange' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## on('change')

```TypeScript
on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

订阅指定应用的账号信息变更事件。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> on('accountChange')
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [on](#onaccountchange)(type: 'accountChange', owners: Array&lt;string&gt;, callback: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| owners | Array & lt;string & gt; | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

## on('accountChange')

```TypeScript
on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

订阅指定应用的账号信息变更事件。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'accountChange' | 是 |
| owners | Array & lt;string & gt; | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

获取指定应用的认证器信息。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

获取指定应用的认证器信息。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |

## removeAccount

```TypeScript
removeAccount(name: string, callback: AsyncCallback<void>): void
```

删除应用账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## removeAccount

```TypeScript
removeAccount(name: string): Promise<void>
```

删除应用账号。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>
```

根据选项选择调用方可访问的账号列表。使用Promise异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的凭据。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [setCredential](#setcredential)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCredential](#setcredential)(name: string, credentialType: string, credential: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>
```

设置指定应用账号的凭据。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [setCredential](#setcredential)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCredential](#setcredential)(name: string, credentialType: string, credential: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的额外信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setCustomData](#setcustomdata)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string): Promise<void>
```

设置指定应用账号的额外信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setCustomData](#setcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void
```

设置指定应用对特定账号的数据访问权限。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| isAccessible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |
| [12400005](../errorcode-account.md#12400005-授权列表已达上限) |

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>
```

设置指定应用对特定账号的数据访问权限。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| isAccessible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |
| [12400005](../errorcode-account.md#12400005-授权列表已达上限) |

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void
```

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setDataSyncEnabled](#setdatasyncenabled)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnable | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>
```

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setDataSyncEnabled](#setdatasyncenabled)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的关联数据。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setCustomData](#setcustomdata)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string): Promise<void>
```

设置指定应用账号的关联数据。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setCustomData](#setcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, callback: AuthCallback): void
```

设置指定应用的认证器属性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void
```

设置指定应用的认证器属性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400004](../errorcode-account.md#12400004-令牌数量已达上限) |

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string): Promise<void>
```

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400004](../errorcode-account.md#12400004-令牌数量已达上限) |

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

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |
| [12400005](../errorcode-account.md#12400005-授权列表已达上限) |

## setAuthTokenVisibility

```TypeScript
setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300107](../errorcode-account.md#12300107-认证类型不存在) |
| [12400001](../errorcode-account.md#12400001-应用不存在) |
| [12400005](../errorcode-account.md#12400005-授权列表已达上限) |

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string,
                             callback: AsyncCallback<void>): void
```

设置指定应用账号的凭据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string): Promise<void>
```

设置指定应用账号的凭据。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的自定义数据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400003](../errorcode-account.md#12400003-自定义数据的数量已达上限) |

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string): Promise<void>
```

设置指定应用账号的自定义数据。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12400003](../errorcode-account.md#12400003-自定义数据的数量已达上限) |

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnabled | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>
```

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [setAuthToken](#setauthtoken)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string): Promise<void>
```

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [setAuthToken](#setauthtoken)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
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

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [setAuthTokenVisibility](#setauthtokenvisibility)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthTokenVisibility](#setauthtokenvisibility)( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback&lt;void&gt; )

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setOAuthTokenVisibility

```TypeScript
setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [setAuthTokenVisibility](#setauthtokenvisibility)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthTokenVisibility](#setauthtokenvisibility)(name: string, authType: string, bundleName: string, isVisible: boolean)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, callback: AuthCallback): void
```

验证指定账号的凭据有效性。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

验证指定账号的凭据。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
