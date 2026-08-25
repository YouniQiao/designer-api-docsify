# DocumentViewPicker

文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.UserFileService

## 导入模块

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

创建DocumentViewPicker对象，不推荐使用该构造函数，会出现概率性失败问题。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor(context: Context)
```

创建DocumentViewPicker对象，推荐使用该构造函数，获取context参考 [getHostContext](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

## constructor

```TypeScript
constructor(context: Context, window: window.Window)
```

应用自行创建窗口中，可用通过该构造函数创建DocumentViewPicker对象。一般场景推荐使用constructor(context: Context)方法 创建DocumentViewPicker对象。

> **说明：**&gt;
> 从API version 19开始，2in1和Tablet设备支持该方法。

**起始版本：** 13

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [window](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) | window.Window | 是 |

## getSelectedIndex

```TypeScript
getSelectedIndex(): number
```

获取保存成功后的文件后缀类型的下标。 该方法只在调用 [save()](#save)时使用生效， 其他场景下不适用。该方法需要配置参数[DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md)。 该方法返回的是所选后缀类型的下标(number)。所选的后缀类型是开发者所传的参数 [DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md)里的某个后缀类型。 如果没有传参，并且调用了getSelectedIndex()方法，返回值为-1。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService.FolderSelection

**返回值：**

| 类型 |
| --- |
| number |

## save

```TypeScript
save(option?: DocumentSaveOptions): Promise<Array<string>>
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## save

```TypeScript
save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## select

```TypeScript
select(option?: DocumentSelectOptions): Promise<Array<string>>
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## select

```TypeScript
select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## select

```TypeScript
select(callback: AsyncCallback<Array<string>>): void
```

通过选择模式拉起documentPicker界面，用户可以选择一个或多个文件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |
