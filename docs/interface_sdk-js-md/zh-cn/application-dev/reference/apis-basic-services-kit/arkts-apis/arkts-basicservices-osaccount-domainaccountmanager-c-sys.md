# DomainAccountManager

域账号管理类。

**起始版本：** 18

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## auth

```TypeScript
static auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void
```

认证指定的域账号。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| credential | Uint8Array | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## auth

```TypeScript
static auth(
      domainAccountInfo: DomainAccountInfo,
      credential: Uint8Array,
      options: DomainAccountAuthOptions,
      callback: IUserAuthCallback): void
```

认证指定的域账号，支持指定认证选项，如服务器参数。使用callback异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| credential | Uint8Array | 是 |
| options | [DomainAccountAuthOptions](arkts-basicservices-osaccount-domainaccountauthoptions-i-sys.md) | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## authWithPopup

```TypeScript
static authWithPopup(callback: IUserAuthCallback): void
```

弹框认证指定的域账号。

**起始版本：** 10

**需要权限：** 
- API版本10：ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## authWithPopup

```TypeScript
static authWithPopup(localId: number, callback: IUserAuthCallback): void
```

弹框认证指定的域账号。

**起始版本：** 10

**需要权限：** 
- API版本10：ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## getAccessToken

```TypeScript
static getAccessToken(businessParams: Record<string, Object>, callback: AsyncCallback<Uint8Array>): void
```

获取当前域账号的业务访问令牌。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [businessParams](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Record & lt;string, Object & gt; | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## getAccessToken

```TypeScript
static getAccessToken(businessParams: Record<string, Object>): Promise<Uint8Array>
```

查询当前域账号的业务访问令牌。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [businessParams](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## getAccountInfo

```TypeScript
static getAccountInfo(options: GetDomainAccountInfoOptions, callback: AsyncCallback<DomainAccountInfo>): void
```

查询指定的域账号信息。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.GET_DOMAIN_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GetDomainAccountInfoOptions](arkts-basicservices-osaccount-getdomainaccountinfooptions-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## getAccountInfo

```TypeScript
static getAccountInfo(options: GetDomainAccountInfoOptions): Promise<DomainAccountInfo>
```

查询指定的域账号信息。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.GET_DOMAIN_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GetDomainAccountInfoOptions](arkts-basicservices-osaccount-getdomainaccountinfooptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## hasAccount

```TypeScript
static hasAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<boolean>): void
```

检查是否存在指定的域账号。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## hasAccount

```TypeScript
static hasAccount(domainAccountInfo: DomainAccountInfo): Promise<boolean>
```

检查是否存在指定的域账号。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| [12300014](../errorcode-account.md#12300014-域账号未认证) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| 12300211 |

## isAuthenticationExpired

```TypeScript
static isAuthenticationExpired(domainAccountInfo: DomainAccountInfo): Promise<boolean>
```

判断指定域账号是否登录超期。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## registerPlugin

```TypeScript
static registerPlugin(plugin: DomainPlugin): void
```

注册域插件。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plugin | [DomainPlugin](arkts-basicservices-osaccount-domainplugin-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 12300201 |

## unregisterPlugin

```TypeScript
static unregisterPlugin(): void
```

注销域插件。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## updateAccountToken

```TypeScript
static updateAccountToken(
      domainAccountInfo: DomainAccountInfo,
      token: Uint8Array,
      callback: AsyncCallback<void>
    ): void
```

更新指定域账号的令牌，空令牌表示目标域账号的令牌失效。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| token | Uint8Array | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## updateAccountToken

```TypeScript
static updateAccountToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array): Promise<void>
```

更新指定域账号的令牌，空令牌表示目标域账号的令牌失效。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| token | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
