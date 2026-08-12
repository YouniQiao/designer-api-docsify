# back

## back

```TypeScript
function back(options?: RouterOptions): void
```

返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。如果此前调用了[showAlertBeforeBackPage](#routershowalertbeforebackpagedeprecated)开启了返回询问对话框，则在执行返回操作时会先弹出确认对话框，用户确认后才执行返回；用户取消则不执行返回。

> **说明：**
> 
> - 从API version 8开始支持，从API version 18开始废弃，建议使用
> [back](arkts-arkui-arkui-uicontext-router-c.md#back)替代。back需先通过
> [UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 8

**废弃版本：** 18

**替代接口：** [back](@ohos.arkui.UIContext:Router#back(options?:)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-router-function back(options?: RouterOptions): void--><!--Device-router-function back(options?: RouterOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 否 |

## 示例

```TypeScript
this.getUIContext().getRouter().back({ url: 'pages/detail' });
```


## back

```TypeScript
function back(index: number, params?: Object): void
```

返回指定的页面，会删除当前页面与指定页面之间的所有页面。如果此前调用了[showAlertBeforeBackPage](#routershowalertbeforebackpagedeprecated)开启了返回询问对话框，则在执行返回操作时会先弹出确认对话框，用户确认后才执行返回；用户取消则不执行返回。

> **说明：**
> 
> - 从API version 12开始支持，从API version 18开始废弃，建议使用
> [back](arkts-arkui-arkui-uicontext-router-c.md#back-1)替代。back需先通过
> [UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 12开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [back](@ohos.arkui.UIContext:Router#back(index:)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-router-function back(index: number, params?: Object): void--><!--Device-router-function back(index: number, params?: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| params | Object | 否 |

## 示例

```TypeScript
this.getUIContext().getRouter().back(1);
```

```TypeScript
this.getUIContext().getRouter().back(1, { info: '来自Home页' }); // 携带参数返回
```
