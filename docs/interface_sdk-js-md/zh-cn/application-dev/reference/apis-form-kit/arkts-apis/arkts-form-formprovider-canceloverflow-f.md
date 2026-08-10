# cancelOverflow

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## cancelOverflow

```TypeScript
function cancelOverflow(formId: string): Promise<void>
```

Cancels an animation. This API takes effect only for   
[scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-formProvider-function cancelOverflow(formId: string): Promise<void>--><!--Device-formProvider-function cancelOverflow(formId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 801 | Capability not supported.function cancelOverflow can not work correctly due to limited device capabilities. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 16501011 | The form cannot support this operation. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整

try {
  formProvider.cancelOverflow(formId).then(() => {
    console.info('cancelOverflow succeed.');
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

