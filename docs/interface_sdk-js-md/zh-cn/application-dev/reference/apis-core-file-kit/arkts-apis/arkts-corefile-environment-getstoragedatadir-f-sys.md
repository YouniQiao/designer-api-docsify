# getStorageDataDir（系统接口）

## 导入模块

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getStorageDataDir

```TypeScript
function getStorageDataDir(): Promise<string>
```

异步方法获取内存存储根目录，使用promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.FileManagement.File.Environment

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 13900042 |


## getStorageDataDir

```TypeScript
function getStorageDataDir(callback: AsyncCallback<string>): void
```

异步方法获取内存存储根目录，使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.FileManagement.File.Environment

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 13900042 |
