# setSurfaceId (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## setSurfaceId

```TypeScript
function setSurfaceId(streamId: int, surfaceId: string, param: SurfaceParam): void
```

Sets the transmission surface.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function setSurfaceId(streamId: int, surfaceId: string, param: SurfaceParam): void--><!--Device-abilityConnectionManager-function setSurfaceId(streamId: int, surfaceId: string, param: SurfaceParam): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of a transport stream. |
| surfaceId | string | Yes | Surface ID. |
| param | [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | Yes | Surface Parameters |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'setSurfaceId');
let sessionId = 100;
abilityConnectionManager.createStream(sessionId ,{name: 'receive', role: 0}).then(async (streamId) => {
  let surfaceParam: abilityConnectionManager.SurfaceParam = {
    width: 640,
    height: 480,
    format: 1
  }
  let surfaceId = abilityConnectionManager.getSurfaceId(streamId, surfaceParam);
  abilityConnectionManager.setSurfaceId(streamId, surfaceId, surfaceParam);
})
```

