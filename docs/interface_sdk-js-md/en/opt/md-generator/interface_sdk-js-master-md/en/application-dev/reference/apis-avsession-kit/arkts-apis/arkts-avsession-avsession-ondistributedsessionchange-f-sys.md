# onDistributedSessionChange (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## onDistributedSessionChange

```TypeScript
function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void
```

Register distributed session changed callback

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
