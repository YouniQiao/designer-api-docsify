# opendir

## 导入模块

```TypeScript
```

## opendir

```TypeScript
declare function opendir(path: string): Promise<Dir>
```

打开文件目录，使用Promise异步回调。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Dir](arkts-corefile-fileio-dir-depr-i.md)&gt; |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + "/testDir";
fileio.opendir(dirPath).then((dir: fileio.Dir) => {
  console.info("opendir succeed");
}).catch((err: BusinessError) => {
  console.error("opendir failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
fileio.opendir(pathDir, (err: BusinessError, dir: fileio.Dir) => {
  // example code in Dir struct
  // use read/readSync/close
});
```


## opendir

```TypeScript
declare function opendir(path: string, callback: AsyncCallback<Dir>): void
```

打开文件目录，使用callback异步回调。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Dir](arkts-corefile-fileio-dir-depr-i.md)&gt; | 是 |

**示例**

参见 [opendir](#opendir)
