# stopDeviceLogging (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## stopDeviceLogging

```TypeScript
function stopDeviceLogging(): Promise<void>
```

Stop the current device written even the discovery is ongoing.

**Since:** 13

<!--Device-avSession-function stopDeviceLogging(): Promise<void>--><!--Device-avSession-function stopDeviceLogging(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
avSession.stopDeviceLogging().then(() => {
  console.info('Succeeded in stopping casting.');
});
```
