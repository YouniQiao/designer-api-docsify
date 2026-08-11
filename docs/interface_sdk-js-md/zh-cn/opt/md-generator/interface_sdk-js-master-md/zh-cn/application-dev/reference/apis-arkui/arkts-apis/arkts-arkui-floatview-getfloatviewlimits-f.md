# getFloatViewLimits

## getFloatViewLimits

```TypeScript
function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits
```

根据传入的模板类型获取对应标准悬浮窗窗口的限制，单位为px。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits--><!--Device-floatView-function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateType | [FloatViewTemplateType](arkts-arkui-floatview-floatviewtemplatetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## 示例

```TypeScript
// 获取圆角矩形模板的闪控窗窗口限制
let limits: floatView.FloatViewLimits = floatView.getFloatViewLimits(floatView.FloatViewTemplateType.ROUNDED_RECTANGLE);
console.info('Float view limits: ' + JSON.stringify(limits));
```
