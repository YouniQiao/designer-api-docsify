# closeFormEditAbility

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## closeFormEditAbility

```TypeScript
function closeFormEditAbility(isMainPage?: boolean): void
```

Closes the widget editing page.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-formProvider-function closeFormEditAbility(isMainPage?: boolean): void--><!--Device-formProvider-function closeFormEditAbility(isMainPage?: boolean): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMainPage | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16501015](../errorcode-form.md#16501015-failed-to-close-semimodal-widget-editing-page-of-another-application) |

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
          try {
            formProvider.closeFormEditAbility();
            console.info(`${TAG} close FormEditAbility success.`);
          } catch (error) {
            console.error(`${TAG} close FormEditAbility failed, code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
