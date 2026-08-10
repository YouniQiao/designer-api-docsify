# getURI

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## getURI

```TypeScript
function getURI(name: string, callback: AsyncCallback<object>): void
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

<!--Device-settings-function getURI(name: string, callback: AsyncCallback<object>): void--><!--Device-settings-function getURI(name: string, callback: AsyncCallback<object>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Indicates the name of the setting to set. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;object&gt; | 是 | The callback of getURI result. |

## 示例

```TypeScript
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS, (uri:string) => {
    console.info(`callback:uri -> ${JSON.stringify(uri)}`)
})
```


## getURI

```TypeScript
function getURI(name: string): Promise<object>
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

<!--Device-settings-function getURI(name: string): Promise<object>--><!--Device-settings-function getURI(name: string): Promise<object>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Indicates the name of the setting to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;object&gt; | Returns the corresponding URI; returns { |

## 示例

```TypeScript
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS).then((uri:string) => {
    console.info(`promise:uri -> ${JSON.stringify(uri)}`)
})
```

