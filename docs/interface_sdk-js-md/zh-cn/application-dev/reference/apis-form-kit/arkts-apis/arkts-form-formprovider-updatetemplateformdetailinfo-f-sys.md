# updateTemplateFormDetailInfo（系统接口）

## 导入模块

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## updateTemplateFormDetailInfo

```TypeScript
function updateTemplateFormDetailInfo(templateFormInfo: Array<formInfo.TemplateFormDetailInfo>): Promise<void>
```

更新当前设备上指定的模板卡片静态配置信息。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateFormInfo | Array & lt;formInfo.TemplateFormDetailInfo & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16501013](../errorcode-form.md#16501013-系统不支持当前操作) |

**示例**

ArkTS-Dyn示例：

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
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { formProvider, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  const info: formInfo.TemplateFormDetailInfo = {
    bundleName: 'com.example.ohos.formjsdemo',
    moduleName: 'entry',
    abilityName: 'EntryAbility',
    formName: 'widget',
    dimension: formInfo.FormDimension.Dimension_2_2,
    detailId: 'detailId',
    displayName: 'displayName',
    description: 'description',
  }
  const templateFormInfo: Array<formInfo.TemplateFormDetailInfo> = [info];
  formProvider.updateTemplateFormDetailInfo(templateFormInfo).then(() => {
    console.info('updateTemplateFormDetailInfo succeed.');
  }).catch((error) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```
