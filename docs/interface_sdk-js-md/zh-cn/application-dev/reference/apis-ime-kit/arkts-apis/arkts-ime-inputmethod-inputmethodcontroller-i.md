# InputMethodController

**起始版本：** 23

<!--Device-inputMethod-interface InputMethodController--><!--Device-inputMethod-interface InputMethodController-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。 <br>- true表示拉起。 <br>- false表示不拉起。 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 | 编辑框的配置信息。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当绑定输入法成功后，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in attaching the inputMethod.');
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let textConfig: inputMethod.TextConfig = {
  inputAttribute: {
    textInputType: inputMethod.TextInputType.TEXT,
    enterKeyType: inputMethod.EnterKeyType.NONE
  }
};
inputMethodController.attach(true, textConfig, (err?: BusinessError) => {
  if (err) {
    console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in attaching the inputMethod.');
});
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。 <br>- true表示拉起。 <br>- false表示不拉起。 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 | 编辑框的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let textConfig: inputMethod.TextConfig = {
  inputAttribute: {
    textInputType: inputMethod.TextInputType.TEXT,
    enterKeyType: inputMethod.EnterKeyType.NONE
  }
};
inputMethodController.attach(true, textConfig).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError): void => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
})
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。 <br>- true表示拉起。 <br>- false表示不拉起。 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 | 编辑框的配置信息。 |
| requestKeyboardReason | RequestKeyboardReason | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().attach(true, textConfig, requestKeyboardReason).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let textConfig: inputMethod.TextConfig = {
  inputAttribute: {
    textInputType: inputMethod.TextInputType.TEXT,
    enterKeyType: inputMethod.EnterKeyType.NONE
  }
};
let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;
inputMethodController.attach(true, textConfig, requestKeyboardReason).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
})
```

## attachWithUIContext

```TypeScript
attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>
```

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodController-attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>--><!--Device-InputMethodController-attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md) | 是 | UIContext实例对象。 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 | 编辑框的配置信息。 |
| attachOptions | AttachOptions | 否 | 绑定附加选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext } from '@kit.ArkUI';

let uiContext: UIContext | undefined = UIContext.getCallingScopeUIContext();
let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let attachOptions: inputMethod.AttachOptions = { showKeyboard: true };
inputMethod.getController().attachWithUIContext(uiContext, textConfig, attachOptions).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext } from '@kit.ArkUI';

let uiContext: UIContext = UIContext.getCallingScopeUIContext()!;
let inputAttribute: inputMethod.InputAttribute = {
    textInputType: inputMethod.TextInputType.TEXT,
    enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let attachOptions: inputMethod.AttachOptions = { showKeyboard: true };
inputMethod.getController().attachWithUIContext(uiContext, textConfig, attachOptions).then(() => {
    console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError): void=> {
    console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

## changeSelection

```TypeScript
changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 整个输入文本。 |
| start | int | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | int | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当文本信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('text', 0, 5, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in changing selection.');
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.changeSelection('text', 0, 5, (err?: BusinessError) => {
  if (err) {
    console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in changing selection.');
});
```

## changeSelection

```TypeScript
changeSelection(text: string, start: int, end: int): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-changeSelection(text: string, start: int, end: int): Promise<void>--><!--Device-InputMethodController-changeSelection(text: string, start: int, end: int): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 整个输入文本。 |
| start | int | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | int | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('test', 0, 5).then(() => {
  console.info('Succeeded in changing selection.');
}).catch((err: BusinessError) => {
  console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.changeSelection('test', 0, 5).then(() => {
  console.info('Succeeded in changing selection.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
})
```

## detach

```TypeScript
detach(callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-detach(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-detach(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当解绑定输入法成功时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach((err: BusinessError) => {
  if (err) {
    console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in detaching inputMethod.');
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.detach((err?: BusinessError) => {
  if (err) {
    console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in detaching inputMethod.');
});
```

## detach

```TypeScript
detach(): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-detach(): Promise<void>--><!--Device-InputMethodController-detach(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach().then(() => {
  console.info('Succeeded in detaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.detach().then(() => {
  console.info('Succeeded in detaching inputMethod.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
});
```

## discardTypingText

```TypeScript
discardTypingText(): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-discardTypingText(): Promise<void>--><!--Device-InputMethodController-discardTypingText(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800015](../errorcode-inputmethod-framework.md#12800015-消息接收端无法接收自定义通信数据) | the other side does not accept the request. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().discardTypingText().then(() => {
  console.info('Succeeded discardTypingText.');
}).catch((err: BusinessError) => {
  console.error(`Failed to discardTypingText, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethod } from '@kit.IMEKit';

inputMethod.getController().discardTypingText().then(() => {
  console.info('Succeeded discardTypingText.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to discardTypingText errCode:${err.code}, errMsg:${err.message}`);
});
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(callback: AsyncCallback<void>): void
```

**起始版本：** 23

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-hideSoftKeyboard(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-hideSoftKeyboard(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当软键盘隐藏成功。err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-权限校验失败) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in hiding softKeyboard.');
  } else {
    console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
  }
})
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.hideSoftKeyboard((err?: BusinessError) => {
  if (!err) {
    console.info('Succeeded in hiding softKeyboard.');
  } else {
    console.error(`Failed to hideSoftKeyboard, code: ${err.code}, message: ${err.message}`);
  }
})
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(): Promise<void>
```

**起始版本：** 23

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-hideSoftKeyboard(): Promise<void>--><!--Device-InputMethodController-hideSoftKeyboard(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-权限校验失败) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard().then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.hideSoftKeyboard().then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to hideSoftKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## hideTextInput

```TypeScript
hideTextInput(callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-hideTextInput(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-hideTextInput(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当成功退出编辑状态时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding text input.');
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.hideTextInput((err?: BusinessError) => {
  if (err) {
    console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding text input.');
});
```

## hideTextInput

```TypeScript
hideTextInput(): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-hideTextInput(): Promise<void>--><!--Device-InputMethodController-hideTextInput(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput().then(() => {
  console.info('Succeeded in hiding inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
})
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.hideTextInput().then(() => {
  console.info('Succeeded in hiding inputMethod.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
})
```

## offDeleteLeft

```TypeScript
offDeleteLeft(callback?: Callback<int>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offDeleteLeft(callback?: Callback<int>): void--><!--Device-InputMethodController-offDeleteLeft(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onDeleteLeftCallback = (length: int) => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
};
inputMethodController.offDeleteLeft(onDeleteLeftCallback);
inputMethodController.offDeleteLeft();
```

## offDeleteRight

```TypeScript
offDeleteRight(callback?: Callback<int>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offDeleteRight(callback?: Callback<int>): void--><!--Device-InputMethodController-offDeleteRight(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onDeleteRightCallback = (length: int) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
};
inputMethodController.offDeleteRight(onDeleteRightCallback);
inputMethodController.offDeleteRight();
```

## offFinishTextPreview

```TypeScript
offFinishTextPreview(callback?: Callback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offFinishTextPreview(callback?: Callback<void>): void--><!--Device-InputMethodController-offFinishTextPreview(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import inputMethod from '@ohos.inputMethod';
let inputMethodController = inputMethod.getController();
let finishTextPreviewCallback1 = () => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2 = () => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

inputMethodController.onFinishTextPreview(finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.onFinishTextPreview(finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.offFinishTextPreview(finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调
inputMethodController.offFinishTextPreview();
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## offGetLeftTextOfCursor

```TypeScript
offGetLeftTextOfCursor(callback?: GetTextCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-offGetLeftTextOfCursor(callback?: GetTextCallback): void--><!--Device-InputMethodController-offGetLeftTextOfCursor(callback?: GetTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let getLeftTextOfCursorCallback = (length: int) => {
  console.info(`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}`);
  let text:string = "";
  return text;
};
inputMethodController.offGetLeftTextOfCursor(getLeftTextOfCursorCallback);
inputMethodController.offGetLeftTextOfCursor();
```

## offGetRightTextOfCursor

```TypeScript
offGetRightTextOfCursor(callback?: GetTextCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-offGetRightTextOfCursor(callback?: GetTextCallback): void--><!--Device-InputMethodController-offGetRightTextOfCursor(callback?: GetTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let getRightTextOfCursorCallback = (length: int) => {
  console.info(`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}`);
  let text:string = "";
  return text;
};
inputMethodController.offGetRightTextOfCursor(getRightTextOfCursorCallback);
inputMethodController.offGetRightTextOfCursor();
```

## offGetTextIndexAtCursor

```TypeScript
offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void
```

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodController-offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void--><!--Device-InputMethodController-offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController = inputMethod.getController();

let getTextIndexAtCursorCallback = () => {
  console.info(`Succeeded in unsubscribing getTextIndexAtCursor.`);
  let index:int = 0;
  return index;
};
inputMethodController.offGetTextIndexAtCursor(getTextIndexAtCursorCallback);
inputMethodController.offGetTextIndexAtCursor();
```

## offHandleExtendAction

```TypeScript
offHandleExtendAction(callback?: Callback<ExtendAction>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offHandleExtendAction(callback?: Callback<ExtendAction>): void--><!--Device-InputMethodController-offHandleExtendAction(callback?: Callback<ExtendAction>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onHandleExtendActionCallback = (action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
};
inputMethodController.offHandleExtendAction(onHandleExtendActionCallback);
inputMethodController.offHandleExtendAction();
```

## offInsertText

```TypeScript
offInsertText(callback?: Callback<string>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offInsertText(callback?: Callback<string>): void--><!--Device-InputMethodController-offInsertText(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。<br/>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onInsertTextCallback = (text: string) => {
  console.info(`Succeeded in subscribing insertText: ${text}`);
};
inputMethodController.offInsertText(onInsertTextCallback);
inputMethodController.offInsertText();
```

## offMoveCursor

```TypeScript
offMoveCursor(callback?: Callback<Direction>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offMoveCursor(callback?: Callback<Direction>): void--><!--Device-InputMethodController-offMoveCursor(callback?: Callback<Direction>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onMoveCursorCallback = (direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
};
inputMethodController.offMoveCursor(onMoveCursorCallback);
inputMethodController.offMoveCursor();
```

## offSelectByMovement

```TypeScript
offSelectByMovement(callback?: Callback<Movement>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offSelectByMovement(callback?: Callback<Movement>): void--><!--Device-InputMethodController-offSelectByMovement(callback?: Callback<Movement>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onSelectByMovementCallback = (movement: inputMethod.Movement) => {
  console.info(`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}`);
};
inputMethodController.offSelectByMovement(onSelectByMovementCallback);
inputMethodController.offSelectByMovement();
```

## offSelectByRange

```TypeScript
offSelectByRange(callback?: Callback<Range>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offSelectByRange(callback?: Callback<Range>): void--><!--Device-InputMethodController-offSelectByRange(callback?: Callback<Range>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onSelectByRangeCallback = (range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}`);
};
inputMethodController.offSelectByRange(onSelectByRangeCallback);
inputMethodController.offSelectByRange();
```

## offSendFunctionKey

```TypeScript
offSendFunctionKey(callback?: Callback<FunctionKey>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offSendFunctionKey(callback?: Callback<FunctionKey>): void--><!--Device-InputMethodController-offSendFunctionKey(callback?: Callback<FunctionKey>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onSendFunctionKey = (functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}`);
};
inputMethodController.offSendFunctionKey(onSendFunctionKey);
inputMethodController.offSendFunctionKey();
```

## offSendKeyboardStatus

```TypeScript
offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void
```

**起始版本：** 23

<!--Device-InputMethodController-offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void--><!--Device-InputMethodController-offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
let onSendKeyboardStatus = (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
};
inputMethodController.offSendKeyboardStatus(onSendKeyboardStatus);
inputMethodController.offSendKeyboardStatus();
```

## offSetPreviewText

```TypeScript
offSetPreviewText(callback?:SetPreviewTextCallback): void
```

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodController-offSetPreviewText(callback?:SetPreviewTextCallback): void--><!--Device-InputMethodController-offSetPreviewText(callback?:SetPreviewTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import inputMethod from '@ohos.inputMethod';
let inputMethodController = inputMethod.getController();
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range) => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range) => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

inputMethodController.onSetPreviewText(setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.onSetPreviewText(setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.offSetPreviewText(setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.offSetPreviewText();
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## off('deleteLeft')

```TypeScript
off(type: 'deleteLeft', callback?: (length: number) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'deleteLeft', callback?: (length: number) => void): void--><!--Device-InputMethodController-off(type: 'deleteLeft', callback?: (length: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'deleteLeft' | 是 | 设置监听，固定取值为'deleteLeft'。 |
| callback | (length: number) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onDeleteLeftCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteLeft', onDeleteLeftCallback);
inputMethodController.off('deleteLeft');
```

## off('deleteRight')

```TypeScript
off(type: 'deleteRight', callback?: (length: number) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'deleteRight', callback?: (length: number) => void): void--><!--Device-InputMethodController-off(type: 'deleteRight', callback?: (length: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'deleteRight' | 是 | 设置监听类型，固定取值为`deleteRight`。 |
| callback | (length: number) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onDeleteRightCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteRight', onDeleteRightCallback);
inputMethodController.off('deleteRight');
```

## off('finishTextPreview')

```TypeScript
off(type: 'finishTextPreview', callback?: Callback<void>): void
```

**起始版本：** 17

<!--Device-InputMethodController-off(type: 'finishTextPreview', callback?: Callback<void>): void--><!--Device-InputMethodController-off(type: 'finishTextPreview', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'finishTextPreview' | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调。
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## off('getLeftTextOfCursor')

```TypeScript
off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void--><!--Device-InputMethodController-off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getLeftTextOfCursor' | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) =&gt; string | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let getLeftTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getLeftTextOfCursor', getLeftTextOfCursorCallback);
inputMethodController.off('getLeftTextOfCursor');
```

## off('getRightTextOfCursor')

```TypeScript
off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void--><!--Device-InputMethodController-off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getRightTextOfCursor' | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) =&gt; string | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let getRightTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getRightTextOfCursor', getRightTextOfCursorCallback);
inputMethodController.off('getRightTextOfCursor');
```

## off('getTextIndexAtCursor')

```TypeScript
off(type: 'getTextIndexAtCursor', callback?: () => number): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'getTextIndexAtCursor', callback?: () => number): void--><!--Device-InputMethodController-off(type: 'getTextIndexAtCursor', callback?: () => number): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getTextIndexAtCursor' | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () =&gt; number | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let getTextIndexAtCursorCallback: () => number = (): number => {
  console.info(`Succeeded in unsubscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getTextIndexAtCursor', getTextIndexAtCursorCallback);
inputMethodController.off('getTextIndexAtCursor');
```

## off('handleExtendAction')

```TypeScript
off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void--><!--Device-InputMethodController-off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'handleExtendAction' | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: ExtendAction) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onHandleExtendActionCallback: Callback<inputMethod.ExtendAction> = (action: inputMethod.ExtendAction): void => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('handleExtendAction', onHandleExtendActionCallback);
inputMethodController.off('handleExtendAction');
```

## off('insertText')

```TypeScript
off(type: 'insertText', callback?: (text: string) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'insertText', callback?: (text: string) => void): void--><!--Device-InputMethodController-off(type: 'insertText', callback?: (text: string) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'insertText' | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。<br/>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onInsertTextCallback: Callback<string> = (text: string): void => {
  console.info(`Succeeded in subscribing insertText: ${text}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('insertText', onInsertTextCallback);
inputMethodController.off('insertText');
```

## off('moveCursor')

```TypeScript
off(type: 'moveCursor', callback?: (direction: Direction) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'moveCursor', callback?: (direction: Direction) => void): void--><!--Device-InputMethodController-off(type: 'moveCursor', callback?: (direction: Direction) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'moveCursor' | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: Direction) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onMoveCursorCallback: Callback<inputMethod.Direction> = (direction: inputMethod.Direction): void => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('moveCursor', onMoveCursorCallback);
inputMethodController.off('moveCursor');
```

## off('selectByMovement')

```TypeScript
off(type: 'selectByMovement', callback?: Callback<Movement>): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'selectByMovement', callback?: Callback<Movement>): void--><!--Device-InputMethodController-off(type: 'selectByMovement', callback?: Callback<Movement>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectByMovement' | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSelectByMovementCallback: Callback<inputMethod.Movement> = (movement: inputMethod.Movement): void => {
  console.info(`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByMovement', onSelectByMovementCallback);
inputMethodController.off('selectByMovement');
```

## off('selectByRange')

```TypeScript
off(type: 'selectByRange', callback?: Callback<Range>): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'selectByRange', callback?: Callback<Range>): void--><!--Device-InputMethodController-off(type: 'selectByRange', callback?: Callback<Range>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectByRange' | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSelectByRangeCallback: Callback<inputMethod.Range> = (range: inputMethod.Range): void => {
  console.info(`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByRange', onSelectByRangeCallback);
inputMethodController.off('selectByRange');
```

## off('sendFunctionKey')

```TypeScript
off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void--><!--Device-InputMethodController-off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sendFunctionKey' | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: FunctionKey) =&gt; void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSendFunctionKey: Callback<inputMethod.FunctionKey> = (functionKey: inputMethod.FunctionKey): void => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendFunctionKey', onSendFunctionKey);
inputMethodController.off('sendFunctionKey');
```

## off('sendKeyboardStatus')

```TypeScript
off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void--><!--Device-InputMethodController-off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sendKeyboardStatus' | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: KeyboardStatus) =&gt; void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSendKeyboardStatus: Callback<inputMethod.KeyboardStatus> = (keyboardStatus: inputMethod.KeyboardStatus): void => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendKeyboardStatus', onSendKeyboardStatus);
inputMethodController.off('sendKeyboardStatus');
```

## off('setPreviewText')

```TypeScript
off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void
```

**起始版本：** 17

<!--Device-InputMethodController-off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void--><!--Device-InputMethodController-off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setPreviewText' | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。 <br>参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

ArkTS-Dyn示例:

```TypeScript
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## onDeleteLeft

```TypeScript
onDeleteLeft(callback: Callback<int>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onDeleteLeft(callback: Callback<int>): void--><!--Device-InputMethodController-onDeleteLeft(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | 回调函数，返回需要向左删除的文本长度。<br/>根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onDeleteLeft((length: int) => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
});
```

## onDeleteRight

```TypeScript
onDeleteRight(callback: Callback<int>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onDeleteRight(callback: Callback<int>): void--><!--Device-InputMethodController-onDeleteRight(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | 回调函数，返回需要向右删除的文本长度。<br/>根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onDeleteRight((length: int) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
});
```

## onFinishTextPreview

```TypeScript
onFinishTextPreview(callback: Callback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onFinishTextPreview(callback: Callback<void>): void--><!--Device-InputMethodController-onFinishTextPreview(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数。用于处理预览文本结束的逻辑，类型为void。 |

**示例**

```TypeScript
import inputMethod from '@ohos.inputMethod';
let inputMethodController = inputMethod.getController();
let finishTextPreviewCallback1 = () => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2 = () => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

inputMethodController.onFinishTextPreview(finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.onFinishTextPreview(finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.offFinishTextPreview(finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调。
inputMethodController.offFinishTextPreview();
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## onGetLeftTextOfCursor

```TypeScript
onGetLeftTextOfCursor(callback: GetTextCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-onGetLeftTextOfCursor(callback: GetTextCallback): void--><!--Device-InputMethodController-onGetLeftTextOfCursor(callback: GetTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 是 | 回调函数，获取编辑框最新状态下光标左侧指定长度的文本内容并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onGetLeftTextOfCursor((length: int) => {
  console.info(`Succeeded in subscribing getLeftTextOfCursor, length: ${length}`);
  let text:string = "";
  return text;
});
```

## onGetRightTextOfCursor

```TypeScript
onGetRightTextOfCursor(callback: GetTextCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-onGetRightTextOfCursor(callback: GetTextCallback): void--><!--Device-InputMethodController-onGetRightTextOfCursor(callback: GetTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 是 | 回调函数，获取编辑框最新状态下光标右侧指定长度的文本内容并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onGetRightTextOfCursor( (length: int) => {
  console.info(`Succeeded in subscribing getRightTextOfCursor, length: ${length}`);
  let text:string = "";
  return text;
});
```

## onGetTextIndexAtCursor

```TypeScript
onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void--><!--Device-InputMethodController-onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | 是 | 回调函数，获取编辑框最新状态下光标处文本索引并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onGetTextIndexAtCursor(():int => {
  console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
  let index:int = 0;
  return index;
});
```

## onHandleExtendAction

```TypeScript
onHandleExtendAction(callback: Callback<ExtendAction>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onHandleExtendAction(callback: Callback<ExtendAction>): void--><!--Device-InputMethodController-onHandleExtendAction(callback: Callback<ExtendAction>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | 是 | 回调函数，返回扩展编辑操作类型。<br/>根据传入的扩展编辑操作类型，做相应的操作，如剪切、复制等。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onHandleExtendAction((action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
});
```

## onInsertText

```TypeScript
onInsertText(callback: Callback<string>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onInsertText(callback: Callback<string>): void--><!--Device-InputMethodController-onInsertText(callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 | 回调函数，返回需要插入的文本内容。<br/>根据传入的文本，在回调函数中操作编辑框中的内容。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
function callback1(text: string) {
  console.info(`Succeeded in getting callback1 data: ${text}`);
}

function callback2(text: string) {
  console.info(`Succeeded in getting callback2 data: ${text}`);
}

inputMethodController.onInsertText(callback1);
inputMethodController.onInsertText(callback2);
inputMethodController.offInsertText(callback1);
inputMethodController.offInsertText();
```

## onMoveCursor

```TypeScript
onMoveCursor(callback: Callback<Direction>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onMoveCursor(callback: Callback<Direction>): void--><!--Device-InputMethodController-onMoveCursor(callback: Callback<Direction>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | 是 | 回调函数，返回光标信息。<br/>根据返回的光标移动方向，改变光标位置，如光标向上或向下。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onMoveCursor((direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
});
```

## onSelectByMovement

```TypeScript
onSelectByMovement(callback: Callback<Movement>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onSelectByMovement(callback: Callback<Movement>): void--><!--Device-InputMethodController-onSelectByMovement(callback: Callback<Movement>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 是 | 回调函数，返回光标移动的方向。<br/>根据传入的光标移动方向，选中编辑框中相应文本。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onSelectByMovement((movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});
```

## onSelectByRange

```TypeScript
onSelectByRange(callback: Callback<Range>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onSelectByRange(callback: Callback<Range>): void--><!--Device-InputMethodController-onSelectByRange(callback: Callback<Range>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 是 | 回调函数，返回需要选中的文本范围。<br/>根据传入的文本范围，开发者在回调函数中编辑框中相应文本。 |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onSelectByRange((range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
});
```

## onSendFunctionKey

```TypeScript
onSendFunctionKey(callback: Callback<FunctionKey>): void
```

**起始版本：** 23

<!--Device-InputMethodController-onSendFunctionKey(callback: Callback<FunctionKey>): void--><!--Device-InputMethodController-onSendFunctionKey(callback: Callback<FunctionKey>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | 是 | 回调函数，返回输入法应用发送的功能键信息。<br/>根据返回的功能键信息，做相应操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onSendFunctionKey((functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
});
```

## onSendKeyboardStatus

```TypeScript
onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void
```

订阅输入法应用发送输入法软键盘状态事件。使用callback异步回调。

**起始版本：** 23

<!--Device-InputMethodController-onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void--><!--Device-InputMethodController-onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | 是 | 回调函数，返回软键盘状态。<br/>根据传入的软键盘状态，在回调函数中做相应操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.onSendKeyboardStatus((keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
});
```

## onSetPreviewText

```TypeScript
onSetPreviewText(callback: SetPreviewTextCallback): void
```

**起始版本：** 23

<!--Device-InputMethodController-onSetPreviewText(callback: SetPreviewTextCallback): void--><!--Device-InputMethodController-onSetPreviewText(callback: SetPreviewTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 是 | 回调函数。用于接收文本预览的内容并返回。 |

**示例**

```TypeScript
import inputMethod from '@ohos.inputMethod';
let inputMethodController = inputMethod.getController();
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range) => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range) => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

inputMethodController.onSetPreviewText(setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.onSetPreviewText(setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.offSetPreviewText(setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.offSetPreviewText();
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## on('deleteLeft')

```TypeScript
on(type: 'deleteLeft', callback: (length: number) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'deleteLeft', callback: (length: number) => void): void--><!--Device-InputMethodController-on(type: 'deleteLeft', callback: (length: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'deleteLeft' | 是 | 设置监听类型，固定取值为'deleteLeft'。 |
| callback | (length: number) =&gt; void | 是 | 回调函数，返回需要向左删除的文本长度。<br/>根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('deleteLeft', (length: number) => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
});
```

## on('deleteRight')

```TypeScript
on(type: 'deleteRight', callback: (length: number) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'deleteRight', callback: (length: number) => void): void--><!--Device-InputMethodController-on(type: 'deleteRight', callback: (length: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'deleteRight' | 是 | 设置监听类型，固定取值为'deleteRight'。 |
| callback | (length: number) =&gt; void | 是 | 回调函数，返回需要向右删除的文本长度。<br/>根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('deleteRight', (length: number) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
});
```

## on('finishTextPreview')

```TypeScript
on(type: 'finishTextPreview', callback: Callback<void>): void
```

**起始版本：** 17

<!--Device-InputMethodController-on(type: 'finishTextPreview', callback: Callback<void>): void--><!--Device-InputMethodController-on(type: 'finishTextPreview', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'finishTextPreview' | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 回调函数。当处理预览文本结束的逻辑成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调。
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## on('getLeftTextOfCursor')

```TypeScript
on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void--><!--Device-InputMethodController-on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getLeftTextOfCursor' | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) =&gt; string | 是 | 回调函数，获取编辑框最新状态下光标左侧指定长度的文本内容并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('getLeftTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

## on('getRightTextOfCursor')

```TypeScript
on(type: 'getRightTextOfCursor', callback: (length: number) => string): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'getRightTextOfCursor', callback: (length: number) => string): void--><!--Device-InputMethodController-on(type: 'getRightTextOfCursor', callback: (length: number) => string): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getRightTextOfCursor' | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) =&gt; string | 是 | 回调函数，获取编辑框最新状态下光标右侧指定长度的文本内容并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('getRightTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

## on('getTextIndexAtCursor')

```TypeScript
on(type: 'getTextIndexAtCursor', callback: () => number): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'getTextIndexAtCursor', callback: () => number): void--><!--Device-InputMethodController-on(type: 'getTextIndexAtCursor', callback: () => number): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'getTextIndexAtCursor' | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () =&gt; number | 是 | 回调函数，获取编辑框最新状态下光标处文本索引并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('getTextIndexAtCursor', () => {
  console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
});
```

## on('handleExtendAction')

```TypeScript
on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void--><!--Device-InputMethodController-on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'handleExtendAction' | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: ExtendAction) =&gt; void | 是 | 回调函数，返回扩展编辑操作类型。<br/>根据传入的扩展编辑操作类型，做相应的操作，如剪切、复制等。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
});
```

## on('insertText')

```TypeScript
on(type: 'insertText', callback: (text: string) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'insertText', callback: (text: string) => void): void--><!--Device-InputMethodController-on(type: 'insertText', callback: (text: string) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'insertText' | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) =&gt; void | 是 | 回调函数，返回需要插入的文本内容。<br/>根据传入的文本，在回调函数中操作编辑框中的内容。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
const callback1 = (text: string): void => {
  console.info(`Succeeded in getting callback1, data: ${text}`);
}

const callback2 = (text: string): void => {
  console.info(`Succeeded in getting callback2, data: ${text}`);
}

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
// 注册回调
inputMethodController.on('insertText', callback1);
inputMethodController.on('insertText', callback2);
// 仅取消insertText的callback1的回调
inputMethodController.off('insertText', callback1);
// 取消insertText的所有回调
inputMethodController.off('insertText');
```

## on('moveCursor')

```TypeScript
on(type: 'moveCursor', callback: (direction: Direction) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'moveCursor', callback: (direction: Direction) => void): void--><!--Device-InputMethodController-on(type: 'moveCursor', callback: (direction: Direction) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'moveCursor' | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: Direction) =&gt; void | 是 | 回调函数，返回光标信息。<br/>根据返回的光标移动方向，改变光标位置，如光标向上或向下。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
});
```

## on('selectByMovement')

```TypeScript
on(type: 'selectByMovement', callback: Callback<Movement>): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'selectByMovement', callback: Callback<Movement>): void--><!--Device-InputMethodController-on(type: 'selectByMovement', callback: Callback<Movement>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectByMovement' | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 是 | 回调函数，返回光标移动的方向。<br/>根据传入的光标移动方向，选中编辑框中相应文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例**

```TypeScript
inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});
```

## on('selectByRange')

```TypeScript
on(type: 'selectByRange', callback: Callback<Range>): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'selectByRange', callback: Callback<Range>): void--><!--Device-InputMethodController-on(type: 'selectByRange', callback: Callback<Range>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectByRange' | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 是 | 回调函数，返回需要选中的文本范围。<br/>根据传入的文本范围，开发者在回调函数中编辑框中相应文本。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例**

```TypeScript
inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
});
```

## on('sendFunctionKey')

```TypeScript
on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void--><!--Device-InputMethodController-on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sendFunctionKey' | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: FunctionKey) =&gt; void | 是 | 回调函数，返回输入法应用发送的功能键信息。<br/>根据返回的功能键信息，做相应操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
});
```

## on('sendKeyboardStatus')

```TypeScript
on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void
```

**起始版本：** 10

<!--Device-InputMethodController-on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void--><!--Device-InputMethodController-on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sendKeyboardStatus' | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: KeyboardStatus) =&gt; void | 是 | 回调函数，返回软键盘状态。<br/>根据传入的软键盘状态，在回调函数中做相应操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |

**示例**

```TypeScript
inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
});
```

## on('setPreviewText')

```TypeScript
on(type: 'setPreviewText', callback: SetPreviewTextCallback): void
```

**起始版本：** 17

<!--Device-InputMethodController-on(type: 'setPreviewText', callback: SetPreviewTextCallback): void--><!--Device-InputMethodController-on(type: 'setPreviewText', callback: SetPreviewTextCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'setPreviewText' | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 是 | 回调函数。用于接收文本预览的内容并返回。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例**

```TypeScript
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

**起始版本：** 23

<!--Device-InputMethodController-recvMessage(msgHandler?: MessageHandler): void--><!--Device-InputMethodController-recvMessage(msgHandler?: MessageHandler): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgHandler | MessageHandler | 否 | 该对象通过 [onMessage](arkts-ime-inputmethod-messagehandler-i.md#onmessage)接收来自输入法应用所发送的自定 义通信数据，并通过[onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)接收终止此对象订阅的消息。 <br>若不填写此参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethod-messagehandler-i.md)对象，同时触发其 [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.recvMessage(messageHandler);
// 取消已注册的MessageHandler
inputMethodController.recvMessage();
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let messageHandler: inputMethod.MessageHandler = {
  onTerminated: (): void => {
    console.info("OnTerminated.");
  },
  onMessage: (msgId: string, msgParam?: ArrayBuffer): void => {
    console.info("recv message.");
  }
}
inputMethodController.recvMessage(messageHandler);
inputMethodController.recvMessage();
```

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>--><!--Device-InputMethodController-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 需要发送至输入法应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至输入法应用的自定义数据的消息体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| [12800016](../errorcode-inputmethod-framework.md#12800016-输入法客户端未处于编辑状态) | input method client is not editable. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800015](../errorcode-inputmethod-framework.md#12800015-消息接收端无法接收自定义通信数据) | the other side does not accept the request. |
| [12800014](../errorcode-inputmethod-framework.md#12800014-输入法应用非完全访问模式) | the input method is in basic mode. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputMethod.getController().sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputMethodController.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to sendMessage, code: ${err.code}, message: ${err.message}`);
});
```

## setCallingWindow

```TypeScript
setCallingWindow(windowId: int, callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-setCallingWindow(windowId: int, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-setCallingWindow(windowId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | int | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置成功时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting callingWindow.');
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let windowId: int = 2000;
inputMethodController.setCallingWindow(windowId, (err?: BusinessError) => {
  if (err) {
    console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting callingWindow.');
});
```

## setCallingWindow

```TypeScript
setCallingWindow(windowId: int): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-setCallingWindow(windowId: int): Promise<void>--><!--Device-InputMethodController-setCallingWindow(windowId: int): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | int | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId).then(() => {
  console.info('Succeeded in setting callingWindow.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
})
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: int = 2000;
inputMethodController.setCallingWindow(windowId).then(() => {
  console.info('Succeeded in setting callingWindow.');
}).catch((err: BusinessError): void => {
  console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
})
```

## showSoftKeyboard

```TypeScript
showSoftKeyboard(callback: AsyncCallback<void>): void
```

**起始版本：** 23

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-showSoftKeyboard(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-showSoftKeyboard(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当软键盘显示成功。err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-权限校验失败) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in showing softKeyboard.');
  } else {
    console.error(`Failed to show softKeyboard, ${err.code}, message: ${err.message}`);
  }
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.showSoftKeyboard((err?: BusinessError) => {
  if (!err) {
    console.info('Succeeded in showing softKeyboard.');
  } else {
    console.error(`Failed to showSoftKeyboard, code: ${err.code}, message: ${err.message}`);
  }
})
```

## showSoftKeyboard

```TypeScript
showSoftKeyboard(): Promise<void>
```

**起始版本：** 23

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-showSoftKeyboard(): Promise<void>--><!--Device-InputMethodController-showSoftKeyboard(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-权限校验失败) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard().then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.showSoftKeyboard().then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to showSoftKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## showTextInput

```TypeScript
showTextInput(callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-showTextInput(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-showTextInput(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。若成功进入编辑状态，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the inputMethod.');
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.showTextInput((err?: BusinessError) => {
  if (err) {
    console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the inputMethod.');
});
```

## showTextInput

```TypeScript
showTextInput(): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-showTextInput(): Promise<void>--><!--Device-InputMethodController-showTextInput(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput().then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

inputMethodController.showTextInput().then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

## showTextInput

```TypeScript
showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>--><!--Device-InputMethodController-showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestKeyboardReason | RequestKeyboardReason | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().showTextInput(requestKeyboardReason).then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let requestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;
inputMethodController.showTextInput(requestKeyboardReason).then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

## stopInput

```TypeScript
stopInput(callback: AsyncCallback<boolean>): void
```

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

<!--Device-InputMethodController-stopInput(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodController-stopInput(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | 回调函数。当会话结束成功，err为undefined，data为true；否则为错误对象。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
});
```

## stopInput

```TypeScript
stopInput(): Promise<boolean>
```

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

<!--Device-InputMethodController-stopInput(): Promise<boolean>--><!--Device-InputMethodController-stopInput(): Promise<boolean>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示会话结束成功；返回false表示会话结束失败。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
});
```

## stopInputSession

```TypeScript
stopInputSession(callback: AsyncCallback<boolean>): void
```

**起始版本：** 23

<!--Device-InputMethodController-stopInputSession(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodController-stopInputSession(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | 回调函数。当结束输入会话成功时，err为undefined，data为true；失败时err为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
inputMethodController.stopInputSession((err: BusinessError | null, result: boolean | undefined) => {
  if (err) {
    console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
});
```

## stopInputSession

```TypeScript
stopInputSession(): Promise<boolean>
```

**起始版本：** 23

<!--Device-InputMethodController-stopInputSession(): Promise<boolean>--><!--Device-InputMethodController-stopInputSession(): Promise<boolean>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示结束输入会话成功，返回false表示结束输入会话失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodController.stopInputSession().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
  }).catch((err: BusinessError): void=> {
  console.error(`Failed to stopInputSession, code: ${error.code}, message: ${error.message}`);
})
```

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | 是 | 编辑框属性对象。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating attribute.');
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: inputMethod.TextInputType.TEXT, enterKeyType: inputMethod.EnterKeyType.NONE };
inputMethodController.updateAttribute(inputAttribute, (err?: BusinessError) => {
  if (err) {
    console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating attribute.');
});
```

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-updateAttribute(attribute: InputAttribute): Promise<void>--><!--Device-InputMethodController-updateAttribute(attribute: InputAttribute): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | 是 | 编辑框属性对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute).then(() => {
  console.info('Succeeded in updating attribute.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: inputMethod.TextInputType.TEXT, enterKeyType: inputMethod.EnterKeyType.NONE };
inputMethodController.updateAttribute(inputAttribute).then(() => {
  console.info('Succeeded in updating attribute.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
})
```

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void
```

**起始版本：** 23

<!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | 是 | 光标信息。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当光标信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating cursorInfo.');
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = { left: 0, top: 0, width: 600, height: 800 };
inputMethodController.updateCursor(cursorInfo, (err?: BusinessError) => {
  if (err) {
    console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating cursorInfo.');
});
```

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo): Promise<void>
```

**起始版本：** 23

<!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo): Promise<void>--><!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | 是 | 光标信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例**

ArkTs-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo).then(() => {
  console.info('Succeeded in updating cursorInfo.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
});
```

ArkTs-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = { left: 0, top: 0, width: 600, height: 800 };
inputMethodController.updateCursor(cursorInfo).then(() => {
  console.info('Succeeded in updating cursorInfo.');
}).catch((err: BusinessError): void => {
  console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
})
```

