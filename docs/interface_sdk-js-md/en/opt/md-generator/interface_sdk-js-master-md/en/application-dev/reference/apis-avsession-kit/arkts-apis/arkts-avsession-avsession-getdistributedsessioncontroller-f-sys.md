# getDistributedSessionController (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## getDistributedSessionController

```TypeScript
function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>
```

Get distributed avsession controller

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>--><!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { avSession } from '@kit.AVSessionKit';

avSession.getDistributedSessionController(avSession.DistributedSessionType.TYPE_SESSION_REMOTE).then((sessionControllers: Array<avSession.AVSessionController>) => {
  console.info(`Succeeded in getting distributed session controller, length: ${sessionControllers.length}`);
});
```
