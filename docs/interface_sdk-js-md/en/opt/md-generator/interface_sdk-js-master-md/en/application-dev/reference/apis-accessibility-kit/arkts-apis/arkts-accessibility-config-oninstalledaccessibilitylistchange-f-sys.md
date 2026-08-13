# onInstalledAccessibilityListChange (System API)

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## onInstalledAccessibilityListChange

```TypeScript
function onInstalledAccessibilityListChange(callback: Callback<void>): void
```

Register the listener that watches for changes in the installed status of accessibility extensions.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function onInstalledAccessibilityListChange(callback: Callback<void>): void--><!--Device-config-function onInstalledAccessibilityListChange(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
