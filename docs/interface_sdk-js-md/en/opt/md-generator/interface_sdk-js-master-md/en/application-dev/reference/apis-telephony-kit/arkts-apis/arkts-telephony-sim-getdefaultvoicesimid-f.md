# getDefaultVoiceSimId

## Modules to Import

```TypeScript
```

## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(callback: AsyncCallback<number>): void
```

Obtains the default SIM ID for the voice service.

**Since:** 23

<!--Device-sim-function getDefaultVoiceSimId(callback: AsyncCallback<int>): void--><!--Device-sim-function getDefaultVoiceSimId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(): Promise<number>
```

Obtains the default SIM ID for the voice service.

**Since:** 23

<!--Device-sim-function getDefaultVoiceSimId(): Promise<int>--><!--Device-sim-function getDefaultVoiceSimId(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let promise = sim.getDefaultVoiceSimId();
promise.then((data: number) => {
    console.info(`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}`);
});
```
