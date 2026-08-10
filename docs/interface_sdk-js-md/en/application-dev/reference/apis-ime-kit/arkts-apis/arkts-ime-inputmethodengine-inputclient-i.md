# InputClient

InputClient是输入法客户端对象，代表当前绑定到输入法应用的编辑框客户端。InputClient实例通过InputMethodAbility的  
[on('inputStart')](inputMethodEngine.InputMethodAbility.on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void))事件回调获取，每个绑定事件对应一个InputClient实例，输入法应用通过该实例与编辑框进行文本交互。  
**核心功能概述：**

- **文本获取**：通过  
[getForward](arkts-ime-inputmethodengine-inputclient-i.md#getforward)/  
[getForwardSync](arkts-ime-inputmethodengine-inputclient-i.md#getforwardsync)获取光标前的文本，通过  
[getBackward](arkts-ime-inputmethodengine-inputclient-i.md#getbackward)/  
[getBackwardSync](arkts-ime-inputmethodengine-inputclient-i.md#getbackwardsync)获取光标后的文本，用于分析已输入内容并提供智能补全。  
- **文本编辑**：通过  
[insertText](arkts-ime-inputmethodengine-inputclient-i.md#inserttext)/  
[insertTextSync](arkts-ime-inputmethodengine-inputclient-i.md#inserttextsync)插入文本，通过  
[deleteForward](arkts-ime-inputmethodengine-inputclient-i.md#deleteforward)/  
[deleteForwardSync](arkts-ime-inputmethodengine-inputclient-i.md#deleteforwardsync)删除光标前的文本，通过  
[deleteBackward](arkts-ime-inputmethodengine-inputclient-i.md#deletebackward)/[deleteBackwardSync](arkts-ime-inputmethodengine-inputclient-i.md#deletebackwardsync)删除光标后的文本。  
- **功能键与光标**：通过  
[sendKeyFunction](arkts-ime-inputmethodengine-inputclient-i.md#sendkeyfunction)发送功能键（如回车键），通过  
[moveCursor](arkts-ime-inputmethodengine-inputclient-i.md#movecursor)/  
[moveCursorSync](arkts-ime-inputmethodengine-inputclient-i.md#movecursorsync)移动光标。  
- **选区操作**：通过  
[selectByRange](arkts-ime-inputmethodengine-inputclient-i.md#selectbyrange)/  
[selectByRangeSync](arkts-ime-inputmethodengine-inputclient-i.md#selectbyrangesync)按范围选中文本，通过  
[selectByMovement](arkts-ime-inputmethodengine-inputclient-i.md#selectbymovement)/[selectByMovementSync](arkts-ime-inputmethodengine-inputclient-i.md#selectbymovementsync)按方向选中文本。  
- **编辑框属性**：通过  
[getEditorAttribute](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattribute)/[getEditorAttributeSync](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattributesync)获取编辑框属性信息（输入类型、回车键类型等），据此调整键盘布局。  
- **文本预览**：通过[setPreviewText](arkts-ime-inputmethodengine-inputclient-i.md#setpreviewtext)/  
[setPreviewTextSync](arkts-ime-inputmethodengine-inputclient-i.md#setpreviewtextsync)设置预览文本，通过  
[finishTextPreview](arkts-ime-inputmethodengine-inputclient-i.md#finishtextpreview)/  
[finishTextPreviewSync](arkts-ime-inputmethodengine-inputclient-i.md#finishtextpreviewsync)结束文本预览。  
- **私有通信**：通过[sendPrivateCommand](arkts-ime-inputmethodengine-inputclient-i.md#sendprivatecommand)向应用发送私有命令，通过  
[sendMessage](arkts-ime-inputmethodengine-inputclient-i.md#sendmessage)/  
[recvMessage](arkts-ime-inputmethodengine-inputclient-i.md#recvmessage)进行消息通信。

下列API均需使用  
[on('inputStart')](inputMethodEngine.InputMethodAbility.on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void))获取到InputClient实例后，通过实例调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-interface InputClient--><!--Device-inputMethodEngine-interface InputClient-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
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

删除光标后固定长度的文本。使用callback异步回调。

**使用场景：** 实现删除键功能、删除光标后的字符、快速修正输入、实现自定义删除逻辑等。

**使用后效果：** 成功时返回true，编辑框中光标后指定长度的文本被删除。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteBackward(length: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-deleteBackward(length: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteBackward(length: int): Promise<boolean>--><!--Device-InputClient-deleteBackward(length: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。resolve返回true表示删除光标后固定长度的文本成功；resolve返回false表示删除光标后固定长度的文本失败；reject时抛出错误对 象，表示执行过程中发生错误。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

## deleteBackwardSync

ArkTS-Dyn:
```TypeScript
deleteBackwardSync(length: number): void
```

ArkTS-Sta:
```TypeScript
deleteBackwardSync(length: int): void
```

删除光标后固定长度的文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteBackwardSync(length: int): void--><!--Device-InputClient-deleteBackwardSync(length: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

```TypeScript
let length: number = 1;
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

删除光标前固定长度的文本。使用callback异步回调。

**使用场景：** 实现退格键功能、逐字删除输入、删除错误的输入、实现自定义删除逻辑等。

**使用后效果：** 成功时返回true，编辑框中光标前指定长度的文本被删除。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteForward(length: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-deleteForward(length: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；当光标前固定长度的文本删除失败，err为 undefined，data为false；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteForward(length: int): Promise<boolean>--><!--Device-InputClient-deleteForward(length: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。resolve返回true表示删除光标前固定长度的文本成功；resolve返回false表示删除光标前固定长度的文本失败；reject时抛出错误对 象，表示执行过程中发生错误。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

## deleteForwardSync

ArkTS-Dyn:
```TypeScript
deleteForwardSync(length: number): void
```

ArkTS-Sta:
```TypeScript
deleteForwardSync(length: int): void
```

删除光标前固定长度的文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-deleteForwardSync(length: int): void--><!--Device-InputClient-deleteForwardSync(length: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

```TypeScript
let length: number = 1;
inputClient.deleteForwardSync(length);
```

## finishTextPreview

```TypeScript
finishTextPreview(): Promise<void>
```

结束预上屏。使用promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InputClient-finishTextPreview(): Promise<void>--><!--Device-InputClient-finishTextPreview(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

## Examples

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

结束预上屏。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InputClient-finishTextPreviewSync(): void--><!--Device-InputClient-finishTextPreviewSync(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

## Examples

```TypeScript
inputClient.finishTextPreviewSync();
```

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions
```

获取绑定输入法时的附加选项。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-InputClient-getAttachOptions(): AttachOptions--><!--Device-InputClient-getAttachOptions(): AttachOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | 返回绑定输入法时的附加选项内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.<br>**Applicable version:** 19 and later |

## Examples

```TypeScript
let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions | null
```

获取绑定输入法时的附加选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-getAttachOptions(): AttachOptions | null--><!--Device-InputClient-getAttachOptions(): AttachOptions | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | 返回绑定输入法时的附加选项内容。 |

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-getBackward(length: int, callback: AsyncCallback<string>): void--><!--Device-InputClient-getBackward(length: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-getBackward(length: int): Promise<string>--><!--Device-InputClient-getBackward(length: int): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回光标后固定长度的文本。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## getBackwardSync

ArkTS-Dyn:
```TypeScript
getBackwardSync(length: number): string
```

ArkTS-Sta:
```TypeScript
getBackwardSync(length: int): string
```

获取光标后固定长度的文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-getBackwardSync(length: int): string--><!--Device-InputClient-getBackwardSync(length: int): string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回光标后固定长度的文本。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo>
```

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo>--><!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;WindowInfo&gt; | Promise对象，返回拉起输入法的输入框所在应用窗口信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800013 | window manager service error. |
| 12800012 | the input method panel does not exist. |

## Examples

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

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo | null>--><!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo | null>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;WindowInfo \| null&gt; | Promise对象，返回拉起输入法的输入框所在应用窗口信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800013 | window manager service error. |
| 12800012 | the input method panel does not exist. |

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

获取编辑框属性值。使用callback异步回调。

**使用场景：** 根据编辑框类型调整输入法界面、根据编辑框配置提供不同的输入建议、实现特定输入逻辑、适配不同类型的输入框等。

**使用后效果：** 返回编辑框属性信息（包括inputPattern输入类型和enterKeyType回车键类型），输入法应用据此调整键盘布局。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void--><!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EditorAttribute&gt; | Yes | 回调函数。当编辑框属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## Examples

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

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute | null>): void
```

获取编辑框属性值。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute | null>): void--><!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute | null>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EditorAttribute \| null&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

获取编辑框属性值。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute>--><!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EditorAttribute&gt; | Promise对象，返回编辑框属性值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute | null>
```

获取编辑框属性值。使用promise异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute | null>--><!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute | null>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EditorAttribute \| null&gt; | Promise对象，返回编辑框属性值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute
```

获取编辑框属性值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-InputClient-getEditorAttributeSync(): EditorAttribute--><!--Device-InputClient-getEditorAttributeSync(): EditorAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) | 编辑框属性对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## Examples

```TypeScript
let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute | null
```

获取编辑框属性值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-getEditorAttributeSync(): EditorAttribute | null--><!--Device-InputClient-getEditorAttributeSync(): EditorAttribute | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) | 编辑框属性对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

## getForward

ArkTS-Dyn:
```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

ArkTS-Sta:
```TypeScript
getForward(length: int, callback: AsyncCallback<string>): void
```

获取光标前固定长度的文本。使用callback异步回调。  
**使用场景：** 分析已输入文本内容以提供智能补全建议、检查文本格式、实现文本预测功能、实现文本语义分析等。  
**使用后效果：** 成功时返回光标前指定长度的文本字符串，输入法应用可据此更新候选词或输入建议。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-getForward(length: int, callback: AsyncCallback<string>): void--><!--Device-InputClient-getForward(length: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-getForward(length: int): Promise<string>--><!--Device-InputClient-getForward(length: int): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回光标前固定长度的文本。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

## getForwardSync

ArkTS-Dyn:
```TypeScript
getForwardSync(length: number): string
```

ArkTS-Sta:
```TypeScript
getForwardSync(length: int): string
```

获取光标前固定长度的文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-getForwardSync(length: int): string--><!--Device-InputClient-getForwardSync(length: int): string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本长度。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回光标前固定长度的文本。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
let length: number = 1;
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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-getTextIndexAtCursor(callback: AsyncCallback<int>): void--><!--Device-InputClient-getTextIndexAtCursor(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | 回调函数。当文本索引获取成功，err为undefined，index为光标所在处的文本索引；否则err为错误对象，index为 undefined。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-getTextIndexAtCursor(): Promise<int>--><!--Device-InputClient-getTextIndexAtCursor(): Promise<int>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回光标所在处的文本索引。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## getTextIndexAtCursorSync

ArkTS-Dyn:
```TypeScript
getTextIndexAtCursorSync(): number
```

ArkTS-Sta:
```TypeScript
getTextIndexAtCursorSync(): int
```

获取光标所在处的文本索引。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-getTextIndexAtCursorSync(): int--><!--Device-InputClient-getTextIndexAtCursorSync(): int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 返回光标所在处的文本索引。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

插入文本。使用callback异步回调。

**使用场景：** 插入候选词、插入特殊符号、实现文本自动补全、快速插入常用短语等。

**使用后效果：** 成功时返回true，文本已插入到编辑框光标位置。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-insertText(text: string, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-insertText(text: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 文本内容。建议长度不超过1KB。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

插入文本。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-insertText(text: string): Promise<boolean>--><!--Device-InputClient-insertText(text: string): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 文本。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。resolve返回true表示插入文本成功；resolve返回false表示插入文本失败；reject时抛出错误对象，表示执行过程中发生错误。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

## insertTextSync

```TypeScript
insertTextSync(text: string): void
```

插入文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-insertTextSync(text: string): void--><!--Device-InputClient-insertTextSync(text: string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 文本内容。建议长度不超过1KB。建议长度不超过1KB。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |

## Examples

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

移动光标。使用callback异步回调。

**使用场景：** 实现光标移动到特定位置、实现上下左右移动光标功能、实现快速定位、实现自定义光标控制等。

**使用后效果：** 成功时编辑框中的光标按指定方向移动一步。direction取值参见

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-moveCursor(direction: int, callback: AsyncCallback<void>): void--><!--Device-InputClient-moveCursor(direction: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 光标移动方向。&lt;br/&gt;- 当值为1时，表示向上。&lt;br/&gt;- 当值为2时，表示向下。&lt;br/&gt;- 当值为3时，表示向左。&lt;br/&gt;- 当值为4时，表示向右。不能小于0。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当光标移动成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-moveCursor(direction: int): Promise<void>--><!--Device-InputClient-moveCursor(direction: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 光标移动方向。&lt;br/&gt;- 当值为1时，表示向上。&lt;br/&gt;- 当值为2时，表示向下。&lt;br/&gt;- 当值为3时，表示向左。&lt;br/&gt;- 当值为4时，表示向右。不能小于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## moveCursorSync

ArkTS-Dyn:
```TypeScript
moveCursorSync(direction: number): void
```

ArkTS-Sta:
```TypeScript
moveCursorSync(direction: int): void
```

移动光标。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-moveCursorSync(direction: int): void--><!--Device-InputClient-moveCursorSync(direction: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 光标移动方向。&lt;br/&gt;- 当值为1时，表示向上。&lt;br/&gt;- 当值为2时，表示向下。&lt;br/&gt;- 当值为3时，表示向左。&lt;br/&gt;- 当值为4时，表示向右。不能小于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

## off('attachOptionsDidChange')

```TypeScript
off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void
```

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-InputClient-off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void--><!--Device-InputClient-off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | No | 取消订阅的回调函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-offAttachOptionsDidChange(callback?: Callback<AttachOptions>): void--><!--Device-InputClient-offAttachOptionsDidChange(callback?: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | No | 回调函数。 可选参数，需取消的目标回调函数：传入指定回调函数实例时，仅取消该回调的订阅；不传入时，取消所有attachOptionsDidChange事件的订阅。 |

## on('attachOptionsDidChange')

```TypeScript
on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void
```

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-InputClient-on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void--><!--Device-InputClient-on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | Yes | 回调函数，返回绑定输入法时的附加选项。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported.<br>**Applicable version:** 19 and later |

## Examples

```TypeScript
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

## onAttachOptionsDidChange

```TypeScript
onAttachOptionsDidChange(callback: Callback<AttachOptions>): void
```

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputClient-onAttachOptionsDidChange(callback: Callback<AttachOptions>): void--><!--Device-InputClient-onAttachOptionsDidChange(callback: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | Yes | 回调函数，返回绑定输入法时的附加选项。 |

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

注册或取消注册Messagehandler。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-InputClient-recvMessage(msgHandler?: MessageHandler): void--><!--Device-InputClient-recvMessage(msgHandler?: MessageHandler): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgHandler | [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | No | 该对象将通过 [onMessage](arkts-ime-inputmethodengine-messagehandler-i.md#onmessage)接收来自已绑定当前 输入法应用的编辑框应用所发送的自定义通信数据，并通过[onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)接收终止此对象订阅的消息。 &lt;br&gt;若不填写此参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md)对象，同时触发其 [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated)回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement, callback: AsyncCallback<void>): void
```

根据光标移动方向选中文本。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByMovement(movement: Movement, callback: AsyncCallback<void>): void--><!--Device-InputClient-selectByMovement(movement: Movement, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes | 选中时光标移动的方向。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement): Promise<void>
```

根据光标移动方向选中文本。使用promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByMovement(movement: Movement): Promise<void>--><!--Device-InputClient-selectByMovement(movement: Movement): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes | 选中时光标移动的方向。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByMovementSync

```TypeScript
selectByMovementSync(movement: Movement): void
```

根据光标移动方向选中文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByMovementSync(movement: Movement): void--><!--Device-InputClient-selectByMovementSync(movement: Movement): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes | 选中时光标移动的方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

## Examples

```TypeScript
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);
```

## selectByRange

```TypeScript
selectByRange(range: Range, callback: AsyncCallback<void>): void
```

根据索引范围选中文本。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByRange(range: Range, callback: AsyncCallback<void>): void--><!--Device-InputClient-selectByRange(range: Range, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 选中文本的范围。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});
```

## selectByRange

```TypeScript
selectByRange(range: Range): Promise<void>
```

根据索引范围选中文本。使用promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByRange(range: Range): Promise<void>--><!--Device-InputClient-selectByRange(range: Range): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 选中文本的范围。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByRangeSync

```TypeScript
selectByRangeSync(range: Range): void
```

根据索引范围选中文本。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-selectByRangeSync(range: Range): void--><!--Device-InputClient-selectByRangeSync(range: Range): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 选中文本的范围。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);
```

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void
```

发送扩展编辑操作。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void--><!--Device-InputClient-sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes | 要发送的扩展操作。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。发送成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

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

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction): Promise<void>
```

发送扩展编辑操作。使用promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputClient-sendExtendAction(action: ExtendAction): Promise<void>--><!--Device-InputClient-sendExtendAction(action: ExtendAction): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes | 要发送的扩展操作。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
});
```

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-sendKeyFunction(action: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-sendKeyFunction(action: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 功能键键值。&lt;br/&gt;- 当值为0时，表示无效按键。&lt;br/&gt;- 当值为1时，表示确认键（即回车键）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。当功能键发送成功，err为undefined，data为true；当功能键发送失败，err为undefined，data为 false；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputClient-sendKeyFunction(action: int): Promise<boolean>--><!--Device-InputClient-sendKeyFunction(action: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| action | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 功能键键值。&lt;br/&gt;当值为0时，表示无效按键；&lt;br/&gt;当值为1时，表示确认键（即回车键）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。resolve返回true表示功能键发送成功；resolve返回false表示功能键发送失败；reject时抛出错误对象，表示执行过程中发生错误。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

## Examples

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

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-InputClient-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>--><!--Device-InputClient-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的标识符。最大长度256字节。最大长度256字节。 |
| msgParam | ArrayBuffer | No | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的消息体。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800016 | input method client is not editable. |
| 12800009 | input method client detached. |
| 12800015 | the other side does not accept the request. |
| 12800014 | the input method is in basic mode. |

## Examples

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

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InputClient-sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>--><!--Device-InputClient-sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| commandData | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, CommandDataType&gt; | Yes | 私有数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800010 | not the preconfigured default input method. |

## Examples

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
    if (err !== undefined) {
      console.error(`sendPrivateCommand catch error: ${err.code} ${err.message}`);
    }
  });
})
```

## setPreviewText

```TypeScript
setPreviewText(text: string, range: Range): Promise<void>
```

设置预上屏文本。使用promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InputClient-setPreviewText(text: string, range: Range): Promise<void>--><!--Device-InputClient-setPreviewText(text: string, range: Range): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 预上屏的文本。建议长度不超过1KB。 |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 替换的文本范围。&lt;br/&gt;- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。&lt;br/&gt;- 当start等于end，默认将参 数text插入start对应的光标位置。&lt;br/&gt;- 当start不等于end，将参数text替换range对应区域的文本。&lt;br/&gt;- 当start与end为其他含有负数值的组合，按照参数错误返回。&lt;br/&gt;- 当输 入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。&lt;br/&gt;- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800011 | text preview not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

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

设置预上屏文本。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-InputClient-setPreviewTextSync(text: string, range: Range): void--><!--Device-InputClient-setPreviewTextSync(text: string, range: Range): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 预上屏的文本。建议长度不超过1KB。 |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 替换的文本范围。&lt;br/&gt;- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。&lt;br/&gt;- 当start等于end，默认将参 数text插入start对应的光标位置。&lt;br/&gt;- 当start不等于end，将参数text替换range对应区域的文本。&lt;br/&gt;- 当start与end为其他含有负数值的组合，按照参数错误返回。&lt;br/&gt;- 当输 入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。&lt;br/&gt;- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 12800011 | text preview not supported. |

## Examples

```TypeScript
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);
```

