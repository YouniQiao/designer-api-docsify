# getContext

## getContext

```TypeScript
declare function getContext(component?: Object): Context
```

Obtains the Context object associated with a component on the page.

**起始版本：** 11

**废弃版本：** 18

**替代接口：** [getHostContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#getHostContext)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function getContext(component?: Object): Context--><!--Device-unnamed-declare function getContext(component?: Object): Context-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [component](../arkts-apis/arkts-arkui-interop-compatiblecomponentinfo-i.md) | Object | 否 |

**返回值：**

| 类型 |
| --- |
| [Context](arkts-arkui-context-t.md) |
