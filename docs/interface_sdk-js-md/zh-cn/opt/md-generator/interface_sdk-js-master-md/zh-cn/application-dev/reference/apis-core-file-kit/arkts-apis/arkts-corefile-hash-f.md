# hash

## 导入模块

```TypeScript
```

## hash

```TypeScript
function hash(path: string, algorithm: string): Promise<string>
```

计算文件的哈希值，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-hash-function hash(path: string, algorithm: string): Promise<string>--><!--Device-hash-function hash(path: string, algorithm: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
hash.hash(filePath, "sha256").then((str: string) => {
  console.info("Succeeded in calculating file hash: " + str);
}).catch((err: BusinessError) => {
  console.error("Failed to calculate file hash. Code: " + err.code + ", message: " + err.message);
});
```


## hash

```TypeScript
function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void
```

计算文件的哈希值，使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-hash-function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void--><!--Device-hash-function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + "/test.txt";
hash.hash(filePath, "sha256", (err: BusinessError, str: string) => {
  if (err) {
    console.error("Failed to calculate file hash. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in calculating file hash: " + str);
  }
});
```
