# getExemptedApps（系统接口）

## 导入模块

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number, callback: AsyncCallback<Array<ExemptedAppInfo>>): void
```

获取进入待机模式的应用名单，使用Callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DEVICE_STANDBY_EXEMPTION

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceTypes | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-资源申请接口信息校验失败) |


## getExemptedApps

```TypeScript
function getExemptedApps(resourceTypes: number): Promise<Array<ExemptedAppInfo>>
```

获取进入待机模式的应用名单，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DEVICE_STANDBY_EXEMPTION

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceTypes | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-资源申请接口信息校验失败) |
