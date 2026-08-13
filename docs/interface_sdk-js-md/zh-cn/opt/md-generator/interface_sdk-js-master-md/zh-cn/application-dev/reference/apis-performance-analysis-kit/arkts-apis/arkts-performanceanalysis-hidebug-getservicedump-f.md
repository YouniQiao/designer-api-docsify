# getServiceDump

## getServiceDump

```TypeScript
function getServiceDump(serviceid : number, fd : number, args : Array<string>) : void
```

获取系统服务信息。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.DUMP

<!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void--><!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| serviceid | number | 是 |
| fd | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11400101](../errorcode-hiviewdfx-hidebug.md#11400101-系统服务获取失败) |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileFd = -1;
try {
  // 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext。
  let path: string = this.getUIContext().getHostContext()!.filesDir + "/serviceInfo.txt";
  console.info("output path: " + path);
  fileFd = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).fd;
  let serviceId: number = 10;
  let args: Array<string> = new Array("allInfo");
  hidebug.getServiceDump(serviceId, fileFd, args);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}

if (fileFd >= 0) {
  fileIo.closeSync(fileFd);
}
```
