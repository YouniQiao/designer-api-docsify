# startScan

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## startScan

```TypeScript
function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>
```

开始使用过滤器扫描指定的NearLink设备。如果不想使用过滤器，可以将过滤器参数设置为{@code null}。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>--><!--Device-scan-function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | ScanFilters[] \| null | Yes | 过滤器列表，必选。 如果不需要使用filter，可以设置为{@code null}。 如果要使用过滤器，至少要设置一个过滤器。 |
| options | [ScanOptions](arkts-connectivity-bluetoothmanager-scanoptions-i.md) | No | 扫描的参数。 默认为低功率模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100042 | Empty array. |
| 36100040 | Integer out of range. |
| 36100041 | Invalid address. |

