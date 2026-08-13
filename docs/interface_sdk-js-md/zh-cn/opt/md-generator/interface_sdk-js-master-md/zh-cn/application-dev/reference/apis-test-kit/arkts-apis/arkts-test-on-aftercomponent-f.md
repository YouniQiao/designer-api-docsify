# afterComponent

## afterComponent

```TypeScript
export function afterComponent(com: Component): On
```

要求目标组件位于由给定[Component](arkts-test-uitest-component-c.md#Component)指定的另一个组件之后 对象，用于相对于组件定位。

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-ON-export function afterComponent(com: Component): On--><!--Device-ON-export function afterComponent(com: Component): On-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| com | [Component](arkts-test-uitest-component-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [On](arkts-test-uitest-on-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
