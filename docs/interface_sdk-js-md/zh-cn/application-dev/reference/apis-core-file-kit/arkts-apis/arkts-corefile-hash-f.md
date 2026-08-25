# hash

## 导入模块

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## hash

```TypeScript
function hash(path: string, algorithm: string): Promise<string>
```

计算文件的哈希值，基于指定算法对文件完整内容进行哈希摘要计算。使用Promise异步回调。

> **说明：**&gt;
> 该接口会读取整个文件内容并计算哈希值，适用于中小文件。对于大文件处理，建议使用HashStream流式计算。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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


## hash

```TypeScript
function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void
```

计算文件的哈希值，基于指定算法对文件完整内容进行哈希摘要计算。使用callback异步回调。

> **说明：**&gt;
> 该接口会读取整个文件内容并计算哈希值，适用于中小文件。对于大文件处理，建议使用HashStream流式计算。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900042 |
