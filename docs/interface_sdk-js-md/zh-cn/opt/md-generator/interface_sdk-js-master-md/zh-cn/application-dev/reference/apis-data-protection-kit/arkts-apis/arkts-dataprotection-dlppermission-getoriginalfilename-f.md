# getOriginalFileName

## getOriginalFileName

```TypeScript
function getOriginalFileName(fileName: string): string
```

获取指定DLP文件名的原始文件名。该接口为同步接口。

根据原始文件名后缀判断文件类型，选择对应的应用打开。

**起始版本：** 10

<!--Device-dlpPermission-function getOriginalFileName(fileName: string): string--><!--Device-dlpPermission-function getOriginalFileName(fileName: string): string-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fileName | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let originalFileName = dlpPermission.getOriginalFileName('test.txt.dlp'); // 获取原始文件名。
console.info('originalFileName:', originalFileName);
```
