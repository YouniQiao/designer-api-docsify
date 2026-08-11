# onGetWantParamsCallback (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## onGetWantParamsCallback

```TypeScript
function onGetWantParamsCallback(callback: formInfo.GetWantParamsCallback): void
```

Register callback of getting the want parameters of the form.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function onGetWantParamsCallback(callback: formInfo.GetWantParamsCallback): void--><!--Device-formHost-function onGetWantParamsCallback(callback: formInfo.GetWantParamsCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.GetWantParamsCallback | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const callback = (formInfos: formInfo.FormInfo[]): Array<Record<string, Object>> => {
    console.info(`onGetWantParamsCallback formInfos length: ${formInfos.length}`);
    let wantParamsList: Array<Record<string, Object>> = [];
    for (let formInfoItem of formInfos) {
      let wantParams: Record<string, Object> = {};
      wantParams['key'] = 'value';
      wantParamsList.push(wantParams);
    }
    return wantParamsList;
  };
  formHost.onGetWantParamsCallback(callback);
  console.info(`onGetWantParamsCallback success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
