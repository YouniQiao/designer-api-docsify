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

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode--><!--Device-config-function stopBlinking(mode: BlinkingMode, scenario: BlinkingScenario): BlinkResultCode-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [BlinkingMode](arkts-accessibility-config-blinkingmode-e-sys.md) | Yes |
| scenario | [BlinkingScenario](arkts-accessibility-config-blinkingscenario-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BlinkResultCode](arkts-accessibility-config-blinkresultcode-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) |

## Examples

```TypeScript
import { config } from '@kit.AccessibilityKit';

try {
  let code: config.BlinkResultCode = config.stopBlinking(config.BlinkingMode.SINGLE_BLINK, config.BlinkingScenario.ALARM);
  console.info(`Succeeded in stopBlinking, result code: ${code}`);
} catch (err) {
  console.error(`Failed to call stopBlinking, code is ${err.code}, message is ${err.message}`);
}
```
