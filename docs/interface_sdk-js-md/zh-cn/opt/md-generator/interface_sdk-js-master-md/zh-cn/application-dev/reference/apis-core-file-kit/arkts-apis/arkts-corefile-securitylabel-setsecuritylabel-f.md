# setSecurityLabel

## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel): Promise<void>
```

设置文件或目录的数据安全等级。数据安全等级仅可由低向高或平级设置。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel): Promise<void>--><!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
securityLabel.setSecurityLabel(filePath, "s0").then(() => {
  console.info("Succeeded in setting security label.");
}).catch((err: BusinessError) => {
  console.error("Failed to set security label. Code: " + err.code + ", message: " + err.message);
});
```


## setSecurityLabel

```TypeScript
function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void
```

设置文件或目录的数据安全等级。数据安全等级仅可由低向高或平级设置。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void--><!--Device-securityLabel-function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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
securityLabel.setSecurityLabel(filePath, "s0", (err: BusinessError) => {
  if (err) {
    console.error("Failed to set security label. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in setting security label.");
  }
});
```
