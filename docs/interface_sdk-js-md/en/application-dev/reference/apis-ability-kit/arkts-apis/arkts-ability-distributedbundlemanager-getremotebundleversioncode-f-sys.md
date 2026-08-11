# getRemoteBundleVersionCode (System API)

## Modules to Import

```TypeScript
import { distributedBundleManager } from 'kits/@kit.AbilityKit';
```

## getRemoteBundleVersionCode

```TypeScript
function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<long>
```

Obtains the version information of an app with a specified bundle name on a specified remote device.This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedBundleManager-function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<long>--><!--Device-distributedBundleManager-function getRemoteBundleVersionCode(deviceId: string, bundleName: string): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | ID of the remote device. You can call getAvailableDeviceList to obtain all trusted device lists. The value is the networkId field in the trusted device information. |
| bundleName | string | Yes | Bundle name of the app. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise object. If the call succeeds, the version information is returned; if the call fails, an error object is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [17700027](../errorcode-bundle.md#17700027-distributed-service-is-not-started) | The distributed service is not running. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [17700007](../errorcode-bundle.md#17700007-incorrect-device-id) | The specified device ID is not found. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle name is not found. |

