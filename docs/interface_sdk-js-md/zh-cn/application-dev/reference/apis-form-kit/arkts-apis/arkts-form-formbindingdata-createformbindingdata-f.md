# createFormBindingData

## 导入模块

```TypeScript
import { formBindingData } from 'kits/@kit.FormKit';
```

## createFormBindingData

```TypeScript
function createFormBindingData(obj?: Object | string): FormBindingData
```

Creates a **FormBindingData** object.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-formBindingData-function createFormBindingData(obj?: Object | string): FormBindingData--><!--Device-formBindingData-function createFormBindingData(obj?: Object | string): FormBindingData-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object \| string | 否 | Data to be displayed on the widget. The value can be an object containing multiple key-value pairs or a JSON string. The image data is identified by **'formImages'**, and the content is multiple key- value pairs, each of which consists of an image identifier and image file descriptor. The final format is {' formImages': {'key1': fd1, 'key2': fd2}}.&lt;br&gt;**NOTE：**&lt;br&gt;During [widget update](../../../form/arkts-ui-widget-interaction-overview.md), when the widget UI receives widget data through @LocalStorageProp, the **FormBindingData** object is serialized, that is, the widget data is converted into the string type. Since API version 20, if the widget data is updated using shared memory, the total size of the updated data cannot exceed 10 MB, and the number of updated images cannot exceed 20. In API version 19 and earlier versions, the maximum number of image files is 5, and the maximum memory size of each image is 2 MB. Exceeding this 2 MB limit for any image will result in abnormal display. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FormBindingData](arkts-form-formbindingdata-formbindingdata-i.md) | FormBindingData** object created based on the passed data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## 示例

```TypeScript
import { formBindingData } from '@kit.FormKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  content = this.getUIContext().getHostContext() as common.UIAbilityContext;
  pathDir: string = this.content.filesDir;

  createFormBindingData() {
    let filePath = this.pathDir + "/form.png";
    let fd: number = -1;
    try {
      fd = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY).fd;
      let formImagesParam: Record<string, number> = {
        'image': fd
      };
      let createFormBindingDataParam: Record<string, string | Record<string, number>> = {
        'name': '21°',
        'imgSrc': 'image',
        'formImages': formImagesParam
      };
      let formBindingDataObj = formBindingData.createFormBindingData(createFormBindingDataParam);
    } catch (error) {
      console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
    } finally {
      if (fd !== -1) {
        fileIo.closeSync(fd);
      }
    }
  }

  build() {
    Button('createFormBindingData')
      .onClick((event: ClickEvent) => {
        this.createFormBindingData();
      })
  }
}
```


## createFormBindingData

```TypeScript
function createFormBindingData(obj?: RecordData): FormBindingData
```

Create an FormBindingData instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-formBindingData-function createFormBindingData(obj?: RecordData): FormBindingData--><!--Device-formBindingData-function createFormBindingData(obj?: RecordData): FormBindingData-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | 否 | Indicates the FormBindingData instance data. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FormBindingData](arkts-form-formbindingdata-formbindingdata-i.md) | Returns the FormBindingData. |

