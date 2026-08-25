# FetchResult

文件检索结果集。

**继承/实现关系：** FetchResult extends lang.ISendable

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { sendablePhotoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

释放FetchResult实例并使其失效。释放后无法调用其他方法。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getAllObjects

```TypeScript
getAllObjects(): Promise<Array<T>>
```

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getCount

```TypeScript
getCount(): number
```

获取文件检索结果中的文件总数。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getFirstObject

```TypeScript
getFirstObject(): Promise<T>
```

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getLastObject

```TypeScript
getLastObject(): Promise<T>
```

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getNextObject

```TypeScript
getNextObject(): Promise<T>
```

获取文件检索结果中的下一个文件资产。使用Promise异步回调。在调用此方法之前，必须使用[isAfterLast()](#isafterlast)来检查当前位置 是否为最后一行。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |

## getObjectByPosition

```TypeScript
getObjectByPosition(index: number): Promise<T>
```

获取文件检索结果中具有指定索引的文件资产。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

检查结果集是否指向最后一行。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 14000011 |
