# queryProbeResult

## Modules to Import

```TypeScript
```

## queryProbeResult

```TypeScript
function queryProbeResult(destination: string, duration: number): Promise<ProbeResultInfo>
```

Query a network probe result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>--><!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](arkts-network-connection-routeinfo-i.md) | string | Yes |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ProbeResultInfo](arkts-network-connection-proberesultinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dest: string = "www.example.com";
let duration: number = 10;

connection.queryProbeResult(dest, duration).then((data: connection.ProbeResultInfo) => {
    console.info(`LossRate: ${data.lossRate}, RTT: ${data.rtt}`);
}).catch((err: BusinessError) => {
    console.error(JSON.stringify(err));
});
```
