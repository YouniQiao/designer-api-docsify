# createStream (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## createStream

```TypeScript
function createStream(sessionId: number, param: StreamParam): Promise<number>
```

Creating a Stream.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function createStream(sessionId: int, param: StreamParam): Promise<int>--><!--Device-abilityConnectionManager-function createStream(sessionId: int, param: StreamParam): Promise<int>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| param | [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [32300004](../../apis-distributedservice-kit/errorcode-device-manager.md#32300004-color-space-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [32300001](../../apis-distributedservice-kit/errorcode-device-manager.md#32300001-transport-stream-repeatedly-created) |
| [32300003](../../apis-distributedservice-kit/errorcode-device-manager.md#32300003-bit-rate-not-supported) |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'startStream');
let sessionId = 100;
abilityConnectionManager.createStream(sessionId ,{name: 'receive', role: 0}).then(async (streamId) => {
  let surfaceParam: abilityConnectionManager.SurfaceParam = {
    width: 640,
    height: 480,
    format: 1
  }
  let surfaceId = abilityConnectionManager.getSurfaceId(streamId, surfaceParam);
  hilog.info(0x0000, 'testTag', 'surfaceId is'+surfaceId);
  AppStorage.setOrCreate<string>('surfaceId', surfaceId);
  abilityConnectionManager.startStream(streamId);
})
```
