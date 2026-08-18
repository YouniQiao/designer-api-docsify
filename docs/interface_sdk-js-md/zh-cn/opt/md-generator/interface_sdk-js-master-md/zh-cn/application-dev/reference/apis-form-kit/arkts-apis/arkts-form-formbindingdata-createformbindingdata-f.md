# createFormBindingData

## 导入模块

```TypeScript
```

## createFormBindingData

```TypeScript
function createFormBindingData(obj?: Object | string): FormBindingData
```

创建一个FormBindingData对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-formBindingData-function createFormBindingData(obj?: Object | string): FormBindingData--><!--Device-formBindingData-function createFormBindingData(obj?: Object | string): FormBindingData-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object \| string | 否 |

**返回值：**

| 类型 |
| --- |
| [FormBindingData](arkts-form-formbindingdata-formbindingdata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

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

<!--Device-formBindingData-function createFormBindingData(obj?: RecordData): FormBindingData--><!--Device-formBindingData-function createFormBindingData(obj?: RecordData): FormBindingData-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FormBindingData](arkts-form-formbindingdata-formbindingdata-i.md) |
