# ImeChangeCallback

```TypeScript
export type ImeChangeCallback = (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
```

当输入法属性对象及子类型对象变化时的回调函数。

**起始版本：** 23

<!--Device-inputMethod-export type ImeChangeCallback = (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void--><!--Device-inputMethod-export type ImeChangeCallback = (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 | 输入法属性对象。 |
| inputMethodSubtype | [InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md) | 是 | 输入法子类型对象。 |

