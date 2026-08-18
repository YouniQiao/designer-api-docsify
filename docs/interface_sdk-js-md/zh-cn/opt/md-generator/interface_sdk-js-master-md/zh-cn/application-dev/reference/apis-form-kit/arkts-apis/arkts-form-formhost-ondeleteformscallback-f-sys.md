# onDeleteFormsCallback（系统接口）

## 导入模块

```TypeScript
```

## onDeleteFormsCallback

```TypeScript
function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void
```

订阅删除卡片事件。使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formHost-function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void--><!--Device-formHost-function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | formInfo.DeleteFormsCallback | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const callback = (formIds: string[]): void => {
    console.info(`onDeleteFormsCallback formIds length: ${formIds.length}`);
    for (let formId of formIds) {
      console.info(`deleted formId: ${formId}`);
    }
  };
  formHost.onDeleteFormsCallback(callback);
  console.info(`onDeleteFormsCallback success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
