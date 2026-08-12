# openFormEditAbility

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## openFormEditAbility

```TypeScript
function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void
```

Opens the widget editing page.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-formProvider-function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void--><!--Device-formProvider-function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| abilityName | string | Yes | Ability name on the editing page. |
| formId | string | Yes | Widget ID. |
| isMainPage | boolean | No | Whether the page is the main editing page.&lt;br&gt;- **true**: The page is the main editing page.&lt;br&gt;- **false**: The page is not the main editing page.&lt;br&gt;Default value: **true**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) | The form cannot be operated by the current application. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.function openFormEditAbility cannot work correctly due to limited device capabilities. |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16501007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501007-untrusted-widget) | Form is not trust. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formProvider } from '@kit.FormKit';

const TAG: string = 'FormEditDemo-Page] -->';

@Entry
@Component
struct Page {
  @State message: string = 'Hello World';

  aboutToAppear(): void {
    console.info(`${TAG} aboutToAppear.....`);
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('PageHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Top },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          console.info(`${TAG} onClick.....`);
          formProvider.openFormEditAbility('ability://EntryFormEditAbility', '1386529921');
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

