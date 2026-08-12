# createCdsmClient

## Modules to Import

```TypeScript
import { cdsm } from '@kit.ConnectivityKit';
```

## createCdsmClient

```TypeScript
function createCdsmClient(address: string): CdsmClient
```

Creates a CDSM client instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-cdsm-function createCdsmClient(address: string): CdsmClient--><!--Device-cdsm-function createCdsmClient(address: string): CdsmClient-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string | Yes | Indicates the address of CDSM server. &lt;br&gt;The length must be 17. Value constraint: The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF. |

**Return value:**

| Type | Description |
| --- | --- |
| [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) | Returns a CDSM client instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100050 | Coordinated Devices Set Management not supported. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100041 | Invalid address. |

