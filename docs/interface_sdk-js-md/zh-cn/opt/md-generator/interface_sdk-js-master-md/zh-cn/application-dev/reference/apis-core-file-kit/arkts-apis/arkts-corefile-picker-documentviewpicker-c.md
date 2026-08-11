# DocumentViewPicker

文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

**起始版本：** 9

<!--Device-picker-class DocumentViewPicker--><!--Device-picker-class DocumentViewPicker-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor()
```

创建DocumentViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-constructor()--><!--Device-DocumentViewPicker-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

## 示例

```TypeScript
let documentPicker = new picker.DocumentViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

## constructor

```TypeScript
constructor(context: Context)
```

创建DocumentViewPicker对象，推荐使用该构造函数，获取context参考  
[getHostContext](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext12)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-constructor(context: Context)--><!--Device-DocumentViewPicker-constructor(context: Context)-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let documentPicker = new picker.DocumentViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## constructor

```TypeScript
constructor(context: Context, window: window.Window)
```

应用自行创建窗口中，可用通过该构造函数创建DocumentViewPicker对象。一般场景推荐使用constructor(context: Context)方法创建DocumentViewPicker对象。

> **说明：**
> 
> 从API version 19开始，2in1和Tablet设备支持该方法。

**起始版本：** 13

<!--Device-DocumentViewPicker-constructor(context: Context, window: window.Window)--><!--Device-DocumentViewPicker-constructor(context: Context, window: window.Window)-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [window](../../apis-arkui/arkts-components/arkts-arkui-window-t.md) | window.Window | 是 |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
import { window } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 请确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let windowClass: window.Window | undefined = undefined;
            windowClass = window.findWindow('test'); // 请确保window已创建，此处的'test'为window创建时的name参数
            let documentPicker = new picker.DocumentViewPicker(context, windowClass);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## getSelectedIndex

```TypeScript
getSelectedIndex(): number
```

获取保存成功后的文件后缀类型的下标。该方法只在调用 [save()](arkts-corefile-picker-documentviewpicker-c.md#save)时使用生效，其他场景下不适用。该方法需要配置参数[DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md)。该方法返回的是所选后缀类型的下标(number)。所选的后缀类型是开发者所传的参数  
[DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md)里的某个后缀类型。如果没有传参，并且调用了getSelectedIndex()方法，返回值为-1。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-getSelectedIndex(): int--><!--Device-DocumentViewPicker-getSelectedIndex(): int-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService.FolderSelection

**返回值：**

| 类型 |
| --- |
| number |

## save

```TypeScript
save(option?: DocumentSaveOptions): Promise<Array<string>>
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-save(option?: DocumentSaveOptions): Promise<Array<string>>--><!--Device-DocumentViewPicker-save(option?: DocumentSaveOptions): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example10(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = ['DocumentViewPicker01.txt'];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError) => {
      console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## save

```TypeScript
save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void--><!--Device-DocumentViewPicker-save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example11(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = ['DocumentViewPicker02.txt'];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions, (err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-save(callback: AsyncCallback<Array<string>>): void--><!--Device-DocumentViewPicker-save(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example12(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save((err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## select

```TypeScript
select(option?: DocumentSelectOptions): Promise<Array<string>>
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-select(option?: DocumentSelectOptions): Promise<Array<string>>--><!--Device-DocumentViewPicker-select(option?: DocumentSelectOptions): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example07(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## select

```TypeScript
select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void--><!--Device-DocumentViewPicker-select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example08(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions, (err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## select

```TypeScript
select(callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-DocumentViewPicker-select(callback: AsyncCallback<Array<string>>): void--><!--Device-DocumentViewPicker-select(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
async function example09(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select((err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```
