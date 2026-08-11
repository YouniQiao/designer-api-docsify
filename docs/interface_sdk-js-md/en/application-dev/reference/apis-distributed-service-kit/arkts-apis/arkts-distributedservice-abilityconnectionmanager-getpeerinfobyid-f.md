# getPeerInfoById

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## getPeerInfoById

```TypeScript
function getPeerInfoById(sessionId: int): PeerInfo | undefined
```

Obtains information about the peer application in the specified session.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | undefined--><!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | undefined-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | ID of the collaboration session. |

**Return value:**

| Type | Description |
| --- | --- |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) | Information about the peer application if the corresponding **peerInfo** exists; **undefined** if the session ID is not found. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'getPeerInfoById called');
let sessionId = 100;
const peerInfo = abilityConnectionManager.getPeerInfoById(sessionId);
```


## getPeerInfoById

```TypeScript
function getPeerInfoById(sessionId: int): PeerInfo | null
```

Get the application information in the ability connection session

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | null--><!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | null-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | Ability connection Session id. |

**Return value:**

| Type | Description |
| --- | --- |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) | Returns the collaborative application information at the sink end. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

