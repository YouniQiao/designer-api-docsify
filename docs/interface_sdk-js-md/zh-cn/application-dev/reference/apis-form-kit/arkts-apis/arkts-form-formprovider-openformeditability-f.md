# openFormEditAbility

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormEditAbility

```TypeScript
function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void
```

Opens the widget editing page.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-formProvider-function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void--><!--Device-formProvider-function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityName | string | 是 | Ability name on the editing page. |
| formId | string | 是 | Widget ID. |
| isMainPage | boolean | 否 | Whether the page is the main editing page.&lt;br&gt;- **true**: The page is the main editing page.&lt;br&gt;- **false**: The page is not the main editing page.&lt;br&gt;Default value: **true**. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 801 | Capability not supported.function openFormEditAbility cannot work correctly due to limited device capabilities. |
| 16501000 | An internal functional error occurred. |
| 16501007 | Form is not trust. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

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

