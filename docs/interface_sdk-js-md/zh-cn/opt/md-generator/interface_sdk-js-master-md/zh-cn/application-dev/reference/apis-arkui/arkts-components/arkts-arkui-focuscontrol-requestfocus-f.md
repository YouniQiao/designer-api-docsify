# requestFocus

## 导入模块

```TypeScript
```

## requestFocus

```TypeScript
function requestFocus(value: string): boolean
```

方法语句中可使用的全局接口，调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。 如果需要指定组件立刻获焦，推荐使用FocusController中的焦点同步转移接口[requestFocus](../arkts-apis/arkts-arkui-arkui-uicontext-focuscontroller-c.md#requestfocus)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-focusControl-function requestFocus(value: string): boolean--><!--Device-focusControl-function requestFocus(value: string): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
