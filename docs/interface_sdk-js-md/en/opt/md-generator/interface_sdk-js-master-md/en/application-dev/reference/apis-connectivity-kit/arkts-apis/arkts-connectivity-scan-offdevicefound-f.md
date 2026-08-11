# offDeviceFound

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## offDeviceFound

```TypeScript
function offDeviceFound(callback?: Callback<ScanResults[]>): void
```

Unsubscribes from NearLink scan results.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void--><!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ScanResults[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
