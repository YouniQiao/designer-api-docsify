# stopDeviceLogging (System API)

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## stopDeviceLogging

```TypeScript
function stopDeviceLogging(): Promise<void>
```

Stop the current device written even the discovery is ongoing.

**Since:** 23

<!--Device-avSession-function stopDeviceLogging(): Promise<void>--><!--Device-avSession-function stopDeviceLogging(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise for the result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avSession.stopDeviceLogging().then(() => {
  console.info('stopCasting successfully');
}).catch((err: BusinessError) => {
  console.error(`stopCasting BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

