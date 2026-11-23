# injectText

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## injectText

```TypeScript
function injectText(text: string): Promise<void>
```

将文本注入到前台应用程序的当前焦点编辑框中。该接口使用promise返回的结果。<br> <br>  
> **注意** <br> <br>
> 此接口仅在PC设备上支持。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.OPERATE_TEXT_ACROSS_APPLICATION or ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function injectText(text: string): Promise<void>--><!--Device-inputMethod-function injectText(text: string): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 要注入的文本。必填，无默认值。UTF-8编码后的长度为0到512字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 不返回任何值的Promise。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | permissions check fails. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | input method manager service error. Possible cause: a system error,such as null pointer, IPC exception. |
| [12800016](../errorcode-inputmethod-framework.md#12800016-输入法客户端未处于编辑状态) | input method client is not editable. |
