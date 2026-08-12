# createFileAccessHelper（系统接口）

## createFileAccessHelper

```TypeScript
function createFileAccessHelper(context: Context): FileAccessHelper
```

以同步方法创建连接当前系统内所有文件管理服务的helper对象。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileAccess-function createFileAccessHelper(context: Context): FileAccessHelper--><!--Device-fileAccess-function createFileAccessHelper(context: Context): FileAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

**错误码：**

| 错误码ID |
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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext; 
function createFileAccessHelper02(context: common.UIAbilityContext) {
  let fileAccessHelperAllServer: fileAccess.FileAccessHelper;
  // 创建连接系统内所有配置fileAccess的文件管理类服务的helper对象
  try {
    // context 是EntryAbility 传过来的context
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

以同步方法创建连接指定wants的helper对象。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileAccess-function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper--><!--Device-fileAccess-function createFileAccessHelper(context: Context, wants: Array<Want>): FileAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| wants | Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [FileAccessHelper](arkts-corefile-fileaccess-fileaccesshelper-i-sys.md) |

**错误码：**

| 错误码ID |
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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
import { common } from '@kit.AbilityKit';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext; 
function createFileAccessHelper01(context: common.UIAbilityContext) {
  let fileAccessHelper: fileAccess.FileAccessHelper;
  // wantInfos 从getFileAccessAbilityInfo()获取
  let wantInfos: Array<Want> = [
    {
      bundleName: "com.ohos.UserFile.ExternalFileManager",
      abilityName: "FileExtensionAbility",
    },
  ]
  try {
    // context 是EntryAbility 传过来的context
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
