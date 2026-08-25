# AccessibilityActionInterceptCallback

```TypeScript
export declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult
```

Defines the callback type used in accessibility action intercept. The value of action indicates the accessibility action type.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | [AccessibilityAction](arkts-arkui-common-accessibilityaction-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AccessibilityActionInterceptResult](arkts-arkui-common-accessibilityactioninterceptresult-e.md) |
