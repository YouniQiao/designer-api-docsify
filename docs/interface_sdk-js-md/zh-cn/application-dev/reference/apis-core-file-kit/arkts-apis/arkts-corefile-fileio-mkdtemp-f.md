# mkdtemp

## 导入模块

```TypeScript
```

## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string): Promise<string>
```

创建临时目录，使用Promise异步回调。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX").then((pathDir: string) => {
  console.info("mkdtemp succeed:" + pathDir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  // do something
});
```


## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void
```

创建临时目录，使用callback异步回调。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [mkdtemp](arkts-corefile-file-fs-mkdtemp-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

参见 [mkdtemp](#mkdtemp)
