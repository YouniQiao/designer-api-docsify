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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>--><!--Device-avSession-function getDistributedSessionController(distributedSessionType: DistributedSessionType): Promise<Array<AVSessionController>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes | Specifies the distributed session type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; | Promise for AVSessionController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied |
| [6600109](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600109-remote-session-does-not-exist) | The remote connection is not established. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

avSession.getDistributedSessionController(avSession.DistributedSessionType.TYPE_SESSION_REMOTE).then((sessionControllers: Array<avSession.AVSessionController>) => {
  console.info(`getDistributedSessionController : SUCCESS : sessionControllers.length : ${sessionControllers.length}`);
}).catch((err: BusinessError) => {
  console.error(`getDistributedSessionController BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

