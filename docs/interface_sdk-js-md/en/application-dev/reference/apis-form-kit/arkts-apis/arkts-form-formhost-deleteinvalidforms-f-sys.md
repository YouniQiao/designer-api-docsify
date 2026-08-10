# deleteInvalidForms (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## deleteInvalidForms

```TypeScript
function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<int>): void
```

Deletes invalid widgets from the list. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<int>): void--><!--Device-formHost-function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes | List of valid widget IDs. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the invalid widgets are deleted, **error** is undefined and **data** is the number of widgets deleted; otherwise, **error** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |


## deleteInvalidForms

```TypeScript
function deleteInvalidForms(formIds: Array<string>): Promise<int>
```

Deletes invalid widgets from the list. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteInvalidForms(formIds: Array<string>): Promise<int>--><!--Device-formHost-function deleteInvalidForms(formIds: Array<string>): Promise<int>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes | List of valid widget IDs. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the number of widgets deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |

