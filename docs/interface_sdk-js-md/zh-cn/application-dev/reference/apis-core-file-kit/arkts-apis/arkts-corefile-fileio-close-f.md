# close

## 导入模块

```TypeScript
```

## close

```TypeScript
declare function close(fd: number): Promise<void>
```

关闭文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [close](arkts-corefile-file-fs-close-f.md)

<!--Device-unnamed-declare function close(fd: number): Promise<void>--><!--Device-unnamed-declare function close(fd: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |

**示例**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd, (err: BusinessError) => {
  // do something
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // do something
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
dir.close().then(() => {
  console.info("close dir successfully");
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
dir.close((err: BusinessError) => {
  console.info("close dir successfully");
});
```


## close

```TypeScript
declare function close(fd: number, callback: AsyncCallback<void>): void
```

关闭文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [close](arkts-corefile-file-fs-close-f.md)

<!--Device-unnamed-declare function close(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function close(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 待关闭文件的文件描述符。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 异步关闭文件之后的回调。 |

**示例**

参见 [close](#close)

