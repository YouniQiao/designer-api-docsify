# isRequestPublishFormSupported (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void
```

Checks whether a widget can be added to the widget host. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-formProvider-function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void--><!--Device-formProvider-function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback function that returns the query result.&lt;br&gt;**true**: The widget can be added to the widget host.&lt;br&gt;**false**: The widget cannot be added to the widget host. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |


## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(): Promise<boolean>
```

Checks whether a widget can be added to the widget host. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-formProvider-function isRequestPublishFormSupported(): Promise<boolean>--><!--Device-formProvider-function isRequestPublishFormSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise that returns whether a widget can be added to the widget host. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

