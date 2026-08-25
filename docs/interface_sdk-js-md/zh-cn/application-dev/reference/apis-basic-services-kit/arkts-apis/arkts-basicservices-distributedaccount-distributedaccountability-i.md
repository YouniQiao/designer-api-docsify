# DistributedAccountAbility

提供查询和更新分布式账号登录状态方法（使用前需要先获取分布式账号的单实例对象）。

**起始版本：** 7

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

获取分布式账号信息。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(): Promise<DistributedInfo>
```

获取分布式账号信息。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;DistributedInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

获取分布式账号信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountDistributedInfo](#getosaccountdistributedinfo)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountDistributedInfo](#getosaccountdistributedinfo)(callback: AsyncCallback&lt;DistributedInfo&gt;)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | 是 |

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(): Promise<DistributedInfo>
```

获取分布式账号信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [getOsAccountDistributedInfo](#getosaccountdistributedinfo)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getOsAccountDistributedInfo](#getosaccountdistributedinfo)()

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise & lt;DistributedInfo & gt; |

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

更新分布式账号信息。使用callback异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300406](../errorcode-account.md#12300406-该分布式账号信息已经与目标系统账号的其他子身份资料绑定) |

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

更新分布式账号信息。使用Promise异步回调。 该接口仅限系统应用调用。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |

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
| [12300406](../errorcode-account.md#12300406-该分布式账号信息已经与目标系统账号的其他子身份资料绑定) |

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

更新分布式账号信息。使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setOsAccountDistributedInfo](#setosaccountdistributedinfo)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setOsAccountDistributedInfo](#setosaccountdistributedinfo)(accountInfo: DistributedInfo, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

更新分布式账号信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。建议使用
> [setOsAccountDistributedInfo](#setosaccountdistributedinfo)
> 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setOsAccountDistributedInfo](#setosaccountdistributedinfo)(accountInfo: DistributedInfo)

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
