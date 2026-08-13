# off_uninstallDLPSandbox（系统接口）

## off_uninstallDLPSandbox

```TypeScript
function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void
```

取消监听DLP沙箱卸载事件。调用成功后，应用不再接收DLP沙箱卸载事件的回调通知。 必须在调用[on](arkts-dataprotection-dlppermission-onopendlpfile-f.md#on_openDLPFile)注册监听后才能调用此方法取消 监听。 DLP管理应用退出或不再需要追踪沙箱状态变化时，取消事件订阅以释放监听资源。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void--><!--Device-dlpPermission-function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'uninstallDLPSandbox' | 是 |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DLPSandboxState](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.off('uninstallDLPSandbox', (info: dlpPermission.DLPSandboxState) => {
  console.info('uninstallDLPSandbox event', info.appIndex, info.bundleName)
}); // 取消订阅。
```
