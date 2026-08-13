# createFileAccessHelper (System API)

## Modules to Import

```TypeScript
import { fileAccess } from '@kit.CoreFileKit';
```

## createFileAccessHelper

```TypeScript
function createFileAccessHelper(context: Context): FileAccessHelper
```

Creates a **Helper** object to bind with all file management services in the system. This API returns the result synchronously.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileAccess-function createFileAccessHelper(context: Context): FileAccessHelper--><!--Device-fileAccess-function createFileAccessHelper(context: Context): FileAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

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
import { common } from '@kit.AbilityKit';
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext; 
function createFileAccessHelper02(context: common.UIAbilityContext) {
  let fileAccessHelperAllServer: fileAccess.FileAccessHelper;
  // Create a Helper object to interact with all file management services configured with fileAccess in the system.
  try {
    // context is passed by EntryAbility.
    fileAccessHelperAllServer = fileAccess.createFileAccessHelper(context);
    if (!fileAccessHelperAllServer) {
      console.error("createFileAccessHelper interface returns an undefined object");
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("createFileAccessHelper failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```


## createFileAccessHelper

```TypeScript
function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper
```

Creates a **Helper** object to bind with the specified Wants. This API returns the result synchronously. The **Helper** object provides file access and management capabilities.

**Since:** 9

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileAccess-function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper--><!--Device-fileAccess-function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| wants | Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

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
import { common } from '@kit.AbilityKit';
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext; 
function createFileAccessHelper01(context: common.UIAbilityContext) {
  let fileAccessHelper: fileAccess.FileAccessHelper;
  // Obtain wantInfos by using getFileAccessAbilityInfo().
  let wantInfos: Array<Want> = [
    {
      bundleName: "com.ohos.UserFile.ExternalFileManager",
      abilityName: "FileExtensionAbility",
    },
  ]
  try {
    // context is passed by EntryAbility.
    fileAccessHelper = fileAccess.createFileAccessHelper(context, wantInfos);
    if (!fileAccessHelper) {
      console.error("createFileAccessHelper interface returns an undefined object");
    }
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("createFileAccessHelper failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```
