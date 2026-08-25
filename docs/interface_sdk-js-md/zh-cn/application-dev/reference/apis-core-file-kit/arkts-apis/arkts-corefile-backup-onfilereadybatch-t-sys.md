# OnFileReadyBatch（系统接口）

```TypeScript
type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void
```

一批文件准备好发送给客户端时触发的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| error | BusinessError & lt;void & gt; | 是 |
| files | Array & lt;File & gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

const onFileReadyBatch: backup.OnFileReadyBatch = (error: BusinessError<void>, files: Array<backup.File>): void => {
  if (error) {
    console.error(`onFileReadyBatch failed. Code: ${error.code}, message: ${error.message}`);
    return;
  }
  for (let file of files) {
    console.info(`onFileReadyBatch success with file: ${file.bundleName}, ${file.uri}`);
    fileIo.closeSync(file.fd);
  }
};
```
