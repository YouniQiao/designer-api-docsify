# isEthernetEnabled (System API)

## Modules to Import

```TypeScript
import { ethernet } from '@kit.NetworkKit';
```

## isEthernetEnabled

```TypeScript
function isEthernetEnabled(): boolean
```

Check whether the global ethernet switch is enabled.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-ethernet-function isEthernetEnabled(): boolean--><!--Device-ethernet-function isEthernetEnabled(): boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if ethernet is globally enabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) | Internal error. |
| [2200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) | Operation failed. Cannot connect to service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

