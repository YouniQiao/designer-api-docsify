# on（系统接口）

## on('uninstallDLPSandbox')

```TypeScript
function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void
```

注册监听DLP沙箱卸载事件，用于感知沙箱环境的变化。注册成功后，当DLP沙箱被卸载时，系统会通过回调函数通知应用。

调用on注册监听后，建议在不需要监听时调用  
[off](dlpPermission.off(type: 'uninstallDLPSandbox', listener?: Callback&lt;DLPSandboxState&gt;))取消监听释放资源。

DLP管理应用需要追踪沙箱的创建和销毁状态，以便维护沙箱列表或执行相关的清理操作。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void--><!--Device-dlpPermission-function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'uninstallDLPSandbox' | 是 |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DLPSandboxState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.on('uninstallDLPSandbox', (info: dlpPermission.DLPSandboxState) => {
  console.info('uninstallDLPSandbox event', info.appIndex, info.bundleName)
}); // 订阅。
```
