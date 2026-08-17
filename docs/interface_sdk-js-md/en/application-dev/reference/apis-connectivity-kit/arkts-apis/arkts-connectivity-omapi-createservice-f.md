# createService

## Modules to Import

```TypeScript
import { omapi } from 'omapi';
```

## createService

```TypeScript
function createService(): Promise<SEService>
```

Establish a new connection that can be used to connect to all the SEs available in the system. The connection process can be quite long, so it happens in an asynchronous way. It is usable only if isConnected() returns true.

**Since:** 12

<!--Device-omapi-function createService(): Promise<SEService>--><!--Device-omapi-function createService(): Promise<SEService>-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[SEService](arkts-connectivity-omapi-seservice-i.md)&gt; | Returns the created SEService instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    omapi.createService().then((data) => {
        seService = data;
        if (seService == undefined || !seService.isConnected()) {
            hilog.error(0x0000, 'testTag', 'seservice state disconnected');
            return;
        }
        hilog.info(0x0000, 'testTag', 'seservice state connected');
    }).catch((error : BusinessError)=> {
        hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
    });
}
```

