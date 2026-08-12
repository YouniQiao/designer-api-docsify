# createPort

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## createPort

```TypeScript
function createPort(uuid: string): void
```

Creates a NearLink listening port that can receive data by UUID.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function createPort(uuid: string): void--><!--Device-dataTransfer-function createPort(uuid: string): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | string | Yes | Indicates application service UUID. &lt;br&gt;The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier. &lt;br&gt;NearLink standard UUIDs not allowed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100020 | The UUID is already registered. |
| 36100021 | Port exceeds the upper limit. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID. |

