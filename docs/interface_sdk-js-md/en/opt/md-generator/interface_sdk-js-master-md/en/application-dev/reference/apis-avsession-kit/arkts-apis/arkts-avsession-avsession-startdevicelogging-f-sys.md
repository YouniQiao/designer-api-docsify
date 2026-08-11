# startDeviceLogging (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## startDeviceLogging

```TypeScript
function startDeviceLogging(url: string, maxSize?: number): Promise<void>
```

Begin to write device logs into a file descriptor for the purpose of problem locating.If the logs exceed max file size, no logs will be written and DEVICE_LOG_FULL event will be omitted.

**Since:** 13

<!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>--><!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| maxSize | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let file = await fileIo.open("filePath");
let url = file.fd.toString();
avSession.startDeviceLogging(url, 2048).then(() => {
  console.info('Succeeded in starting device logging.');
})
```
