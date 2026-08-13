# offDeviceFound

## Modules to Import

```TypeScript
import { scan } from '@kit.ConnectivityKit';
```

## offDeviceFound

```TypeScript
function offDeviceFound(callback?: Callback<ScanResults[]>): void
```

Unsubscribes from NearLink scan results.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void--><!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScanResults](arkts-connectivity-scan-scanresults-i.md)[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
