# getServiceDump

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getServiceDump

```TypeScript
function getServiceDump(serviceid : number, fd : number, args : Array<string>) : void
```

Obtains system service information.It need dump permission.This API can be called only by system application.

**Since:** 9

**Required permissions:** ohos.permission.DUMP

<!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void--><!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serviceid | number | Yes |
| fd | number | Yes |
| args | Array&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [11400101](../errorcode-hiviewdfx-hidebug.md#11400101-failed-to-obtain-the-system-service) |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let fileFd = -1;
try {
  // Obtain the context from the component and ensure that the return value of this.getUiContext().getHostContext() is UIAbilityContext.
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
