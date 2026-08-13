# onWaterMarkFlagChange (System API)

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## onWaterMarkFlagChange

```TypeScript
function onWaterMarkFlagChange(callback: Callback<boolean>): void
```

Subscribes to the watermark status change event.

**Since:** 23

**Deprecated since:** -1

<!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void--><!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
