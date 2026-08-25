# getPublishedFormInfoById

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedFormInfoById

```TypeScript
function getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>
```

Obtains the information of the widget that has been added to the home screen on the device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This field is supported since API version 18 and deprecated since API version 20. You are advised to use
> [getPublishedRunningFormInfoById](arkts-form-formprovider-getpublishedrunningforminfobyid-f.md) instead.

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [getPublishedRunningFormInfoById](arkts-form-formprovider-getpublishedrunningforminfobyid-f.md)

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;formInfo.FormInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
