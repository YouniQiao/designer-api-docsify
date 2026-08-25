# InputMethodController

下列API示例中都需使用[getController](arkts-ime-inputmethod-getcontroller-f.md)获取到InputMethodController实例，再通过实例调用对应方法。 InputMethodController是输入法客户端控制器，面向前台应用提供与输入法交互的核心能力。通过`inputMethod.getController()`获取实例后，可进行以下操作：   
- 绑定管理：通过 [attach](#attach) 建立与输入法的绑定，通过[detach](#detach)解除绑定。attach和 detach必须配对使用。   
- 键盘控制：通过[showTextInput](#showtextinput)拉起软键盘 进入编辑状态，通过[hideTextInput](#hidetextinput)隐藏软键盘 退出编辑状态。showTextInput和hideTextInput必须配对使用。   
- 编辑框状态同步：通过 [updateCursor](#updatecursor) 、 [changeSelection](#changeselection) 、 [updateAttribute](#updateattribute) 等接口向输入法同步光标、选区、属性等编辑框状态信息。   
- 事件订阅：通过on('insertText')、on('deleteLeft')等接口订阅输入法应用发送的文本操作事件。   
 典型调用序列：`getController()` → `attach()` → `showTextInput()`/`hideTextInput()` → `detach()`   
> **说明：**
   
> 
   
> attach和detach必须配对使用，showTextInput和hideTextInput必须配对使用，否则可能导致资源泄漏或状态不一致。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void
```

自绘控件绑定输入法。使用callback异步回调。 含义/功能：建立自绘控件与输入法应用之间的绑定关系，是自绘控件使用输入法功能的前提。 使用场景：自绘控件（非系统原生编辑框）需要与输入法交互时，必须先调用此接口建立绑定。原生编辑框获焦时系统自动绑定，无需调用此接口。 使用后效果：绑定成功后，自绘控件可调用showTextInput/hideTextInput控制键盘显隐、调用updateCursor/changeSelection同步编辑框状态、订阅输入法事件等。 前提条件/前置操作：自绘控件所在窗口需处于获焦状态，否则绑定会失败。 相关接口间的配合/制约关系：attach必须与detach配对使用。调用attach后才能调用showTextInput、hideTextInput、updateCursor等接口。 相似接口差异点及选取原则：   
- attach：不需要传入UIContext，适用于API version 10+的自绘控件绑定场景。   
- attachWithUIContext：需要传入UIContext，适用于API version 23+的Stage模型场景，支持更多绑定选项。   
- 选取原则：API version 23+的Stage模型应用优先使用attachWithUIContext，以获得更完整的绑定选项支持。   
   
> **说明：**
   
> 
   
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。
   
> 
   
> 当自绘控件所在窗口通过
   
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable)
   
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考
   
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 10

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

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。   
> **说明：**
   
> 
   
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。
   
> 
   
> 当自绘控件所在窗口通过
   
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable)
   
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考
   
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 10

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

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。   
> **说明：**
   
> 
   
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。
   
> 
   
> 当自绘控件所在窗口通过
   
> [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable)
   
> 设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考
   
> [不可获焦窗口中输入框与输入法交互指南](../../../inputmethod/use-inputmethod-in-not-focusable-window.md)。

**起始版本：** 15

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

## attachWithUIContext

```TypeScript
attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>
```

自绘控件绑定输入法。使用promise异步回调。   
> **说明：**
   
> 
   
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**起始版本：** 23

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

## changeSelection

```TypeScript
changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void
```

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用callback异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口更新文本选区信息。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| start | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

## changeSelection

```TypeScript
changeSelection(text: string, start: number, end: number): Promise<void>
```

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用promise异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口更新文本选区信息。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| start | number | 是 |
| end | number | 是 |

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

## detach

```TypeScript
detach(callback: AsyncCallback<void>): void
```

自绘控件解除与输入法的绑定。使用callback异步回调。 含义/功能：解除自绘控件与输入法应用之间的绑定关系，释放相关资源。 使用场景：自绘控件不再需要与输入法交互时调用（如页面切换、编辑框被销毁等）。 使用后效果：解除绑定后，不能再调用showTextInput、hideTextInput、updateCursor等需要绑定状态的接口。输入法软键盘将被隐藏。 相关接口间的配合/制约关系：detach必须与attach配对使用。建议在hideTextInput之后调用detach，完整流程为：attach → showTextInput → hideTextInput → detach。

**起始版本：** 10

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

## detach

```TypeScript
detach(): Promise<void>
```

自绘控件解除与输入法的绑定。使用promise异步回调。 含义/功能：解除自绘控件与输入法应用之间的绑定关系，释放相关资源。 使用场景：自绘控件不再需要与输入法交互时调用。 使用后效果：解除绑定后，不能再调用需要绑定状态的接口。输入法软键盘将被隐藏。 相关接口间的配合/制约关系：detach必须与attach配对使用。

**起始版本：** 10

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

## discardTypingText

```TypeScript
discardTypingText(): Promise<void>
```

编辑框应用发送“清空正在输入的文字”命令到输入法。使用promise异步回调。   
> **说明：**
   
> 

> 当编辑框应用与输入法绑定成功后，才可调用该接口实现此功能。

**起始版本：** 20

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

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(callback: AsyncCallback<void>): void
```

隐藏输入法软键盘。使用callback异步回调。 含义/功能：强制隐藏当前输入法的软键盘。 使用场景：系统应用需要强制隐藏输入法软键盘时使用。 使用后效果：输入法软键盘被隐藏。 前提条件/前置操作：编辑框与输入法绑定时才能调用。 相似接口差异点及选取原则：   
- hideSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY，仅隐藏键盘不退出编辑状态。   
- hideTextInput：面向自绘控件，隐藏键盘并退出编辑状态，可再次showTextInput重新进入。   
- 选取原则：自绘控件使用hideTextInput；系统应用且有权限时使用hideSoftKeyboard。   
   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**起始版本：** 9

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

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(): Promise<void>
```

隐藏输入法软键盘。使用Promise异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**起始版本：** 9

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

## hideTextInput

```TypeScript
hideTextInput(callback: AsyncCallback<void>): void
```

退出文本编辑状态。使用callback异步回调。 含义/功能：隐藏软键盘，使编辑框退出文本编辑状态。 使用场景：自绘控件不再需要输入时调用，如用户点击了编辑框外的区域、切换到其他页面等。 使用后效果：软键盘被隐藏，编辑框退出编辑状态。调用此接口不会解除与输入法的绑定，再次调用showTextInput可重新进入编辑状态。 前提条件/前置操作：需先调用 [attach](#attach) 完成绑定，且已调用showTextInput进入编辑状态。 相关接口间的配合/制约关系：hideTextInput与showTextInput必须配对使用。hideTextInput后如需再次输入，必须先调用showTextInput重新进入编辑状态，不能直接调用其他编辑操作。 相似接口差异点及选取原则：   
- hideTextInput：面向自绘控件，退出编辑状态但不解除绑定，可再次showTextInput重新进入。适用于自绘控件需要暂时隐藏键盘的场景。   
- hideSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY。仅隐藏键盘，不改变编辑状态。   
- 选取原则：自绘控件优先使用hideTextInput；系统应用且有特殊需求时使用hideSoftKeyboard。   
   
> **说明：**
   
> 
   
> 调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。
   
> 
   
> 调用该接口不会解除与输入法的绑定，再次调用
   
> [showTextInput](#showtextinput)时，可重新进入文本编
   
> 辑状态。

**起始版本：** 10

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

## hideTextInput

```TypeScript
hideTextInput(): Promise<void>
```

退出文本编辑状态。使用promise异步回调。   
> **说明：**
   
> 
   
> 调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。
   
> 
   
> 调用该接口不会解除与输入法的绑定，再次调用
   
> [showTextInput](#showtextinput)时，可重新进入文本编
   
> 辑状态。

**起始版本：** 10

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

## off('selectByRange')

```TypeScript
off(type: 'selectByRange', callback?: Callback<Range>): void
```

取消订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByRange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | 否 |

## off('selectByMovement')

```TypeScript
off(type: 'selectByMovement', callback?: Callback<Movement>): void
```

取消订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectByMovement' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | 否 |

## off('insertText')

```TypeScript
off(type: 'insertText', callback?: (text: string) => void): void
```

取消订阅输入法应用插入文本事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'insertText' | 是 |
| callback | (text: string) = & gt; void | 否 |

## off('deleteLeft')

```TypeScript
off(type: 'deleteLeft', callback?: (length: number) => void): void
```

取消订阅输入法应用向左删除文本事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteLeft' | 是 |
| callback | (length: number) = & gt; void | 否 |

## off('deleteRight')

```TypeScript
off(type: 'deleteRight', callback?: (length: number) => void): void
```

取消订阅输入法应用向右删除文本事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deleteRight' | 是 |
| callback | (length: number) = & gt; void | 否 |

## off('sendKeyboardStatus')

```TypeScript
off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void
```

取消订阅输入法应用发送输入法软键盘状态事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendKeyboardStatus' | 是 |
| callback | (keyboardStatus: KeyboardStatus) = & gt; void | 否 |

## off('sendFunctionKey')

```TypeScript
off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void
```

取消订阅输入法应用发送功能键事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sendFunctionKey' | 是 |
| callback | (functionKey: FunctionKey) = & gt; void | 否 |

## off('moveCursor')

```TypeScript
off(type: 'moveCursor', callback?: (direction: Direction) => void): void
```

取消订阅输入法应用移动光标事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'moveCursor' | 是 |
| callback | (direction: Direction) = & gt; void | 否 |

## off('handleExtendAction')

```TypeScript
off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void
```

取消订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'handleExtendAction' | 是 |
| callback | (action: ExtendAction) = & gt; void | 否 |

## off('getLeftTextOfCursor')

```TypeScript
off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void
```

取消订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getLeftTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 否 |

## off('getRightTextOfCursor')

```TypeScript
off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void
```

取消订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getRightTextOfCursor' | 是 |
| callback | (length: number) = & gt; string | 否 |

## off('getTextIndexAtCursor')

```TypeScript
off(type: 'getTextIndexAtCursor', callback?: () => number): void
```

取消订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getTextIndexAtCursor' | 是 |
| callback | () = & gt; number | 否 |

## off('setPreviewText')

```TypeScript
off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void
```

取消订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

**起始版本：** 17

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setPreviewText' | 是 |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | 否 |

## off('finishTextPreview')

```TypeScript
off(type: 'finishTextPreview', callback?: Callback<void>): void
```

取消订阅结束文本预览事件。使用callback异步回调。

**起始版本：** 17

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'finishTextPreview' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## on('selectByRange')

```TypeScript
on(type: 'selectByRange', callback: Callback<Range>): void
```

订阅输入法应用按范围选中文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('selectByMovement')

```TypeScript
on(type: 'selectByMovement', callback: Callback<Movement>): void
```

订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('insertText')

```TypeScript
on(type: 'insertText', callback: (text: string) => void): void
```

订阅输入法应用插入文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('deleteLeft')

```TypeScript
on(type: 'deleteLeft', callback: (length: number) => void): void
```

订阅输入法应用向左删除文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('deleteRight')

```TypeScript
on(type: 'deleteRight', callback: (length: number) => void): void
```

订阅输入法应用向右删除文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('sendKeyboardStatus')

```TypeScript
on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void
```

订阅输入法应用发送输入法软键盘状态事件。使用callback异步回调。

**起始版本：** 10

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

## on('sendFunctionKey')

```TypeScript
on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void
```

订阅输入法应用发送功能键事件。使用callback异步回调。

**起始版本：** 10

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

## on('moveCursor')

```TypeScript
on(type: 'moveCursor', callback: (direction: Direction) => void): void
```

订阅输入法应用移动光标事件。使用callback异步回调。

**起始版本：** 10

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

## on('handleExtendAction')

```TypeScript
on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void
```

订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**起始版本：** 10

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

## on('getLeftTextOfCursor')

```TypeScript
on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void
```

订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('getRightTextOfCursor')

```TypeScript
on(type: 'getRightTextOfCursor', callback: (length: number) => string): void
```

订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**起始版本：** 10

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

## on('getTextIndexAtCursor')

```TypeScript
on(type: 'getTextIndexAtCursor', callback: () => number): void
```

订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**起始版本：** 10

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

## on('setPreviewText')

```TypeScript
on(type: 'setPreviewText', callback: SetPreviewTextCallback): void
```

订阅输入法应用操作文本预览内容的事件。使用callback异步回调。   
> **说明：**
   
> 
   
> 使用预览文本功能，需在调用
   
> [attach](#attach)
   
> 前订阅此事件，并和
   
> on('finishTextPreview')
   
> 一起订阅。

**起始版本：** 17

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

## on('finishTextPreview')

```TypeScript
on(type: 'finishTextPreview', callback: Callback<void>): void
```

订阅结束文本预览事件。使用callback异步回调。   
> **说明：**
   
> 
   
> 使用预览文本功能，需在调用
   
> [attach](#attach)
   
> 前订阅此事件，并和
   
> [on('setPreviewText')](#onsetpreviewtext)
   
> 一起订阅。

**起始版本：** 17

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

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

注册或取消注册MessageHandler。   
> **说明：**
   
> 
   
> [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的
   
> [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)回调函数。
   
> 
   
> 未填写参数，则取消全局已注册的[MessageHandler](arkts-ime-inputmethod-messagehandler-i.md)，并触发被取消注册对象中
   
> [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated)回调函数。

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

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

发送自定义通信至输入法应用。使用Promise异步回调。   
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

## setCallingWindow

```TypeScript
setCallingWindow(windowId: number, callback: AsyncCallback<void>): void
```

设置要避让软键盘的窗口。使用callback异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口设置避让软键盘的窗口。
   
> 
   
> 将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-输入法客户端未绑定) |

## setCallingWindow

```TypeScript
setCallingWindow(windowId: number): Promise<void>
```

设置要避让软键盘的窗口。使用promise异步回调。   
> **说明：**
   
> 
   
> 将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

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

## showSoftKeyboard

```TypeScript
showSoftKeyboard(callback: AsyncCallback<void>): void
```

显示输入法软键盘。使用callback异步回调。 含义/功能：强制显示当前输入法的软键盘。 使用场景：系统应用需要强制显示输入法软键盘时使用（如设置应用测试输入法）。 使用后效果：输入法软键盘弹出显示。 前提条件/前置操作：编辑框与输入法绑定时才能调用。 相似接口差异点及选取原则：   
- showSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY，仅显示键盘不改变编辑状态。   
- showTextInput：面向自绘控件，需先attach绑定，拉起键盘并进入编辑状态。   
- 选取原则：自绘控件使用showTextInput；系统应用且有权限时使用showSoftKeyboard。   
   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**起始版本：** 9

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

## showSoftKeyboard

```TypeScript
showSoftKeyboard(): Promise<void>
```

显示输入法软键盘。使用Promise异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**起始版本：** 9

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

## showTextInput

```TypeScript
showTextInput(callback: AsyncCallback<void>): void
```

进入文本编辑状态。使用callback异步回调。 含义/功能：拉起软键盘，使编辑框进入文本编辑状态。 使用场景：自绘控件绑定输入法后，需要显示软键盘开始文本输入时调用。 使用后效果：软键盘弹出，编辑框进入可输入的文本编辑状态。 前提条件/前置操作：需先调用 [attach](#attach) 完成绑定，否则会报12800009错误。 相关接口间的配合/制约关系：showTextInput与hideTextInput必须配对使用。调用hideTextInput退出编辑状态后，需再次调用showTextInput才能重新进入编辑状态。 相似接口差异点及选取原则：   
- showTextInput：面向自绘控件，需先attach绑定后调用。适用于自绘控件场景，是标准的键盘显示方式。   
- showSoftKeyboard：面向系统应用，需权限ohos.permission.CONNECT_IME_ABILITY。适用于系统应用需要强制显示键盘的场景。   
- 选取原则：自绘控件优先使用showTextInput；系统应用且有特殊需求时使用showSoftKeyboard。   
   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 10

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

## showTextInput

```TypeScript
showTextInput(): Promise<void>
```

进入文本编辑状态。使用promise异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 10

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

## showTextInput

```TypeScript
showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

进入文本编辑状态。使用promise异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**起始版本：** 15

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

## stopInput

```TypeScript
stopInput(callback: AsyncCallback<boolean>): void
```

结束输入会话。使用callback异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## stopInput

```TypeScript
stopInput(): Promise<boolean>
```

结束输入会话。使用promise异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [stopInputSession](#stopinputsession)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## stopInputSession

```TypeScript
stopInputSession(callback: AsyncCallback<boolean>): void
```

结束输入会话。使用callback异步回调。 含义/功能：结束当前的输入会话，隐藏软键盘。 使用场景：应用需要主动结束输入会话时调用（如用户完成了输入操作）。 使用后效果：软键盘被隐藏，输入会话结束。 前提条件/前置操作：编辑框与输入法绑定时才能调用，即点击编辑控件后。 相关接口间的配合/制约关系：stopInputSession会隐藏软键盘并结束输入会话。如果使用自绘控件的attach/showTextInput/hideTextInput/detach流程，建议使用 hideTextInput而非stopInputSession。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 9

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

## stopInputSession

```TypeScript
stopInputSession(): Promise<boolean>
```

结束输入会话。使用promise异步回调。   
> **说明：**
   
> 
   
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**起始版本：** 9

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

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void
```

更新编辑框属性信息。使用callback异步回调。

**起始版本：** 10

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

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute): Promise<void>
```

更新编辑框属性信息。使用promise异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口更新编辑框属性信息。

**起始版本：** 10

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

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void
```

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用callback异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口更新光标信息。

**起始版本：** 10

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

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo): Promise<void>
```

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用promise异步回调。   
> **说明：**
   
> 
   
> 编辑框与输入法绑定成功后，才可调用该接口更新光标信息。

**起始版本：** 10

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
