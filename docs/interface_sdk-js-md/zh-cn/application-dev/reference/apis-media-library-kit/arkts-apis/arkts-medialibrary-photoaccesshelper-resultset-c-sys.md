# ResultSet（系统接口）

提供通过查询数据库生成的数据库结果集的访问方法。下列API示例中，需先使用[query](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i-sys.md#query)方法获取ResultSet实例，再调用对应方法。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## close

```TypeScript
close(): void
```

关闭结果集，若不关闭可能会引起内存泄漏。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getRow

```TypeScript
getRow(): ValuesBucket
```

获取指定行的所有列值。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ValuesBucket](../../apis-arkdata/arkts-apis/arkts-arkdata-rdb-valuesbucket-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getValue

```TypeScript
getValue(columnIndex: number): ValueType
```

获取当前行中指定列的值。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [columnIndex](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## goToFirstRow

```TypeScript
goToFirstRow(): boolean
```

转到结果集的第一行。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## goToNextRow

```TypeScript
goToNextRow(): boolean
```

转到结果集的下一行。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## goToRow

```TypeScript
goToRow(position: number): boolean
```

转到结果集的指定行。

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## columnCount

```TypeScript
columnCount: number
```

获取结果集的列数。

**类型：** number

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## isAtLastRow

```TypeScript
isAtLastRow: boolean
```

检查游标是否位于最后一行。true表示位于最后一行，false表示不位于最后一行。

**类型：** boolean

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## rowCount

```TypeScript
rowCount: number
```

获取结果集的行数。

**类型：** number

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## rowIndex

```TypeScript
rowIndex: number
```

获取结果集的当前行索引。

**类型：** number

**起始版本：** 22

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。
