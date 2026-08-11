# stopBlinking (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## stopBlinking

```TypeScript
function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode
```

Stop the flash or screen to blink for flash alert.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode--><!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlinkingMode](arkts-accessibility-config-blinkingmode-e-sys.md) | Yes | Indicates the mode of screen flickering or flash light flashing. |
| scenario | [BlinkingScenario](arkts-accessibility-config-blinkingscenario-e-sys.md) | Yes | Indicates the scenario that blinking is triggered. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlinkResultCode](arkts-accessibility-config-blinkresultcode-e-sys.md) | Returns the result code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. &lt;br&gt;A non-system application calls a system API. |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) | System abnormality.Possible causes: &lt;br&gt;1.Internal operation failed. &lt;br&gt;2.Failed to obtain the required service or client object (null pointer). &lt;br&gt;3.IPC communication failed. &lt;br&gt;4.Failed to obtain the accessibility service proxy. |

