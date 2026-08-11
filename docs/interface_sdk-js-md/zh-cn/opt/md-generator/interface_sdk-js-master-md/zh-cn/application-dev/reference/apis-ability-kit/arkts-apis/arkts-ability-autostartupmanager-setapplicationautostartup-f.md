# setApplicationAutoStartup

## setApplicationAutoStartup

```TypeScript
function setApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void
```

设置应用组件开机自启动。使用callback异步回调。从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-autoStartupManager-function setApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void--><!--Device-autoStartupManager-function setApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## setApplicationAutoStartup

```TypeScript
function setApplicationAutoStartup(info: AutoStartupInfo): Promise<void>
```

设置应用组件开机自启动。使用Promise异步回调。从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-autoStartupManager-function setApplicationAutoStartup(info: AutoStartupInfo): Promise<void>--><!--Device-autoStartupManager-function setApplicationAutoStartup(info: AutoStartupInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
