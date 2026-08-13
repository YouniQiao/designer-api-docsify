# updateTemplateFormDetailInfo (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## updateTemplateFormDetailInfo

```TypeScript
function updateTemplateFormDetailInfo(templateFormInfo: Array<formInfo.TemplateFormDetailInfo>): Promise<void>
```

Updates the static configuration information of a specified template widget on the current device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-formProvider-function updateTemplateFormDetailInfo(templateFormInfo: Array<formInfo.TemplateFormDetailInfo>): Promise<void>--><!--Device-formProvider-function updateTemplateFormDetailInfo(templateFormInfo: Array<formInfo.TemplateFormDetailInfo>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateFormInfo | Array & lt;formInfo.TemplateFormDetailInfo & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16501013](../errorcode-form.md#16501013-operation-not-supported) |
