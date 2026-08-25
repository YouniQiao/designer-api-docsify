# registerWebAdInterface

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## registerWebAdInterface

```TypeScript
function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext): void
```

注入广告JavaScript对象到Web组件中（该接口仅对部分系统预置应用开放）。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | web_webview.WebviewController | 是 |
| context | common.UIAbilityContext | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |


## registerWebAdInterface

```TypeScript
function registerWebAdInterface(controller: web_webview.WebviewController, context: common.UIAbilityContext, 
    needRefresh: boolean): void
```

注入广告JavaScript对象到Web组件中（该接口仅对部分系统预置应用开放）。

**起始版本：** 16

**原子化服务API：** 从API版本16开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | web_webview.WebviewController | 是 |
| context | common.UIAbilityContext | 是 |
| needRefresh | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
