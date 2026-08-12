# offDiscoveryResult

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## offDiscoveryResult

```TypeScript
function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void--><!--Device-connection-function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;[DiscoveryResult](arkts-connectivity-connection-discoveryresult-i.md)&gt;&gt; | No | Callback used to listen for the discovering event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

