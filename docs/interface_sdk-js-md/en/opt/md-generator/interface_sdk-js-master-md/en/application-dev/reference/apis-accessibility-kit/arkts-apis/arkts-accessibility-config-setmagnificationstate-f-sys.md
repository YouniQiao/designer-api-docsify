# setMagnificationState (System API)

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## setMagnificationState

```TypeScript
function setMagnificationState(state: boolean): void
```

Sets the magnification state. Ensure that magnification is enabled before calling this API.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function setMagnificationState(state: boolean): void--><!--Device-config-function setMagnificationState(state: boolean): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9300007](../errorcode-accessibility.md#9300007-magnification-trigger-failed) |

## Examples

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  config.setMagnificationState(true);
} catch (err) {
  let e = err as BusinessError;
  console.error(`Failed to set magnification. Code: ${e.code}, message: ${e.message}`);
}
```
