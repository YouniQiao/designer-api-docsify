# RootInfo（系统接口）

表示设备的根属性信息和接口能力。

**起始版本：** 9

**废弃版本：** 23

<!--Device-fileAccess-interface RootInfo--><!--Device-fileAccess-interface RootInfo-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## listFile

```TypeScript
listFile(filter?: Filter): FileIterator
```

以同步方法从某个目录，基于过滤器，获取下一级符合条件的文件(夹)信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md#FileInfo（系统接口）)。目前仅支持内置存储设备过滤，外置存储设备不支持过滤。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** listFile

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-listFile(filter?: Filter): FileIterator--><!--Device-RootInfo-listFile(filter?: Filter): FileIterator-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
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
// rootInfo 从getRoots()获取
// let filter = {suffix : [".txt", ".jpg", ".xlsx"]};
let rootInfo: Array<fileAccess.FileInfo> = [];
let fileInfos: Array<fileAccess.FileInfo> = [];
let isDone: boolean = false;
try {
  for (let i = 0; i < rootInfo.length; ++i) {
    let fileIterator = rootInfo[i].listFile();
    // 含过滤器实现的listFile
    // let fileIterator = rootInfo.listFile(filter);
    if (!fileIterator) {
      console.error("listFile interface returns an undefined object");
    }
    while (!isDone) {
      let result = fileIterator.next();
      console.info("next result = " + JSON.stringify(result));
      isDone = result.done;
      if (!isDone) {
        fileInfos.push(result.value);
      }
    }
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("listFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## scanFile

```TypeScript
scanFile(filter?: Filter): FileIterator
```

以同步方法从某设备根节点开始，基于过滤器，递归获取符合条件的文件信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md#FileInfo（系统接口）)。目前仅支持内置存储设备。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-scanFile(filter?: Filter): FileIterator--><!--Device-RootInfo-scanFile(filter?: Filter): FileIterator-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| 14000004 |
| 13900038 |
| 14000001 |
| 13900033 |
| 13900034 |
| 14000003 |
| 14000002 |
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
// rootInfo 从 getRoots()获取
// let filter = {suffix : [".txt", ".jpg", ".xlsx"]};
let rootInfo: Array<fileAccess.FileInfo> = [];
let fileInfos: Array<fileAccess.FileInfo> = [];
let isDone: boolean = false;
try {
  for (let i = 0; i < rootInfo.length; ++i) {
    let fileIterator = rootInfo[i].scanFile();
    // 含过滤器实现的scanFile
    // let fileIterator = rootInfo.scanFile(filter);
    if (!fileIterator) {
      console.error("scanFile interface returns undefined object");
    }
    while (!isDone) {
      let result = fileIterator.next();
      console.info("next result = " + JSON.stringify(result));
      isDone = result.done;
      if (!isDone) {
        fileInfos.push(result.value);
      }
    }
  }
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("scanFile failed, errCode:" + error.code + ", errMessage:" + error.message);
}
```

## deviceFlags

```TypeScript
deviceFlags: number
```

设备支持的能力。

**类型：** number

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-deviceFlags: number--><!--Device-RootInfo-deviceFlags: number-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## deviceType

```TypeScript
deviceType: number
```

设备支持的能力。

**类型：** number

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-deviceType: number--><!--Device-RootInfo-deviceType: number-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## displayName

```TypeScript
displayName: string
```

设备支持的能力。

**类型：** string

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-displayName: string--><!--Device-RootInfo-displayName: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## relativePath

```TypeScript
relativePath: string
```

根目录的相对路径。

**类型：** string

**起始版本：** 10

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-relativePath: string--><!--Device-RootInfo-relativePath: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## uri

```TypeScript
uri: string
```

设备支持的能力。

**类型：** string

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootInfo-uri: string--><!--Device-RootInfo-uri: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。
