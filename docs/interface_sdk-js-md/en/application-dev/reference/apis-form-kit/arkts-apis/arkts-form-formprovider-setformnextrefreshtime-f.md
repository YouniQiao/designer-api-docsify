# setFormNextRefreshTime

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void
```

Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void--><!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |
| minute | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) | The form cannot be operated by the current application. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16501002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501002-too-many-widgets) | The number of forms exceeds the maximum allowed. |
| [16501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) | The ID of the form to be operated does not exist. |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500060](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) | Service connection error. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
try {
  formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
    if (error) {
      console.error(`callback error, code: ${error.code}, message: ${error.message})`);
      return;
    }
    console.info(`formProvider setFormNextRefreshTime success`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```


## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: int): Promise<void>
```

Sets the next refresh time for a widget. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int): Promise<void>--><!--Device-formProvider-function setFormNextRefreshTime(formId: string, minute: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |
| minute | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) | The form cannot be operated by the current application. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16501002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501002-too-many-widgets) | The number of forms exceeds the maximum allowed. |
| [16501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) | The ID of the form to be operated does not exist. |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500060](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) | Service connection error. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
try {
  formProvider.setFormNextRefreshTime(formId, 5).then(() => {
    console.info(`formProvider setFormNextRefreshTime success`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message})`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```

