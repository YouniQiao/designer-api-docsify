# off（系统接口）

## off('formUninstall')

```TypeScript
function off(type: 'formUninstall', callback?: Callback<string>): void
```

Unsubscribes from widget uninstall events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget
> is automatically uninstalled.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** @ohos.app.form.formHost:formHost#off

<!--Device-formHost-function off(type: 'formUninstall', callback?: Callback<string>): void--><!--Device-formHost-function off(type: 'formUninstall', callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'formUninstall' | 是 | Event type. The value **'formUninstall'** indicates a widget uninstallation event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | Callback used to return the widget ID. If it is left unspecified, it indicates the callback for all the events that have been subscribed. &lt;br&gt; The value must be the same as that in **on('formUninstall')**. |

