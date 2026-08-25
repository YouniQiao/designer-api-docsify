# InputClient

InputClient是输入法客户端对象，代表当前绑定到输入法应用的编辑框客户端。InputClient实例通过InputMethodAbility的 on('inputStart') 事件回调获取，每个绑定事件对应一个InputClient实例，输入法应用通过该实例与编辑框进行文本交互。 核心功能概述：   
- 文本获取：通过[getForward](#getforward) /[getForwardSync](#getforwardsync)获取光标前的文本，通过 [getBackward](#getbackward)/ [getBackwardSync](#getbackwardsync)获取光标后的文本，用于分析已输入内容并提供智能补全。   
- 文本编辑：通过 [insertText](#inserttext)/ [insertTextSync](#inserttextsync)插入文本，通过 [deleteForward](#deleteforward)/ [deleteForwardSync](#deleteforwardsync)删除光标前的文本，通过 [deleteBackward](#deletebackward) /[deleteBackwardSync](#deletebackwardsync)删除光标后的文本。   
- 功能键与光标：通过 [sendKeyFunction](#sendkeyfunction) 发送功能键（如回车键），通过 [moveCursor](#movecursor)/ [moveCursorSync](#movecursorsync)移动光标。   
- 选区操作：通过 [selectByRange](#selectbyrange)/ [selectByRangeSync](#selectbyrangesync)按范围选中文本，通过 [selectByMovement](#selectbymovement) /[selectByMovementSync](#selectbymovementsync)按方向选中文本。   
- 编辑框属性：通过 [getEditorAttribute](#geteditorattribute) /[getEditorAttributeSync](#geteditorattributesync)获取编辑框属性信息（输入类型、回车键类型等），据此调整键 盘布局。   
- 文本预览：通过[setPreviewText](#setpreviewtext)/ [setPreviewTextSync](#setpreviewtextsync)设置预览文本，通过 [finishTextPreview](#finishtextpreview)/ [finishTextPreviewSync](#finishtextpreviewsync)结束文本预览。   
- 私有通信：通过[sendPrivateCommand](#sendprivatecommand)向应用发送私有命令，通过 [sendMessage](#sendmessage)/ [recvMessage](#recvmessage)进行消息通信。   
 注意事项：   
- InputClient实例与当前绑定的编辑框关联，当编辑框失去焦点或输入法解绑时，该实例可能失效。   
- 同名Sync后缀接口为同步接口，阻塞主线程，容易影响UI交互，需谨慎使用。   
 下列API均需使用 on('inputStart') 获取到InputClient实例后，通过实例调用。

**起始版本：** 9

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

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## deleteBackward

```TypeScript
deleteBackward(length: number): Promise<boolean>
```

删除光标后固定长度的文本。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## deleteBackwardSync

```TypeScript
deleteBackwardSync(length: number): void
```

删除光标后固定长度的文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [deleteBackward](#deletebackward)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## deleteForward

```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

删除光标前固定长度的文本。使用callback异步回调。 使用场景：实现退格键功能、逐字删除输入、删除错误的输入、实现自定义删除逻辑等。 使用后效果：成功时返回true，编辑框中光标前指定长度的文本被删除。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## deleteForward

```TypeScript
deleteForward(length: number): Promise<boolean>
```

删除光标前固定长度的文本。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## deleteForwardSync

```TypeScript
deleteForwardSync(length: number): void
```

删除光标前固定长度的文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [deleteForward](#deleteforward)
   
> 。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## finishTextPreview

```TypeScript
finishTextPreview(): Promise<void>
```

结束预上屏。使用promise异步回调。   
> **说明：**
   
> 
   
> 若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-当前输入框不支持预上屏) |

## finishTextPreviewSync

```TypeScript
finishTextPreviewSync(): void
```

结束预上屏。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [finishTextPreview](#finishtextpreview)。
   
> 
   
> 若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-当前输入框不支持预上屏) |

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions
```

获取绑定输入法时的附加选项。

**起始版本：** 19

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getBackward

```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

获取光标后固定长度的文本。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getBackward

```TypeScript
getBackward(length: number): Promise<string>
```

获取光标后固定长度的文本。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getBackwardSync

```TypeScript
getBackwardSync(length: number): string
```

获取光标后固定长度的文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [getBackward](#getbackward)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo>
```

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。   
> **说明：**
   
> 
   
> 本接口仅适用于适配使用[Panel](arkts-ime-inputmethodengine-panel-i.md)作为软键盘窗口的输入法应用。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;WindowInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800012](../errorcode-inputmethod-framework.md#12800012-软键盘类型面板未创建) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

获取编辑框属性值。使用callback异步回调。 使用场景：根据编辑框类型调整输入法界面、根据编辑框配置提供不同的输入建议、实现特定输入逻辑、适配不同类型的输入框等。 使用后效果：返回编辑框属性信息（包括inputPattern输入类型和enterKeyType回车键类型），输入法应用据此调整键盘布局。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

获取编辑框属性值。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute
```

获取编辑框属性值。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [getEditorAttribute](#geteditorattribute)
   
> 。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## getForward

```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

获取光标前固定长度的文本。使用callback异步回调。 使用场景：分析已输入文本内容以提供智能补全建议、检查文本格式、实现文本预测功能、实现文本语义分析等。 使用后效果：成功时返回光标前指定长度的文本字符串，输入法应用可据此更新候选词或输入建议。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getForward

```TypeScript
getForward(length: number): Promise<string>
```

获取光标前固定长度的文本。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getForwardSync

```TypeScript
getForwardSync(length: number): string
```

获取光标前固定长度的文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口[getForward](#getforward)
   
> 。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(callback: AsyncCallback<number>): void
```

获取光标所在处的文本索引。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(): Promise<number>
```

获取光标所在处的文本索引。使用promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## getTextIndexAtCursorSync

```TypeScript
getTextIndexAtCursorSync(): number
```

获取光标所在处的文本索引。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [getTextIndexAtCursor](#gettextindexatcursor)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

插入文本。使用callback异步回调。 使用场景：插入候选词、插入特殊符号、实现文本自动补全、快速插入常用短语等。 使用后效果：成功时返回true，文本已插入到编辑框光标位置。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

插入文本。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## insertTextSync

```TypeScript
insertTextSync(text: string): void
```

插入文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [insertText](#inserttext)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## moveCursor

```TypeScript
moveCursor(direction: number, callback: AsyncCallback<void>): void
```

移动光标。使用callback异步回调。 使用场景：实现光标移动到特定位置、实现上下左右移动光标功能、实现快速定位、实现自定义光标控制等。 使用后效果：成功时编辑框中的光标按指定方向移动一步。direction取值，1为上移，2为下移，3为左移，4为右移。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## moveCursor

```TypeScript
moveCursor(direction: number): Promise<void>
```

移动光标。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## moveCursorSync

```TypeScript
moveCursorSync(direction: number): void
```

移动光标。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [moveCursor](#movecursor)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## off('attachOptionsDidChange')

```TypeScript
off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void
```

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | 否 |

## on('attachOptionsDidChange')

```TypeScript
on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void
```

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**起始版本：** 19

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

注册或取消注册Messagehandler。   
> **说明：**
   
> 
   
> [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的
   
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)回调函数。
   
> 
   
> 未填写参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md)，并会触发被取消注册对象中
   
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)回调函数。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msgHandler | [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## selectByMovement

```TypeScript
selectByMovement(movement: Movement, callback: AsyncCallback<void>): void
```

根据光标移动方向选中文本。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## selectByMovement

```TypeScript
selectByMovement(movement: Movement): Promise<void>
```

根据光标移动方向选中文本。使用promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## selectByMovementSync

```TypeScript
selectByMovementSync(movement: Movement): void
```

根据光标移动方向选中文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [selectByMovement](#selectbymovement)。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## selectByRange

```TypeScript
selectByRange(range: Range, callback: AsyncCallback<void>): void
```

根据索引范围选中文本。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## selectByRange

```TypeScript
selectByRange(range: Range): Promise<void>
```

根据索引范围选中文本。使用promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## selectByRangeSync

```TypeScript
selectByRangeSync(range: Range): void
```

根据索引范围选中文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [selectByRange](#selectbyrange)
   
> 。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void
```

发送扩展编辑操作。使用callback异步回调。 使用场景：输入法应用需要触发编辑框的扩展编辑功能。例如：用户点击键盘上的剪切按钮时发送CUT操作；用户点击复制按钮时发送COPY操作；用户点击粘贴按钮时发送PASTE操作；用户点击全选按钮时发送SELECT_ALL操作；自定义 工具栏中集成编辑快捷操作。   
> **说明：**
   
> 
   
> 输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件
   
> on('handleExtendAction')
   
> ，从而进一步做出处理。
   
> 
   
> 编辑框响应[ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md)的PASTE命令时，需要编辑框应用申请
   
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
   
> 权限。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction): Promise<void>
```

发送扩展编辑操作。使用promise异步回调。   
> **说明：**
   
> 
   
> 输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件
   
> on('handleExtendAction')
   
> ，从而进一步做出处理。
   
> 
   
> 编辑框响应[ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md)的PASTE命令时，需要编辑框应用申请
   
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
   
> 权限。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

发送功能键。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number): Promise<boolean>
```

发送功能键。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。
   
> 
   
> msgId最大限制256B，msgParam最大限制128KB。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | 是 |
| msgParam | ArrayBuffer | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |
| [12800014](../errorcode-inputmethod-framework.md#12800014-输入法应用非完全访问模式) |
| [12800015](../errorcode-inputmethod-framework.md#12800015-消息接收端无法接收自定义通信数据) |
| [12800016](../errorcode-inputmethod-framework.md#12800016-输入法客户端未处于编辑状态) |

## sendPrivateCommand

```TypeScript
sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。   
> **说明:**
   
> 
   
> - 私有数据通道是系统预置输入法应用与系统特定组件（如文本框、桌面应用等）的通信机制，常用于设备级厂商在特定设备上实现自定义的输入法功能。
   
> 
   
> - 私有数据规格限制：总大小32KB，数量限制5条。
   
> 
   
> - 私有数据默认发送给文本框，如果需要发送给桌面应用，请在私有数据中携带一条`{'sys_cmd':1}`数据。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| commandData | Record & lt;string, CommandDataType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

## setPreviewText

```TypeScript
setPreviewText(text: string, range: Range): Promise<void>
```

设置预上屏文本。使用promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-当前输入框不支持预上屏) |

## setPreviewTextSync

```TypeScript
setPreviewTextSync(text: string, range: Range): void
```

设置预上屏文本。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口[setPreviewText](#setpreviewtext)。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-当前输入框不支持预上屏) |
