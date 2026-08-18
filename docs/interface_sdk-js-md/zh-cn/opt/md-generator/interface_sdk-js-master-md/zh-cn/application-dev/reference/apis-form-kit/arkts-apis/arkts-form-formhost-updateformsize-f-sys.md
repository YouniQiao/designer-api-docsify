# updateFormSize（系统接口）

## 导入模块

```TypeScript
```

## updateFormSize

```TypeScript
function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void
```

调整卡片尺寸。

**起始版本：** 23

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void--><!--Device-formHost-function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| newDimension | formInfo.FormDimension | 是 |
| newRect | formInfo.Rect | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16501012](../errorcode-form.md#16501012-卡片尺寸错误) |

**示例**

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let formId: string = '12400633174999288';
  let newDimension = formInfo.FormDimension.Dimension_1_2;
  let newRect: formInfo.Rect = {
    left: 1,
    top: 2,
    width: 100,
    height: 100
  };
  formHost.updateFormSize(formId, newDimension, newRect);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
