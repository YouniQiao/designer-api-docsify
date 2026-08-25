# AtManager

程序访问控制管理类，提供权限校验、运行时权限弹窗申请、设置页授权引导、全局开关请求和权限状态监听等能力。通过[createAtManager](arkts-ability-abilityaccessctrl-createatmanager-f.md) 获取实例。

**起始版本：** 8

**系统能力：** SystemCapability.Security.AccessToken

## 导入模块

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, Permissions } from 'kits/@kit.AbilityKit';
```

## checkAccessToken

```TypeScript
checkAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>
```

校验应用是否已被授予指定权限。调用成功后，返回当前权限的授权状态，开发者可据此决定直接执行后续业务、继续发起权限申请，或引导用户前往系统设置修改授权状态。使用Promise异步回调。适用于应用访问相机、麦克风、位置等受保护资源前进行前置权限判断的场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;GrantStatus & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |

## checkAccessTokenSync

```TypeScript
checkAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus
```

校验应用是否已被授予指定权限，同步返回该权限的授权状态。开发者可据此决定直接执行后续业务流程，或继续发起权限申请，或引导用户前往设置页修改授权状态。与[checkAccessToken](#checkaccesstoken)相比，本接口同步返回授权状态，适用于无需异步处理的权限校验场景。适用于应用访问相机、麦克风、位置等受保护资源前进行前置权限判断的场景。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| [GrantStatus](arkts-ability-abilityaccessctrl-grantstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |

## getSelfPermissionStatus

```TypeScript
getSelfPermissionStatus(permissionName: Permissions): PermissionStatus
```

查询当前应用的权限状态，同步返回结果。调用成功后，返回当前权限的状态。与[checkAccessToken](#checkaccesstoken)不同，本接口无 需传入应用身份标识，仅用于查询当前应用自身权限状态。适用于在判断是否需要请求权限前、权限申请后确认授权结果、或监听到权限状态变化后重新查询等场景。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| [PermissionStatus](arkts-ability-abilityaccessctrl-permissionstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## off('selfPermissionStateChange')

```TypeScript
off(
      type: 'selfPermissionStateChange',
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

取消订阅自身指定权限列表的权限状态变更事件。取消订阅成功后，将不再接收指定权限列表的状态变化通知。在无需继续监听权限变化、应用退出或切换页面等场景下，可调用该接口取消订阅。

> **说明：**
> 当不传入callback参数时，将批量删除与permissionList相关联的所有回调函数。
> 该接口通常与[on](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#onpermissionstatechange)配套使用，用于取消通过on创建的监听关系。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selfPermissionStateChange' | 是 |
| permissionList | Array & lt;Permissions & gt; | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## on('selfPermissionStateChange')

```TypeScript
on(
      type: 'selfPermissionStateChange',
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

订阅本应用的指定权限列表的权限授权状态变化事件，使用callback异步回调。可在需要根据权限状态实时更新UI或业务逻辑、监听用户授权行为等场景中使用。不再需要监听时，调用[off](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#offpermissionstatechange)取消订阅。  
- 多次调用本订阅接口时，如果订阅的权限列表相同，callback不同，允许订阅成功。  
- 多次调用本订阅接口时，如果订阅的权限列表间有相同的子集，callback相同时，订阅失败。

> **说明：**
> 权限状态由“已授权”变更为“未授权”可能存在两种场景：
> - 用户主动撤销：系统会终止对应应用进程。
> - 系统主动回收：应用进程不会终止。典型场景如安全控件的单次授权，在授权周期结束后由系统自动回收。
> 该接口通常与[off](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#offpermissionstatechange)配套使用，当不再需要监听时应调用off取消订阅。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selfPermissionStateChange' | 是 |
| permissionList | Array & lt;Permissions & gt; | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100005](../errorcode-access-token.md#12100005-监听器数量超过限制) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## openPermissionOnSetting

```TypeScript
openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>
```

用于[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)/ [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)拉起权限设置页面。调用成功后会打开权限设置页面，用户在页面中 操作后，返回用户在设置页面中的选择结果。使用Promise异步回调。适用于 [manual_settings](../../../security/AccessToken/app-permission-mgmt-overview.md#manual_settings手动设置授权) 类型权限无法通过普通授权弹窗申请、必须引导用户进入系统设置完成授权的场景。manual_settings类型权限是指只能由用户在系统设置中手动开启的权限，无法通过普通授权弹窗直接申请。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | 是 |
| permission | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SelectedResult](arkts-ability-abilityaccessctrl-selectedresult-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [12100014](../errorcode-access-token.md#12100014-非预期的权限) |

## requestGlobalSwitch

```TypeScript
requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>
```

用于UIAbility/UIExtensionAbility拉起全局开关设置弹窗。调用成功后，若全局开关处于关闭状态，则弹出全局开关设置界面供用户操作；若全局开关已开启，则不拉起弹窗并返回true。使用Promise异步回调。适用于依赖系统级全局开关（如相机、麦克风、定位）开启的场景。当应用需要使用相机、麦克风或定位等需要全局开关管控的功能时，如果对应的全局开关被关闭，应用可拉起此弹窗请求用户开启对应功能。如果当前全局开关的状态为开启，则不拉起弹窗。<!--RP5--><!--RP5End-->

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | 是 |
| type | [SwitchType](arkts-ability-abilityaccessctrl-switchtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [12100013](../errorcode-access-token.md#12100013-全局开关已开启) |

## requestPermissionOnSetting

```TypeScript
requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>
```

用于[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)/ [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)二次拉起权限设置弹窗，返回授权状态数组。使用Promise异 步回调。适用于用户在首次弹窗中已拒绝过该权限授予，需要通过设置页面继续申请权限的场景。在调用此接口前，应用需要先调用 [requestPermissionsFromUser](#requestpermissionsfromuser)。 如果用户已在首次弹窗中授权，则调用当前接口不会拉起授权弹窗。<!--RP4--><!--RP4End-->

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | 是 |
| permissionList | Array & lt;Permissions & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;GrantStatus & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |
| [12100010](../errorcode-access-token.md#12100010-存在未被处理的请求) |
| [12100011](../errorcode-access-token.md#12100011-输入的所有权限均已被授权) |
| [12100012](../errorcode-access-token.md#12100012-输入的权限中存在未被用户拒绝过的权限) |
| [12100014](../errorcode-access-token.md#12100014-非预期的权限) |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>) : void
```

用于<!--RP1-->[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)<!--RP1End-->拉起弹窗请求 [用户授权](../../../security/AccessToken/request-user-authorization.md)，返回本次请求权限的授权结果。使用callback异步回调。适用于应用首次访问受保护资源前主动向用户申请 [user_grant](../../../security/AccessToken/app-permission-mgmt-overview.md#user_grant用户授权) 权限的场景。如果用户拒绝授权，将无法通过此接口再次拉起授权弹窗。开发者可引导用户前往系统设置界面手动授权，或调用 [requestPermissionOnSetting](#requestpermissiononsetting)拉起权限设置弹窗，引导用户完成授权。<!--RP3--><!--RP3End-->

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | 是 |
| permissionList | Array & lt;Permissions & gt; | 是 |
| requestCallback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

用于<!--RP1-->[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)<!--RP1End-->拉起弹窗请求 [用户授权](../../../security/AccessToken/request-user-authorization.md)，返回本次请求权限的授权结果。使用Promise异步回调。适用于应用首次访问受保护资源前主动向用户申请user_grant权限的场景。

> **说明：**
> 如果用户拒绝授权，将无法通过此接口再次拉起授权弹窗。开发者可引导用户前往系统设置界面手动授权，或调用
> [requestPermissionOnSetting](#requestpermissiononsetting)拉起权限设置弹窗，引导用户完成授权。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | 是 |
| permissionList | Array & lt;Permissions & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [12100009](../errorcode-access-token.md#12100009-服务内部错误) |

## verifyAccessToken

```TypeScript
verifyAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>
```

校验应用是否已被授予指定权限，调用成功后，返回当前权限的授权状态，开发者可据此决定直接执行后续业务、继续发起权限申请，或引导用户前往系统设置修改授权状态。使用Promise异步回调。适用于应用访问受保护资源前进行前置权限判断的场景。

> **说明：**
> 建议使用[checkAccessToken](#checkaccesstoken)替代。

**起始版本：** 9

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;GrantStatus & gt; |

## verifyAccessToken

```TypeScript
verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>
```

校验应用是否已被授予指定权限。调用成功后，返回当前权限的授权状态，开发者可据此决定后续操作。使用Promise异步回调。

> **说明：**
> 从API version 8开始支持，从API version 9开始废弃，建议使用[checkAccessToken](#checkaccesstoken)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [checkAccessToken](#checkaccesstoken)

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;GrantStatus & gt; |

## verifyAccessTokenSync

```TypeScript
verifyAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus
```

校验应用是否已被授予指定权限，同步返回该权限的授权状态。开发者可据此决定直接执行后续业务流程，或继续发起权限申请，或引导用户前往系统设置修改授权状态。适用于应用访问相机、麦克风、位置等受保护资源前进行前置权限判断的场景。建议使用[checkAccessTokenSync](#checkaccesstokensync)替代。

**起始版本：** 9

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| [GrantStatus](arkts-ability-abilityaccessctrl-grantstatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
