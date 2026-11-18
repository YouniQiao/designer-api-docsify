# injectTextSync

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## injectTextSync

```TypeScript
function injectTextSync(text: string): void
```

同步向当前获焦、与输入法应用绑定且处于编辑状态的编辑框发送文本。适用于PC Stage应用需要在当前调用中取得发送结果的场景，支持密码框。与injectText不同，本接口发送成功时正常返回，失败时抛出BusinessError。本同步接口阻塞调用线程，在主线程调用容易影响UI交互，需谨慎使用。目标由当前输入焦点确定，无默认文本，不支持调用方指定目标。仅支持PC，不支持跨平台应用、元服务或卡片。空字符串同样经过权限及目标检查后下传，不新增编码合法性校验。参数错误抛BusinessError 401。正常返回不代表目标完成编辑，也不读取目标文本。应处理异常，禁止记录敏感文本。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_DEVICE or ohos.permission.OPERATE_TEXT_ACROSS_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function injectTextSync(text: string): void--><!--Device-inputMethod-function injectTextSync(text: string): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 必填文本，无默认值。UTF-8编码后的长度为0到512字节。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | 权限校验失败，两项允许权限均未获得。 |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | 设备不支持该能力。 |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) | 无合法获焦且绑定的编辑框，或目标失效。 |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) | 输入法服务不可用或请求发送失败。 |
| [12800016](../errorcode-inputmethod-framework.md#12800016-输入法客户端未处于编辑状态) | 目标编辑框处于非编辑状态。 |
