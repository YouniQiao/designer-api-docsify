# InputClient

InputClient是输入法客户端对象，代表当前绑定到输入法应用的编辑框客户端。InputClient实例通过InputMethodAbility的 on('inputStart') 事件回调获取，每个绑定事件对应一个InputClient实例，输入法应用通过该实例与编辑框进行文本交互。 <br> <br>核心功能概述： <br> <br>- 文本获取：通过[getForward](#getforward) /[getForwardSync](#getforwardsync)获取光标前的文本，通过 [getBackward](#getbackward)/ [getBackwardSync](#getbackwardsync)获取光标后的文本，用于分析已输入内容并提供智能补全。 <br>- 文本编辑：通过 [insertText](#inserttext)/ [insertTextSync](#inserttextsync)插入文本，通过 [deleteForward](#deleteforward)/ [deleteForwardSync](#deleteforwardsync)删除光标前的文本，通过 [deleteBackward](#deletebackward) /[deleteBackwardSync](#deletebackwardsync)删除光标后的文本。 <br>- 功能键与光标：通过 [sendKeyFunction](#sendkeyfunction) 发送功能键（如回车键），通过 [moveCursor](#movecursor)/ [moveCursorSync](#movecursorsync)移动光标。 <br>- 选区操作：通过 [selectByRange](#selectbyrange)/ [selectByRangeSync](#selectbyrangesync)按范围选中文本，通过 [selectByMovement](#selectbymovement) /[selectByMovementSync](#selectbymovementsync)按方向选中文本。 <br>- 编辑框属性：通过 [getEditorAttribute](#geteditorattribute) /[getEditorAttributeSync](#geteditorattributesync)获取编辑框属性信息（输入类型、回车键类型等），据此调整键 盘布局。 <br>- 文本预览：通过[setPreviewText](#setpreviewtext)/ [setPreviewTextSync](#setpreviewtextsync)设置预览文本，通过 [finishTextPreview](#finishtextpreview)/ [finishTextPreviewSync](#finishtextpreviewsync)结束文本预览。 <br>- 私有通信：通过[sendPrivateCommand](#sendprivatecommand)向应用发送私有命令，通过 [sendMessage](#sendmessage)/ [recvMessage](#recvmessage)进行消息通信。 <br> <br>注意事项： <br> <br>- InputClient实例与当前绑定的编辑框关联，当编辑框失去焦点或输入法解绑时，该实例可能失效。 <br>- 同名Sync后缀接口为同步接口，阻塞主线程，容易影响UI交互，需谨慎使用。 <br> <br>下列API均需使用 on('inputStart') 获取到InputClient实例后，通过实例调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## deleteBackward

ArkTS-Dyn:
```TypeScript
deleteBackward(length: number, callback: AsyncCallback<boolean>): void
```

ArkTS-Sta:
```TypeScript
deleteBackward(length: int, callback: AsyncCallback<boolean>): void
```

删除光标后固定长度的文本。使用callback异步回调。 <br> <br>使用场景：实现删除键功能、删除光标后的字符、快速修正输入、实现自定义删除逻辑等。 <br> <br>使用后效果：成功时返回true，编辑框中光标后指定长度的文本被删除。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(`Failed to deleteBackward.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(`Failed to deleteBackward.`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## deleteBackward

ArkTS-Dyn:
```TypeScript
deleteBackward(length: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
deleteBackward(length: int): Promise<boolean>
```

删除光标后固定长度的文本。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

参见 [deleteBackward](#deletebackward)

## deleteBackwardSync

ArkTS-Dyn:
```TypeScript
deleteBackwardSync(length: number): void
```

ArkTS-Sta:
```TypeScript
deleteBackwardSync(length: int): void
```

删除光标后固定长度的文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [deleteBackward](#deletebackward)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let length: number = 1;
inputClient.deleteBackwardSync(length);
```

ArkTS-Sta示例：

```TypeScript
let length: int = 1;
inputClient.deleteBackwardSync(length);
```

## deleteForward

ArkTS-Dyn:
```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

ArkTS-Sta:
```TypeScript
deleteForward(length: int, callback: AsyncCallback<boolean>): void
```

删除光标前固定长度的文本。使用callback异步回调。 <br> <br>使用场景：实现退格键功能、逐字删除输入、删除错误的输入、实现自定义删除逻辑等。 <br> <br>使用后效果：成功时返回true，编辑框中光标前指定长度的文本被删除。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(`Failed to deleteForward.`);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(`Failed to deleteForward.`);
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to deleteForward.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

## deleteForward

ArkTS-Dyn:
```TypeScript
deleteForward(length: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
deleteForward(length: int): Promise<boolean>
```

删除光标前固定长度的文本。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

参见 [deleteForward](#deleteforward)

## deleteForwardSync

ArkTS-Dyn:
```TypeScript
deleteForwardSync(length: number): void
```

ArkTS-Sta:
```TypeScript
deleteForwardSync(length: int): void
```

删除光标前固定长度的文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [deleteForward](#deleteforward) &lt;br
&gt; 
> 。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let length: number = 1;
inputClient.deleteForwardSync(length);
```

ArkTS-Sta示例：

```TypeScript
let length: int = 1;
inputClient.deleteForwardSync(length);
```

## finishTextPreview

```TypeScript
finishTextPreview(): Promise<void>
```

结束预上屏。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.finishTextPreview().then(() => {
  console.info('Succeeded in finishing text preview.');
}).catch((err: BusinessError) => {
  console.error(`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}`);
});
```

## finishTextPreviewSync

```TypeScript
finishTextPreviewSync(): void
```

结束预上屏。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [finishTextPreview](#finishtextpreview)。 &lt;br
&gt; 
> &lt;br
&gt; 
> 若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-当前输入框不支持预上屏) |

**示例**

```TypeScript
inputClient.finishTextPreviewSync();
```

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions
```

获取绑定输入法时的附加选项。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

```TypeScript
let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions | null
```

获取绑定输入法时的附加选项。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| AttachOptions \| null |

**示例**

参见 [getAttachOptions](#getattachoptions)

## getBackward

ArkTS-Dyn:
```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

ArkTS-Sta:
```TypeScript
getBackward(length: int, callback: AsyncCallback<string>): void
```

获取光标后固定长度的文本。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length).then((text: string) => {
  console.info(`'Succeeded in getting backward: ${text}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## getBackward

ArkTS-Dyn:
```TypeScript
getBackward(length: number): Promise<string>
```

ArkTS-Sta:
```TypeScript
getBackward(length: int): Promise<string>
```

获取光标后固定长度的文本。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

参见 [getBackward](#getbackward)

## getBackwardSync

ArkTS-Dyn:
```TypeScript
getBackwardSync(length: number): string
```

ArkTS-Sta:
```TypeScript
getBackwardSync(length: int): string
```

获取光标后固定长度的文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [getBackward](#getbackward)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

ArkTS-Dyn示例：

```TypeScript
let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

ArkTS-Sta示例：

```TypeScript
let length: int = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo>
```

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 本接口仅适用于适配使用[Panel](arkts-ime-inputmethodengine-panel-i.md)作为软键盘窗口的输入法应用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
  console.info(`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}`);
  console.info(`windowInfo.status: ${windowInfo.status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}`);
});
```

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo | null>
```

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 本接口仅适用于适配使用[Panel](arkts-ime-inputmethodengine-panel-i.md)作为软键盘窗口的输入法应用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;WindowInfo \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800012](../errorcode-inputmethod-framework.md#12800012-软键盘类型面板未创建) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

参见 [getCallingWindowInfo](#getcallingwindowinfo)

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

获取编辑框属性值。使用callback异步回调。 <br> <br>使用场景：根据编辑框类型调整输入法界面、根据编辑框配置提供不同的输入建议、实现特定输入逻辑、适配不同类型的输入框等。 <br> <br>使用后效果：返回编辑框属性信息（包括inputPattern输入类型和enterKeyType回车键类型），输入法应用据此调整键盘布局。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';


textInputClient.getEditorAttribute((err: BusinessError,
  editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute | null>): void
```

获取编辑框属性值。使用callback异步回调。 <br> <br>使用场景：根据编辑框类型调整输入法界面、根据编辑框配置提供不同的输入建议、实现特定输入逻辑、适配不同类型的输入框等。 <br> <br>使用后效果：返回编辑框属性信息（包括inputPattern输入类型和enterKeyType回车键类型），输入法应用据此调整键盘布局。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) \| null & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [getEditorAttribute](#geteditorattribute)

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

获取编辑框属性值。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [getEditorAttribute](#geteditorattribute)

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute | null>
```

获取编辑框属性值。使用promise异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [getEditorAttribute](#geteditorattribute)

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute
```

获取编辑框属性值。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [getEditorAttribute](#geteditorattribute) &lt;br
&gt; 
> 。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

```TypeScript
let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute | null
```

获取编辑框属性值。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [getEditorAttribute](#geteditorattribute) &lt;br
&gt; 
> 。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) \| null |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [getEditorAttributeSync](#geteditorattributesync)

## getForward

ArkTS-Dyn:
```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

ArkTS-Sta:
```TypeScript
getForward(length: int, callback: AsyncCallback<string>): void
```

获取光标前固定长度的文本。使用callback异步回调。 <br> <br>使用场景：分析已输入文本内容以提供智能补全建议、检查文本格式、实现文本预测功能、实现文本语义分析等。 使用后效果：成功时返回光标前指定长度的文本字符串，输入法应用可据此更新候选词或输入建议。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: int = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

## getForward

ArkTS-Dyn:
```TypeScript
getForward(length: number): Promise<string>
```

ArkTS-Sta:
```TypeScript
getForward(length: int): Promise<string>
```

获取光标前固定长度的文本。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

参见 [getForward](#getforward)

## getForwardSync

ArkTS-Dyn:
```TypeScript
getForwardSync(length: number): string
```

ArkTS-Sta:
```TypeScript
getForwardSync(length: int): string
```

获取光标前固定长度的文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口[getForward](#getforward) &lt;br
&gt; 
> 。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

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

**示例**

ArkTS-Dyn示例：

```TypeScript
let length: number = 1;
let text: string = inputClient.getForwardSync(length);
console.info(`Succeeded in getting forward, text: ${text}`);
```

ArkTS-Sta示例：

```TypeScript
let length: int = 1;
let text: string = inputClient.getForwardSync(length);
console.info(`Succeeded in getting forward, text: ${text}`);
```

## getTextIndexAtCursor

ArkTS-Dyn:
```TypeScript
getTextIndexAtCursor(callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
getTextIndexAtCursor(callback: AsyncCallback<int>): void
```

获取光标所在处的文本索引。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
  if (err) {
    console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: int) => {
  if (err) {
    console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: int) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## getTextIndexAtCursor

ArkTS-Dyn:
```TypeScript
getTextIndexAtCursor(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getTextIndexAtCursor(): Promise<int>
```

获取光标所在处的文本索引。使用promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

**示例**

参见 [getTextIndexAtCursor](#gettextindexatcursor)

## getTextIndexAtCursorSync

ArkTS-Dyn:
```TypeScript
getTextIndexAtCursorSync(): number
```

ArkTS-Sta:
```TypeScript
getTextIndexAtCursorSync(): int
```

获取光标所在处的文本索引。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [getTextIndexAtCursor](#gettextindexatcursor)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-输入法控制器异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

ArkTS-Sta示例：

```TypeScript
let index: int = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

插入文本。使用callback异步回调。 <br> <br>使用场景：插入候选词、插入特殊符号、实现文本自动补全、快速插入常用短语等。 <br> <br>使用后效果：成功时返回true，文本已插入到编辑框光标位置。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';


inputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

插入文本。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

参见 [insertText](#inserttext)

## insertTextSync

```TypeScript
insertTextSync(text: string): void
```

插入文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [insertText](#inserttext)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
inputClient.insertTextSync('test');
```

## moveCursor

ArkTS-Dyn:
```TypeScript
moveCursor(direction: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
moveCursor(direction: int, callback: AsyncCallback<void>): void
```

移动光标。使用callback异步回调。 <br> <br>使用场景：实现光标移动到特定位置、实现上下左右移动光标功能、实现快速定位、实现自定义光标控制等。 <br> <br>使用后效果：成功时编辑框中的光标按指定方向移动一步。direction取值，1为上移，2为下移，3为左移，4为右移。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving cursor.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## moveCursor

ArkTS-Dyn:
```TypeScript
moveCursor(direction: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
moveCursor(direction: int): Promise<void>
```

移动光标。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [moveCursor](#movecursor)

## moveCursorSync

ArkTS-Dyn:
```TypeScript
moveCursorSync(direction: number): void
```

ArkTS-Sta:
```TypeScript
moveCursorSync(direction: int): void
```

移动光标。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [moveCursor](#movecursor)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

```TypeScript
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

## off('attachOptionsDidChange')

```TypeScript
off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void
```

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | 否 |

**示例**

```TypeScript
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (_attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

## offAttachOptionsDidChange

```TypeScript
offAttachOptionsDidChange(callback?: Callback<AttachOptions>): void
```

取消订阅附加选项变更（attachOptionsDidChange）事件，停止监听输入法附加配置项的变更动作。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | 否 |

**示例**

```TypeScript
let attachOptionsDidChangeCallback = (attachOptions: inputMethodEngine.AttachOptions) => {
  console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
};

inputMethodEngine.getInputMethodAbility()
  .onInputStart((kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
  let keyboardController = kbController;
  let inputClient = client;
  inputClient.onAttachOptionsDidChange(attachOptionsDidChangeCallback);
  console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
  inputClient.offAttachOptionsDidChange(attachOptionsDidChangeCallback);
  console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
});
```

## on('attachOptionsDidChange')

```TypeScript
on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void
```

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**起始版本：** 19

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为19。

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

**示例**

```TypeScript
// 创建附加选项变更回调函数
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (_attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

// 订阅绑定输入法时的附加选项变更事件
inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
// 取消订阅绑定输入法时的附加选项变更事件
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

## onAttachOptionsDidChange

```TypeScript
onAttachOptionsDidChange(callback: Callback<AttachOptions>): void
```

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | 是 |

**示例**

```TypeScript
let attachOptionsDidChangeCallback = (attachOptions: inputMethodEngine.AttachOptions) => {
  console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
};

inputMethodEngine.getInputMethodAbility()
  .onInputStart((kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
  let keyboardController = kbController;
  let inputClient = client;
  inputClient.onAttachOptionsDidChange(attachOptionsDidChangeCallback);
  console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
  inputClient.offAttachOptionsDidChange(attachOptionsDidChangeCallback);
  console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
});
```

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

注册或取消注册Messagehandler。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的 &lt;br
&gt; 
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 未填写参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md)，并会触发被取消注册对象中 &lt;br
&gt; 
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)回调函数。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msgHandler | [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      // 创建消息处理器，用于接收编辑框应用发送的自定义通信数据
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      // 注册消息处理器
      client.recvMessage(messageHandler);
    });
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement, callback: AsyncCallback<void>): void
```

根据光标移动方向选中文本。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置选中时光标向上移动
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置选中时光标向上移动
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement): Promise<void>
```

根据光标移动方向选中文本。使用promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

参见 [selectByMovement](#selectbymovement)

## selectByMovementSync

```TypeScript
selectByMovementSync(movement: Movement): void
```

根据光标移动方向选中文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [selectByMovement](#selectbymovement)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// 设置选中时光标向上移动
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);
```

## selectByRange

```TypeScript
selectByRange(range: Range, callback: AsyncCallback<void>): void
```

根据索引范围选中文本。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置预上屏文本的替换范围为第一个字符
// 设置选中文本的起始和结束位置
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置预上屏文本的替换范围为第一个字符
// 设置选中文本的起始和结束位置
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByRange

```TypeScript
selectByRange(range: Range): Promise<void>
```

根据索引范围选中文本。使用promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

参见 [selectByRange](#selectbyrange)

## selectByRangeSync

```TypeScript
selectByRangeSync(range: Range): void
```

根据索引范围选中文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口 &lt;br
&gt; 
> [selectByRange](#selectbyrange) &lt;br
&gt; 
> 。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// 设置预上屏文本的替换范围为第一个字符
// 设置选中文本的起始和结束位置
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);
```

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void
```

发送扩展编辑操作。使用callback异步回调。 <br> <br>使用场景：输入法应用需要触发编辑框的扩展编辑功能。例如：用户点击键盘上的剪切按钮时发送CUT操作；用户点击复制按钮时发送COPY操作；用户点击粘贴按钮时发送PASTE操作；用户点击全选按钮时发送SELECT_ALL操作；自定义 <br> <br>工具栏中集成编辑快捷操作。 <br> <br>   
> **说明：**&lt;br
&gt; 
> &lt;br
&gt; 
> 输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件 &lt;br
&gt; 
> on('handleExtendAction') &lt;br
&gt; 
> ，从而进一步做出处理。 &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框响应[ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md)的PASTE命令时，需要编辑框应用申请 &lt;br
&gt; 
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard) &lt;br
&gt; 
> 权限。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in sending extend action.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
});
```

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction): Promise<void>
```

发送扩展编辑操作。使用promise异步回调。 <br> <br>   
> **说明：**&lt;br
&gt; 
> &lt;br
&gt; 
> 输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件 &lt;br
&gt; 
> on('handleExtendAction') &lt;br
&gt; 
> ，从而进一步做出处理。 &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框响应[ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md)的PASTE命令时，需要编辑框应用申请 &lt;br
&gt; 
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard) &lt;br
&gt; 
> 权限。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

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

**示例**

参见 [sendExtendAction](#sendextendaction)

## sendKeyFunction

ArkTS-Dyn:
```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

ArkTS-Sta:
```TypeScript
sendKeyFunction(action: int, callback: AsyncCallback<boolean>): void
```

发送功能键。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: int = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: int = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}`);
});
```

## sendKeyFunction

ArkTS-Dyn:
```TypeScript
sendKeyFunction(action: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
sendKeyFunction(action: int): Promise<boolean>
```

发送功能键。使用promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

**示例**

参见 [sendKeyFunction](#sendkeyfunction)

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。 &lt;br
&gt; 
> &lt;br
&gt; 
> msgId最大限制256B，msgParam最大限制128KB。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputClient.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message. Code is ${err.code}, message is ${err.message}`);
});
```

## sendPrivateCommand

```TypeScript
sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。 <br> <br>   
> **说明:** &lt;br
&gt; 
> &lt;br
&gt; 
> - 私有数据通道是系统预置输入法应用与系统特定组件（如文本框、桌面应用等）的通信机制，常用于设备级厂商在特定设备上实现自定义的输入法功能。 &lt;br
&gt; 
> &lt;br
&gt; 
> - 私有数据规格限制：总大小32KB，数量限制5条。 &lt;br
&gt; 
> &lt;br
&gt; 
> - 私有数据默认发送给文本框，如果需要发送给桌面应用，请在私有数据中携带一条`{'sys_cmd':1}`数据。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
  let record: Record<string, inputMethodEngine.CommandDataType> = {
    "valueString1": "abcdefg",
    "valueString2": true,
    "valueString3": 500,
  }
  textInputClient.sendPrivateCommand(record).then(() => {
  }).catch((err: BusinessError) => {
    if (err) {
      console.error(`sendPrivateCommand catch error: ${err.code}, message: ${err.message}`);
    }
  });
})
```

## setPreviewText

```TypeScript
setPreviewText(text: string, range: Range): Promise<void>
```

设置预上屏文本。使用promise异步回调。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置预上屏文本的替换范围为第一个字符
// 设置选中文本的起始和结束位置
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewText('test', range).then(() => {
  console.info('Succeeded in setting preview text.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}`);
});
```

## setPreviewTextSync

```TypeScript
setPreviewTextSync(text: string, range: Range): void
```

设置预上屏文本。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口[setPreviewText](#setpreviewtext)。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// 设置预上屏文本的替换范围为第一个字符
// 设置选中文本的起始和结束位置
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);
```
