# getFileAccessAbilityInfo (System API)

## Modules to Import

```TypeScript
import { fileAccess } from '@kit.CoreFileKit';
```

## getFileAccessAbilityInfo

```TypeScript
function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void
```

Obtains information about all Wants with **extension** set to **fileAccess** in the system. A Want contains information for starting an ability. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileAccess-function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void--><!--Device-fileAccess-function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
async function getFileAccessAbilityInfo() {
  try {
    fileAccess.getFileAccessAbilityInfo((err: BusinessError, wantInfos: Array<Want>) => {
      if (err) {
        console.error("Failed to getFileAccessAbilityInfo in async, errCode:" + err.code + ", errMessage:" + err.message);
        return;
      }
      console.info("getFileAccessAbilityInfo data " + JSON.stringify(wantInfos));
    });
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getFileAccessAbilityInfo failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```


## getFileAccessAbilityInfo

```TypeScript
function getFileAccessAbilityInfo(): Promise<Array<Want>>
```

Obtains information about all Wants with **extension** set to **fileAccess** in the system. A Want contains information for starting an ability. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileAccess-function getFileAccessAbilityInfo(): Promise<Array<Want>>--><!--Device-fileAccess-function getFileAccessAbilityInfo(): Promise<Array<Want>>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 14300002 |
| 13900013 |
| 14300003 |
| 13900014 |
| 13900015 |
| 14300001 |
| 13900008 |
| 14300004 |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
async function getFileAccessAbilityInfo() {
  let wantInfos: Array<Want> = [];
  try {
    wantInfos = await fileAccess.getFileAccessAbilityInfo();
    console.info("getFileAccessAbilityInfo data " + JSON.stringify(wantInfos));
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("getFileAccessAbilityInfo failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```
