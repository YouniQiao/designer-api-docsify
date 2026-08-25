# OsAccountSubProfileManager（系统接口）

系统账号子身份资料管理器类。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## createOsAccountSubProfile

```TypeScript
createOsAccountSubProfile(osAccountLocalId: number): Promise<OsAccountSubProfile>
```

创建一个系统账号子身份资料。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300008](../errorcode-account.md#12300008-受限的账号) |
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300402](../errorcode-account.md#12300402-系统账号下的子身份资料数量已达到上限) |

## deleteOsAccountSubProfile

```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

删除一个系统账号子身份资料。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

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
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |
| [12300403](../errorcode-account.md#12300403-受限的系统账号子身份资料) |
| [12300404](../errorcode-account.md#12300404-系统账号的前台子身份资料不允许被删除) |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(): Promise<number>
```

获取调用方所属系统账号的前台子身份资料的标识符。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: number): Promise<number>
```

获取指定系统账号的前台子身份资料标识符。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |

## getOsAccountLocalIdForSubProfile

```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: number): Promise<number>
```

获取子身份资料所属系统账号的本地标识符。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(subProfileId: number): Promise<OsAccountSubProfile>
```

获取调用方所属系统账号的子身份资料对象信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<OsAccountSubProfile>
```

获取指定系统账号的子身份资料对象信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(): Promise<number[]>
```

获取调用方所属系统账号的子身份资料标识符列表。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: number): Promise<number[]>
```

获取指定系统账号的子身份资料标识符列表。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## offOsAccountSubProfileEvent

```TypeScript
offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void
```

取消订阅系统账号子身份资料的事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## onOsAccountSubProfileEvent

```TypeScript
onOsAccountSubProfileEvent(
      events: OsAccountSubProfileEvent[],
      callback: Callback<OsAccountSubProfileEventData>): void
```

订阅系统账号子身份资料的事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| events | [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md)[] | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |

## switchOsAccountSubProfile

```TypeScript
switchOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

切换至一个系统账号子身份资料。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| osAccountLocalId | number | 是 |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | 是 |

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
| [12300010](../errorcode-account.md#12300010-账号服务忙碌) |
| [12300401](../errorcode-account.md#12300401-系统账号子身份资料不存在) |
| [12300403](../errorcode-account.md#12300403-受限的系统账号子身份资料) |
| [12300405](../errorcode-account.md#12300405-已登录分布式账号的前台子身份不可直接切换到后台) |
