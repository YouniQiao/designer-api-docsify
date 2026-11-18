# injectText

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## injectText

```TypeScript
function injectText(text: string): Promise<void>
```

异步向当前获焦、与输入法应用绑定且处于编辑状态的编辑框发送文本。适用于PC Stage应用集成跨应用文本输入，支持密码框。与injectTextSync不同，本接口通过Promise报告发送结果，不等待目标完成编辑。目标由当前输入焦点确定，无默认文本，不支持调用方指定目标。仅支持PC，不支持跨平台应用、元服务或卡片。空字符串同样经过权限及目标检查后下传，不新增编码合法性校验。参数错误通过Promise拒绝返回BusinessError 401。应处理拒绝结果，禁止记录敏感文本。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_DEVICE or ohos.permission.OPERATE_TEXT_ACROSS_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function injectText(text: string): Promise<void>--><!--Device-inputMethod-function injectText(text: string): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 必填文本，无默认值。UTF-8编码后的长度为0到512字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 请求发送成功时完成的Promise，不代表目标已完成编辑。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | 权限校验失败，两项允许权限均未获得。 |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | 设备不支持该能力。 |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | 无合法获焦且绑定的编辑框，或目标失效。 |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | 输入法服务不可用或请求发送失败。 |
| [12800016](../errorcode-inputmethod-framework.md#12800016-输入法客户端未处于编辑状态) | 目标编辑框处于非编辑状态。 |
