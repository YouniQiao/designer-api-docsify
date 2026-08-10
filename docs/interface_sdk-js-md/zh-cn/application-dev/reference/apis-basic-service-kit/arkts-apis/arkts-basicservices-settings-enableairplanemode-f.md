# enableAirplaneMode

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## enableAirplaneMode

```TypeScript
function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void
```

Enables or disables airplane mode.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Specifies whether to enable airplane mode. The value {@code true} means to enable airplane mode, and {@code false} means to disable airplane mode. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback of enableAirplaneMode result. |

## 示例

```TypeScript
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled, (err:Error) => {
    if (err) {
        console.error('Failed to enable AirplaneMode.');
        return;
    }
    console.info('Return true if enable.');
})
```


## enableAirplaneMode

```TypeScript
function enableAirplaneMode(enable: boolean): Promise<void>
```

Enables or disables airplane mode.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>--><!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Specifies whether to enable airplane mode. The value {@code true} means to enable airplane mode, and {@code false} means to disable airplane mode. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Return Promise. |

## 示例

```TypeScript
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled).then(() => {
  console.info('Succeeded in enabling AirplaneMode.');
}).catch((err:Error) => {
  console.error(`Failed to enable AirplaneMode. Cause: ${err}`);
})
```

