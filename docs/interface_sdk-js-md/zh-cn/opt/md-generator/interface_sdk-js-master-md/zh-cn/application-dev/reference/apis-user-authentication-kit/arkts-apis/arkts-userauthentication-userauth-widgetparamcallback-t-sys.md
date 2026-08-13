# WidgetParamCallback（系统接口）

```TypeScript
type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam
```

获取远程认证页面参数的回调函数类型。该类型用于远程认证场景，在需要获取远程认证界面的配置参数时，系统会调用此回调函数。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam--><!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) |
