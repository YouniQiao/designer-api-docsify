# installDLPSandbox（系统接口）

## installDLPSandbox

```TypeScript
function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string): Promise<DLPSandboxInfo>
```

安装一个应用的DLP沙箱。DLP沙箱为受保护的DLP文件创建独立的运行环境，与原应用进程隔离，确保数据在授权范围内安全流转。沙箱应用继承原应用的功能但仅能访问授权的DLP文件。使用Promise异步回调。 调用installDLPSandbox成功后必须在使用完毕后调用 [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox（系统接口）) 卸载沙箱。 DLP文件管理应用打开受保护文件前，需要先为目标应用安装DLP沙箱。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string): Promise<DLPSandboxInfo>--><!--Device-dlpPermission-function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string): Promise<DLPSandboxInfo>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| access | [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) | 是 |
| userId | number | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DLPSandboxInfo](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md)&gt; |

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

let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
dlpPermission.installDLPSandbox('com.ohos.note', dlpPermission.DLPFileAccess.READ_ONLY, 100,
  uri).then((dlpSandboxInfo: dlpPermission.DLPSandboxInfo) => {
  console.info('dlpSandboxInfo: ', JSON.stringify(dlpSandboxInfo));
}).catch((error: BusinessError)=> {
  console.error(error.message);
}); // 安装DLP沙箱。
```


## installDLPSandbox

```TypeScript
function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string, callback: AsyncCallback<DLPSandboxInfo>): void
```

安装一个应用的DLP沙箱。使用callback异步回调。调用成功后，系统为应用创建DLP沙箱环境并返回沙箱信息。 调用installDLPSandbox成功后必须在使用完毕后调用 [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox（系统接口）) 卸载沙箱。 DLP文件管理应用打开受保护文件前，需要先为目标应用安装DLP沙箱。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string, callback: AsyncCallback<DLPSandboxInfo>): void--><!--Device-dlpPermission-function installDLPSandbox(bundleName: string, access: DLPFileAccess, userId: number, uri: string, callback: AsyncCallback<DLPSandboxInfo>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| access | [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) | 是 |
| userId | number | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPSandboxInfo](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md)&gt; | 是 |

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

let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
dlpPermission.installDLPSandbox('com.ohos.note', dlpPermission.DLPFileAccess.READ_ONLY, 100, uri, (err, res) => {
  if (err) {
    console.error('installDLPSandbox error,', err.code, err.message);
  } else {
    console.info('res', JSON.stringify(res));
  }
}); // 安装DLP沙箱。
```
