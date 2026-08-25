# getContext

## 导入模块

```TypeScript
```

## getContext

```TypeScript
declare function getContext(component?: Object): Context
```

Obtains the Context object associated with a component on the page.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**废弃版本：** 18

**替代接口：** [getHostContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#gethostcontext)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [component](../arkts-apis/arkts-arkui-interop-compatiblecomponentinfo-i.md) | Object | 否 |

**返回值：**

| 类型 |
| --- |
| [Context](arkts-arkui-context-t.md) |
