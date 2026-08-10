# off (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## off('activeStateChange')

```TypeScript
function off(
    type: 'activeStateChange',
    permissionList: Array<Permissions>,
    callback?: Callback<ActiveChangeResponse>): void
```

取消订阅指定权限列表的权限使用状态变更事件。取消订阅成功后，将不再接收指定权限列表的状态变更通知。

取消订阅时，若不传入回调函数，则批量删除permissionList下的所有回调函数。

> **说明：**
> 该接口通常与[on](privacyManager.on)配套使用，用于取消通过on创建的监听关系。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function off(    type: 'activeStateChange',    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function off(    type: 'activeStateChange',    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'activeStateChange' | Yes | 取消订阅事件类型，固定为'activeStateChange'，权限使用状态变更事件。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 取消订阅的权限名列表，为空时表示取消订阅所有的权限状态变化，必须与on的输入一致。 &lt;br&gt;取值约束：数组长度不能超过1024。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActiveChangeResponse&gt; | No | 回调函数，返回取消订阅指定tokenId与指定权限名状态变更事件的对象。需与 [on](privacyManager.on(type: 'activeStateChange', permissionList: Array&lt;Permissions&gt;, callback: Callback&lt;ActiveChangeResponse&gt;)) 传入的callback一致；不传入此参数时，将批量删除permissionList下的所有回调函数。 &lt;br&gt;取值约束：数组长度不能超过1024。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100008 | Out of memory. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 12100001 | Invalid parameter. The permissionList is not in the listening list. |
| 202 | Not system app. Interface caller is not a system app. |
| 12100004 | The API is not used in pair with 'on'. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let permissionList: Array<Permissions> = [];
try {
    // Unsubscribe from permission usage status change events
    privacyManager.off('activeStateChange', permissionList);
} catch (err) {
    let error = err as BusinessError;
    console.error(`Catch errcode: ${error.code}, message: ${error.message}`);
}
```

