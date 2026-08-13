# getCurrentInputMethodSubtype（系统接口）

## getCurrentInputMethodSubtype

```TypeScript
function getCurrentInputMethodSubtype(userId?: number): InputMethodSubtype
```

获取指定用户的当前输入法子类型。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function getCurrentInputMethodSubtype(userId?: int): InputMethodSubtype--><!--Device-inputMethod-function getCurrentInputMethodSubtype(userId?: int): InputMethodSubtype-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## 示例

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

try {
  let currentImeSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype(100);
  console.info('Succeeded in getting current input method subtype, id: ' + currentImeSubType.id);
} catch (err) {
  console.error(`Failed to getCurrentInputMethodSubtype. Code: ${err.code}, message: ${err.message}`);
}
```
