# onFoldStatusChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onFoldStatusChange

```TypeScript
function onFoldStatusChange(callback: Callback<FoldStatus>): void
```

Register the callback for fold status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function onFoldStatusChange(callback: Callback<FoldStatus>): void--><!--Device-display-function onFoldStatusChange(callback: Callback<FoldStatus>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;FoldStatus&gt; | Yes | Callback used to return the current fold status of device |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

