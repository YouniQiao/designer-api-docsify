# onGetFormRect (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## onGetFormRect

```TypeScript
function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void
```

Listens to the event of get form rect.You can use this method to listen to the event of get form rect.

**Since:** 23

<!--Device-formHost-function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void--><!--Device-formHost-function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.GetFormRectInfoCallback | Yes | The callback of get form rect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

