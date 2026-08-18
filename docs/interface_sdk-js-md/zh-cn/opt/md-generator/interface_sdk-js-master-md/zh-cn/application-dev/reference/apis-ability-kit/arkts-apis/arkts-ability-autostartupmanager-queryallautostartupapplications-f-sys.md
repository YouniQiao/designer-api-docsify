# queryAllAutoStartupApplications（系统接口）

## 导入模块

```TypeScript
```

## queryAllAutoStartupApplications

```TypeScript
function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void
```

查询自启动应用组件信息。使用callback异步回调。 从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。 对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-autoStartupManager-function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void--><!--Device-autoStartupManager-function queryAllAutoStartupApplications(callback: AsyncCallback<Array<AutoStartupInfo>>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## queryAllAutoStartupApplications

```TypeScript
function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>
```

查询自启动应用组件信息。使用Promise异步回调。 从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。 对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-autoStartupManager-function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>--><!--Device-autoStartupManager-function queryAllAutoStartupApplications(): Promise<Array<AutoStartupInfo>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
