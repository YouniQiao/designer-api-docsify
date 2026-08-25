# print

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## print

```TypeScript
function print(files: Array<string>, callback: AsyncCallback<PrintTask>): void
```

打印接口，传入文件进行打印，使用callback异步回调。拉起系统打印预览界面，需要使用[print](#print)接口，传入 context。

**起始版本：** 10

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## print

```TypeScript
function print(files: Array<string>): Promise<PrintTask>
```

打印接口，传入文件进行打印，使用Promise异步回调。拉起系统打印预览界面，需要使用[print](#print)接口，传入 context。

**起始版本：** 10

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## print

```TypeScript
function print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void
```

打印接口，传入文件进行打印，使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## print

```TypeScript
function print(files: Array<string>, context: Context): Promise<PrintTask>
```

打印接口，传入文件进行打印，使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## print

```TypeScript
function print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes,
    context: Context): Promise<PrintTask>
```

打印接口，传入文件进行打印，三方应用需要更新打印文件，使用Promise异步回调。当前支持的文件类型：".pdf"。

**起始版本：** 11

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [jobName](arkts-basicservices-print-printjobdata-i.md) | string | 是 |
| printAdapter | [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) | 是 |
| printAttributes | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | 是 |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
