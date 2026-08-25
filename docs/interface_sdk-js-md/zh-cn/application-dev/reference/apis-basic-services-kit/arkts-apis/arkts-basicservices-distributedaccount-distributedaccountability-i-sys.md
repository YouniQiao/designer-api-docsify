# DistributedAccountAbility

提供查询和更新分布式账号登录状态方法（使用前需要先获取分布式账号的单实例对象）。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountDistributedInfoByLocalId

```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number, callback: AsyncCallback<DistributedInfo>): void
```

获取指定系统账号的分布式账号信息。使用callback异步回调。

**起始版本：** 10

**需要权限：** 
- API版本20+：ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API版本10 - 19：ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getOsAccountDistributedInfoByLocalId

```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number): Promise<DistributedInfo>
```

获取指定系统账号的分布式账号信息。使用Promise异步回调。

**起始版本：** 10

**需要权限：** 
- API版本20+：ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API版本10 - 19：ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DistributedInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## setOsAccountDistributedInfoByLocalId

```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

设置指定系统账号的分布式账号信息。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |
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
| [12300406](../errorcode-account.md#12300406-该分布式账号信息已经与目标系统账号的其他子身份资料绑定) |

## setOsAccountDistributedInfoByLocalId

```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo): Promise<void>
```

设置指定系统账号的分布式账号信息。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localId | number | 是 |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |

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
| [12300406](../errorcode-account.md#12300406-该分布式账号信息已经与目标系统账号的其他子身份资料绑定) |
