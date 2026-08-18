# connect

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## connect

```TypeScript
function connect(sessionId: int): Promise<ConnectResult>
```

Sets up a UIAbility connection after a collaboration session is created and the session ID is obtained. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function connect(sessionId: int): Promise<ConnectResult>--><!--Device-abilityConnectionManager-function connect(sessionId: int): Promise<ConnectResult>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | int | Yes | ID of the collaboration session. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ConnectResult&gt; | Promise used to return the [connection result]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**Examples**

After an application sets up a collaboration session and obtains the session ID on device A, it calls connect() to set up a UIAbility connection and start the application on device B.

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.connect(sessionId).then((ConnectResult) => {
  if (!ConnectResult.isConnected) {
    hilog.info(0x0000, 'testTag', 'connect failed');
    return;
  }
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

