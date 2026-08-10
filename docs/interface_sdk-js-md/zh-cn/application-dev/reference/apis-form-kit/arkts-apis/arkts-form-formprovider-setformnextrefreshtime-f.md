# setFormNextRefreshTime

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void
```

Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void--><!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| minute | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
try {
  formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
    if (error) {
      console.error(`callback error, code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`formProvider setFormNextRefreshTime success`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```


## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: int): Promise<void>
```

Sets the next refresh time for a widget. This API uses a promise to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int): Promise<void>--><!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| minute | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
try {
  formProvider.setFormNextRefreshTime(formId, 5).then(() => {
    console.info(`formProvider setFormNextRefreshTime success`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

