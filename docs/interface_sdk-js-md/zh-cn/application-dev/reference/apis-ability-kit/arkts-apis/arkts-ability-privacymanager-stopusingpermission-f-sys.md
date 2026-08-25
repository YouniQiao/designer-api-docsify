# stopUsingPermission（系统接口）

## 导入模块

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## stopUsingPermission

```TypeScript
function stopUsingPermission(tokenID: number, permissionName: Permissions): Promise<void>
```

系统应用调用此接口，标记不再使用指定权限。调用成功后，隐私服务将此状态变化通知所有该权限使用状态变更事件的订阅者。 适用于应用完成敏感操作后或退出前台时，通知系统权限使用结束。使用Promise异步回调。该接口需与[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md)配套使用。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |


## stopUsingPermission

```TypeScript
function stopUsingPermission(tokenID: number, permissionName: Permissions, callback: AsyncCallback<void>): void
```

系统应用调用此接口，标记不再使用指定权限。调用成功后，隐私服务将此状态变化通知所有该权限使用状态变更事件的订阅者。 适用于应用完成敏感操作后或退出前台时，通知系统权限使用结束。使用callback异步回调。该接口需与[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md)配套使用。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |


## stopUsingPermission

```TypeScript
function stopUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    pid?: number,
    options?: PermissionUsingOptions
  ): Promise<void>
```

系统应用调用此接口，标记不再使用指定权限。调用成功后，隐私服务将此状态变化通知所有该权限使用状态变更事件的订阅者。 适用于应用完成敏感操作后或退出前台时，通知系统权限使用结束。使用Promise异步回调。pid需要与[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md)传入的pid相同。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| pid | number | 否 |
| options | [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |


## stopUsingPermission

```TypeScript
function stopUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    pid?: number
  ): Promise<void>
```

系统应用调用此接口，标记不再使用指定权限。调用成功后，隐私服务将此状态变化通知所有该权限使用状态变更事件的订阅者。适用于应用完成敏感操作后或退出前台时，通知系统权限使用结束。使用Promise异步回调。pid需要与 [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md) 传入的pid相同。

**起始版本：** 18

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| pid | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
