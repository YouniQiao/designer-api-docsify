# UserAuth（系统接口）

用户认证类。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

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

认证当前用户。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |
| [12300105](../errorcode-account.md#12300105-可信等级不支持) |
| [12300106](../errorcode-account.md#12300106-认证类型不支持) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| [12300117](../errorcode-account.md#12300117-pin码过期) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-凭据已失效) |
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

基于指定的挑战值、认证类型（如口令、人脸、指纹等）、认证可信等级以及可选参数（如账号标识、认证意图等）进行身份认证。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |
| options | [AuthOptions](arkts-basicservices-osaccount-authoptions-i-sys.md) | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |
| [12300105](../errorcode-account.md#12300105-可信等级不支持) |
| [12300106](../errorcode-account.md#12300106-认证类型不支持) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| [12300117](../errorcode-account.md#12300117-pin码过期) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-凭据已失效) |
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

认证指定用户。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| challenge | Uint8Array | 是 |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300013](../errorcode-account.md#12300013-网络异常) |
| 12300020 |
| 12300090 |
| 12300091 |
| [12300101](../errorcode-account.md#12300101-凭据不正确) |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |
| [12300105](../errorcode-account.md#12300105-可信等级不支持) |
| [12300106](../errorcode-account.md#12300106-认证类型不支持) |
| [12300109](../errorcode-account.md#12300109-认证凭据录入更新等操作被取消) |
| [12300110](../errorcode-account.md#12300110-认证被锁定) |
| [12300111](../errorcode-account.md#12300111-认证超时) |
| [12300112](../errorcode-account.md#12300112-认证服务忙) |
| [12300113](../errorcode-account.md#12300113-认证服务不存在) |
| [12300114](../errorcode-account.md#12300114-认证服务异常) |
| [12300117](../errorcode-account.md#12300117-pin码过期) |
| 12300119 |
| [12300120](../errorcode-account.md#12300120-凭据已失效) |
| 12300211 |

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): void
```

取消指定的认证操作。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| contextID | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## constructor

```TypeScript
constructor()
```

创建用户认证的实例。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: AuthType, authTrustLevel: AuthTrustLevel): number
```

获取指定认证类型和认证可信等级的认证能力的可用状态。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| authTrustLevel | [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300117](../errorcode-account.md#12300117-pin码过期) |

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest, callback: AsyncCallback<ExecutorProperty>): void
```

基于指定的请求信息获取属性。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| 12300020 |

## getProperty

```TypeScript
getProperty(request: GetPropertyRequest): Promise<ExecutorProperty>
```

基于指定的请求信息获取属性。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| 12300020 |

## getPropertyByCredentialId

```TypeScript
getPropertyByCredentialId(credentialId: Uint8Array, keys: Array<GetPropertyType>): Promise<ExecutorProperty>
```

基于凭据id获取关联执行器的指定属性信息。使用Promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| credentialId | Uint8Array | 是 |
| keys | Array&lt;[GetPropertyType](arkts-basicservices-osaccount-getpropertytype-e-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| 12300020 |
| [12300102](../errorcode-account.md#12300102-凭据不存在) |

## getVersion

```TypeScript
getVersion(): number
```

返回版本信息。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## prepareRemoteAuth

```TypeScript
prepareRemoteAuth(remoteNetworkId: string): Promise<void>
```

准备远端认证。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| remoteNetworkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| 12300090 |
| 12300091 |
| [12300111](../errorcode-account.md#12300111-认证超时) |

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest, callback: AsyncCallback<void>): void
```

设置可用于初始化算法的属性。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## setProperty

```TypeScript
setProperty(request: SetPropertyRequest): Promise<void>
```

设置可用于初始化算法的属性。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) | 是 |

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
