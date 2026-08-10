# offEnabledAccessibilityExtensionListChange (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## offEnabledAccessibilityExtensionListChange

```TypeScript
function offEnabledAccessibilityExtensionListChange(callback?: Callback<void>): void
```

Unregister listener that watches for changes in the enabled status of accessibility extensions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function offEnabledAccessibilityExtensionListChange(callback?: Callback<void>): void--><!--Device-config-function offEnabledAccessibilityExtensionListChange(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |

