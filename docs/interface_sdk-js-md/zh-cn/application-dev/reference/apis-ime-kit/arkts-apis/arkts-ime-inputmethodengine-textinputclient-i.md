# TextInputClient

下列API示例中都需使用 on('inputStart') 回调获取到TextInputClient实例，再通过此实例调用对应方法。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [InputClient](arkts-ime-inputmethodengine-inputclient-i.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## deleteBackward

```TypeScript
deleteBackward(length: number, callback: AsyncCallback<boolean>): void
```

删除光标后固定长度的文本。使用callback异步回调。 使用场景：实现删除键功能、删除光标后的字符、快速修正输入、实现自定义删除逻辑等。 使用后效果：成功时返回true，编辑框中光标后指定长度的文本被删除。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteBackward](arkts-ime-inputmethodengine-inputclient-i.md#deletebackward)(length: int, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## deleteBackward

```TypeScript
deleteBackward(length: number): Promise<boolean>
```

删除光标后固定长度的文本。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** deleteBackward(length: int): Promise&lt;boolean&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## deleteForward

```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

删除光标前固定长度的文本。使用callback异步回调。 使用场景：实现退格键功能、逐字删除输入、删除错误的输入、实现自定义删除逻辑等。 使用后效果：成功时返回true，编辑框中光标前指定长度的文本被删除。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteForward](arkts-ime-inputmethodengine-inputclient-i.md#deleteforward)(length: int, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## deleteForward

```TypeScript
deleteForward(length: number): Promise<boolean>
```

删除光标前固定长度的文本。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** deleteForward(length: int): Promise&lt;boolean&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## getBackward

```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

获取光标后固定长度的文本。使用callback异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getBackward](arkts-ime-inputmethodengine-inputclient-i.md#getbackward)(length: int, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getBackward

```TypeScript
getBackward(length: number): Promise<string>
```

获取光标后固定长度的文本。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getBackward(length: int): Promise&lt;string&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

获取编辑框属性值。使用callback异步回调。 使用场景：根据编辑框类型调整输入法界面、根据编辑框配置提供不同的输入建议、实现特定输入逻辑、适配不同类型的输入框等。 使用后效果：返回编辑框属性信息（包括inputPattern输入类型和enterKeyType回车键类型），输入法应用据此调整键盘布局。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getEditorAttribute](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattribute)(callback: AsyncCallback&lt;EditorAttribute&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | 是 |

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

获取编辑框属性值。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getEditorAttribute](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattribute)(callback: AsyncCallback&lt;EditorAttribute&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; |

## getForward

```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

获取光标前固定长度的文本。使用callback异步回调。 使用场景：分析已输入文本内容以提供智能补全建议、检查文本格式、实现文本预测功能、实现文本语义分析等。 使用后效果：成功时返回光标前指定长度的文本字符串，输入法应用可据此更新候选词或输入建议。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getForward](arkts-ime-inputmethodengine-inputclient-i.md#getforward)(length: int, callback: AsyncCallback&lt;string&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getForward

```TypeScript
getForward(length: number): Promise<string>
```

获取光标前固定长度的文本。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getForward(length: int): Promise&lt;string&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

插入文本。使用callback异步回调。 使用场景：插入候选词、插入特殊符号、实现文本自动补全、快速插入常用短语等。 使用后效果：成功时返回true，文本已插入到编辑框光标位置。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [insertText](arkts-ime-inputmethodengine-inputclient-i.md#inserttext)(text: string, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

插入文本。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** insertText(text: string): Promise&lt;boolean&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

发送功能键。使用callback异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sendKeyFunction](arkts-ime-inputmethodengine-inputclient-i.md#sendkeyfunction)(action: int, callback: AsyncCallback&lt;boolean&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number): Promise<boolean>
```

发送功能键。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** sendKeyFunction(action: int): Promise&lt;boolean&gt;

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
