# getTotalSize

## 导入模块

```TypeScript
import { statfs } from 'kits/@kit.CoreFileKit';
```

## getTotalSize

```TypeScript
function getTotalSize(path: string): Promise<number>
```

获取指定文件或目录所在文件系统的总字节数。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900033 |
| 13900038 |
| 13900042 |


## getTotalSize

```TypeScript
function getTotalSize(path: string, callback: AsyncCallback<number>): void
```

获取指定文件或目录所在文件系统的总字节数。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900033 |
| 13900038 |
| 13900042 |
