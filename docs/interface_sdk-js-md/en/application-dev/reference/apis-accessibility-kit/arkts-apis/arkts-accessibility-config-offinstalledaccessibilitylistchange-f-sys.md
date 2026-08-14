# offInstalledAccessibilityListChange (System API)

## Modules to Import

```TypeScript
import { config } from 'config';
```

## offInstalledAccessibilityListChange

```TypeScript
function offInstalledAccessibilityListChange(callback?: Callback<void>): void
```

Unregister listener that watches for changes in the installed status of accessibility extensions.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function offInstalledAccessibilityListChange(callback?: Callback<void>): void--><!--Device-config-function offInstalledAccessibilityListChange(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Indicates the listener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

