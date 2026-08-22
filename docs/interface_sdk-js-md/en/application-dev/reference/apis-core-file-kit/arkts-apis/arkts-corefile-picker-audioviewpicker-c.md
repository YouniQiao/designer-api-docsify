# AudioViewPicker

Provides APIs for selecting and saving audio clips. Before using the APIs of **AudioViewPicker**, you need to create an **AudioViewPicker** instance.

**Since:** 23

<!--Device-picker-class AudioViewPicker--><!--Device-picker-class AudioViewPicker-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create an **AudioViewPicker** instance. This constructor is not recommended due to the potential risk of operation failure.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioViewPicker-constructor()--><!--Device-AudioViewPicker-constructor()-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
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
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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
let documentPicker = new picker.DocumentViewPicker(); // Construction without parameter is not recommended. There is a possibility that the DocumentViewPicker instance fails to start.
```

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
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            let windowClass: window.Window | undefined = undefined;
            windowClass = window.findWindow('test'); // Ensure that the window has been created. Here, 'test' is the value of the name parameter when the window is created.
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
import  { picker } from '@kit.CoreFileKit';
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
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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
let audioPicker = new picker.AudioViewPicker(); // Construction without parameter is not recommended. There is a possibility that the AudioViewPicker instance fails to start.
```

```TypeScript
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
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
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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
let photoPicker = new picker.PhotoViewPicker(); // Construction without parameter is not recommended. There is a possibility that the PhotoViewPicker instance fails to start.
```

## constructor

```TypeScript
constructor(context: Context)
```

A constructor used to create an **AudioViewPicker** instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AudioViewPicker-constructor(context: Context)--><!--Device-AudioViewPicker-constructor(context: Context)-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Application context (only **UIAbilityContext** is supported). For details about the application context of the stage model, see Context. |

**Examples**

See [constructor](#constructor)

## save

```TypeScript
save(option?: AudioSaveOptions): Promise<Array<string>>
```

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioViewPicker-save(option?: AudioSaveOptions): Promise<Array<string>>--><!--Device-AudioViewPicker-save(option?: AudioSaveOptions): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-c.md) | No | Options for saving audio clips. If this parameter is not specified, an **audioPicker** page will be displayed for the user to enter the names of the files to save. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the URIs of the audio clips saved. <br>**Note：**: For details about how to use the returned URIs, see [Using a Document URI](../../../file-management/user-file-uri-intro.md#using-a-document-uri). |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example10(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example11(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example12(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example16(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example17(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example18(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example04(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker01.jpg', 'PhotoViewPicker01.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions).then((photoSaveResult: Array<string>) => {
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
      console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example05(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = ['PhotoViewPicker02.jpg','PhotoViewPicker02.mp4'];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions, (err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example06(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save((err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

## save

```TypeScript
save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void
```

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioViewPicker-save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void--><!--Device-AudioViewPicker-save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-c.md) | Yes | Options for saving audio clips. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback invoked to return the URIs of the audio clips saved. <br>**Note：**: For details about how to use the returned URIs, see [Using a Document URI](../../../file-management/user-file-uri-intro.md#using-a-document-uri). |

**Examples**

See [save](#save)

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioViewPicker-save(callback: AsyncCallback<Array<string>>): void--><!--Device-AudioViewPicker-save(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback invoked to return the URIs of the audio clips saved. <br>**Note：**: For details about how to use the returned URIs, see [Using a Document URI](../../../file-management/user-file-uri-intro.md#using-a-document-uri). |

**Examples**

See [save](#save)

## select

```TypeScript
select(option?: AudioSelectOptions): Promise<Array<string>>
```

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioViewPicker-select(option?: AudioSelectOptions): Promise<Array<string>>--><!--Device-AudioViewPicker-select(option?: AudioSelectOptions): Promise<Array<string>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-c.md) | No | Options for selecting audio clips. If this parameter is not specified, the **audioPicker** page is displayed by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the URIs of the audio clips selected. <br>**Note：**: For details about how to use the returned URIs, see [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri). |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example07(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example08(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example09(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example13(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example14(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example15(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example01(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions).then((photoSelectResult: picker.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example02(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example03(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select((err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}
```

## select

```TypeScript
select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void
```

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioViewPicker-select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void--><!--Device-AudioViewPicker-select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-c.md) | Yes | Options for selecting audio clips. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback invoked to return the URIs of the audio clips selected. <br>**Note：**: For details about how to use the returned URIs, see [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri). |

**Examples**

See [select](#select)

## select

```TypeScript
select(callback: AsyncCallback<Array<string>>): void
```

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous callback to return the result. **System capability**: SystemCapability.FileManagement.UserFileService

**Since:** 23

<!--Device-AudioViewPicker-select(callback: AsyncCallback<Array<string>>): void--><!--Device-AudioViewPicker-select(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback invoked to return the URIs of the audio clips selected. <br>**Note：**: For details about how to use the returned URIs, see [Using a Media File URI](../../../file-management/user-file-uri-intro.md#using-a-media-file-uri). |

**Examples**

See [select](#select)

