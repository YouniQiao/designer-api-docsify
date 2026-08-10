# addForm (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## addForm

```TypeScript
function addForm(want: Want): Promise<formInfo.RunningFormInfo>
```

Add a form.

You can use this method to create a theme form.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function addForm(want: Want): Promise<formInfo.RunningFormInfo>--><!--Device-formHost-function addForm(want: Want): Promise<formInfo.RunningFormInfo>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Indicates want of the form. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;formInfo.RunningFormInfo&gt; | Return the form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |

