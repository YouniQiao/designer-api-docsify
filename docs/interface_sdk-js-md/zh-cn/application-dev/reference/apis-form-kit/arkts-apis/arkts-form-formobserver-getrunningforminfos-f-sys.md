# getRunningFormInfos（系统接口）

## 导入模块

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## getRunningFormInfos

```TypeScript
function getRunningFormInfos(callback: AsyncCallback<Array<formInfo.RunningFormInfo>>, hostBundleName?: string): void
```

获取设备上正在运行的所有非临时卡片信息。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(
    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>,
    isUnusedIncluded: boolean,
    hostBundleName?: string
  ): void
```

获取设备上正在运行的所有非临时卡片信息。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 |
| [isUnusedIncluded](arkts-form-forminfo-formproviderfilter-i-sys.md) | boolean | 是 |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(hostBundleName?: string): Promise<Array<formInfo.RunningFormInfo>>
```

获取设备上正在运行的所有非临时卡片信息。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.RunningFormInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |


## getRunningFormInfos

```TypeScript
function getRunningFormInfos(
    isUnusedIncluded: boolean,
    hostBundleName?: string
  ): Promise<Array<formInfo.RunningFormInfo>>
```

获取设备上正在运行的所有非临时卡片信息。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isUnusedIncluded](arkts-form-forminfo-formproviderfilter-i-sys.md) | boolean | 是 |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.RunningFormInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
