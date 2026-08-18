# getAllTemplateFormsInfo (System API)

## Modules to Import

```TypeScript
```

## getAllTemplateFormsInfo

```TypeScript
function getAllTemplateFormsInfo(): Promise<Array<formInfo.FormInfo>>
```

Obtains the template widget information provided by all applications on the device. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getAllTemplateFormsInfo(): Promise<Array<formInfo.FormInfo>>--><!--Device-formHost-function getAllTemplateFormsInfo(): Promise<Array<formInfo.FormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
