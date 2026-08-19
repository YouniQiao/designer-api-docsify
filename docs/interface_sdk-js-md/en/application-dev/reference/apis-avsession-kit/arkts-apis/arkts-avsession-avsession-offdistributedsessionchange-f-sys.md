# offDistributedSessionChange (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## offDistributedSessionChange

```TypeScript
function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void
```

Unregister distributed session changed callback

**Since:** 23

<!--Device-avSession-function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes | Indicates the distributed session type |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; | No | The callback will return remote changed AVSessionController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

