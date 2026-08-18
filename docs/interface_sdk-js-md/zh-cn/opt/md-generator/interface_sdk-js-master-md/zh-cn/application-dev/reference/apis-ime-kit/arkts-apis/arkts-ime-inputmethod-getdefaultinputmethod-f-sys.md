# getDefaultInputMethod（系统接口）

## 导入模块

```TypeScript
```

## getDefaultInputMethod

```TypeScript
function getDefaultInputMethod(userId?: number): InputMethodProperty
```

获取指定用户的默认输入法。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function getDefaultInputMethod(userId?: int): InputMethodProperty--><!--Device-inputMethod-function getDefaultInputMethod(userId?: int): InputMethodProperty-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod(100);
  console.info('Succeeded in getting default input method, name: ' + defaultIme.name + ', id: ' + defaultIme.id);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getDefaultInputMethod. Code: ${error.code}, message: ${error.message}`);
}
```
