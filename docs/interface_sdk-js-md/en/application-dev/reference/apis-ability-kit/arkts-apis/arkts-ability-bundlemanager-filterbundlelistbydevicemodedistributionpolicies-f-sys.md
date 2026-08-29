# filterBundleListByDeviceModeDistributionPolicies (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## filterBundleListByDeviceModeDistributionPolicies

```TypeScript
function filterBundleListByDeviceModeDistributionPolicies(
    policies: Array<DeviceModeDistributionPolicy>): Promise<void>
```

Filters the bundle list by device mode distribution policies. This API uses a promise to return the result.

> **NOTE：**
> 
> The input parameter cannot be empty. All values must be within the range of the enumerated values of
> DeviceModeDistributionPolicy, and the policies for all different packages
> (UNIVERSAL_DIFFERENT_PACKAGE, PARTIAL_COMPATIBLE_DIFFERENT_PACKAGE, and FULL_COMPATIBLE_DIFFERENT_PACKAGE)
> must be included.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policies | Array&lt;[DeviceModeDistributionPolicy](arkts-ability-bundlemanager-devicemodedistributionpolicy-e-sys.md)&gt; | Yes | Array of DeviceModeDistributionPolicy values. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Non-system APP calling system API. |
| 17700097 | The device does not support the dual mode. |
| 17700098 | The input parameter is invalid. It is either outside the range of valid enum values or does not include the following required enum values: [DeviceModeDistributionPolicy.UNIVERSAL_DIFFERENT_PACKAGE, DeviceModeDistributionPolicy.PARTIAL_COMPATIBLE_DIFFERENT_PACKAGE, DeviceModeDistributionPolicy.FULL_COMPATIBLE_DIFFERENT_PACKAGE]. |
| 17700099 | The device is installing or uninstalling an application, or a previous API call is still being processed. Please try again. |
