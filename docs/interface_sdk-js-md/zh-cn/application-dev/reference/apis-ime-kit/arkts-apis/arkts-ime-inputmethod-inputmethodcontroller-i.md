# InputMethodController

下列API示例中都需使用[getController](arkts-ime-inputmethod-getcontroller-f.md)获取到InputMethodController实例，再通过实例调用对应方法。 <br> <br>InputMethodController是输入法客户端控制器，面向前台应用提供与输入法交互的核心能力。通过`inputMethod.getController()`获取实例后，可进行以下操作： <br> <br>- 绑定管理：通过 [attach](#attach) 建立与输入法的绑定，通过[detach](#detach)解除绑定。attach和 detach必须配对使用。 <br>- 键盘控制：通过[showTextInput](#showtextinput)拉起软键盘 进入编辑状态，通过[hideTextInput](#hidetextinput)隐藏软键盘 退出编辑状态。showTextInput和hideTextInput必须配对使用。 <br>- 编辑框状态同步：通过 [updateCursor](#updatecursor) 、 [changeSelection](#changeselection) 、 [updateAttribute](#updateattribute) 等接口向输入法同步光标、选区、属性等编辑框状态信息。 <br>- 事件订阅：通过on('insertText')、on('deleteLeft')等接口订阅输入法应用发送的文本操作事件。 <br> <br>典型调用序列：`getController()` → `attach()` → `showTextInput()`/`hideTextInput()` → `detach()` <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> attach和detach必须配对使用，showTextInput和hideTextInput必须配对使用，否则可能导致资源泄漏或状态不一致。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void
```

自绘控件绑定输入法。使用callback异步回调。 <br> <br>含义/功能：建立自绘控件与输入法应用之间的绑定关系，是自绘控件使用输入法功能的前提。 <br> <br>使用场景：自绘控件（非系统原生编辑框）需要与输入法交互时，必须先调用此接口建立绑定。原生编辑框获焦时系统自动绑定，无需调用此接口。 <br> <br>使用后效果：绑定成功后，自绘控件可调用showTextInput/hideTextInput控制键盘显隐、调用updateCursor/changeSelection同步编辑框状态、订阅输入法事件等。 <br> <br>前提条件/前置操作：自绘控件所在窗口需处于获焦状态，否则绑定会失败。 <br> <br>相关接口间的配合/制约关系：attach必须与detach配对使用。调用attach后才能调用showTextInput、hideTextInput、updateCursor等接口。 <br> <br>相似接口差异点及选取原则： <br> <br>- attach：不需要传入UIContext，适用于API version 10+的自绘控件绑定场景。 <br>- attachWithUIContext：需要传入UIContext，适用于API version 23+的Stage模型场景，支持更多绑定选项。 <br>- 选取原则：API version 23+的Stage模型应用优先使用attachWithUIContext，以获得更完整的绑定选项支持。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。 &lt;br
&gt; 
> &lt;br
&gt; 
> 当自绘控件所在窗口通过 &lt;br
&gt; 
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable) &lt;br
&gt; 
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考 &lt;br
&gt; 
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | 是 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。 &lt;br
&gt; 
> &lt;br
&gt; 
> 当自绘控件所在窗口通过 &lt;br
&gt; 
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable) &lt;br
&gt; 
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考 &lt;br
&gt; 
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | 是 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [attach](#attach)

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。 &lt;br
&gt; 
> &lt;br
&gt; 
> 当自绘控件所在窗口通过 &lt;br
&gt; 
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable) &lt;br
&gt; 
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考 &lt;br
&gt; 
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | 是 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 |
| requestKeyboardReason | [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [attach](#attach)

## attachWithUIContext

```TypeScript
attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | 是 |
| attachOptions | [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

ArkTS-Dyn:
```TypeScript
changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void
```

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口更新文本选区信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| start | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## changeSelection

ArkTS-Dyn:
```TypeScript
changeSelection(text: string, start: number, end: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
changeSelection(text: string, start: int, end: int): Promise<void>
```

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口更新文本选区信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| start | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [changeSelection](#changeselection)

## detach

```TypeScript
detach(callback: AsyncCallback<void>): void
```

自绘控件解除与输入法的绑定。使用callback异步回调。 <br> <br>含义/功能：解除自绘控件与输入法应用之间的绑定关系，释放相关资源。 <br> <br>使用场景：自绘控件不再需要与输入法交互时调用（如页面切换、编辑框被销毁等）。 <br> <br>使用后效果：解除绑定后，不能再调用showTextInput、hideTextInput、updateCursor等需要绑定状态的接口。输入法软键盘将被隐藏。 <br> <br>相关接口间的配合/制约关系：detach必须与attach配对使用。建议在hideTextInput之后调用detach，完整流程为：attach → showTextInput → hideTextInput → detach。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

## detach

```TypeScript
detach(): Promise<void>
```

自绘控件解除与输入法的绑定。使用promise异步回调。 <br> <br>含义/功能：解除自绘控件与输入法应用之间的绑定关系，释放相关资源。 <br> <br>使用场景：自绘控件不再需要与输入法交互时调用。 <br> <br>使用后效果：解除绑定后，不能再调用需要绑定状态的接口。输入法软键盘将被隐藏。 <br> <br>相关接口间的配合/制约关系：detach必须与attach配对使用。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [detach](#detach)

## discardTypingText

```TypeScript
discardTypingText(): Promise<void>
```

编辑框应用发送“清空正在输入的文字”命令到输入法。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> <br>
> 当编辑框应用与输入法绑定成功后，才可调用该接口实现此功能。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |
| [12800015](../errorcode-inputmethod-framework.md#12800015-消息接收端无法接收自定义通信数据) |

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

隐藏输入法软键盘。使用callback异步回调。 <br> <br>含义/功能：强制隐藏当前输入法的软键盘。 <br> <br>使用场景：系统应用需要强制隐藏输入法软键盘时使用。 <br> <br>使用后效果：输入法软键盘被隐藏。 <br> <br>前提条件/前置操作：编辑框与输入法绑定时才能调用。 <br> <br>相似接口差异点及选取原则： <br> <br>- hideSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY，仅隐藏键盘不退出编辑状态。 <br>- hideTextInput：面向自绘控件，隐藏键盘并退出编辑状态，可再次showTextInput重新进入。 <br>- 选取原则：自绘控件使用hideTextInput；系统应用且有权限时使用hideSoftKeyboard。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: number = 30;
inputMethod.getController().hideSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: long = 30;
inputMethod.getController().hideSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(): Promise<void>
```

隐藏输入法软键盘。使用Promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [hideSoftKeyboard](#hidesoftkeyboard)

## hideTextInput

```TypeScript
hideTextInput(callback: AsyncCallback<void>): void
```

退出文本编辑状态。使用callback异步回调。 <br> <br>含义/功能：隐藏软键盘，使编辑框退出文本编辑状态。 <br> <br>使用场景：自绘控件不再需要输入时调用，如用户点击了编辑框外的区域、切换到其他页面等。 <br> <br>使用后效果：软键盘被隐藏，编辑框退出编辑状态。调用此接口不会解除与输入法的绑定，再次调用showTextInput可重新进入编辑状态。 <br> <br>前提条件/前置操作：需先调用 [attach](#attach) 完成绑定，且已调用showTextInput进入编辑状态。 <br> <br>相关接口间的配合/制约关系：hideTextInput与showTextInput必须配对使用。hideTextInput后如需再次输入，必须先调用showTextInput重新进入编辑状态，不能直接调用其他编辑操作。 <br> <br>相似接口差异点及选取原则： <br> <br>- hideTextInput：面向自绘控件，退出编辑状态但不解除绑定，可再次showTextInput重新进入。适用于自绘控件需要暂时隐藏键盘的场景。 <br>- hideSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY。仅隐藏键盘，不改变编辑状态。 <br>- 选取原则：自绘控件优先使用hideTextInput；系统应用且有特殊需求时使用hideSoftKeyboard。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。 &lt;br
&gt; 
> &lt;br
&gt; 
> 调用该接口不会解除与输入法的绑定，再次调用 &lt;br
&gt; 
> [showTextInput](#showtextinput)时，可重新进入文本编 &lt;br
&gt; 
> 辑状态。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## hideTextInput

```TypeScript
hideTextInput(): Promise<void>
```

退出文本编辑状态。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。 &lt;br
&gt; 
> &lt;br
&gt; 
> 调用该接口不会解除与输入法的绑定，再次调用 &lt;br
&gt; 
> [showTextInput](#showtextinput)时，可重新进入文本编 &lt;br
&gt; 
> 辑状态。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [hideTextInput](#hidetextinput)

## off('selectByRange')

```TypeScript
off(type: 'selectByRange', callback?: Callback<Range>): void
```

取消订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByRange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 否 |

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

## off('selectByMovement')

```TypeScript
off(type: 'selectByMovement', callback?: Callback<Movement>): void
```

取消订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByMovement' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 否 |

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

## off('insertText')

```TypeScript
off(type: 'insertText', callback?: (text: string) => void): void
```

取消订阅输入法应用插入文本事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'insertText' | 是 |
| callback | (text: string) = & gt; void | 否 |

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

## off('deleteLeft')

```TypeScript
off(type: 'deleteLeft', callback?: (length: number) => void): void
```

取消订阅输入法应用向左删除文本事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteLeft' | 是 |
| callback | (length: number) = & gt; void | 否 |

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

取消订阅输入法应用向右删除文本事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteRight' | 是 |
| callback | (length: number) = & gt; void | 否 |

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

## off('sendKeyboardStatus')

```TypeScript
off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void
```

取消订阅输入法应用发送输入法软键盘状态事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendKeyboardStatus' | 是 |
| callback | (keyboardStatus: KeyboardStatus) = & gt; void | 否 |

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

## off('sendFunctionKey')

```TypeScript
off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void
```

取消订阅输入法应用发送功能键事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendFunctionKey' | 是 |
| callback | (functionKey: FunctionKey) = & gt; void | 否 |

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

## off('moveCursor')

```TypeScript
off(type: 'moveCursor', callback?: (direction: Direction) => void): void
```

取消订阅输入法应用移动光标事件。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'moveCursor' | 是 |
| callback | (direction: Direction) = & gt; void | 否 |

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

## off('handleExtendAction')

```TypeScript
off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void
```

取消订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'handleExtendAction' | 是 |
| callback | (action: ExtendAction) = & gt; void | 否 |

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

## off('getLeftTextOfCursor')

```TypeScript
off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void
```

取消订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getLeftTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 否 |

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

取消订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getRightTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 否 |

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

取消订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getTextIndexAtCursor' | 是 |
| callback | () = & gt; number | 否 |

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

## off('setPreviewText')

```TypeScript
off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void
```

取消订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setPreviewText' | 是 |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 否 |

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

## off('finishTextPreview')

```TypeScript
off(type: 'finishTextPreview', callback?: Callback<void>): void
```

取消订阅结束文本预览事件。使用callback异步回调。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'finishTextPreview' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

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

## offDeleteLeft

```TypeScript
offDeleteLeft(callback?: Callback<int>): void
```

取消订阅输入法应用向左删除文本事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 |

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

取消订阅输入法应用向右删除文本事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 |

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

取消订阅结束文本预览事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

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

取消订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 否 |

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

取消订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 否 |

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

取消订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | 否 |

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

取消订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | 否 |

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

取消订阅输入法应用插入文本事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

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

取消订阅输入法应用移动光标事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | 否 |

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

取消订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 否 |

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

取消订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 否 |

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

取消订阅输入法应用发送功能键事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | 否 |

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

取消订阅输入法应用发送输入法软键盘状态事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | 否 |

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

取消订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 否 |

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

## on('selectByRange')

```TypeScript
on(type: 'selectByRange', callback: Callback<Range>): void
```

订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByRange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
});
```

## on('selectByMovement')

```TypeScript
on(type: 'selectByMovement', callback: Callback<Movement>): void
```

订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByMovement' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});
```

## on('insertText')

```TypeScript
on(type: 'insertText', callback: (text: string) => void): void
```

订阅输入法应用插入文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'insertText' | 是 |
| callback | (text: string) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## on('deleteLeft')

```TypeScript
on(type: 'deleteLeft', callback: (length: number) => void): void
```

订阅输入法应用向左删除文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteLeft' | 是 |
| callback | (length: number) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用向右删除文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteRight' | 是 |
| callback | (length: number) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('deleteRight', (length: number) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
});
```

## on('sendKeyboardStatus')

```TypeScript
on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void
```

订阅输入法应用发送输入法软键盘状态事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendKeyboardStatus' | 是 |
| callback | (keyboardStatus: KeyboardStatus) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
});
```

## on('sendFunctionKey')

```TypeScript
on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void
```

订阅输入法应用发送功能键事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendFunctionKey' | 是 |
| callback | (functionKey: FunctionKey) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
});
```

## on('moveCursor')

```TypeScript
on(type: 'moveCursor', callback: (direction: Direction) => void): void
```

订阅输入法应用移动光标事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'moveCursor' | 是 |
| callback | (direction: Direction) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
});
```

## on('handleExtendAction')

```TypeScript
on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void
```

订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'handleExtendAction' | 是 |
| callback | (action: ExtendAction) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
});
```

## on('getLeftTextOfCursor')

```TypeScript
on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void
```

订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getLeftTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getRightTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getTextIndexAtCursor' | 是 |
| callback | () = & gt; number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

```TypeScript
inputMethod.getController().on('getTextIndexAtCursor', () => {
  console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
});
```

## on('setPreviewText')

```TypeScript
on(type: 'setPreviewText', callback: SetPreviewTextCallback): void
```

订阅输入法应用操作文本预览内容的事件。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 使用预览文本功能，需在调用 &lt;br
&gt; 
> [attach](#attach) &lt;br
&gt; 
> 前订阅此事件，并和 &lt;br
&gt; 
> on('finishTextPreview') &lt;br
&gt; 
> 一起订阅。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setPreviewText' | 是 |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

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

## on('finishTextPreview')

```TypeScript
on(type: 'finishTextPreview', callback: Callback<void>): void
```

订阅结束文本预览事件。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 使用预览文本功能，需在调用 &lt;br
&gt; 
> [attach](#attach) &lt;br
&gt; 
> 前订阅此事件，并和 &lt;br
&gt; 
> [on('setPreviewText')](#onsetpreviewtext) &lt;br
&gt; 
> 一起订阅。

**起始版本：** 17

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为17。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'finishTextPreview' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

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

## onDeleteLeft

```TypeScript
onDeleteLeft(callback: Callback<int>): void
```

订阅输入法应用向左删除文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用向右删除文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅结束文本预览事件。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 使用预览文本功能，需在调用 &lt;br
&gt; 
> [attach](#attach) &lt;br
&gt; 
> 前订阅此事件，并和 &lt;br
&gt; 
> [on('setPreviewText')](#onsetpreviewtext) &lt;br
&gt; 
> 一起订阅。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

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

订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用插入文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用移动光标事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 是 |

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

订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 是 |

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

订阅输入法应用发送功能键事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

订阅输入法应用操作文本预览内容的事件。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 使用预览文本功能，需在调用 [attach](#attach) 前订阅此事件，并和 on('finishTextPreview') 一起订阅。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 是 |

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

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

注册或取消注册MessageHandler。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的 &lt;br
&gt; 
> [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 未填写参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethod-messagehandler-i.md)，并触发被取消注册对象中 &lt;br
&gt; 
> [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)回调函数。

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

发送自定义通信至输入法应用。使用Promise异步回调。 <br> <br>   
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

ArkTS-Dyn:
```TypeScript
setCallingWindow(windowId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setCallingWindow(windowId: int, callback: AsyncCallback<void>): void
```

设置要避让软键盘的窗口。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口设置避让软键盘的窗口。 &lt;br
&gt; 
> &lt;br
&gt; 
> 将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## setCallingWindow

ArkTS-Dyn:
```TypeScript
setCallingWindow(windowId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setCallingWindow(windowId: int): Promise<void>
```

设置要避让软键盘的窗口。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [setCallingWindow](#setcallingwindow)

## showSoftKeyboard

```TypeScript
showSoftKeyboard(callback: AsyncCallback<void>): void
```

显示输入法软键盘。使用callback异步回调。 <br> <br>含义/功能：强制显示当前输入法的软键盘。 <br> <br>使用场景：系统应用需要强制显示输入法软键盘时使用（如设置应用测试输入法）。 <br> <br>使用后效果：输入法软键盘弹出显示。 <br> <br>前提条件/前置操作：编辑框与输入法绑定时才能调用。 <br> <br>相似接口差异点及选取原则： <br> <br>- showSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY，仅显示键盘不改变编辑状态。 <br>- showTextInput：面向自绘控件，需先attach绑定，拉起键盘并进入编辑状态。 <br>- 选取原则：自绘控件使用showTextInput；系统应用且有权限时使用showSoftKeyboard。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: number = 20;
inputMethod.getController().showSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let displayId: long = 20;
inputMethod.getController().showSoftKeyboard(displayId).then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError): void=> {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## showSoftKeyboard

```TypeScript
showSoftKeyboard(): Promise<void>
```

显示输入法软键盘。使用Promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [showSoftKeyboard](#showsoftkeyboard)

## showTextInput

```TypeScript
showTextInput(callback: AsyncCallback<void>): void
```

进入文本编辑状态。使用callback异步回调。 <br> <br>含义/功能：拉起软键盘，使编辑框进入文本编辑状态。 <br> <br>使用场景：自绘控件绑定输入法后，需要显示软键盘开始文本输入时调用。 <br> <br>使用后效果：软键盘弹出，编辑框进入可输入的文本编辑状态。 <br> <br>前提条件/前置操作：需先调用 [attach](#attach) 完成绑定，否则会报12800009错误。 <br> <br>相关接口间的配合/制约关系：showTextInput与hideTextInput必须配对使用。调用hideTextInput退出编辑状态后，需再次调用showTextInput才能重新进入编辑状态。 <br> <br>相似接口差异点及选取原则： <br> <br>- showTextInput：面向自绘控件，需先attach绑定后调用。适用于自绘控件场景，是标准的键盘显示方式。 <br>- showSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY。适用于系统应用需要强制显示键盘的场景。 <br>- 选取原则：自绘控件优先使用showTextInput；系统应用且有特殊需求时使用showSoftKeyboard。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## showTextInput

```TypeScript
showTextInput(): Promise<void>
```

进入文本编辑状态。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [showTextInput](#showtextinput)

## showTextInput

```TypeScript
showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

进入文本编辑状态。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestKeyboardReason | [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [showTextInput](#showtextinput)

## stopInput

```TypeScript
stopInput(callback: AsyncCallback<boolean>): void
```

结束输入会话。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

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

## stopInput

```TypeScript
stopInput(): Promise<boolean>
```

结束输入会话。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**示例**

参见 [stopInput](#stopinput)

## stopInputSession

```TypeScript
stopInputSession(callback: AsyncCallback<boolean>): void
```

结束输入会话。使用callback异步回调。 <br> <br>含义/功能：结束当前的输入会话，隐藏软键盘。 <br> <br>使用场景：应用需要主动结束输入会话时调用（如用户完成了输入操作）。 <br> <br>使用后效果：软键盘被隐藏，输入会话结束。 <br> <br>前提条件/前置操作：编辑框与输入法绑定时才能调用，即点击编辑控件后。 <br> <br>相关接口间的配合/制约关系：stopInputSession会隐藏软键盘并结束输入会话。如果使用自绘控件的attach/showTextInput/hideTextInput/detach流程，建议使用 hideTextInput而非stopInputSession。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

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

## stopInputSession

```TypeScript
stopInputSession(): Promise<boolean>
```

结束输入会话。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

**示例**

参见 [stopInputSession](#stopinputsession)

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void
```

更新编辑框属性信息。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute): Promise<void>
```

更新编辑框属性信息。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口更新编辑框属性信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [updateAttribute](#updateattribute)

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void
```

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用callback异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口更新光标信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cursorInfo](arkts-ime-inputmethod-textconfig-i.md) | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

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

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo): Promise<void>
```

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用promise异步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 编辑框与输入法绑定成功后，才可调用该接口更新光标信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cursorInfo](arkts-ime-inputmethod-textconfig-i.md) | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

**示例**

参见 [updateCursor](#updatecursor)
