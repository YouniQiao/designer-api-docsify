# getFileAccessAbilityInfo（系统接口）

## getFileAccessAbilityInfo

```TypeScript
function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void
```

以异步方法获取系统内extension配置为fileAccess类型的所有Want信息。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileAccess-function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void--><!--Device-fileAccess-function getFileAccessAbilityInfo(callback: AsyncCallback<Array<Want>>): void-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; | 是 |

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

以异步方法获取系统内extension配置为fileAccess类型的所有Want信息。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-fileAccess-function getFileAccessAbilityInfo(): Promise<Array<Want>>--><!--Device-fileAccess-function getFileAccessAbilityInfo(): Promise<Array<Want>>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; |

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
