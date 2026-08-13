# offFoldStatusChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offFoldStatusChange

```TypeScript
function offFoldStatusChange(callback?: Callback<FoldStatus>): void
```

Unregister the callback for fold status changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void--><!--Device-display-function offFoldStatusChange(callback?: Callback<FoldStatus>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldStatus&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
