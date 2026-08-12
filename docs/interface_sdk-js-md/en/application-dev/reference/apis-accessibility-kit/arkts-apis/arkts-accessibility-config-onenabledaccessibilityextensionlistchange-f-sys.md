# onEnabledAccessibilityExtensionListChange (System API)

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## onEnabledAccessibilityExtensionListChange

```TypeScript
function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void
```

Register the listener that watches for changes in the enabled status of accessibility extensions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void--><!--Device-config-function onEnabledAccessibilityExtensionListChange(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

