# getPublishedFormInfos

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedFormInfos

```TypeScript
function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>
```

Obtains the information of all widgets that have been added to the home screen on the device. This API uses a promise to return the result.

> **NOTE：**
> 
> This field is supported since API version 18 and deprecated since API version 20. You are advised to use
> [getPublishedRunningFormInfos](arkts-form-formprovider-getpublishedrunningforminfos-f.md#getpublishedrunningforminfos) instead.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**废弃版本：** 20

**替代接口：** [formProvider.getPublishedRunningFormInfos](arkts-form-formprovider-getpublishedrunningforminfos-f.md#getpublishedrunningforminfos)

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-formProvider-function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>--><!--Device-formProvider-function getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;formInfo.FormInfo&gt;&gt; | Promise used to return the information obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getPublishedFormInfos().then((data: formInfo.FormInfo[]) => {
    console.info(`formProvider getPublishedFormInfos, data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

