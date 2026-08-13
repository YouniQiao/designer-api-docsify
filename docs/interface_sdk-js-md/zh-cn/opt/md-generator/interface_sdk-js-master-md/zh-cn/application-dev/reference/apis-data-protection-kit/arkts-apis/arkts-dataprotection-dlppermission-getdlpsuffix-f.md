# getDLPSuffix

## getDLPSuffix

```TypeScript
function getDLPSuffix(): string
```

获取DLP文件扩展名。调用成功后返回DLP文件扩展名（如'.dlp'）。接口为同步接口。 用于获取DLP文件的标准扩展名，便于构建DLP文件名或进行文件类型判断。

**起始版本：** 10

**废弃版本：** -1

<!--Device-dlpPermission-function getDLPSuffix(): string--><!--Device-dlpPermission-function getDLPSuffix(): string-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let dlpSuffix = dlpPermission.getDLPSuffix(); // 获取DLP扩展名。
console.info('dlpSuffix:', dlpSuffix);
```
