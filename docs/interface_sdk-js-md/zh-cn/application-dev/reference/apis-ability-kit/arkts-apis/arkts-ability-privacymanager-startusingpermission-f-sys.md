# startUsingPermission（系统接口）

## 导入模块

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## startUsingPermission

```TypeScript
function startUsingPermission(tokenID: number, permissionName: Permissions): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考[on](arkts-ability-privacymanager-on-f-sys.md)）。使用Promise异步回调。开始使用权限后，需要在权限使用结束时调用[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md)停止使用权限。

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
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    pid?: number,
    usedType?: PermissionUsedType
  ): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考 on）。 使用Promise异步回调。开始使用权限后，需要在权限使用结束时调用 [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) 停止使用权限。

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
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 否 |

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


## startUsingPermission

```TypeScript
function startUsingPermission(
     tokenID: number,
     permissionName: Permissions,
     pid?: number,
     usedType?: PermissionUsedType,
     options?: PermissionUsingOptions
   ): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考 on ）。使用Promise异步回调。开始使用权限后，需要在权限使用结束时调用 [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) 停止使用权限。当传入pid时，pid需要与 [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) 传入的pid相同，不满足配套关系返回错误码12100004。

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
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 否 |
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


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    callback: AsyncCallback<void>
  ): void
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考 on ）。使用callback异步回调。开始使用权限后，需要在权限使用结束时调用 [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md) 停止使用权限。

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
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
