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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16501013](../errorcode-form.md#16501013-operation-not-supported) |

**Examples**

```TypeScript
import { formProvider, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const templateFormInfo: formInfo.TemplateFormDetailInfo[] = [{
    bundleName: 'com.example.ohos.formjsdemo',
    moduleName: 'entry',
    abilityName: 'EntryAbility',
    formName: 'widget',
    dimension: 2,
    detailId: 'detailId',
    displayName: 'displayName',
    description: 'description',
  }];
  formProvider.updateTemplateFormDetailInfo(templateFormInfo).then(() => {
    console.info('updateTemplateFormDetailInfo succeed.');
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message})`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```
