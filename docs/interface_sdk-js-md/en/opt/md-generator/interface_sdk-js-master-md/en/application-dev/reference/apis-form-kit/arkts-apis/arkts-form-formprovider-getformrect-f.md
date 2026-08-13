# getFormRect

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## getFormRect

```TypeScript
function getFormRect(formId: string): Promise<formInfo.Rect>
```

Obtains the position and dimension of a widget. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-formProvider-function getFormRect(formId: string): Promise<formInfo.Rect>--><!--Device-formProvider-function getFormRect(formId: string): Promise<formInfo.Rect>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;formInfo.Rect & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## Examples

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // formId of the widget. Use the actual form ID.

try {
  formProvider.getFormRect(formId).then((data: formInfo.Rect) => {
    console.info(`getFormRect succeed, data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
