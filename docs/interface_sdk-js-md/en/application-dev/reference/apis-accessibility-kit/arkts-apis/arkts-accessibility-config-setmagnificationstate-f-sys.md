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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function setMagnificationState(state: boolean): void--><!--Device-config-function setMagnificationState(state: boolean): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | boolean | Yes | Whether to trigger or disable the magnification feature.&lt;br&gt;- **true**: to trigger the magnification feature.&lt;br&gt;- **false**: to disable the magnification feature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [9300007](../errorcode-accessibility.md#9300007-magnification-trigger-failed) | Trigger magnification failed. |

