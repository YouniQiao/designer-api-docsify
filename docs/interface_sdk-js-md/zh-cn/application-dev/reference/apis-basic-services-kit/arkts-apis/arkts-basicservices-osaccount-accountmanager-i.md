# AccountManager

系统账号管理类。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void
```

判断是否支持多系统账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(): Promise<boolean>
```

判断是否支持多系统账号。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void
```

判断指定系统账号是否处于激活状态。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number): Promise<boolean>
```

判断指定系统账号是否处于激活状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

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

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

判断指定系统账号是否具有指定约束。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>
```

判断指定系统账号是否具有指定约束。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |

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

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(callback: AsyncCallback<boolean>): void
```

检查当前系统账号是否为测试账号。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(): Promise<boolean>
```

检查当前系统账号是否为测试账号。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(callback: AsyncCallback<boolean>): void
```

检查当前系统账号是否已认证解锁。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。建议使用
> [isOsAccountUnlocked](#isosaccountunlocked)替代。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [isOsAccountUnlocked](#isosaccountunlocked)()

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(): Promise<boolean>
```

检查当前系统账号是否已认证解锁。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。建议使用
> [isOsAccountUnlocked](#isosaccountunlocked)替代。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [isOsAccountUnlocked](#isosaccountunlocked)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

检查指定系统账号是否已验证。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number): Promise<boolean>
```

检查指定系统账号是否已验证。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

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

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void
```

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(): Promise<Array<number>>
```

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(callback: AsyncCallback<number>): void
```

获取已创建的系统账号数量。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountCount](#getosaccountcount)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountCount](#getosaccountcount)(callback: AsyncCallback&lt;int&gt;)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(): Promise<number>
```

获取已创建的系统账号数量。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountCount](#getosaccountcount)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountCount](#getosaccountcount)()

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

查询当前进程所属的系统账号的信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** 
- API版本10+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API版本9：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(): Promise<OsAccountInfo>
```

查询当前进程所属的系统账号的信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** 
- API版本10+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API版本9：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

获取分布式虚拟设备ID。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)(callback: AsyncCallback&lt;string&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(): Promise<string>
```

获取分布式虚拟设备ID。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)()

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getForegroundOsAccountLocalId

```TypeScript
getForegroundOsAccountLocalId(): Promise<number>
```

获取前台系统账号的ID。使用Promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

获取指定系统账号的全部约束。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number): Promise<Array<string>>
```

获取指定系统账号的全部约束。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

获取指定系统账号的全部约束。使用callback异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number): Promise<Array<string>>
```

获取指定系统账号的全部约束。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**起始版本：** 9

**废弃版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountCount

```TypeScript
getOsAccountCount(callback: AsyncCallback<number>): void
```

获取已创建的系统账号数量。使用callback异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountCount

```TypeScript
getOsAccountCount(): Promise<number>
```

获取已创建的系统账号数量。使用Promise异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountDomainInfo

```TypeScript
getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>
```

获取指定系统账号关联的域账号信息。使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.GET_DOMAIN_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(callback: AsyncCallback<number>): void
```

获取当前进程所属的系统账号ID。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(): Promise<number>
```

获取当前进程所属的系统账号ID。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void
```

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long, callback: AsyncCallback&lt;int&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serialNumber | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>
```

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serialNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void
```

根据域账号信息，获取与其关联的系统账号ID。使用callback异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>
```

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void
```

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serialNumber | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>
```

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serialNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void
```

根据uid查询对应的系统账号ID。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: number): Promise<number>
```

根据uid查询对应的系统账号ID。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getOsAccountLocalIdForUidSync

```TypeScript
getOsAccountLocalIdForUidSync(uid: number): number
```

根据uid查询对应的系统账号ID。使用同步方式返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void
```

根据域账号信息，获取与其关联的系统账号的账号ID。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo, callback: AsyncCallback&lt;int&gt;)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>
```

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void
```

获取当前进程所属的系统账号ID。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalId](#getosaccountlocalid)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountLocalId](#getosaccountlocalid)(callback: AsyncCallback&lt;int&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(): Promise<number>
```

获取当前进程所属的系统账号ID。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalId](#getosaccountlocalid)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountLocalId](#getosaccountlocalid)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void
```

根据uid查询对应的系统账号ID。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int, callback: AsyncCallback&lt;int&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number): Promise<number>
```

根据uid查询对应的系统账号ID。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIds

```TypeScript
getOsAccountLocalIds(): Promise<number[]>
```

获取所有非系统级的操作系统账号的本地ID。非系统级的操作系统账号对用户可见，通常用于登录等操作。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountName

```TypeScript
getOsAccountName(): Promise<string>
```

查询调用方所属系统账号的名称。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountNameByLocalId

```TypeScript
getOsAccountNameByLocalId(localId: number): Promise<string>
```

根据系统账号的本地ID获取系统账号的名称。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## getOsAccountType

```TypeScript
getOsAccountType(callback: AsyncCallback<OsAccountType>): void
```

查询当前进程所属的系统账号的账号类型。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountType

```TypeScript
getOsAccountType(): Promise<OsAccountType>
```

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void
```

查询当前进程所属的系统账号的账号类型。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountType](#getosaccounttype)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountType](#getosaccounttype)(callback: AsyncCallback&lt;OsAccountType&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | 是 |

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(): Promise<OsAccountType>
```

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountType](#getosaccounttype)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountType](#getosaccounttype)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void
```

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int, callback: AsyncCallback&lt;long&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number): Promise<number>
```

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void
```

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: number): Promise<number>
```

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void
```

判断是否支持多系统账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)(callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(): Promise<boolean>
```

判断是否支持多系统账号。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void
```

判断指定系统账号是否处于激活状态。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number): Promise<boolean>
```

判断指定系统账号是否处于激活状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

判断指定系统账号是否具有指定约束。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>
```

判断指定系统账号是否具有指定约束。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountConstraintEnabled

```TypeScript
isOsAccountConstraintEnabled(constraint: string): Promise<boolean>
```

判断当前系统账号是否使能指定约束。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constraint | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## isOsAccountUnlocked

```TypeScript
isOsAccountUnlocked(): Promise<boolean>
```

检查当前系统账号是否已解锁。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(callback: AsyncCallback<boolean>): void
```

检查当前系统账号是否已验证。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkOsAccountVerified](#checkosaccountverified)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkOsAccountVerified](#checkosaccountverified)(callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

检查指定系统账号是否已验证。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId?: number): Promise<boolean>
```

检查指定系统账号是否已验证。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isTestOsAccount

```TypeScript
isTestOsAccount(callback: AsyncCallback<boolean>): void
```

检查当前系统账号是否为测试账号。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkOsAccountTestable](#checkosaccounttestable)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkOsAccountTestable](#checkosaccounttestable)(callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isTestOsAccount

```TypeScript
isTestOsAccount(): Promise<boolean>
```

检查当前系统账号是否为测试账号。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [checkOsAccountTestable](#checkosaccounttestable)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkOsAccountTestable](#checkosaccounttestable)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void
```

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)(callback: AsyncCallback&lt;Array&lt;int&gt;&gt;)

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(): Promise<Array<number>>
```

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用
> [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)()

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

查询当前进程所属的系统账号的信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | 是 |

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(): Promise<OsAccountInfo>
```

查询当前进程所属的系统账号的信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

获取分布式虚拟设备ID。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(): Promise<string>
```

获取分布式虚拟设备ID。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
