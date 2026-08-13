# updateFormSize (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## updateFormSize

```TypeScript
function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void
```

Updates the size of the widget.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void--><!--Device-formHost-function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| newDimension | formInfo.FormDimension | Yes |
| newRect | formInfo.Rect | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16501012](../errorcode-form.md#16501012-incorrect-widget-dimension) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let formId: string = '12400633174999288';
  let newDimension = formInfo.FormDimension.Dimension_1_2;
  let newRect: formInfo.Rect = {
    left: 1,
    top: 2,
    width: 100,
    height: 100
  };
  formHost.updateFormSize(formId, newDimension, newRect);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
