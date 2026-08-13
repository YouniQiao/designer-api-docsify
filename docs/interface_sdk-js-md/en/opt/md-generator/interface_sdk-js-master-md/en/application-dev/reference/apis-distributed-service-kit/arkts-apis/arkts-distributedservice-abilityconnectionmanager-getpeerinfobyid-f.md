# getPeerInfoById

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## getPeerInfoById

```TypeScript
function getPeerInfoById(sessionId: number): PeerInfo | undefined
```

Obtains information about the peer application in the specified session.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | undefined--><!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | undefined-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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
function getPeerInfoById(sessionId: number): PeerInfo | null
```

Get the application information in the ability connection session

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | null--><!--Device-abilityConnectionManager-function getPeerInfoById(sessionId: int): PeerInfo | null-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PeerInfo](arkts-distributedservice-abilityconnectionmanager-peerinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
