# getSecurityLabel

## getSecurityLabel

```TypeScript
function getSecurityLabel(path: string): Promise<string>
```

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-securityLabel-function getSecurityLabel(path: string): Promise<string>--><!--Device-securityLabel-function getSecurityLabel(path: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath).then((type: string) => {
  console.info("Succeeded in getting security label, Label: " + type);
}).catch((err: BusinessError) => {
  console.error("Failed to get security label. Code: " + err.code + ", message: " + err.message);
});
```


## getSecurityLabel

```TypeScript
function getSecurityLabel(path: string, callback: AsyncCallback<string>): void
```

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-securityLabel-function getSecurityLabel(path: string, callback: AsyncCallback<string>): void--><!--Device-securityLabel-function getSecurityLabel(path: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath, (err: BusinessError, type: string) => {
  if (err) {
    console.error("Failed to get security label. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in getting security label, Label: " + type);
  }
});
```
