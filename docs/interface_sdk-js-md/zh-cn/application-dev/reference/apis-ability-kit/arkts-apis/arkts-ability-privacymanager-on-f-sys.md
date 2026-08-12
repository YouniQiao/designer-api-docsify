# on（系统接口）

## on('activeStateChange')

```TypeScript
function on(type: 'activeStateChange',
    permissionList: Array<Permissions>,
    callback: Callback<ActiveChangeResponse>): void
```

订阅指定权限列表的权限使用状态变更事件。权限使用状态变更由[startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission)和[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission)调用触发。订阅成功后，当权限使用状态变更时，回调函数会被触发，返回[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md#ActiveChangeResponse)对象，包含权限使用状态变化的详情。使用callback异步回调。

允许相同permissionList订阅多个回调函数。

> **说明：**
> 不允许使用有交集的两个permissionList分别订阅同一个回调函数。即如果两个permissionList包含相同的权限名，则不能使用同一个回调函数进行订阅。该接口通常与[off](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off)配套使用，在不再需要监听时应调用off取消订阅。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function on(type: 'activeStateChange',    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function on(type: 'activeStateChange',    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'activeStateChange' | 是 | 订阅事件类型，固定为'activeStateChange'，权限使用状态变更事件。 |
| permissionList | Array&lt;Permissions&gt; | 是 | 订阅的权限名列表。为空时表示订阅所有的权限使用状态变化。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：数组长度不能超过1024。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | 是 | 回调函数，返回订阅指定权限使用状态变更事件的对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12100008](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100008-内存申请失败) | Out of memory. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-入参错误) | Invalid parameter. The permissionList exceeds the size limit, or the permissionNames in the list are all invalid. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not system app. Interface caller is not a system app. |
| [12100004](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100004-接口未配套使用) | The API is used repeatedly with the same input. |
| [12100005](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100005-监听器数量超过限制) | The registration time has exceeded the limit. |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-系统服务工作异常) | Service exception. |

## 示例

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let permissionList: Array<Permissions> = [];
try {
    // 订阅权限使用状态变更事件
    privacyManager.on('activeStateChange', permissionList, (data: privacyManager.ActiveChangeResponse) => {
        console.debug(`receive permission state change, data: ${data}`);
    });
} catch (err) {
    let error = err as BusinessError;
    console.error(`Catch errcode: ${error.code}, message: ${error.message}`);
}
```

