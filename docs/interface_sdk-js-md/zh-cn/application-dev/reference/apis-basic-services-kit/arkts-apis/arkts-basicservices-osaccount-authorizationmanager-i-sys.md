# AuthorizationManager（系统接口）

系统账号授权管理类，用于管理系统账号授权。

**起始版本：** 24

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## acquireAuthorization

```TypeScript
acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>
```

为当前进程获取授权。

**起始版本：** 24

**需要权限：** ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |
| options | [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AcquireAuthorizationResult](arkts-basicservices-osaccount-acquireauthorizationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## hasAuthorization

```TypeScript
hasAuthorization(privilege: string): Promise<boolean>
```

检查当前进程是否已获得指定特权的授权。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## releaseAuthorization

```TypeScript
releaseAuthorization(privilege: string): Promise<void>
```

为当前进程撤销指定特权的授权。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| privilege | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
