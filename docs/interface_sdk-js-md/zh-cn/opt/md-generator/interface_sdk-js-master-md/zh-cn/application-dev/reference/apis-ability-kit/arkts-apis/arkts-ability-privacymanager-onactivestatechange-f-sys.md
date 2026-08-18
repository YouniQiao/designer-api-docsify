# onActiveStateChange（系统接口）

## 导入模块

```TypeScript
```

## onActiveStateChange

```TypeScript
function onActiveStateChange(
    permissionList: Array<Permissions>,
    callback: Callback<ActiveChangeResponse>): void
```

订阅指定权限列表的权限使用状态变更事件。权限使用状态变更由 [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission系统接口)和 [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission系统接口)调用触发。订阅成功 后，当权限使用状态变更时，回调函数会被触发，返回[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md#activechangeresponse系统接口)对象，包含权限使用状态变化的详情。使用 callback异步回调。 允许相同permissionList订阅多个回调函数。 > **说明：**> 不允许使用有交集的两个permissionList分别订阅同一个回调函数。即如果两个permissionList包含相同的权限名，则不能使用同一个回调函数进行订阅。 > 该接口通常与[offActiveStateChange](arkts-ability-privacymanager-offactivestatechange-f-sys.md#offactivestatechange)配套使用，在不再需要监听时应调用offActiveStateChange取消订阅。

**起始版本：** 23

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionList | Array & lt;Permissions & gt; | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100005](../errorcode-access-token.md#12100005-监听器数量超过限制) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |
