# stopPassiveRanging

## Modules to Import

```TypeScript
import { ranging } from '@kit.ConnectivityKit';
```

## stopPassiveRanging

```TypeScript
function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void
```

Stops passive ranging mode.

Stops the passive ranging broadcast and cleans up associated resources based on the specified handle and ranging capability type.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void--><!--Device-ranging-function stopPassiveRanging(handle: int, capabilityType: RangingTypes): void-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the handle number of ranging monitoring. |
| capabilityType | [RangingTypes](arkts-connectivity-ranging-rangingtypes-e.md) | Yes | Indicates the capability type for ranging. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 34900052 | The specified type of ranging service is not supported. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 34900054 | The parameter value does not meet specifications. |
| [34900099](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-fusionConnectivity.md#34900099-operation-failed) | Internal system error. For example, Internal object is invalid. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

