# getSecurityLabel

## 导入模块

```TypeScript
import { securityLabel } from 'kits/@kit.CoreFileKit';
```

## getSecurityLabel

```TypeScript
function getSecurityLabel(path: string): Promise<string>
```

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用Promise异步回调。

**起始版本：** 9

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
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |


## getSecurityLabel

```TypeScript
function getSecurityLabel(path: string, callback: AsyncCallback<string>): void
```

获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |
