# getDefaultInputMethod

## getDefaultInputMethod

```TypeScript
function getDefaultInputMethod(): InputMethodProperty
```

获取默认输入法。

**起始版本：** 11

<!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty--><!--Device-inputMethod-function getDefaultInputMethod(): InputMethodProperty-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();
```
