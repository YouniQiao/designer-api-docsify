# getServiceDump

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getServiceDump

```TypeScript
function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void
```

��ȡϵͳ������Ϣ��

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DUMP

<!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void--><!--Device-hidebug-function getServiceDump(serviceid : int, fd : int, args : Array<string>) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serviceid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ϵͳ����ID�����ڱ�ʶҪ��ȡ��Ϣ��ϵͳ����ȡֵ��ϵͳ���壬ȡֵ��Χ[0, 255]��������Чֵʱ���ش�����401�� |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | �ļ����������ӿڻ����fdд�����ݡ�������Ч�ļ�������ʱ���ش�����401�� |
| args | Array&lt;string&gt; | Yes | ϵͳ�����dump�ӿڲ����б���string���ȵ����ֵΪ254���������ֽ��ᱻ�ضϡ� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | the parameter check failed, Possible causes: 1.the parameter type error 2.the args parameter is not string array |
| 11400101 | ServiceId invalid. The system ability does not exist. |

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

