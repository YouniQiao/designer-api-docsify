# startScan

## Modules to Import

```TypeScript
import { scan } from '@kit.ConnectivityKit';
```

## startScan

```TypeScript
function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>
```

Starts scanning for specified NearLink devices with filters.It is allowed to set filter parameter to {@code null} if you do not want to use filter.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>--><!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | [ScanFilters](arkts-connectivity-scan-scanfilters-i.md)[] \| null | Yes | The list of filters and this parameter is mandatory. If you do not want to use filter, set this parameter to {@code null}. If you want to use filter, at least one filter should be set. |
| options | ScanOptions | No | The parameters for scanning, and the low power mode is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise object is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100042 | Empty array. |
| 36100040 | Integer out of range. |
| 36100041 | Invalid address. |

