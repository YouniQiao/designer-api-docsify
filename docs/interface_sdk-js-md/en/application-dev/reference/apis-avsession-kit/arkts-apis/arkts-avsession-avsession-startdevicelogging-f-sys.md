# startDeviceLogging (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## startDeviceLogging

```TypeScript
function startDeviceLogging(url: string, maxSize?: int): Promise<void>
```

Begin to write device logs into a file descriptor for the purpose of problem locating.If the logs exceed max file size, no logs will be written and DEVICE_LOG_FULL event will be omitted.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>--><!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The file descriptor to be written. |
| maxSize | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | The max size to be written in kilobyte. if not set, then written process will exit when there is no space to write. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let file = await fileIo.open("filePath");
let url = file.fd.toString();
avSession.startDeviceLogging(url, 2048).then(() => {
  console.info('startDeviceLogging successfully');
}).catch((err: BusinessError) => {
  console.error(`startDeviceLogging BusinessError: code: ${err.code}, message: ${err.message}`);
})
```

