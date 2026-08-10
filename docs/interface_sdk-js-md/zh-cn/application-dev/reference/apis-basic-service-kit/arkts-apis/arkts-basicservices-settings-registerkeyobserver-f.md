# registerKeyObserver

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## registerKeyObserver

```TypeScript
function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean
```

Monitor registration key(synchronous method)  
[USER_SECURE] domain need ohos.permission.MANAGE_SECURE_SETTINGS permission.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-settings-function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean--><!--Device-settings-function registerKeyObserver(context: Context, name: string, domainName: string, observer: AsyncCallback<void>): boolean-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Application context. Only UIAbilityContext and ExtensionContext are supported. |
| name | string | 是 | Indicates the name of the character string. |
| domainName | string | 是 | Indicates the name of the domain name to set. |
| observer | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | callback when monitored key value is changed. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.registerKeyObserver(context, settings.display.SCREEN_BRIGHTNESS_STATUS, settings.domainName.DEVICE_SHARED, () => {
  let value:string = settings.getValueSync(context, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
  console.info(`Promise:value -> ${value}`);
});
```

