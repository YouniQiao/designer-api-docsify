# newSEService

## Modules to Import

```TypeScript
import { omapi } from 'kits/@kit.ConnectivityKit';
```

## newSEService

```TypeScript
function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService
```

Establish a new connection that can be used to connect to all the SEs available in the system.The connection process can be quite long, so it happens in an asynchronous way. It is usable only if the specified callback is called or if isConnected() returns true.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Substitutes:** [omapi#createService](arkts-connectivity-omapi-createservice-f.md#createservice)

<!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService--><!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'serviceState' | Yes | nfc serviceState |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ServiceState&gt; | Yes | The callback to return the service. |

**Return value:**

| Type | Description |
| --- | --- |
| [SEService](arkts-connectivity-omapi-seservice-i.md) | The new SEService instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

## Examples

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    // Obtain the service.
    try {
        seService = omapi.newSEService("serviceState", (state) => {
        hilog.info(0x0000, 'testTag', 'se service state = %{public}s', JSON.stringify(state));
        });
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'newSEService error %{public}s', JSON.stringify(error));
    }
    if (seService == undefined || !seService.isConnected()) {
        hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
        return;
    }
}
```

