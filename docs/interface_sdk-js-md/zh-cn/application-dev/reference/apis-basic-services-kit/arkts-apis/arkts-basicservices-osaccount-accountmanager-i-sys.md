# AccountManager

系统账号管理类。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## activateOsAccount

```TypeScript
activateOsAccount(localId: number, callback: AsyncCallback<void>): void
```

激活指定系统账号。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300009](../errorcode-account.md#12300009-账号已激活) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300016](../errorcode-account.md#12300016-账号登录数已达上限) |

## activateOsAccount

```TypeScript
activateOsAccount(localId: number): Promise<void>
```

激活指定系统账号。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

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
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300009](../errorcode-account.md#12300009-账号已激活) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300016](../errorcode-account.md#12300016-账号登录数已达上限) |

## activateOsAccount

```TypeScript
activateOsAccount(localId: number, displayId: number): Promise<void>
```

在指定逻辑屏激活（前台启动或切换）目标系统账号。使用Promise异步回调。 当前不支持跨逻辑屏激活，即在指定逻辑屏上激活另一个已在逻辑屏前台运行的系统账号。

**起始版本：** 23

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300016](../errorcode-account.md#12300016-账号登录数已达上限) |
| [12300018](../errorcode-account.md#12300018-逻辑屏未找到) |
| [12300019](../errorcode-account.md#12300019-不支持跨逻辑屏激活) |

## bindDomainAccount

```TypeScript
bindDomainAccount(localId: number, domainAccountInfo: DomainAccountInfo): Promise<void>
```

在指定系统账号上绑定指定域账号。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300021](../errorcode-account.md#12300021-系统账号已绑定域账号) |
| [12300022](../errorcode-account.md#12300022-域账号已被绑定) |

## createOsAccount

```TypeScript
createOsAccount(localName: string, type: OsAccountType, callback: AsyncCallback<OsAccountInfo>): void
```

创建一个系统账号。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localName | string | 是 |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300005](../errorcode-account.md#12300005-不支持多用户) |
| [12300006](../errorcode-account.md#12300006-不支持的账号类型) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300023](../errorcode-account.md#12300023-指定类型的账号数量已达到上限) |

## createOsAccount

```TypeScript
createOsAccount(localName: string, type: OsAccountType, options?: CreateOsAccountOptions): Promise<OsAccountInfo>
```

创建一个系统账号。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localName | string | 是 |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | 是 |
| options | [CreateOsAccountOptions](arkts-basicservices-osaccount-createosaccountoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300005](../errorcode-account.md#12300005-不支持多用户) |
| [12300006](../errorcode-account.md#12300006-不支持的账号类型) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300015](../errorcode-account.md#12300015-短名称已存在) |
| [12300023](../errorcode-account.md#12300023-指定类型的账号数量已达到上限) |

## createOsAccountForDomain

```TypeScript
createOsAccountForDomain(
      type: OsAccountType,
      domainInfo: DomainAccountInfo,
      callback: AsyncCallback<OsAccountInfo>
    ): void
```

根据域账号信息，创建一个系统账号并将其与域账号关联。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | 是 |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300005](../errorcode-account.md#12300005-不支持多用户) |
| [12300006](../errorcode-account.md#12300006-不支持的账号类型) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300023](../errorcode-account.md#12300023-指定类型的账号数量已达到上限) |

## createOsAccountForDomain

```TypeScript
createOsAccountForDomain(type: OsAccountType, domainInfo: DomainAccountInfo, options?: CreateOsAccountForDomainOptions): Promise<OsAccountInfo>
```

根据传入的域账号信息，创建与其关联的系统账号。使用Promise异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | 是 |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| options | [CreateOsAccountForDomainOptions](arkts-basicservices-osaccount-createosaccountfordomainoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300004](../errorcode-account.md#12300004-账号已存在) |
| [12300005](../errorcode-account.md#12300005-不支持多用户) |
| [12300006](../errorcode-account.md#12300006-不支持的账号类型) |
| [12300007](../errorcode-account.md#12300007-账号数量已达上限) |
| [12300015](../errorcode-account.md#12300015-短名称已存在) |
| [12300023](../errorcode-account.md#12300023-指定类型的账号数量已达到上限) |

## deactivateOsAccount

```TypeScript
deactivateOsAccount(localId: number): Promise<void>
```

注销（退出登录）指定系统账号。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

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
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |

## getBundleIdForUid

```TypeScript
getBundleIdForUid(uid: number, callback: AsyncCallback<number>): void
```

通过uid查询对应的bundleId。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getBundleIdForUid

```TypeScript
getBundleIdForUid(uid: number): Promise<number>
```

通过uid查询对应的bundleId。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getBundleIdForUidSync

```TypeScript
getBundleIdForUidSync(uid: number): number
```

通过uid查询对应的bundleId。使用同步方式返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## getEnabledOsAccountConstraints

```TypeScript
getEnabledOsAccountConstraints(localId: number): Promise<Array<string>>
```

获取指定系统账号已使能的全部约束。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getForegroundOsAccountDisplayId

```TypeScript
getForegroundOsAccountDisplayId(localId: number): Promise<number>
```

获取指定前台系统账号所运行的逻辑屏ID。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300017](../errorcode-account.md#12300017-前台系统账号未找到) |

## getForegroundOsAccountLocalId

```TypeScript
getForegroundOsAccountLocalId(displayId: number): Promise<number>
```

获取指定逻辑屏上运行的前台系统账号ID。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300017](../errorcode-account.md#12300017-前台系统账号未找到) |

## getOsAccountConstraintSourceTypes

```TypeScript
getOsAccountConstraintSourceTypes(localId: number, constraint: string, callback: AsyncCallback<Array<ConstraintSourceTypeInfo>>): void
```

查询指定系统账号的指定约束来源信息。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ConstraintSourceTypeInfo](arkts-basicservices-osaccount-constraintsourcetypeinfo-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountConstraintSourceTypes

```TypeScript
getOsAccountConstraintSourceTypes(localId: number, constraint: string): Promise<Array<ConstraintSourceTypeInfo>>
```

查询指定系统账号的指定约束来源信息。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| constraint | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ConstraintSourceTypeInfo](arkts-basicservices-osaccount-constraintsourcetypeinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountProfilePhoto

```TypeScript
getOsAccountProfilePhoto(localId: number, callback: AsyncCallback<string>): void
```

获取指定系统账号的头像信息。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountProfilePhoto

```TypeScript
getOsAccountProfilePhoto(localId: number): Promise<string>
```

获取指定系统账号的头像信息。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountType

```TypeScript
getOsAccountType(localId: number): Promise<OsAccountType>
```

查询指定系统账号的类型。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## isMainOsAccount

```TypeScript
isMainOsAccount(callback: AsyncCallback<boolean>): void
```

查询当前进程是否处于主用户。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## isMainOsAccount

```TypeScript
isMainOsAccount(): Promise<boolean>
```

查询当前进程是否处于主用户。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## isOsAccountActivated

```TypeScript
isOsAccountActivated(localId: number): Promise<boolean>
```

判断指定系统账号是否处于激活状态。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## isOsAccountConstraintEnabled

```TypeScript
isOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>
```

判断指定系统账号是否使能指定约束。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## isOsAccountUnlocked

```TypeScript
isOsAccountUnlocked(localId: number): Promise<boolean>
```

检查指定系统账号是否已解锁。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## off('activate' | 'activating')

```TypeScript
off(type: 'activate' | 'activating', name: string, callback?: Callback<number>): void
```

取消订阅系统账号的激活完成与激活中的事件。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activate' \| 'activating' | 是 |
| name | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## off('activate' | 'activating')

```TypeScript
off(type: 'activate' | 'activating', name: string, callback?: Callback<number>): void
```

取消订阅系统账号的激活完成与激活中的事件。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activate' \| 'activating' | 是 |
| name | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## off('switching')

```TypeScript
off(type: 'switching', callback?: Callback<OsAccountSwitchEventData>): void
```

取消订阅系统账号的前后台正在切换事件。使用callback异步回调。

**起始版本：** 12

**需要权限：** 
- API版本23+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API版本12 - 22：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'switching' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## off('switched')

```TypeScript
off(type: 'switched', callback?: Callback<OsAccountSwitchEventData>): void
```

取消订阅系统账号的前后台切换结束事件。使用callback异步回调。

**起始版本：** 12

**需要权限：** 
- API版本23+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API版本12 - 22：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'switched' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## offConstraintChanged

```TypeScript
offConstraintChanged(callback?: Callback<ConstraintChangeInfo>): void
```

取消与指定回调关联的约束变更订阅记录。若未指定回调，则取消所有订阅记录。

**起始版本：** 23

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ConstraintChangeInfo](arkts-basicservices-osaccount-constraintchangeinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## on('activate' | 'activating')

```TypeScript
on(type: 'activate' | 'activating', name: string, callback: Callback<number>): void
```

订阅系统账号的激活完成与激活中的事件。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activate' \| 'activating' | 是 |
| name | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## on('activate' | 'activating')

```TypeScript
on(type: 'activate' | 'activating', name: string, callback: Callback<number>): void
```

订阅系统账号的激活完成与激活中的事件。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'activate' \| 'activating' | 是 |
| name | string | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## on('switching')

```TypeScript
on(type: 'switching', callback: Callback<OsAccountSwitchEventData>): void
```

订阅系统账号的前后台正在切换事件。使用callback异步回调。

**起始版本：** 12

**需要权限：** 
- API版本23+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API版本12 - 22：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'switching' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## on('switched')

```TypeScript
on(type: 'switched', callback: Callback<OsAccountSwitchEventData>): void
```

订阅系统账号的前后台切换结束事件。使用callback异步回调。

**起始版本：** 12

**需要权限：** 
- API版本23+：ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API版本12 - 22：ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'switched' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## onConstraintChanged

```TypeScript
onConstraintChanged(constraints: string[], callback: Callback<ConstraintChangeInfo>): void
```

订阅调用方所属系统账号的一种或多种约束变更事件。使用callback异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | string[] | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ConstraintChangeInfo](arkts-basicservices-osaccount-constraintchangeinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## queryAllCreatedOsAccounts

```TypeScript
queryAllCreatedOsAccounts(callback: AsyncCallback<Array<OsAccountInfo>>): void
```

查询已创建的所有系统账号的信息列表。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryAllCreatedOsAccounts

```TypeScript
queryAllCreatedOsAccounts(): Promise<Array<OsAccountInfo>>
```

查询已创建的所有系统账号的信息列表。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryMaxLoggedInOsAccountNumber

```TypeScript
queryMaxLoggedInOsAccountNumber(): Promise<number>
```

查询允许同时登录的系统账号的最大数量。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryMaxOsAccountNumber

```TypeScript
queryMaxOsAccountNumber(callback: AsyncCallback<number>): void
```

查询允许创建的系统账号的最大数量。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryMaxOsAccountNumber

```TypeScript
queryMaxOsAccountNumber(): Promise<number>
```

查询允许创建的系统账号的最大数量。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryOsAccount

```TypeScript
queryOsAccount(): Promise<OsAccountInfo>
```

查询当前进程所属的系统账号的信息。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryOsAccountById

```TypeScript
queryOsAccountById(localId: number, callback: AsyncCallback<OsAccountInfo>): void
```

查询指定系统账号的信息。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## queryOsAccountById

```TypeScript
queryOsAccountById(localId: number): Promise<OsAccountInfo>
```

查询指定系统账号的信息。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## removeOsAccount

```TypeScript
removeOsAccount(localId: number, callback: AsyncCallback<void>): void
```

删除指定系统账号。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |

## removeOsAccount

```TypeScript
removeOsAccount(localId: number): Promise<void>
```

删除指定系统账号。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |

## removeOsAccount

```TypeScript
removeOsAccount(localId: number, options: RemoveOsAccountOptions): Promise<void>
```

根据删除选项，删除指定系统账号。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| options | [RemoveOsAccountOptions](arkts-basicservices-osaccount-removeosaccountoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |

## setOsAccountConstraints

```TypeScript
setOsAccountConstraints(localId: number, constraints: Array<string>, enable: boolean, callback: AsyncCallback<void>): void
```

为指定系统账号设置/删除约束。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | Array & lt;string & gt; | 是 |
| enable | boolean | 是 |
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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountConstraints

```TypeScript
setOsAccountConstraints(localId: number, constraints: Array<string>, enable: boolean): Promise<void>
```

为指定系统账号设置/删除约束。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | Array & lt;string & gt; | 是 |
| enable | boolean | 是 |

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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountName

```TypeScript
setOsAccountName(localId: number, localName: string, callback: AsyncCallback<void>): void
```

设置指定系统账号的账号名。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| localName | string | 是 |
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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountName

```TypeScript
setOsAccountName(localId: number, localName: string): Promise<void>
```

设置指定系统账号的账号名。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| localName | string | 是 |

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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountProfilePhoto

```TypeScript
setOsAccountProfilePhoto(localId: number, photo: string, callback: AsyncCallback<void>): void
```

为指定系统账号设置头像信息。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| photo | string | 是 |
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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountProfilePhoto

```TypeScript
setOsAccountProfilePhoto(localId: number, photo: string): Promise<void>
```

为指定系统账号设置头像信息。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| photo | string | 是 |

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
| [12300008](../errorcode-account.md#12300008-受限的账号) |

## setOsAccountType

```TypeScript
setOsAccountType(localId: number, type: OsAccountType, options?: SetOsAccountTypeOptions): Promise<void>
```

设置指定系统账号的账号类型。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | 是 |
| options | [SetOsAccountTypeOptions](arkts-basicservices-osaccount-setosaccounttypeoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300023](../errorcode-account.md#12300023-指定类型的账号数量已达到上限) |
