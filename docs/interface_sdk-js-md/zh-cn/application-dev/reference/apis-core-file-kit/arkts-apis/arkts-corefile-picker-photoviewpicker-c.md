# PhotoViewPicker

图库选择器对象，用来支撑选择图片/视频和保存图片/视频等用户场景。选择文件推荐使用 [PhotoAccessHelper的PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-file-photoaccesshelper.md)。 在使用前，需要先创建PhotoViewPicker实例。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

<!--Device-picker-class PhotoViewPicker--><!--Device-picker-class PhotoViewPicker-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

## 导入模块

```TypeScript
import { picker } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoViewPicker-constructor()--><!--Device-PhotoViewPicker-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**示例**

```TypeScript
import { common } from '@kit.AbilityKit';

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

```TypeScript
let documentPicker = new picker.DocumentViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

```TypeScript
import { common } from '@kit.AbilityKit';
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

```TypeScript
import { common } from '@kit.AbilityKit';

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
            let audioPicker = new picker.AudioViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

```TypeScript
let audioPicker = new picker.AudioViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

```TypeScript
import { common } from '@kit.AbilityKit';

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
            let photoPicker = new picker.PhotoViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

```TypeScript
let photoPicker = new picker.PhotoViewPicker(); // 不推荐使用无参构造，会出现概率性拉起失败问题
```

## constructor

```TypeScript
constructor(context: Context)
```

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

<!--Device-PhotoViewPicker-constructor(context: Context)--><!--Device-PhotoViewPicker-constructor(context: Context)-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | 应用上下文（仅支持UIAbilityContext）。 Stage模型的应用Context定义见Context。 |

**示例**

参见 [constructor](#constructor)

## save

```TypeScript
save(option?: PhotoSaveOptions): Promise<Array<string>>
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用Promise异步返回形式， 传入可选参数PhotoSaveOptions对象，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

<!--Device-PhotoViewPicker-save(option?: PhotoSaveOptions): Promise<Array<string>>--><!--Device-PhotoViewPicker-save(option?: PhotoSaveOptions): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | 否 | photoPicker保存图片或视频文件选项。若无此参数， 则拉起photoPicker界面后需用户自行输入保存的文件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise对象。返回photoPicker保存图片或视频文件后的结果集。 <br>**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的 [文档类uri的使用方式](../../../file-management/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example10(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSaveOptions: picker.DocumentSaveOptions = {
      newFileNames: ['DocumentViewPicker01.txt']
    };
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError): void => {
      console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (err: BusinessError) {
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example11(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    const documentSaveOptions: picker.DocumentSaveOptions = {
      newFileNames: ['DocumentViewPicker02.txt'],
      defaultFilePathUri: 'xxx',
      fileSuffixChoices: ['txt|文本文件', 'doc|Word文档'],
      pickerMode: picker.DocumentPickerMode.DEFAULT
    };
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions, (err: BusinessError | null, documentSaveResult: Array<string> | undefined) => {
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

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example12(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save((err: BusinessError | null, documentSaveResult: Array<string> | undefined) => {
      if (err) {
        console.error(`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (err: BusinessError) {
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example16(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions).then((audioSaveResult: Array<string>) => {
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult))
    }).catch((err: BusinessError) => {
      console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example16(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions: picker.AudioSaveOptions = {
      newFileNames: ['AudioViewPicker01.mp3']
    };
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions).then((audioSaveResult: Array<string>) => {
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult))
    }).catch((err: BusinessError): void => {
      console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (err:BusinessError) {
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example17(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = ['AudioViewPicker02.mp3'];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions, (err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example17(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSaveOptions: picker.AudioSaveOptions = {
      newFileNames: ['AudioViewPicker01.mp3']
    };
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions, (err: BusinessError | null, audioSaveResult: Array<string> | undefined) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (err: BusinessError) {
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example18(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save((err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
        console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example18(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save((err: BusinessError | null, audioSaveResult: Array<string> | undefined) => {
      if (err) {
        console.error(`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
        console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example04(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker01.jpg', 'PhotoViewPicker01.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions).then((photoSaveResult: Array<string>) => {
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example05(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker02.jpg','PhotoViewPicker02.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions, (err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error(`PhotoViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example06(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save((err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error(`PhotoViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## save

```TypeScript
save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式， 传入参数PhotoSaveOptions对象，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

<!--Device-PhotoViewPicker-save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void--><!--Device-PhotoViewPicker-save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | 是 | photoPicker保存图片或视频文件选项。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 | callback 返回photoPicker保存图片或视频文件后的结果集。 <br>**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的 [文档类uri的使用方式](../../../file-management/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例**

参见 [save](#save)

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

<!--Device-PhotoViewPicker-save(callback: AsyncCallback<Array<string>>): void--><!--Device-PhotoViewPicker-save(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 | callback 返回photoPicker保存图片或视频文件后的结果集。 <br>**注意**：此接口会将文件保存在文件管理器，而不是图库。返回的uri数组的具体使用方式参见用户文件uri介绍中的 [文档类uri的使用方式](../../../file-management/user-file-uri-intro.md#文档类uri的使用方式)。 |

**示例**

参见 [save](#save)

## select

```TypeScript
select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用Promise异步返回形式， 传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option?: PhotoSelectOptions)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoViewPicker-select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>--><!--Device-PhotoViewPicker-select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | PhotoSelectOptions | 否 | photoPicker选择选项。若无此参数，则默认选择媒体文件类型为图片和视频类型。 选择媒体文件数量的默认最大值为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PhotoSelectResult&gt; | Promise对象。返回photoPicker选择后的结果集。 <br>**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口 [photoAccessHelper.getAssets]{ |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example07(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions: picker.DocumentSelectOptions = {
      selectMode: picker.DocumentSelectMode.MIXED
    };
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    }).catch((err: BusinessError): void => {
      console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (err: BusinessError) {
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example08(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentSelectOptions: picker.DocumentSelectOptions = {
      selectMode: picker.DocumentSelectMode.MIXED
    };
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions, (err: BusinessError|null, documentSelectResult: Array<string>|undefined) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (err: BusinessError) {
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example09(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select((err: BusinessError | null, documentSelectResult: Array<string> | undefined) => {
      if (err) {
        console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (err: BusinessError) {
    console.error(`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example13(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example13(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions: picker.AudioSelectOptions = {
      maxSelectNumber: 5
    };
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    }).catch((err: BusinessError): void => {
      console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (err: BusinessError) {
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example14(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions, (err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example14(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioSelectOptions: picker.AudioSelectOptions = {
      maxSelectNumber: 5
    };
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions, (err: BusinessError | null, audioSelectResult: Array<string> | undefined) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (err: BusinessError) {
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example15(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select((err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

function example15(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select((err: BusinessError | null, audioSelectResult: Array<string> | undefined) => {
      if (err) {
        console.error(`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example01(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions).then((photoSelectResult: picker.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example02(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function example03(context: common.UIAbilityContext) { // 需确保 context 由 UIAbilityContext 转换而来
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select((err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err, code is: ${err.code}, message is: ${err.message}`);
  }
}
```

## select

```TypeScript
select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式， 传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoViewPicker-select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void--><!--Device-PhotoViewPicker-select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | PhotoSelectOptions | 是 | photoPicker选择选项。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | 是 | callback返回photoPicker选择后的结果集。 <br>**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口 [photoAccessHelper.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets) 去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../../../file-management/user-file-uri-intro.md#媒体文件uri的使用方式)。 |

**示例**

参见 [select](#select)

## select

```TypeScript
select(callback: AsyncCallback<PhotoSelectResult>): void
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式， 返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoViewPicker-select(callback: AsyncCallback<PhotoSelectResult>): void--><!--Device-PhotoViewPicker-select(callback: AsyncCallback<PhotoSelectResult>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | 是 | callback返回photoPicker选择后的结果集。 <br>**注意**：此接口返回的PhotoSelectResult对象中的photoUris只能通过临时授权的方式调用接口 [photoAccessHelper.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets) 去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../../../file-management/user-file-uri-intro.md#媒体文件uri的使用方式)。 |

**示例**

参见 [select](#select)

