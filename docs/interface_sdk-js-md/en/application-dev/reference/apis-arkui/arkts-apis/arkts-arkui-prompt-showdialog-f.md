# showDialog

## Modules to Import

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void
```

Displays the dialog box.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** showDialog

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ShowDialogSuccessResponse&gt; | Yes |


## showDialog

```TypeScript
function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>
```

Displays the dialog box.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** showDialog

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ShowDialogSuccessResponse & gt; |
